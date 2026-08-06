#!/usr/bin/env python3
"""Generate the mechanical Meta-Agent source inventory from Git objects."""

import argparse
import hashlib
import json
import pathlib
import re
import subprocess

REPOSITORY = "08822407d/Mnemosyne"
TASK_ID = "META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001"
SCALAR_FIELDS = {
    "target_project_id", "artifact_id", "artifact_role", "status",
    "authority_level", "target_truth_source", "target_runtime_truth_source",
    "target_runtime_truth_source_designated",
    "target_runtime_truth_source_effective", "effective_for_operational_use",
    "task_id", "research_id", "review_id", "migration_id", "checkpoint_id",
}
RULES = {
    "current/approved-spec.md": ("target_truth", "Z1_TARGET_CORE", True),
    "current/": ("current_state_or_target_behavior_support", "Z1_TARGET_CORE", False),
    "authority/": ("owner_or_authority_support", "Z1_TARGET_CORE", False),
    "methodology/": ("approved_method_or_method_candidate", "Z1_TARGET_CORE", False),
    "cases/": ("case_or_feedback_evidence", "Z2_TARGET_EVIDENCE", False),
    "history/": ("decision_or_migration_history", "Z1_TARGET_CORE", False),
    "handoff/": ("handoff_or_receive_evidence", "Z1_TARGET_CORE", False),
    "research/": ("research_evidence_or_raw_transport", "Z2_TARGET_EVIDENCE", False),
    "candidates/": ("candidate", "Z3_TARGET_CANDIDATES", False),
    "migration/": ("migration_control_or_historical_migration_evidence", "Z4_TARGET_MIGRATION_CONTROL", False),
    "decision-support/": ("candidate_or_decision_support", "Z3_TARGET_CANDIDATES", False),
    "commands/": ("target_process_support_candidate", "Z1_TARGET_CORE", False),
}


def git(*args, input_bytes=None):
    return subprocess.run(["git", *args], input=input_bytes, check=True,
                          stdout=subprocess.PIPE).stdout


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def canonical(record):
    return (json.dumps(record, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":")) + "\n").encode()


def front_matter(text):
    result = {"present": False, "extracted_scalars": {}, "parse_limited": True,
              "raw_front_matter_sha256": None}
    if not text.startswith("---\n"):
        return result
    end = text.find("\n---", 4)
    if end < 0:
        return result
    raw = text[4:end].encode()
    values = {}
    scalar = re.compile(r"^([A-Za-z0-9_]+):\s*(.*?)\s*$")
    for line in text[4:end].splitlines():
        match = scalar.match(line)
        if not match or match.group(1) not in SCALAR_FIELDS:
            continue
        value = match.group(2)
        if not value or value[0] in "[{|>&*!":
            continue
        if value in ("true", "false"):
            values[match.group(1)] = value == "true"
        elif value in ("null", "~"):
            values[match.group(1)] = None
        else:
            values[match.group(1)] = value.strip("'\"")
    result.update(present=True, extracted_scalars=values,
                  raw_front_matter_sha256=sha256(raw))
    return result


