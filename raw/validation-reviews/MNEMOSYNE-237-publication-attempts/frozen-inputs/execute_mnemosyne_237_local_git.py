#!/usr/bin/env python3
"""One-shot local-Git publisher for the frozen MNEMOSYNE-237 package.

The script performs one clone, one commit, one non-force push and one Ready PR creation.
It never retries.  All destination paths come from the external manifest and all exact-byte
checks are delegated to the supplied verifier.  A blocked run preserves a structured command
receipt and does not clean local or remote side effects.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import urllib.parse
import zipfile
from pathlib import Path
from typing import Any


PRIMARY_REPOSITORY = "08822407d/Mnemosyne"
VALIDATION_REPOSITORY = "08822407d/mnemosyne-target-lifecycle-validation-002"
EXPECTED_VALIDATION_MASTER = "e8e3296922185b4b70997c2351d6f39423f2cd4f"
A1_BRANCHES = [
    "v2a-a1-001-controller",
    "v2a-a1-001-alpha",
    "v2a-a1-001-beta",
    "v2a-a1-001-order-alpha-beta",
    "v2a-a1-001-order-beta-alpha",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def redact_arg(value: str) -> str:
    if "://" not in value:
        return value
    try:
        parts = urllib.parse.urlsplit(value)
    except ValueError:
        return "<redacted-url>"
    if parts.username is None and parts.password is None:
        return value
    host = parts.hostname or ""
    if parts.port:
        host = f"{host}:{parts.port}"
    return urllib.parse.urlunsplit((parts.scheme, host, parts.path, parts.query, parts.fragment))


def safe_command(args: list[str]) -> list[str]:
    return [redact_arg(str(arg)) for arg in args]


def run_command(
    receipt: dict[str, Any],
    args: list[str],
    *,
    cwd: Path | None = None,
    binary_stdout: bool = False,
) -> subprocess.CompletedProcess:
    sequence = len(receipt["commands"]) + 1
    cp = subprocess.run(
        args,
        cwd=cwd,
        text=not binary_stdout,
        capture_output=True,
        check=False,
    )
    record: dict[str, Any] = {
        "seq": sequence,
        "timestamp_utc": utc_now(),
        "command": safe_command(args),
        "cwd": str(cwd) if cwd else None,
        "exit_status": cp.returncode,
        "retry_count": 0,
    }
    if binary_stdout:
        stdout = bytes(cp.stdout)
        stderr = bytes(cp.stderr)
        record["stdout"] = {"bytes": len(stdout), "sha256": sha256_bytes(stdout)}
        record["stderr_text"] = stderr.decode("utf-8", errors="backslashreplace")
    else:
        record["stdout"] = cp.stdout
        record["stderr"] = cp.stderr
    receipt["commands"].append(record)
    if cp.returncode:
        raise RuntimeError(f"command failed at sequence {sequence}: {safe_command(args)!r}")
    return cp


def parse_ls_remote(stdout: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in stdout.splitlines():
        if not line.strip():
            continue
        sha, ref = line.split(maxsplit=1)
        result[ref] = sha
    return result


def require_primary_refs(receipt: dict[str, Any], repo_url: str, manifest: dict) -> dict[str, str]:
    cp = run_command(
        receipt,
        ["git", "ls-remote", "--heads", repo_url, "master", manifest["branch"]],
    )
    refs = parse_ls_remote(cp.stdout)
    expected = {
        "refs/heads/master": manifest["base_commit"],
        f"refs/heads/{manifest['branch']}": manifest["base_commit"],
    }
    if refs != expected:
        raise RuntimeError(f"primary remote-ref precondition mismatch: {refs!r}")
    return refs


def require_validation_refs(receipt: dict[str, Any], validation_repo_url: str) -> dict[str, str]:
    cp = run_command(
        receipt,
        ["git", "ls-remote", "--heads", validation_repo_url, "master", *A1_BRANCHES],
    )
    refs = parse_ls_remote(cp.stdout)
    if refs.get("refs/heads/master") != EXPECTED_VALIDATION_MASTER:
        raise RuntimeError("validation master mismatch")
    unexpected = [name for name in A1_BRANCHES if f"refs/heads/{name}" in refs]
    if unexpected:
        raise RuntimeError(f"A1 branches unexpectedly present: {unexpected!r}")
    return refs


def require_no_open_prs(receipt: dict[str, Any], branch: str) -> None:
    run_command(receipt, ["gh", "--version"])
    run_command(receipt, ["gh", "auth", "status"])
    primary = run_command(
        receipt,
        [
            "gh",
            "pr",
            "list",
            "--repo",
            PRIMARY_REPOSITORY,
            "--state",
            "open",
            "--head",
            branch,
            "--json",
            "number,url",
        ],
    )
    if json.loads(primary.stdout) != []:
        raise RuntimeError("an open PR already exists from the recovery branch")
    validation = run_command(
        receipt,
        [
            "gh",
            "pr",
            "list",
            "--repo",
            VALIDATION_REPOSITORY,
            "--state",
            "open",
            "--json",
            "number,url",
        ],
    )
    if json.loads(validation.stdout) != []:
        raise RuntimeError("validation repository has an open PR")


def verify_input_identities(args: argparse.Namespace, manifest: dict) -> None:
    expected_zip = manifest.get("payload_zip")
    if not isinstance(expected_zip, dict):
        raise RuntimeError("payload ZIP identity missing from manifest")
    if args.payload_zip.stat().st_size != expected_zip["bytes"]:
        raise RuntimeError("payload ZIP byte-count mismatch")
    if sha256_file(args.payload_zip) != expected_zip["sha256"]:
        raise RuntimeError("payload ZIP SHA-256 mismatch")

    expected_pr_body = manifest.get("pr_body")
    if not isinstance(expected_pr_body, dict):
        raise RuntimeError("PR-body identity missing from manifest")
    if args.pr_body.stat().st_size != expected_pr_body["bytes"]:
        raise RuntimeError("PR-body byte-count mismatch")
    if sha256_file(args.pr_body) != expected_pr_body["sha256"]:
        raise RuntimeError("PR-body SHA-256 mismatch")

    tool_paths = {
        "notes/validation-tools/execute_mnemosyne_237_local_git.py": Path(__file__),
        "notes/validation-tools/verify_mnemosyne_237_publication.py": args.verifier,
    }
    entries = {entry["path"]: entry for entry in manifest["files"]}
    for repository_path, local_path in tool_paths.items():
        entry = entries.get(repository_path)
        if entry is None:
            raise RuntimeError(f"tool entry absent from manifest: {repository_path}")
        data = local_path.read_bytes()
        if len(data) != entry["bytes"] or sha256_bytes(data) != entry["sha256"]:
            raise RuntimeError(f"external tool identity mismatch: {local_path.name}")


def write_receipt(path: Path, receipt: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-url", required=True)
    parser.add_argument("--validation-repo-url", required=True)
    parser.add_argument("--payload-zip", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--verifier", required=True, type=Path)
    parser.add_argument("--pr-body", required=True, type=Path)
    parser.add_argument("--workdir", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument(
        "--commit-message",
        default="MNEMOSYNE-237: recover F2 G2A and handoff-audit closeout publication",
    )
    parser.add_argument(
        "--pr-title",
        default="MNEMOSYNE-237 — recover F2 G2A and handoff-audit closeout publication",
    )
    args = parser.parse_args()

    receipt: dict[str, Any] = {
        "task_id": "MNEMOSYNE-237",
        "status": "RUNNING",
        "started_at_utc": utc_now(),
        "commands": [],
        "G2A_issued": False,
        "A1_execution_authorized": False,
        "A1_executed": False,
        "validation_repository_written": False,
        "retry_count": 0,
    }
    stage = "INITIALIZE"
    payload_root: Path | None = None

    try:
        if args.workdir.exists():
            raise RuntimeError("workdir already exists; cleanup/reuse is prohibited")
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        stage = "VERIFY_INPUT_IDENTITIES"
        verify_input_identities(args, manifest)

        stage = "REMOTE_PREFLIGHT"
        initial_primary_refs = require_primary_refs(receipt, args.repo_url, manifest)
        initial_validation_refs = require_validation_refs(receipt, args.validation_repo_url)
        require_no_open_prs(receipt, manifest["branch"])
        receipt["preflight"] = {
            "primary_refs": initial_primary_refs,
            "validation_refs": initial_validation_refs,
            "open_prs": 0,
        }

        stage = "CLONE"
        run_command(receipt, ["git", "clone", "--no-tags", args.repo_url, str(args.workdir)])
        run_command(receipt, ["git", "checkout", manifest["branch"]], cwd=args.workdir)
        head = run_command(receipt, ["git", "rev-parse", "HEAD"], cwd=args.workdir).stdout.strip()
        if head != manifest["base_commit"]:
            raise RuntimeError("local branch base mismatch")
        name = run_command(receipt, ["git", "config", "--get", "user.name"], cwd=args.workdir).stdout.strip()
        email = run_command(receipt, ["git", "config", "--get", "user.email"], cwd=args.workdir).stdout.strip()
        if not name or not email:
            raise RuntimeError("git user.name and user.email must already be configured")
        receipt["git_identity"] = {"user_name": name, "user_email": email}

        stage = "EXTRACT_PAYLOAD"
        payload_root = args.workdir.parent / "mnemosyne-237-payload-extracted"
        if payload_root.exists():
            raise RuntimeError("payload extraction directory already exists")
        payload_root.mkdir()
        with zipfile.ZipFile(args.payload_zip) as archive:
            expected_names = [entry["path"] for entry in manifest["files"]]
            if archive.namelist() != expected_names:
                raise RuntimeError("ZIP/manifest ordered path mismatch")
            for info in archive.infolist():
                if info.filename.startswith("/") or ".." in Path(info.filename).parts:
                    raise RuntimeError(f"unsafe ZIP path: {info.filename}")
                destination = payload_root / info.filename
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(archive.read(info.filename))

        stage = "VERIFY_SOURCE_AND_BASE"
        run_command(
            receipt,
            [
                sys.executable,
                str(args.verifier),
                "--manifest",
                str(args.manifest),
                "--payload-root",
                str(payload_root),
                "--repo",
                str(args.workdir),
            ],
        )

        stage = "RECHECK_BEFORE_MATERIALIZE"
        if require_primary_refs(receipt, args.repo_url, manifest) != initial_primary_refs:
            raise RuntimeError("primary refs moved before materialization")
        if require_validation_refs(receipt, args.validation_repo_url) != initial_validation_refs:
            raise RuntimeError("validation refs moved before materialization")

        stage = "MATERIALIZE_AND_VERIFY_INDEX"
        run_command(
            receipt,
            [
                sys.executable,
                str(args.verifier),
                "--manifest",
                str(args.manifest),
                "--payload-root",
                str(payload_root),
                "--repo",
                str(args.workdir),
                "--materialize",
            ],
        )
        run_command(receipt, ["git", "diff", "--cached", "--stat"], cwd=args.workdir)

        stage = "RECHECK_BEFORE_COMMIT"
        if require_primary_refs(receipt, args.repo_url, manifest) != initial_primary_refs:
            raise RuntimeError("primary refs moved before commit")
        if require_validation_refs(receipt, args.validation_repo_url) != initial_validation_refs:
            raise RuntimeError("validation refs moved before commit")
        require_no_open_prs(receipt, manifest["branch"])

        stage = "CREATE_ONE_LOCAL_COMMIT"
        run_command(
            receipt,
            ["git", "-c", "commit.gpgsign=false", "commit", "-m", args.commit_message],
            cwd=args.workdir,
        )
        commit = run_command(receipt, ["git", "rev-parse", "HEAD"], cwd=args.workdir).stdout.strip()
        run_command(
            receipt,
            [
                sys.executable,
                str(args.verifier),
                "--manifest",
                str(args.manifest),
                "--payload-root",
                str(payload_root),
                "--repo",
                str(args.workdir),
                "--verify-commit",
                commit,
            ],
        )

        stage = "RECHECK_IMMEDIATELY_BEFORE_PUSH"
        if require_primary_refs(receipt, args.repo_url, manifest) != initial_primary_refs:
            raise RuntimeError("primary refs moved before push")
        if require_validation_refs(receipt, args.validation_repo_url) != initial_validation_refs:
            raise RuntimeError("validation refs moved before push")
        require_no_open_prs(receipt, manifest["branch"])

        stage = "ONE_NON_FORCE_PUSH"
        run_command(
            receipt,
            ["git", "push", "origin", f"HEAD:refs/heads/{manifest['branch']}"],
            cwd=args.workdir,
        )

        stage = "POST_PUSH_READBACK"
        remote_after_push = parse_ls_remote(
            run_command(
                receipt,
                ["git", "ls-remote", "--heads", args.repo_url, "master", manifest["branch"]],
            ).stdout
        )
        if remote_after_push.get("refs/heads/master") != manifest["base_commit"]:
            raise RuntimeError("master moved during publication")
        if remote_after_push.get(f"refs/heads/{manifest['branch']}") != commit:
            raise RuntimeError("post-push branch head mismatch")
        if require_validation_refs(receipt, args.validation_repo_url) != initial_validation_refs:
            raise RuntimeError("validation refs moved during publication")
        run_command(receipt, ["git", "fetch", "origin", manifest["branch"]], cwd=args.workdir)
        fetched = run_command(receipt, ["git", "rev-parse", "FETCH_HEAD"], cwd=args.workdir).stdout.strip()
        if fetched != commit:
            raise RuntimeError("fetched remote branch does not equal local commit")
        run_command(
            receipt,
            [
                sys.executable,
                str(args.verifier),
                "--manifest",
                str(args.manifest),
                "--payload-root",
                str(payload_root),
                "--repo",
                str(args.workdir),
                "--verify-commit",
                fetched,
            ],
        )

        stage = "CREATE_ONE_READY_PR"
        pr_create = run_command(
            receipt,
            [
                "gh",
                "pr",
                "create",
                "--repo",
                PRIMARY_REPOSITORY,
                "--base",
                "master",
                "--head",
                manifest["branch"],
                "--title",
                args.pr_title,
                "--body-file",
                str(args.pr_body),
            ],
        )
        pr_url = pr_create.stdout.strip().splitlines()[-1]
        pr_view = run_command(
            receipt,
            [
                "gh",
                "pr",
                "view",
                pr_url,
                "--repo",
                PRIMARY_REPOSITORY,
                "--json",
                "number,url,state,isDraft,title,baseRefName,headRefName",
            ],
        )
        pr = json.loads(pr_view.stdout)
        if (
            pr.get("state") != "OPEN"
            or pr.get("isDraft") is not False
            or pr.get("baseRefName") != "master"
            or pr.get("headRefName") != manifest["branch"]
            or pr.get("title") != args.pr_title
        ):
            raise RuntimeError(f"PR verification mismatch: {pr!r}")

        receipt.update(
            {
                "status": "MNEMOSYNE_237_READY_PR_CREATED",
                "completed_at_utc": utc_now(),
                "stage": "COMPLETE",
                "commit": commit,
                "branch": manifest["branch"],
                "changed_path_count": manifest["changed_path_count"],
                "PR": pr,
            }
        )
        write_receipt(args.receipt, receipt)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        print("MNEMOSYNE_237_READY_PR_CREATED")
        return 0

    except Exception as exc:
        receipt.update(
            {
                "status": "MNEMOSYNE_237_BLOCKED",
                "completed_at_utc": utc_now(),
                "stage": stage,
                "error": repr(exc),
                "local_workdir_preserved": str(args.workdir),
                "payload_extraction_preserved": str(payload_root) if payload_root else None,
            }
        )
        write_receipt(args.receipt, receipt)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        print("MNEMOSYNE_237_BLOCKED")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
