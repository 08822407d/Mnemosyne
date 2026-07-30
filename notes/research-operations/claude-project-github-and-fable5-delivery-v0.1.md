# Claude Project/GitHub and Fable5 Research Delivery Workflow v0.1

> Non-execution-source operating design. This file records the verified/observed Claude.ai access model and a bounded delivery workflow for Mnemosyne Fable5 research tasks. It does not authorize a research run, GitHub write from Claude, validation execution, target-project modification, or execution-source change.

```yaml
workflow_id: MNEMOSYNE-CLAUDE-FABLE5-DELIVERY-001
created_by_task: MNEMOSYNE-183
verified_or_observed_at: 2026-07-30
repository: 08822407d/Mnemosyne
status: active_delivery_guidance_pending_empirical_connector_receipts
repository_write_by_Fable5: prohibited
research_execution_authority: user_only
exact_backend_identity: unknown_or_not_attestable
```

## 1. Product surfaces must be kept separate

### 1.1 Project Files / project knowledge

Official Anthropic documentation describes Project knowledge as persistent content used across all chats in that Project. GitHub content added from the Project knowledge area is selected by file/folder and added to that shared knowledge base. Selected GitHub content can be synchronized and reconfigured. Project knowledge may switch to RAG when it approaches the context limit.

Operational meaning:

```yaml
Project_Files:
  scope: all_chats_in_that_Project
  role: persistent_shared_project_knowledge
  capacity_effect: counts_toward_project_knowledge_and_may_trigger_RAG
  recommended_for_entire_Mnemosyne_repository: false
  independence_risk: prior_tasks_reports_or_keys_can_affect_later_project_chats
```

Do not add the whole Mnemosyne repository to Project Files. Use only a small, deliberately selected set when persistent cross-chat knowledge is genuinely required.

### 1.2 Chat-level `+` -> `Add from GitHub`

Anthropic documentation describes chat-level GitHub attachment as selecting repository files/folders for that chat. The 2026-07-30 user-observed UI instead says that a repository and branch are linked to the chat, nothing is downloaded immediately, and Claude reads through the GitHub connector when needed.

Because the observed rollout wording and the help article are not identical, treat exact behavior as current-surface dependent:

```yaml
Chat_GitHub_link:
  scope: current_chat
  expected_role: authenticated_read_connector_or_selected_chat_attachment
  whole_repository_preloaded: not_assumed
  arbitrary_file_read_without_explicit_path: not_assumed
  connector_success: must_be_verified_by_exact_path_receipts
  beta_or_rollout_variation: possible
```

The visible GitHub tree URL created by the `+` flow is evidence that the repository/branch was linked. It is not evidence that any mandatory file was successfully read. A manually pasted ordinary GitHub URL is not treated as equivalent to selecting GitHub through the `+` flow.

### 1.3 Project membership alone

Being inside a Claude Project does not by itself establish repository access. A run must have one of:

- exact task material in Project knowledge;
- exact files/folders attached to that chat;
- a chat-level GitHub connector link that successfully reads every required path.

A run that cannot prove one of these returns an input/repository integrity failure before analysis.

## 2. Preferred Fable5 independent-run environment

For adversarial or framing-independent Fable5 work:

1. use a fresh standalone chat outside an existing context-rich Project, or a new one-run Project;
2. do not reuse a Project whose Memory, Files, Instructions, prior chats, prior reports, hidden keys or prior adjudication may frame the result;
3. keep Project Files empty unless the exact task-specific selection route is deliberately chosen;
4. link GitHub at chat level through `+` and select the exact repository/branch;
5. provide the exact ready-task path and require file receipts before substantive work;
6. do not attach prior Pro/Fable reports unless the task explicitly makes them evidence.

The existing `Mnemosyne 复合评审` Project is suitable for continuity-oriented review, but it is not the preferred clean environment for the two independent Stage-A audits because its visible Memory and prior chats create an avoidable framing dependency.

## 3. Access routes for a ready task

### Route A — chat-level connector, preferred

```yaml
route: CHAT_GITHUB_ON_DEMAND
steps:
  - open_fresh_chat_or_one_run_Project
  - select_GitHub_via_chat_plus_menu
  - select_08822407d/Mnemosyne_and_required_branch
  - verify_repository_link_visible
  - send_exact_ready_task_path
  - require_task_and_mandatory_path_receipts
  - stop_if_any_path_is_missing_truncated_or_wrong_ref
Project_Files_required: false
whole_repository_added_to_Project: false
```

### Route B — explicit GitHub file/folder selection

Use when the current chat flow exposes a file/folder browser or when on-demand reads fail. Select only the exact set in the task's `input-manifest.yaml`. Folder selection is allowed when the manifest names the folder and the resulting file inventory is reviewed.

### Route C — manual upload fallback

Download and upload only the manifest-listed files. Do not upload the whole repository. The current Stage-A sets fit within the documented chat upload count when selected as listed. Preserve filenames and record the source commit.

## 4. Ready-queue and archive lifecycle

The only human-facing directory for runnable Fable5 tasks is:

```text
handoff/fable5-ready/
```

Rules:

```yaml
ready_queue:
  contains_only: runnable_user_authorized_candidates_not_yet_completed
  task_directory_required: true
  required_files:
    - task.md
    - OPERATOR.md
    - input-manifest.yaml
  completed_redirects_allowed_inside_ready_queue: false
  prior_reports_allowed_inside_ready_queue: false

on_completion_and_acceptance:
  - preserve_original_task_under_raw/research-reports/cycles/<cycle>/tasks/
  - preserve_report_or_receipt_under_the_same_cycle
  - remove_the_task_directory_from_handoff/fable5-ready/
  - update_cycle_manifest_and_current_status
  - optionally_leave_a_short_registry_redirect_outside_the_ready_queue

on_retirement_without_execution:
  - remove_from_ready_queue
  - record_reason_and_source_ref_in_a_non_runnable_archive_or_plan
```

`notes/research-prompts/` is retained as a legacy registry/history surface and may contain redirects. It is not the directory an operator should browse to find the next runnable Fable5 task.

## 5. Mandatory task contract

Every ready task must state:

- exact task ID and topic;
- exact ready-task path;
- repository and branch/commit rule;
- exact mandatory paths or attachment selection set;
- whether prior reports are prohibited;
- read-only/write boundary;
- input-integrity failure return;
- complete report return destination;
- archive destination after acceptance.

Every operator guide must state:

- which Claude surface to use;
- whether Project Files should remain empty;
- exact `+` menu operation;
- exact files/folders to select if needed;
- a copyable startup instruction;
- fallback behavior if GitHub reads fail;
- whether the Project/chat may be reused.

## 6. Current product-fact sources

Checked 2026-07-30:

- https://support.anthropic.com/en/articles/10167454-using-the-github-integration
- https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects
- https://support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- https://support.anthropic.com/en/articles/11088861-using-research-on-claude-ai
- https://support.anthropic.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai

Product behavior is time-sensitive. Operator-observed UI text should be recorded with date and compared with current official documentation. Connector availability, successful file reads, project-memory scope and exact model backend are never inferred from a repository hyperlink alone.

## 7. Current boundaries

This workflow does not:

- approve either Stage-A Fable5 run;
- assert that the connector will succeed in every chat;
- authorize Claude/Fable to modify GitHub;
- make Project Memory an execution source;
- require loading the whole repository;
- authorize prior-report contamination;
- change the underlying research questions or validation package by itself.