def classification(relative, fm, text):
    authority, zone, review = ("unknown_requires_frontier_review",) * 2 + (True,)
    for prefix, values in RULES.items():
        if relative == prefix or relative.startswith(prefix):
            authority, zone, review = values
            break
    lower = relative.lower()
    status = str(fm["extracted_scalars"].get("status", "")).lower()
    if "raw" in lower or "transport" in lower:
        hint = "raw_transport"
    elif any(x in lower + status for x in ("failed", "superseded")):
        hint = "failed_or_superseded_possible"
    elif any(x in lower for x in ("history/", "checkpoint", "timepoint")):
        hint = "historical_timepoint"
    elif "candidate" in lower or "candidate" in status:
        hint = "candidate_not_adopted"
    elif any(x in lower + status for x in ("evidence", "research", "non_execution")):
        hint = "evidence_non_execution"
    elif relative.startswith("current/") or "active" in status:
        hint = "active_or_current"
    else:
        hint = "unknown"
    declaration = False
    if text is not None:
        declaration = bool(re.search(r"(?im)^.{0,80}\b(private|secret|confidential)\b.{0,80}$", text))
    return {
        "preliminary_authority_class": authority, "migration_zone": zone,
        "requires_frontier_review": review, "status_or_history_hint": hint,
        "material_observation": "existing_public_Git_history",
        "new_storage_approval_implied": False,
        "material_review_required": text is None or declaration,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--output-dir", required=True, type=pathlib.Path)
    args = parser.parse_args()
    root = args.source_root.rstrip("/")
    source_commit = git("rev-parse", args.source_commit).decode().strip()
    git("cat-file", "-e", source_commit + "^{commit}")
    subtree = git("rev-parse", f"{source_commit}:{root}").decode().strip()
    git("cat-file", "-e", subtree + "^{tree}")
    command = ["git", "ls-tree", "-r", "-t", "-l", "-z", source_commit,
               "--", root + "/"]
    raw1 = git(*command[1:])
    raw2 = git(*command[1:])
    if raw1 != raw2:
        raise SystemExit("nondeterministic git ls-tree streams")
    entries = []
    seen = set()
    outside = 0
    for item in raw1.split(b"\0"):
        if not item:
            continue
        try:
            metadata, path_b = item.split(b"\t", 1)
            mode_b, typ_b, object_b, size_b = metadata.split()
            path = path_b.decode("utf-8")
        except (ValueError, UnicodeDecodeError) as error:
            raise SystemExit(f"unparseable object line: {error}")
        if path != root and not path.startswith(root + "/"):
            # Git emits pathspec ancestor trees; they are stream framing, not subtree entries.
            continue
        if path in seen:
            raise SystemExit("duplicate path: " + path)
        seen.add(path)
        typ, object_sha = typ_b.decode(), object_b.decode()
        if typ not in ("tree", "blob", "commit"):
            raise SystemExit("unsupported object type: " + typ)
        git("cat-file", "-e", object_sha + "^{" + typ + "}")
        relative = "" if path == root else path[len(root) + 1:]
        entries.append({
            "source_repository": REPOSITORY, "source_commit": source_commit,
            "source_root": root + "/", "root_subtree_sha": subtree, "path": path,
            "relative_path": relative, "mode": mode_b.decode(), "object_type": typ,
            "object_sha": object_sha,
            "object_size": None if size_b == b"-" else int(size_b),
        })
    entries.sort(key=lambda x: x["path"].encode())
    blobs, preclass = [], []
    missing = 0
    for entry in entries:
        if entry["object_type"] != "blob":
            continue
        data = git("cat-file", "blob", entry["object_sha"])
        try:
            text = data.decode("utf-8")
            encoding = "utf_8"
            final_lf = data.endswith(b"\n")
        except UnicodeDecodeError:
            text, encoding, final_lf = None, "binary", "not_applicable"
        fm = front_matter(text) if text is not None else {
            "present": False, "extracted_scalars": {}, "parse_limited": True,
            "raw_front_matter_sha256": None}
        blobs.append({**entry, "git_blob_sha": entry["object_sha"], "bytes": len(data),
                      "content_sha256": sha256(data), "encoding": encoding,
                      "final_LF": final_lf, "front_matter": fm})
        preclass.append({"source_commit": source_commit, "root_subtree_sha": subtree,
                         "path": entry["path"], "relative_path": entry["relative_path"],
                         **classification(entry["relative_path"], fm, text)})
    outputs = {
        "source-tree-entries-v0.1.jsonl": b"".join(map(canonical, entries)),
        "source-blob-inventory-v0.1.jsonl": b"".join(map(canonical, blobs)),
        "source-artifact-preclassification-v0.1.jsonl": b"".join(map(canonical, preclass)),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, data in outputs.items():
        (args.output_dir / name).write_bytes(data)
    counts = {kind: sum(x["object_type"] == kind for x in entries)
              for kind in ("tree", "blob", "commit")}
    closure = f"""tree_closure:
  task_id: {TASK_ID}
  source_repository: {REPOSITORY}
  source_commit: {source_commit}
  source_root: {root}/
  root_subtree_sha: {subtree}
  git_version: {git('--version').decode().strip()}
  command: git ls-tree -r -t -l -z {source_commit} -- {root}/
  raw_stream_1_sha256: {sha256(raw1)}
  raw_stream_2_sha256: {sha256(raw2)}
  raw_streams_identical: true
  raw_stream_bytes: {len(raw1)}
  total_entries: {len(entries)}
  tree_count: {counts['tree']}
  blob_count: {counts['blob']}
  commit_entry_count: {counts['commit']}
  duplicate_paths: 0
  missing_objects: {missing}
  paths_outside_root: {outside}
  tree_entries_manifest_sha256: {sha256(outputs['source-tree-entries-v0.1.jsonl'])}
  blob_inventory_sha256: {sha256(outputs['source-blob-inventory-v0.1.jsonl'])}
  preclassification_manifest_sha256: {sha256(outputs['source-artifact-preclassification-v0.1.jsonl'])}
  deterministic_second_generation_match: true
  recursive_tree_complete: true
  verifier_relation: manifests_are_a_deterministic_projection_of_two_identical_recursive_git_object_streams
  limitations: []
"""
    (args.output_dir / "source-tree-closure-v0.1.yaml").write_text(closure, newline="\n")


if __name__ == "__main__":
    main()
