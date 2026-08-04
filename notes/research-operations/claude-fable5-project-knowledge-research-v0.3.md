# Claude/Fable5 Project-Knowledge Research Workflow v0.3

> Non-execution-source operating guidance for the two current Stage-A Fable5 tasks. It repairs the observed boundary between ordinary-chat GitHub reads and Claude Research by making the exact task inputs persistent Project knowledge before Research starts. It does not execute Fable5, spend quota, modify the validation package, select an execution surface for V0, or authorize V0/V1.

```yaml
workflow_id: MNEMOSYNE-FABLE5-PROJECT-KNOWLEDGE-RESEARCH-001
version: 0.3.0
created_by_task: MNEMOSYNE-188
status: prepared_pending_PR_merge_not_empirically_validated
repository: 08822407d/Mnemosyne
execution_source: current/human-approved-spec.md
execution_source_modified: false
applies_to:
  - FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  - FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
```

## 1. Problem and direct evidence

A1 run 001 used this sequence:

```text
ordinary chat GitHub read
  -> four-path preflight PASS
  -> operator-reported full-input read
  -> enable Advanced Research
  -> Research executor could retrieve only the canonical task
  -> remaining 18 inputs inaccessible
  -> INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
```

The failure supports only a task-local conclusion:

```yaml
observed:
  ordinary_chat_GitHub_access_qualifies_later_Research_context: false_for_run_001
not_proven:
  universal_Claude_connector_failure: true
  hidden_backend_cause: true
  validation_package_defect: true
```

The previous v0.2 route avoided the transition by keeping Advanced Research off. That was a conservative fallback, not a validated repair of Research-mode input access.

## 2. Current official product facts reviewed on 2026-08-03

Authoritative sources:

```yaml
sources:
  GitHub_integration:
    url: https://support.claude.com/en/articles/10167454-use-the-github-integration
    claim_scope:
      - in_Projects_selected_GitHub_files_or_folders_are_added_to_Project_knowledge
      - Project_GitHub_content_can_be_synced_and_reconfigured
      - thoughtful_small_selection_is_recommended

  Research:
    url: https://support.claude.com/en/articles/11088861-use-research-on-claude
    claim_scope:
      - Research_operates_agentically_over_web_and_internal_context
      - web_search_must_be_enabled
      - Research_can_consume_usage_faster

  Project_RAG:
    url: https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
    claim_scope:
      - Project_knowledge_can_use_RAG_when_large
      - RAG_for_Projects_works_with_Research

  connector_safety:
    url: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
    claim_scope:
      - Research_may_invoke_enabled_connector_tools_automatically
      - write_capable_tools_should_be_disabled_when_not_needed

  file_limits:
    url: https://support.claude.com/en/articles/8241126-upload-files-to-claude
    claim_scope:
      - Project_files_have_a_30MB_per_file_limit
      - Project_file_count_is_unlimited_subject_to_content_and_context_limits
```

These facts support a stronger candidate than v0.2:

> Put the exact task inputs into a new one-run Project's Files/Project knowledge first; then run Research against that Project knowledge. Do not rely on chat-level GitHub state, raw GitHub URLs or a receipt from another execution context.

They do not prove that the current user account, Fable5 rollout or Research executor will successfully read every selected Project file. That remains an empirical gate.

## 3. Revised architecture

```yaml
surface:
  environment: new_one_run_Claude_Project
  Project_history: none
  Project_Memory_input: none
  Project_Instructions: minimal_read_only_task_boundary
  Project_Files: exact_task_specific_subset_only
  Project_File_source: GitHub_selection_or_exact_manual_upload
  whole_repository: prohibited
  visible_model: Fable_5
  visible_effort: Max
  Research:
    probe: enabled
    substantive_run: enabled_only_after_probe_PASS
  chat_level_GitHub_connector_during_Research: disabled
  other_connectors_during_Research: disabled
  repository_write: prohibited
```

The Project Files route is materially different from run 001:

```yaml
run_001:
  durable_internal_input_surface: absent
  ordinary_chat_connector_state: present
  later_Research_inheritance: assumed_and_failed

v0_3:
  durable_internal_input_surface: Project_knowledge
  Research_direct_access: required
  connector_inheritance_assumption: absent
```

## 4. Two-stage Research gate

### R0 — direct Project-knowledge visibility probe

R0 is a real Research invocation but not the substantive research report.

It must:

