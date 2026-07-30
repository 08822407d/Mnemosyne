# Claude Project, GitHub, and Fable5 Research Delivery Workflow v0.1

> Non-execution-source operating guidance for delivering bounded Mnemosyne research tasks to Claude/Fable5. This file does not authorize a research run, validation execution, GitHub write from Claude, target-project modification, or execution-source change.

```yaml
workflow_id: MNEMOSYNE-CLAUDE-FABLE5-DELIVERY-001
created_by_task: MNEMOSYNE-184
verified_or_observed_at: 2026-07-30
repository: 08822407d/Mnemosyne
status: active_after_MNEMOSYNE_184_merge
research_execution_authority: user_only
repository_write_by_Fable5: prohibited_unless_a_future_task_explicitly_changes_this_boundary
exact_backend_identity: unknown_or_not_attestable
```

## 1. Evidence classes used here

```yaml
product_fact_classes:
  official_current_documentation:
    role: strongest_available_product_description
  operator_observed_UI:
    role: current_account_and_rollout_evidence
  run_specific_connector_receipt:
    role: evidence_that_exact_paths_were_read_in_one_chat
  model_self_report_or_visible_link_only:
    role: insufficient_for_access_or_backend_attestation
```

Official documentation and the current observed UI are not fully identical. This workflow preserves the difference rather than silently choosing one description.

## 2. Project Files / project knowledge

Official Claude documentation states that content added to the Project knowledge area is available across all chats in that Project. GitHub content added there is selected by file or folder, can be synchronized, and can later be reconfigured. Project instructions also apply across Project chats.

```yaml
Project_Files:
  scope: persistent_across_all_chats_in_one_Project
  role: shared_project_knowledge
  GitHub_selection: specific_files_or_folders
  update_model: sync_and_reconfigure
  file_count: officially_unlimited
  practical_capacity: constrained_by_extracted_content_context_and_RAG_capacity
  RAG_activation: automatic_when_project_knowledge_approaches_context_limits
  recommended_for_entire_Mnemosyne_repository: false
```

The user's concern remains substantively valid even though the current official limit is not a simple fixed file-count ceiling. Adding the whole repository would:

- consume project-knowledge and RAG capacity;
- increase retrieval noise and stale-content risk;
- make independent reviews inherit unrelated files, prior reports, hidden keys or old task framing;
- increase synchronization and configuration burden;
- make it harder to prove what a particular run could see.

Therefore, Project Files should contain only a deliberately selected persistent subset when cross-chat reuse is genuinely needed. The whole Mnemosyne repository must not be added by default.

## 3. Project Memory is separate from Project Files

On paid plans, a Project can also have project-specific memory derived from chats in that Project. This is distinct from Project Files. A Project with empty Files may still carry prior-chat framing through Project Memory.

```yaml
independent_research_implication:
  existing_context_rich_Project: avoid_for_framing_independent_run
  preferred_environment:
    - fresh_standalone_chat
    - or_new_one_run_Project_with_no_prior_chats_and_empty_Project_Files
  existing_Mnemosyne_复合评审_Project:
    suitable_for: continuity_oriented_review
    not_preferred_for: independent_problem_reconstruction_or_adversarial_audit
```

## 4. Chat-level `+` -> `Add from GitHub`

Official documentation describes chat-level GitHub use as selecting specific repository files and folders for that chat. The user's 2026-07-30 UI instead displayed:

```text
Pick a repository and branch to link in this chat.
Claude reads it through the GitHub connector when it needs it.
Nothing is downloaded now, and sending is never blocked.
```

This is treated as operator-observed rollout behavior. It suggests an authenticated, chat-scoped, on-demand repository link, but does not prove that every arbitrary path can be read or that the entire repository is preloaded.

```yaml
Chat_GitHub:
  scope: current_chat
  official_documentation_model: selected_files_or_folders_are_accessed_and_processed
  observed_UI_model: repository_and_branch_linked_for_on_demand_connector_reads
  whole_repository_preloaded: not_assumed
  arbitrary_path_read_success: must_be_tested_in_that_chat
  visible_repository_hyperlink: link_receipt_only_not_file_read_receipt
  Project_Files_required_for_this_route: false
```

