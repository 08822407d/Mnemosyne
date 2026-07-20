# Operator Evidence Record — MNEMOSYNE-ARTIFACT-DELIVERY-VALIDATION-001

> Non-execution-source evidence record. This file preserves operator-observed UI facts and artifact checks reported in the originating maintenance conversation. It does not prove hidden backend model identity and does not authorize external actions.

```yaml
validation_id: MNEMOSYNE-ARTIFACT-DELIVERY-VALIDATION-001
record_type: operator_evidence_record
recorded_by_task: MNEMOSYNE-137
execution_source: current/human-approved-spec.md
tested_guard:
  path: current/artifact-delivery-and-direct-generation-guard.md
  branch: master
  blob_sha: 95f9f404e5de0d06b52a9be314b2fb2e76636ac2
```

## Environment facts

```yaml
operator_observed_environment:
  project_name: Mnemosyne Artifact Delivery Validation
  project_memory_mode: Project-only
  project_instructions: empty
  library_access: disabled
  visible_model_label: GPT-5.6 Sol
  visible_reasoning_label: 极高
  Pro_selected: false
observation_boundaries:
  assistant_UI_observation_available: false
  hidden_model_identity_inferred: false
  automatic_model_routing_inferred: false
  internal_reasoning_implementation_inferred: false
  prior_context_expected: false
  prior_context_relied_upon: false
surface: ChatGPT_conversation
GitHub_task_authority: read_only
```

The operator supplied screenshots showing Project memory set to `Project-only`, project instructions empty, Library access disabled, and the model picker displaying `GPT-5.6 Sol` with reasoning level `极高`. These are operator-observed UI facts only.

## Guidance initialization result

The fresh conversation reported:

- behavior-guidance refresh only;
- `current/human-approved-spec.md` as the only execution source;
- no handoff started;
- no maintenance live route imported;
- no GitHub write authority;
- all five validation cases initially `NOT_RUN`;
- file-generation tooling available but not yet behavior-tested.

Required files reported read:

```yaml
guidance_files_read:
  README.md: e40643fc208a3a7d2b77c820021322781d0d09db
  current/human-approved-spec.md: 01f64a8223677829320c66dd46d3f172cc9155cc
  commands/load-mnemosyne-guidance.md: a555cbbb716ba225db6b8baaf1fc86c8bc8dbc2b
  current/artifact-delivery-and-direct-generation-guard.md: 95f9f404e5de0d06b52a9be314b2fb2e76636ac2
  notes/artifact-delivery-behavior-validation-v0.1.md: 2873e5e163bca712fd93719f6503e87075a3e42d
```

## Case-by-case operator checks

### ARTIFACT-DELIVERY-001

```yaml
filename: codex-scoped-repository-change-task-prompt.md
link_present: true
link_opened: true
file_downloaded: true
file_content_nonempty: true
full_long_prompt_duplicated_inline: false
github_write_observed: false
size_bytes: 16355
sha256: 3072fb778709243062c5cf5f3253e03e4a401676d86d0a034a670100ba4a8a47
```

The operator downloaded the file and returned it to the maintenance conversation. Maintainer-side mechanical size and SHA-256 checks matched the executor report.

### ARTIFACT-DELIVERY-002

```yaml
filename: synthetic-five-item-checklist.md
link_present: true
link_opened: true
file_downloaded: true
file_content_nonempty: true
extra_confirmation_requested: false
future_generation_only_response: false
github_write_observed: false
size_bytes: 397
sha256: 80775a5246a4115c5cf0d3789d3094aa29e67e174fb9832544c4a5d8cf85ae66
```

The operator downloaded the file and returned it to the maintenance conversation. Maintainer-side mechanical size and SHA-256 checks matched the executor report.

### ARTIFACT-DELIVERY-003

```yaml
concise_inline_answer: true
exactly_three_items: true
unnecessary_file_created: false
download_link_created: false
github_write_observed: false
```

The operator supplied a screenshot showing exactly three concise checklist items and no downloadable artifact.

### ARTIFACT-DELIVERY-004

```yaml
long_task_brief_created: true
downloadable_file_created: true
filename: deep-research-artifact-delivery-task.md
link_present: true
link_opened: true
file_downloaded: true
file_content_nonempty: true
full_long_prompt_duplicated_inline: false
complete_final_report_body_required: true
download_export_auxiliary_only: true
summary_or_link_only_prohibited: true
github_write_observed: false
size_bytes: 13198
sha256: 68c46821ed65b44b265d07df92d4b41b5eae01d2df5c9b1e75e9346c9a9e7fea
```

The operator downloaded the file and returned it to the maintenance conversation. Maintainer-side mechanical size and SHA-256 checks matched the executor report.

### ARTIFACT-DELIVERY-005

```yaml
result: NOT_RUN
reason: no_natural_tool_unavailability_or_generation_failure_observed
```

No artificial failure was induced. This conditional case is therefore not evidence about failure-handling behavior.

## Operator evidence limitations

- The maintenance conversation did not independently observe the fresh conversation's internal UI state; UI values are operator-reported and screenshot-supported.
- Successful download and return of all three files establish that the artifacts were obtainable, but do not constitute a formal no-write proof.
- GitHub write testing and §19 no-write proof were explicitly out of scope.
- Case 005 remains untested.
