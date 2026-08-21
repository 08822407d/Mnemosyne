# MNEMOSYNE-237 — Deterministic Local-Git Recovery Publication

```yaml
task_id: MNEMOSYNE-237
repository: 08822407d/Mnemosyne
validation_repository_read_only: 08822407d/mnemosyne-target-lifecycle-validation-002
architecture: LOCAL_DETERMINISTIC_GIT_PRIMARY
base_commit: e726dea818dca9418181775d0e7dcd62eb6c464a
base_tree: de6474d8c4d75f9b445048129d862e190837f0a4
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
existing_branch: mnemosyne-235-f2-g2a-and-handoff-audit-closeout
changed_path_count: 69
write_authorized_by_task: true
Ready_PR_authorized: true
merge_authorized: false
G2A_issued: false
A1_execution_authorized: false
validation_repository_write_authorized: false
retry_authorized: false
cleanup_authorized: false
```

## Exact required inputs

```yaml
payload_zip:
  filename: MNEMOSYNE-237-repository-payload.zip
  bytes: 268791
  sha256: 82eda85120d9bdd1f167e6a3fac2dcc5a41885b0f159e13bb4f49469568fd488
payload_manifest:
  filename: MNEMOSYNE-237-repository-payload-manifest.json
  bytes: 27897
  sha256: e2b3077afffc70c8d9683c97b4de0600c10f2b75d1950a9de3aba10c7a980cd7
verifier:
  filename: verify_mnemosyne_237_publication.py
  bytes: 11054
  sha256: 9865da1850826ed163a8b043cbad5c6856eb5400ca35993faa54bc9e90926ca3
executor:
  filename: execute_mnemosyne_237_local_git.py
  bytes: 17861
  sha256: 25e06d8d871977103d10c39543258bda8e998f7080d050dc99fade767ce36c37
PR_body:
  filename: MNEMOSYNE-237-PR-BODY.md
  bytes: 4030
  sha256: d6843705eb7e6ee424a6bf9e474a69b035a14a0217dbf64a13ad0724a7812dd2
```

Any identity mismatch blocks before repository mutation.

## First operation

Use the GitHub connector to verify:

- primary `master` and `mnemosyne-235-f2-g2a-and-handoff-audit-closeout` both equal `e726dea818dca9418181775d0e7dcd62eb6c464a` and compare identical;
- no open PR exists from the branch;
- validation `master` equals `e8e3296922185b4b70997c2351d6f39423f2cd4f`;
- all five `v2a-a1-001-*` branches are absent and the validation repository has no open PR;
- current F2 status still records G2A/A1 false.

Then read the payload-local `notes/validation-run-decisions/MNEMOSYNE-237-RECOVERY-PUBLICATION-CONTRACT-001.md`. Block on any mismatch. Do not infer authority from the blocked 235/236 tasks.

## Execution

Use an authenticated local shell with `git`, `gh`, push credentials, configured `git user.name` and `git user.email`, and the supplied one-shot executor. Do not use the low-level object API or Contents API for publication.

The executor must:

- derive every path only from the parsed external manifest;
- verify the exact add-vs-modify base state and four expected base blobs;
- create one local commit, one non-force push to the existing branch, and one Ready PR;
- read back the fetched remote commit and all 69 files;
- preserve the complete structured execution receipt.

## Stop

The first mismatch or failed command returns `MNEMOSYNE_237_BLOCKED`. No retry, cleanup, second branch, second commit, force-push, amend, merge, G2A, A1, validation write or prior-object reuse.

Success line:

```text
MNEMOSYNE_237_READY_PR_CREATED
```