A chat inside a Project does not gain repository access merely because it belongs to that Project. It needs one of:

1. exact GitHub content already present in Project Files;
2. exact files/folders added to that chat;
3. a chat-level repository/branch link whose connector successfully reads every required path.

## 5. What the GitHub integration retrieves

Official documentation states that the integration retrieves file names and contents from a specific branch. It does not provide commit history, pull requests or other repository metadata as part of the synced content model.

Consequences:

- a task must not assume PR or commit-history access merely because GitHub is linked;
- branch-only UI cannot by itself attest an exact historical commit;
- when an audit is pinned to a commit but the UI exposes only a branch, the task must verify package IDs, versions, exact paths and consistency, and explicitly record the remaining commit-attestation limitation;
- if exact historical identity is material and cannot be established, return an integrity failure or use explicit files exported from that commit.

## 6. Research and connector boundary

Claude Research uses the web and connected internal context. Connector tools may be invoked during Research. For repository-bound Fable5 work:

```yaml
preferred_sequence:
  - keep_Research_off_during_connector_preflight
  - link_or_select_GitHub_in_the_same_chat
  - read_exact_entrypoint_and_manifest_paths
  - return_structured_path_receipts
  - enable_Research_only_after_preflight_passes
  - execute_the_task_in_the_same_chat
```

This sequencing separates a cheap access test from a quota-consuming research run and prevents a polished report from hiding a failed repository bind.

No write-capable connector or unrelated connected tool should be enabled for a read-only research task. GitHub platform permission is not research-task write authorization.

## 7. Model and effort receipt

For the current tasks, the preferred visible selection is:

```yaml
preferred_visible_condition:
  model: Fable_5
  effort: Max
```

The operator must record the exact visible model and effort text shown for the run. Any visible fallback, model change, quota warning or feature change must be recorded. Visible selection, response style, latency and model self-identification do not attest the exact served backend.

## 8. Access routes in priority order

### Route A — chat-level GitHub connector, preferred

Use when the current UI supports the repository/branch link shown by the user or equivalent chat-level GitHub selection.

```yaml
CHAT_GITHUB_ON_DEMAND:
  Project_Files: empty_or_unchanged
  whole_repository_added_to_Project: false
  steps:
    - open_fresh_chat_or_new_one_run_Project
    - select_Fable_5_and_Max_effort
    - keep_Research_off
    - click_plus_then_Add_from_GitHub
    - select_08822407d/Mnemosyne_and_required_branch
    - confirm_link_or_selection_receipt
    - send_exact_path_preflight_from_OPERATOR.md
    - continue_only_after_complete_read_receipts
    - enable_Research
    - send_the_task_startup_instruction
```

### Route B — explicit GitHub file/folder selection

Use when the current UI exposes a file browser, or when on-demand path reads fail. Select only the groups listed in `input-manifest.yaml`. Prefer selecting a task-specific folder over clicking each file separately.

### Route C — task-specific Project Files

Use only when persistent cross-chat access is required or chat-level selection cannot support the run. Prefer a new one-run Project. Add only the manifest-listed task folder and evidence folders/files. Do not add the whole repository. Remove or archive the one-run Project after the result is safely returned if no further reuse is approved.

### Route D — manual upload fallback

Download and upload only the manifest-listed files from the recorded source ref. Respect the current chat upload count and size limits. If the set does not fit comfortably, do not split it ad hoc across unrelated contexts; instead use folder selection, a connector route, or a deliberately generated single task bundle whose provenance is reviewed.

## 9. Mandatory connector preflight

Every repository-bound Fable5 run must first return:

```yaml
repository_read_preflight:
  task_id:
  repository: 08822407d/Mnemosyne
  selected_branch_or_ref:
  repository_link_visible: true | false
  exact_path_receipts:
    - path:
      complete_read: true | false
      visible_artifact_id_or_heading:
      source_identity_observed:
      limitation:
  Project_Files_used: true | false
  chat_level_GitHub_used: true | false
  Research_enabled_during_preflight: false
  write_action_performed: false
  result: PASS | INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
```

