# MNEMOSYNE-239 — Blocked Ubuntu-successor incident record

```yaml
task_id: MNEMOSYNE-239
disposition: BLOCKED_CLOSED_NO_RETRY
base_commit: e726dea818dca9418181775d0e7dcd62eb6c464a
intended_branch: mnemosyne-239-f2-g2a-and-handoff-audit-closeout
stage: MATERIALIZE
proximate_cause: Windows_native_worktree_path_length_limit
payload_and_manifest_preflight: PASS
base_and_validation_refs: PASS
local_clone_created: true
local_branch_created: true
commit_created: false
remote_branch_created: false
push_performed: false
PR_created: false
G2A_issued: false
A1_executed: false
validation_repository_written: false
cleanup_performed: false
```

The exact 86-path payload and base verification passed. Windows rejected a manifest-authorized long path during `git add` before commit creation. The first reported failing path was:

```text
raw/validation-reviews/MNE-DR-005-MNEMOSYNE-235-236-dual-failure-forensic-audit-002/WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002-chat-natural-language-response.txt
```

The failure is an execution-surface limitation, not evidence that the substantive Fable/Pro artifacts or the payload member bytes were invalid. MNEMOSYNE-239 is nevertheless terminal under its one-shot contract. MNEMOSYNE-240 is a new additive Ubuntu-native successor; it does not retry 239 and uses a new task-number-aligned branch.

Exact uploaded output evidence is preserved under `raw/validation-reviews/MNEMOSYNE-239-publication-attempt/`.
