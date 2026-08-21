# MNEMOSYNE-235/236 Dual-Failure — Consolidated Pro Adjudication 001

```yaml
adjudication_id: MNE-235-236-DUAL-FAILURE-FORENSIC-PRO-ADJUDICATION-001
source_Fable_task: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002
source_Fable_verdict: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
review_surface: current_ChatGPT_conversation_operator_reported_Pro
backend_identity: unknown_or_not_attestable
repository_write_performed_by_this_adjudication: false
G2A_issued: false
A1_execution_authorized: false
formal_recovery_architecture: LOCAL_DETERMINISTIC_GIT_PRIMARY
fallback_architecture: LOW_LEVEL_OBJECT_API_WITH_PER_CALL_RECEIPTS_ONLY
contents_API_sequential_commits: PROHIBITED
```

## 1. Input and evidence disposition

The eight Fable deliverables were received without alteration. The source output manifest's seven non-self entries match the corresponding uploaded bytes and SHA-256 values exactly. Both machine-readable ledgers parse as YAML.

The no-ZIP transport limitation remains explicit: Fable independently verified the Base64 evidence bundle against the original payload manifest, but did not independently inspect the original ZIP container. The ZIP-to-bundle link is therefore supported by the separately generated mechanical extraction receipt, not by a Fable observation of the container.

## 2. MNEMOSYNE-235

```yaml
cause_status: SUFFICIENTLY_DETERMINED
source_payload_integrity: PASS
proximate_cause: executor_path_case_drift_during_create_tree_entry_assembly
task_design_contribution: mechanical_path_derivation_not_mandatory
fail_closed_behavior: CORRECT
reachable_content_commit: none
branch_effect: empty_branch_at_original_base
retry_allowed: false
```

The correct manifest path existed exactly once. A staged tree path changed the uppercase task-ID filename component to the lowercase directory-style spelling. The executor introduced the immediate defect, while the task contract left a contributory gap by requiring exact content hashes without also requiring all tree paths to be emitted only from parsed manifest strings.

## 3. MNEMOSYNE-236

```yaml
cause_status: PARTIAL_ONLY
passed_gates:
  - source_and_manifest
  - exact_path_plan
  - recoverability
  - bounded_target_blobs
  - G2A_A1_state
recorded_stop_phase: create_blob_content_transport_before_final_tree
specific_root_cause: unknown
retry_allowed: false
```

The failed run did not preserve the exact filename, encoding, request body, HTTP/connector response, returned object SHA, or per-call order. Size, object ordering at create-blob time, and inherent source-content invalidity are not credible causes on the preserved evidence. Encoding declaration, request shape, connector semantics, and transport behavior remain unresolved. No exact cause is reconstructed.

## 4. Current Pro object-API investigation

The later Pro investigation is separate evidence. It proves that the connector can create unreferenced blobs and trees, and that a locally known or computed object ID is not proof that a correctly typed blob already exists in the target repository. It does not prove causal identity with the external MNEMOSYNE-236 failure.

No object from MNEMOSYNE-235, MNEMOSYNE-236, or the Pro investigation may be reused. No cleanup is authorized.

## 5. Architecture decision

```yaml
primary:
  architecture: deterministic_local_git_worktree
  requirements:
    - authenticated shell and git
    - exact base checkout
    - source-manifest-driven materialization
    - exact index/tree verification before commit
    - one local commit
    - one non-force push to the existing empty branch
    - post-push path/blob readback
  failure_geometry: remote_unchanged_before_push
fallback:
  architecture: low_level_Git_object_API
  requirements:
    - Base64 create_blob for every file
    - returned SHA plus readback receipt for every blob
    - one flat-path create_tree using the verified returned SHAs
    - candidate-tree verification before create_commit
    - one non-force update_ref
    - exact failing request and response preserved on first failure
rejected:
  architecture: Contents_API_sequential_commits
  reason: reachable_partial_publication_on_midrun_failure
```

The primary selection is `LOCAL_DETERMINISTIC_GIT_PRIMARY`. It removes the model from path construction and lets Git compute and transport a self-consistent object graph atomically at ref push.

## 6. Corrections to the Fable draft MNEMOSYNE-237 contract

The Fable draft is valuable design evidence but is not executable as written.

1. **Incorrect base-tree identity.** The draft states `de6474d84b5b4ada6b73b0f2545372f4bd50d975`; execution-time master `e726dea818dca9418181775d0e7dcd62eb6c464a` actually has root tree `de6474d8c4d75f9b445048129d862e190837f0a4`.
2. **Obsolete 41-path count.** The count omits the completed forensic audit, completed HVAL audit, their original files, new Pro adjudications, and the HVAL derivative. A new publication manifest must be generated from scratch.
3. **`handoff-current` direction conflict.** The staged Pro decision is to deprecate the file as a global route selector, not point it at MNEMOSYNE-237 as a new live handoff truth source.
4. **Result self-reference.** A one-commit publication cannot embed its own eventual commit SHA or PR URL. Committed result/finalization records must state that those values are carried by the external execution receipt and live PR, not use mutable placeholders or require a second commit.

These corrections do not invalidate the forensic findings or Architecture A recommendation. They require a Pro-generated final MNEMOSYNE-237 contract and a newly computed publication set.

## 7. Formal disposition

```yaml
Fable_forensic_findings: ACCEPTED_WITH_PRO_CORRECTIONS
MNEMOSYNE_235: CLOSED_BLOCKED_NO_RETRY
MNEMOSYNE_236: CLOSED_BLOCKED_NO_RETRY
recovery_architecture_ready: true
new_additive_task_id: MNEMOSYNE-237
repository_write_authorized_by_this_adjudication: false
safe_next_action: execute_only_the_Pro_frozen_MNEMOSYNE_237_package_on_an_authenticated_local_git_surface
```