A repository URL, link chip or model statement that it "has access" is not enough. At least the ready entrypoint, canonical task and manifest must be read before Research starts. The task then verifies every mandatory evidence path.

## 10. Task classes and how much repository context to provide

### 10.1 Independent greenfield design

Purpose: reconstruct a problem without inheriting the existing solution.

Provide:

- the complete task statement;
- minimum authority, privacy and non-write boundaries;
- only source evidence explicitly needed for the question.

Do not provide the full repository, prior reports, adjudication or current preferred design unless the task explicitly audits them.

### 10.2 Repository-bound artifact audit

Purpose: challenge a concrete package, protocol, PR or design.

Provide:

- one ready-task directory;
- an exact input manifest;
- the bounded artifact folder(s);
- only the external authority/evidence files required to interpret those artifacts.

This is the class used by the two current Stage-A Fable5 tasks.

### 10.3 Broad repository health review

Purpose: discover unknown cross-cutting problems rather than review a fixed object.

Use a dedicated clean chat or Project and a staged repository-discovery contract:

1. link the repository read-only at chat level;
2. read a small repository map and authority packet first;
3. allow bounded on-demand search by path class;
4. record every material file accessed;
5. keep write tools disabled;
6. use staged findings so an initial inventory can narrow later reads;
7. stop if repository search or path-level reads are not demonstrable.

Do not preload the entire repository into a long-lived Project merely to support a broad review.

## 11. Human-facing ready queue

The sole operator-facing queue for runnable Fable5 tasks is:

```text
handoff/fable5-ready/
```

Each active task has one directory:

```text
handoff/fable5-ready/<TASK_ID>/
├── task.md
├── OPERATOR.md
└── input-manifest.yaml
```

Roles:

- `task.md`: short, stable entrypoint binding the task ID, canonical task and return route;
- `OPERATOR.md`: exact UI steps, copyable preflight/start prompt and fallbacks;
- `input-manifest.yaml`: exact required paths, grouping, source identity and contamination exclusions.

The ready queue contains only uncompleted runnable candidates. It contains no prior report, hidden reviewer key from another test, completed redirect or retired task.

## 12. Research prompt registry and lifecycle

`notes/research-prompts/` remains a design/registry surface, not the operator queue.

```yaml
lifecycle:
  draft:
    location: notes/research-prompts/
    operator_runnable: false_unless_also_published_to_ready_queue
  ready:
    required_operator_entrypoint: handoff/fable5-ready/<TASK_ID>/
  completed_and_accepted:
    actions:
      - preserve_original_task_under_raw/research-reports/cycles/<cycle>/tasks/
      - preserve_report_or_report_receipt_under_the_same_cycle
      - update_cycle_manifest_and_current_status
      - remove_the_task_directory_from_handoff/fable5-ready/
      - convert_or_replace_the_old_registry_path_with_a_short_completion_redirect_if_needed
  retired_without_execution:
    actions:
      - remove_from_ready_queue
      - preserve_reason_and_source_ref_in_a_non_runnable_plan_or_retired_record
```

Operators must never determine the next task by browsing all files in `notes/research-prompts/`. They use only `handoff/fable5-ready/` and the current research-delivery status.

## 13. Current official sources

Checked on 2026-07-30:

- `https://support.claude.com/en/articles/10167454-use-the-github-integration`
- `https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects`
- `https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects`
- `https://support.claude.com/en/articles/8241126-upload-files-to-claude`
- `https://support.claude.com/en/articles/11088861-use-research-on-claude`
- `https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings`
- `https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp`

Product behavior is time-sensitive. Reverify these facts and the current UI before a materially different future run.

## 14. Boundaries

This workflow does not:

- execute either current Fable5 task;
- assert that chat-level GitHub will succeed in every rollout;
- require loading the whole Mnemosyne repository;
- authorize Claude or Fable5 to write GitHub;
- make Project Memory or Project Files an execution source;
- permit prior-report contamination in an independent task;
- attest an exact backend;
- select or authorize V0/V1;
- modify Meta-Agent or the non-FABLE health-review route.
