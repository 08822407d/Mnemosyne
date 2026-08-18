# V2-A A1 Package 003 — Canonical Runtime-Wrapper Transport and Comparison Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUNTIME-WRAPPER-COMPARISON-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-003
status: frozen_contract_not_authorization
```

The load-bearing runtime wrapper is the complete text block from `BEGIN` through `END`. Prose outside it is navigation only and cannot change the immutable package task. Canonical serialization is UTF-8 without BOM, LF line endings, no trailing spaces, and exactly one LF after the `END` line. Preserve exact line order and text; do not trim, reorder, case-fold, rewrap or otherwise normalize after canonicalization. Authorized and selected labels must each be one line and must not contain CR/LF. Exactly one role-specific selected-label placeholder may be replaced.

## Alpha template

```text
MNE_A1_RUNTIME_WRAPPER_V1_BEGIN
schema=MNE-A1-WORKER-RUNTIME-WRAPPER-001
run_id=MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
role=Alpha
task_id=MNE-V2A-A1-ALPHA-001
task_contract_path=notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md
task_contract_blob=9cb67f6e8b007941779326509db0b2d07fd035dd
repository=08822407d/mnemosyne-target-lifecycle-validation-002
branch=v2a-a1-001-alpha
required_current_branch_head=81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
owner_authorized_visible_label=<ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>
operator_selected_visible_label=__MNE_ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__
selected_evidence_class=operator_reported
backend_identity=unknown_or_not_attestable
prohibition_profile=MNE-A1-WORKER-PROHIBITIONS-001
MNE_A1_RUNTIME_WRAPPER_V1_END
```

## Beta template

```text
MNE_A1_RUNTIME_WRAPPER_V1_BEGIN
schema=MNE-A1-WORKER-RUNTIME-WRAPPER-001
run_id=MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
role=Beta
task_id=MNE-V2A-A1-BETA-001
task_contract_path=notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md
task_contract_blob=9544963bc40face1eb3caca190de6fe5f96802f5
repository=08822407d/mnemosyne-target-lifecycle-validation-002
branch=v2a-a1-001-beta
required_current_branch_head=81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
owner_authorized_visible_label=<BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>
operator_selected_visible_label=__MNE_BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__
selected_evidence_class=operator_reported
backend_identity=unknown_or_not_attestable
prohibition_profile=MNE-A1-WORKER-PROHIBITIONS-001
MNE_A1_RUNTIME_WRAPPER_V1_END
```

The controller fills only the authorized-label placeholder before freezing each template. The operator later replaces only the selected-label placeholder.

`MNE-A1-WORKER-PROHIBITIONS-001` means the union of the exact package-001 role task prohibitions plus: exact two-path write only; no branch/PR/evidence file; no peer runtime output; no other App/private material/quota; no model substitution, expected-value refresh, repair, retry, reset, force-push, rollback or cleanup; immediate stop on missing/unknown/mismatch. The profile ID alone is insufficient; controller/final reviewer verify exact package path/blob.

Before write, worker reconstructs and exactly compares the full block, labels, task path/blob, repository, branch/base and profile. Mismatch returns `WORKER_BLOCKED_BEFORE_WRITE` with no write.

Worker raw output must echo the complete received canonical block verbatim, report `received_wrapper_sha256`, and report its self-check fields. Owner returns the exact canonical block actually sent. Controller computes SHA-256 over all three canonical UTF-8/LF representations and then independently compares:

- expected frozen template with one selected-label substitution;
- exact Owner-sent block;
- exact worker-received echo.

Positive result requires all three byte-identical, all three SHA-256 values equal, exactly one permitted selected-label substitution relative to the frozen template, and every fixed field exact. This proves only equality of preserved text representations, not hidden backend identity or provider-signed telemetry.
