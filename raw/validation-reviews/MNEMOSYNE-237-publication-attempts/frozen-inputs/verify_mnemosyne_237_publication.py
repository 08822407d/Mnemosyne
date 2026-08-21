#!/usr/bin/env python3
"""Deterministic verifier/materializer for the frozen MNEMOSYNE-237 payload.

The verifier never derives a destination path from a task ID or filename convention.
Every path comes from the parsed external JSON manifest.  It validates source bytes,
base-tree operation expectations, the staged index, and an optional committed tree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Iterable


EXPECTED_MANIFEST_ID = "MNEMOSYNE-237-OPERATOR-PAYLOAD-MANIFEST-003"
EXPECTED_MODIFY_PATHS = {
    "current/fable5-cross-repository-safe-concurrency-research-status.md",
    "handoff/handoff-current.md",
    "notes/registries/project-research-display-name-registry-v0.1.md",
    "notes/todos/MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001.md",
}
FORBIDDEN_EXACT_PATHS = {"current/human-approved-spec.md", "README.md"}
FORBIDDEN_PREFIXES = ("commands/",)


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def run_text(args: list[str], cwd: Path, *, check: bool = True) -> str:
    cp = subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)
    if check and cp.returncode:
        raise RuntimeError(
            f"command failed: {args!r}; exit={cp.returncode}; "
            f"stdout={cp.stdout!r}; stderr={cp.stderr!r}"
        )
    return cp.stdout


def run_bytes(args: list[str], cwd: Path, *, check: bool = True) -> bytes:
    cp = subprocess.run(args, cwd=cwd, text=False, capture_output=True, check=False)
    if check and cp.returncode:
        raise RuntimeError(
            f"command failed: {args!r}; exit={cp.returncode}; "
            f"stderr={cp.stderr.decode('utf-8', errors='backslashreplace')!r}"
        )
    return cp.stdout


def load_manifest(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "manifest_id",
        "base_commit",
        "base_tree",
        "branch",
        "changed_path_count",
        "allowed_modify_paths",
        "files",
    }
    if not isinstance(obj, dict) or not required.issubset(obj):
        raise RuntimeError("manifest shape mismatch")
    if obj["manifest_id"] != EXPECTED_MANIFEST_ID:
        raise RuntimeError("manifest ID mismatch")
    return obj


def validate_manifest_policy(manifest: dict) -> list[str]:
    entries = manifest["files"]
    if not isinstance(entries, list):
        raise RuntimeError("manifest files must be a list")
    paths = [entry["path"] for entry in entries]
    if paths != sorted(paths):
        raise RuntimeError("manifest paths are not in canonical sorted order")
    if len(paths) != manifest["changed_path_count"] or len(paths) != len(set(paths)):
        raise RuntimeError("path count or duplicate mismatch")

    folded: dict[str, list[str]] = {}
    for path in paths:
        if not isinstance(path, str) or path.startswith("/") or ".." in Path(path).parts:
            raise RuntimeError(f"unsafe path: {path!r}")
        if path in FORBIDDEN_EXACT_PATHS or path.startswith(FORBIDDEN_PREFIXES):
            raise RuntimeError(f"forbidden path in publication manifest: {path}")
        if path.startswith("current/") and path not in EXPECTED_MODIFY_PATHS:
            raise RuntimeError(f"unexpected current/ path: {path}")
        folded.setdefault(path.casefold(), []).append(path)
    if any(len(group) > 1 for group in folded.values()):
        raise RuntimeError("case-insensitive path collision")

    manifest_modify_paths = set(manifest["allowed_modify_paths"])
    if manifest_modify_paths != EXPECTED_MODIFY_PATHS:
        raise RuntimeError("allowed modify-path set mismatch")

    entry_modify_paths = {entry["path"] for entry in entries if entry.get("operation") == "modify"}
    if entry_modify_paths != EXPECTED_MODIFY_PATHS:
        raise RuntimeError("entry modify-operation set mismatch")

    for entry in entries:
        operation = entry.get("operation")
        if operation not in {"add", "modify"}:
            raise RuntimeError(f"invalid operation for {entry['path']}: {operation!r}")
        expected_base_blob = entry.get("expected_base_blob")
        if operation == "modify" and not isinstance(expected_base_blob, str):
            raise RuntimeError(f"missing expected base blob: {entry['path']}")
        if operation == "add" and expected_base_blob is not None:
            raise RuntimeError(f"add entry unexpectedly declares a base blob: {entry['path']}")
    return paths


def verify_sources(manifest: dict, payload_root: Path) -> None:
    for entry in manifest["files"]:
        source = payload_root / entry["path"]
        if not source.is_file():
            raise RuntimeError(f"payload source missing: {entry['path']}")
        data = source.read_bytes()
        if len(data) != entry["bytes"]:
            raise RuntimeError(f"byte mismatch: {entry['path']}")
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"sha256 mismatch: {entry['path']}")
        if git_blob_sha1(data) != entry["git_blob_sha1"]:
            raise RuntimeError(f"git blob mismatch: {entry['path']}")


def verify_repo_base(manifest: dict, repo: Path, *, require_head_at_base: bool) -> None:
    base = manifest["base_commit"]
    resolved_base = run_text(["git", "rev-parse", base], repo).strip()
    tree = run_text(["git", "rev-parse", f"{base}^{{tree}}"], repo).strip()
    if resolved_base != base:
        raise RuntimeError("base commit object mismatch")
    if tree != manifest["base_tree"]:
        raise RuntimeError("root-tree/base mismatch")
    if require_head_at_base:
        head = run_text(["git", "rev-parse", "HEAD"], repo).strip()
        if head != base:
            raise RuntimeError("HEAD/base mismatch")

    for entry in manifest["files"]:
        path = entry["path"]
        cp = subprocess.run(
            ["git", "cat-file", "-e", f"{base}:{path}"],
            cwd=repo,
            text=True,
            capture_output=True,
            check=False,
        )
        exists = cp.returncode == 0
        if entry["operation"] == "add":
            if exists:
                raise RuntimeError(f"add path already exists at base: {path}")
        else:
            if not exists:
                raise RuntimeError(f"modify path missing at base: {path}")
            actual_blob = run_text(["git", "rev-parse", f"{base}:{path}"], repo).strip()
            if actual_blob != entry["expected_base_blob"]:
                raise RuntimeError(f"base blob mismatch: {path}")


def parse_name_status_z(data: bytes) -> dict[str, str]:
    parts = data.split(b"\0")
    if parts and parts[-1] == b"":
        parts.pop()
    if len(parts) % 2:
        raise RuntimeError("unexpected name-status -z structure")
    result: dict[str, str] = {}
    for index in range(0, len(parts), 2):
        status = parts[index].decode("ascii")
        path = parts[index + 1].decode("utf-8")
        if status not in {"A", "M"}:
            raise RuntimeError(f"unexpected staged status {status!r} for {path}")
        if path in result:
            raise RuntimeError(f"duplicate staged path: {path}")
        result[path] = status
    return result


def expected_status_map(manifest: dict) -> dict[str, str]:
    return {
        entry["path"]: "M" if entry["operation"] == "modify" else "A"
        for entry in manifest["files"]
    }


def materialize(manifest: dict, payload_root: Path, repo: Path, paths: list[str]) -> None:
    for entry in manifest["files"]:
        source = payload_root / entry["path"]
        destination = repo / entry["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source.read_bytes())

    subprocess.check_call(["git", "add", "--", *paths], cwd=repo)

    staged = parse_name_status_z(
        run_bytes(["git", "diff", "--cached", "--name-status", "--no-renames", "-z"], repo)
    )
    if staged != expected_status_map(manifest):
        raise RuntimeError("staged operation/path map mismatch")

    if run_bytes(["git", "diff", "--name-only", "-z"], repo):
        raise RuntimeError("unstaged tracked changes exist")
    if run_bytes(["git", "ls-files", "--others", "--exclude-standard", "-z"], repo):
        raise RuntimeError("untracked files exist inside repository worktree")

    for entry in manifest["files"]:
        index_blob = run_text(["git", "rev-parse", f":{entry['path']}"], repo).strip()
        if index_blob != entry["git_blob_sha1"]:
            raise RuntimeError(f"index blob mismatch: {entry['path']}")


def verify_commit(manifest: dict, payload_root: Path, repo: Path, commit: str) -> None:
    parent = run_text(["git", "rev-parse", f"{commit}^"], repo).strip()
    if parent != manifest["base_commit"]:
        raise RuntimeError("commit parent mismatch")

    committed = parse_name_status_z(
        run_bytes(
            [
                "git",
                "diff-tree",
                "--no-commit-id",
                "--name-status",
                "--no-renames",
                "-r",
                "-z",
                commit,
            ],
            repo,
        )
    )
    if committed != expected_status_map(manifest):
        raise RuntimeError("committed operation/path map mismatch")

    for entry in manifest["files"]:
        data = run_bytes(["git", "show", f"{commit}:{entry['path']}"], repo)
        source = (payload_root / entry["path"]).read_bytes()
        if data != source:
            raise RuntimeError(f"committed byte mismatch: {entry['path']}")
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"committed sha256 mismatch: {entry['path']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--payload-root", required=True, type=Path)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--materialize", action="store_true")
    parser.add_argument("--verify-commit")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    paths = validate_manifest_policy(manifest)
    verify_sources(manifest, args.payload_root)
    verify_repo_base(manifest, args.repo, require_head_at_base=not bool(args.verify_commit))
    if args.materialize:
        materialize(manifest, args.payload_root, args.repo, paths)
    if args.verify_commit:
        verify_commit(manifest, args.payload_root, args.repo, args.verify_commit)

    print(
        json.dumps(
            {
                "status": "PASS",
                "manifest_id": manifest["manifest_id"],
                "changed_path_count": len(paths),
                "G2A_issued": False,
                "A1_executed": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
