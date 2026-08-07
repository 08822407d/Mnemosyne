# Paused Task — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

```yaml
queue_status: INDEFINITELY_PAUSED_BY_OWNER_AND_PENDING_VALID_A1_ADJUDICATION
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
display_name: MNE-DR-002 表面威胁
display_name_registry: notes/registries/project-research-display-name-registry-v0.1.md
pause_record: notes/route-pauses/frontier-clarification-validation-fable5-indefinite-pause-2026-08.md
resumption_handoff: handoff/mnemosyne-frontier-clarification-validation-fable-resumption-package.md
canonical_threat_model_specification: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
active_execution_contract_if_future_resumed: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.4.md
operator_guide_if_future_resumed: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
workflow_if_future_resumed: notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md
exact_topic: Independent threat model and evidence audit of a manual multi-conversation surface for Mnemosyne frontier-clarification V0
source_candidate_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
repository_access: read_only
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
current_execution_disposition: DEFERRED_INDEFINITELY_BY_OWNER_AND_DEPENDENCY
current_execution_requested: false
current_execution_required: false
quota_authorized: false
Project_creation_authorized: false
canonical_research_question_and_output_contract_changed: false
```

## Pause notice

**Do not create the A2 Claude Project, run Fable/Research, enable connectors, create live V0 contexts, or spend quota while the indefinite pause is active.**

The historical directory name `handoff/fable5-ready/` does not make A2 ready or selected.

A future separate conversation must first receive:

```text
handoff/mnemosyne-frontier-clarification-validation-fable-resumption-package.md
```

and stop after a receive-only pause/state receipt.

## Dependency remains active

```yaml
A2:
  attempts: 0
  current_disposition: DEFERRED_INDEFINITELY_BY_OWNER_AND_PENDING_VALID_A1_ADJUDICATION
  prerequisites_before_any_future_selection:
    - explicit_user_resumption_in_a_separate_dedicated_conversation
    - valid_A1_report_returned_and_adjudicated
    - A2_audit_object_confirmed_current
    - current_product_surface_reverified
    - explicit_RUN_disposition
    - explicit_quota_acceptance
```

A2 may not be resumed directly even after the general pause is lifted.

## Preserved future candidate

If all future gates pass, the preserved v0.4 candidate uses one Research invocation with an internal G0 semantic-coverage gate and G1 substantive threat model in the same invocation. It prohibits a separate paid visibility probe and any live V0 worker/reviewer/adjudicator or connector experiment.

Until the Owner explicitly resumes and selects A2 after a valid A1 adjudication, this file is preserved task material only.
