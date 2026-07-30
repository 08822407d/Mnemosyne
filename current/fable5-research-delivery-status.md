# Fable5 Research Delivery Status

> Non-execution-source current status for operator-facing Fable5 task delivery. `current/human-approved-spec.md` remains Mnemosyne's sole execution source.

```yaml
status_id: MNEMOSYNE-FABLE5-RESEARCH-DELIVERY-STATUS-001
created_by_task: MNEMOSYNE-183
repository: 08822407d/Mnemosyne
verified_master_before_task: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
status: delivery_workflow_and_ready_queue_prepared_in_MNEMOSYNE_183
research_executed: false
reports_received: false
repository_write_by_Fable5_authorized: false
```

## 1. Product-access finding

```yaml
Claude_Project_Files:
  role: persistent_project_knowledge_shared_across_project_chats
  whole_Mnemosyne_repository_recommended: false
  RAG_may_activate: true

Claude_chat_plus_GitHub:
  role: chat_scoped_repository_or_file_access
  current_UI_observation: repository_and_branch_link_read_on_demand
  file_read_success_assumed_from_link: false
  exact_path_receipts_required: true

Project_membership_alone_grants_repo_access: false
```

Official help documentation and the user's 2026-07-30 UI screenshots are not fully identical about whether the current chat flow first exposes a file browser or creates an on-demand repository link. The workflow supports both and blocks analysis when exact reads fail.

## 2. Ready queue

```text
handoff/fable5-ready/
```

Ready tasks:

```yaml
A1:
  id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  directory: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
  status: ready_not_executed

A2:
  id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  directory: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
  status: ready_not_executed
```

The two runs require separate fresh chats/projects and no cross-report visibility before both complete.

## 3. Recommended environment

```yaml
preferred:
  - fresh_standalone_chat_or_new_one_run_Project
  - empty_Project_Files
  - no_prior_Mnemosyne_or_Fable_reports
  - chat_plus_Add_from_GitHub
  - exact_ready_task_path
  - exact_commit_and_file_receipts

not_preferred_for_independent_Stage_A:
  - existing_Mnemosyne_复合评审_Project
reason:
  - visible_Memory
  - prior_chats
  - avoidable_framing_dependency
```

## 4. File lifecycle

```yaml
runnable_tasks:
  only_human_facing_location: handoff/fable5-ready/

completed_tasks:
  archive_under: raw/research-reports/cycles/<cycle>/
  remove_from_ready_queue: required

legacy_registry:
  path: notes/research-prompts/
  may_contain_completed_redirects: true
  use_for_runnable_task_discovery: false
```

## 5. Research state

```yaml
foundational_Pro_research: complete_adjudicated
foundational_Fable_research: complete_adjudicated_no_rerun
Stage_A_post_package_tasks: two_ready_not_executed
Stage_B_topics: four_deferred_not_runnable
V0_selected: false
V0_authorized: false
V0_executed: false
```

## 6. Exactly one safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_single_MNEMOSYNE_183_delivery_workflow_PR
  after_merge:
    - user_may_run_A1_and_A2_separately_using_each_OPERATOR_file
    - return_complete_reports_for_adjudication
  automatic_research_execution: false
  automatic_V0_execution: false
```
