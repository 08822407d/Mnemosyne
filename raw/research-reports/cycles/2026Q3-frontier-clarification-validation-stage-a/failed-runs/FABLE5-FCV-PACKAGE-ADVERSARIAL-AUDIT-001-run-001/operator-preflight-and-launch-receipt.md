# A1 Run 001 — Operator Preflight and Launch Receipt

> Normalized record of text supplied by the operator to the Mnemosyne maintainer conversation. It is not claimed to be a byte-identical export of the Claude chat and is not a substantive research report.

```yaml
run_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-RUN-001
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
artifact_role: operator_provided_execution_receipt
source: current_Mnemosyne_conversation_user_message
exact_original_message_bytes_preserved: false
repository_write_by_Fable5: false
```

## 1. Ordinary-chat four-path preflight

The operator returned this result:

```yaml
repository_read_preflight:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  repository: https://github.com/08822407d/Mnemosyne (08822407d/Mnemosyne)
  selected_branch_or_ref: master (HEAD 7bcddd60e209afe6496fa3091332496e20c3e245 at read time)
  repository_link_visible: true
  exact_path_receipts:
    - path: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
      complete_read: true
      visible_artifact_id_or_heading: "H1: Ready Task — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001; queue_status: READY_NOT_EXECUTED"
      source_identity_observed: task_id FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001; source_package_commit 67eb96d5317a2bb589236a4a8b2e75be2508d830
      limitation: none (1,955 bytes / 31 lines fully retrieved)
    - path: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
      complete_read: true
      visible_artifact_id_or_heading: "manifest_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-INPUTS-001 (v0.1.0)"
      source_identity_observed: task_id FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001; package_id MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001 (v0.1.0, merge_commit 67eb96d5…); repository 08822407d/Mnemosyne; the four preflight_minimum_paths match the four paths read here
      limitation: none (4,520 bytes / 85 lines fully retrieved)
    - path: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
      complete_read: true
      visible_artifact_id_or_heading: "H1: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 (canonical task, sections 1–17)"
      source_identity_observed: task_id FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001; repository 08822407d/Mnemosyne; pinned_baseline_commit 67eb96d5317a2bb589236a4a8b2e75be2508d830
      limitation: none (17,081 bytes / 379 lines fully retrieved; final line has no trailing newline and was verified byte-level)
    - path: notes/frontier-clarification-validation-package/README.md
      complete_read: true
      visible_artifact_id_or_heading: "H1: Frontier Clarification Validation Package"
      source_identity_observed: package_id MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001 (version 0.1.0, status prepared_not_selected_not_executed); repository 08822407d/Mnemosyne
      limitation: read at current master HEAD (7bcddd6…), which postdates pinned package commit 67eb96d5…; byte-identity to the pinned commit not attested (commit-level API access rate-limited this run). Manifest's current_master_allowed_only_if conditions otherwise satisfied — all required paths readable, package_id/version match, content consistent with manifest.
  Project_Files_used: false
  chat_level_GitHub_used: true
  Research_enabled_during_preflight: false
  write_action_performed: false
  result: PASS
```

## 2. Pre-launch reread and 19-input claim

Before the Advanced Research launch, the same Claude chat reported:

```text
Preflight re-verified before launch — gate result: PASS.

Re-read receipt: task.md (1,955 B, sha256 6d1ee40f…) and input-manifest.yaml (4,520 B, sha256 1bd196e5…) were re-fetched and are byte-identical to the copies fully read in the first preflight. Identity bindings re-confirmed: task_id FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001; package_id MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001, package_version 0.1.0, merge_commit 67eb96d5….

Mandatory-path verification (all 19 audit inputs): every path returned HTTP 200 with full content. All 15 package files and all 3 external adjudication files are byte-identical (sha256-compared) between the pinned package commit 67eb96d5317a2bb589236a4a8b2e75be2508d830 and current master HEAD 7bcddd60e209afe6496fa3091332496e20c3e245, via commit-addressed read-only raw retrieval. The canonical task file itself resolves at master only, which is expected and consistent: the manifest pins the source package to that commit, and the audit task postdates it.
```

The same response stated that the visible model was `Claude Fable 5`, Advanced Research was enabled for the authorized run, no effort-selector label was independently visible to the executor, and no repository write was performed.

## 3. Paid execution observation

The product UI then displayed:

```text
Warming up the engines...
Mnemosyne validation package audit
Research complete
151 sources and counting...
151 sources
6m 13s
```

The operator later reported approximately USD 8 of Fable5 quota use. This is an approximate operator report, not a billing receipt.

## 4. Final state conflict

The Advanced Research final response stated that only the canonical task was retrievable and all other 18 mandatory inputs were inaccessible. It did not accept the ordinary-chat preflight as independent proof for its own execution context.

```yaml
ordinary_chat_claim:
  canonical_task_complete: true
  all_19_audit_inputs_accessible: true
Advanced_Research_final_claim:
  canonical_task_accessible: true
  package_and_external_inputs_accessible: 0_of_18
  substantive_analysis_started: false
```

This conflict is the basis for the MNEMOSYNE-186 execution-surface repair. It is not resolved by choosing one self-report as universally authoritative; instead, the revised run removes the transition between the two contexts.