- use the same one-run Project and exact Project Files intended for the report;
- use Project knowledge only;
- avoid external web/source collection;
- read every required file named by the task manifest;
- return only a structured input-binding receipt;
- stop on any missing, truncated, mismatched or inaccessible file;
- issue no substantive disposition.

```yaml
R0_result:
  PASS: every_required_Project_file_is_readable_and_bound
  INPUT_OR_PROJECT_KNOWLEDGE_INTEGRITY_FAILURE: one_or_more_required_files_fail
  RESEARCH_SURFACE_NOT_SUPPORTED: Research_cannot_use_the_selected_Project_knowledge
  INVALID: wrong_Project_wrong_task_contamination_or_write_action
```

Operator cancellation rule:

> During R0, if the progress surface starts broad external-web collection before the Project-file gate is complete, stop/cancel the run. R0 is not allowed to consume a large source search merely to discover that internal inputs are missing.

R0 consumes some quota. Its purpose is to cap the risk of another full report run that cannot see its primary inputs.

### R1 — substantive report

R1 begins only after R0 returns `PASS`.

It must:

- remain in the same Project and same chat;
- keep the same model and effort selection;
- use Project knowledge as the primary audit object;
- use the web only as permitted by the canonical task;
- revalidate input access if any file becomes unavailable;
- return one complete canonical report and exactly one allowed disposition.

A failed R0 never automatically falls back to chat-level GitHub or raw URLs.

## 5. Project preparation controls

Each task uses a separate new Project.

```yaml
Project_controls:
  existing_Mnemosyne_continuity_Project: prohibited
  Project_prior_chats: 0
  Project_Files_before_selection: 0
  Project_Instructions:
    - one_run_read_only
    - use_only_named_Project_files_as_internal_evidence
    - no_repository_write
    - no_other_task_material
  files_selected_from_GitHub: exact_manifest_paths_only
  sync_after_selection: required
  unrelated_files: 0
  prior_Pro_or_Fable_reports: prohibited
  other_Stage_A_task_or_report: prohibited
```

After Project Files are populated, disable GitHub and all other connector tools in the Research chat. The files are already Project knowledge; keeping connector tools enabled creates an unnecessary access and write surface.

## 6. Selection and transfer fallback

Preferred:

```yaml
preferred:
  - add_exact_files_and_folders_to_Project_Files_via_GitHub
  - sync
```

Fallback:

```yaml
fallback:
  - manually_download_exact_manifest_set
  - upload_exact_files_to_Project_Files
  - preserve_filenames_and_a_transfer_receipt
```

Do not:

- add the whole repository;
- use only a repository hyperlink;
- use a chat-level GitHub read as proof of Research access;
- upload prior reports or the other task;
- transform, concatenate or omit source files without an explicit manifest and integrity review;
- ask Research to discover hidden inputs through public web search.

A future deterministic bundle may be introduced if the exact multi-file Project route proves too burdensome. This v0.3 workflow does not claim such a bundle already exists.

## 7. Cost and stop controls

```yaml
cost_controls:
  no_substantive_run_before_R0_PASS: true
  R0_external_web_collection: prohibited
  cancel_on_broad_external_collection_during_R0: true
  failed_R0_retry_same_configuration: prohibited
  configuration_change_required_before_retry: true
  automatic_second_full_run: prohibited
```

The operator records:

- visible model and effort;
- whether Project RAG is indicated;
- exact Project Files selection;
- R0 duration and any displayed source count;
- quota/fallback warnings;
- final R0 and R1 outputs.

## 8. Independence and route boundaries

A1 and A2 require separate Projects. A2 does not see A1's task or report before its independent run. Current staged policy still prefers adjudicating A1 before selecting A2, because A1 may require package amendments that change the A2 audit object.

This workflow does not:

- make Research output an execution source;
- authorize package amendments;
- select the manual surface;
- authorize V0/V1;
- modify Meta-Agent or non-FABLE health-review routes;
- attest the exact served backend;
- guarantee that official product behavior matches the current user's rollout.

## 9. Current evidence status

```yaml
v0_3_evidence_status:
  official_product_support_for_Project_knowledge_in_Research: present
  direct_empirical_A1_or_A2_run: absent
  R0_probe_result: absent
  R1_report_result: absent
  readiness: candidate_ready_after_MNEMOSYNE_188_merge
```

The first valid R0 is itself execution-surface evidence. A valid R1 is still required before any package or surface decision.