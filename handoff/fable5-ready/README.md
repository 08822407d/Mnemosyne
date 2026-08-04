# Fable5 Ready Queue

> Human-facing queue for current Stage-A Fable5 research tasks. This directory is navigation and transfer support, not execution source or research evidence.

```yaml
queue_id: MNEMOSYNE-FABLE5-READY-QUEUE-001
created_by_task: MNEMOSYNE-184
last_updated_by_task: MNEMOSYNE-188
status: Project_knowledge_Research_candidate_queue_active_after_MNEMOSYNE_188_merge
repository: 08822407d/Mnemosyne
research_execution_authority: user_only
repository_write_by_Fable5: prohibited
```

## Current task state

```yaml
A1:
  directory: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
  attempts: 1
  substantive_reports_received: 0
  prior_result: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
  current_state_after_merge: READY_NOT_SELECTED
  current_contract_version: 0.3.0
  execution_surface: one_run_Project_Files_plus_Research_R0_R1

A2:
  directory: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
  attempts: 0
  substantive_reports_received: 0
  current_state_after_merge: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  current_contract_version: 0.3.0
  execution_surface: prepared_one_run_Project_Files_plus_Research_R0_R1
```

Each directory contains:

```text
task.md
OPERATOR.md
input-manifest.yaml
```

The active v0.3 execution contract is named by `task.md` and the manifest. Long canonical specifications remain under `notes/research-prompts/` and are unchanged.

## Access correction history

```yaml
run_001:
  ordinary_chat_GitHub_preflight: PASS
  later_Research_non_task_inputs_accessible: 0_of_18
  substantive_report: absent

v0_2:
  approach: Research_off_same_ordinary_chat
  role: conservative_fallback
  executed: false

v0_3:
  approach: exact_Project_Files_then_Research_direct_Project_knowledge_probe
  rationale:
    - selected_Project_files_become_Project_knowledge
    - Project_RAG_is_officially_documented_to_work_with_Research
    - no_chat_connector_inheritance_assumption
  empirical_R0_result: absent
```

## v0.3 Project and Research rules

```yaml
Project:
  new_one_run_Project_per_task: required
  prior_chats: 0
  existing_continuity_Project: prohibited
  Project_Files: exact_manifest_set_only
  whole_repository: prohibited
  sync: required

Research:
  visible_model: Fable_5
  visible_effort: Max
  R0_Project_knowledge_probe: required
  R1_substantive_report: only_after_R0_PASS
  chat_level_GitHub: disabled
  other_connectors: disabled
  repository_write: prohibited
```

R0 uses no external web sources and produces no substantive findings. If it begins broad external collection before binding Project files, the operator cancels it. A failed R0 is surface evidence only.

## Queue and execution-intent rules

```yaml
readiness_is_not_selection: true
A1_run_requested_by_queue_entry: false
A2_run_requested_by_queue_entry: false
quota_use_authorized_by_queue_entry: false
```

A task becomes a current user operation only after a maintainer response declares a `RUN_*` disposition and provides the complete visible operator flow. A2 additionally requires valid A1 adjudication and input freshness confirmation.

## Completion and retirement

After a substantive report is returned and accepted:

1. preserve the active execution contract and canonical specification in the research cycle;
2. preserve the report and R0 receipt;
3. update cycle manifest/current status;
4. remove the completed task from this queue;
5. leave historical redirects outside the ready queue.

Failed probes or input-binding runs are stored as `failed-runs/` evidence and do not count as substantive completion.

## Current operating guidance

```text
notes/research-operations/claude-fable5-project-knowledge-research-v0.3.md
```

Historical workflows remain available for audit but are not current operator guidance.