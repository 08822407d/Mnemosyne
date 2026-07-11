# MNEMOSYNE-107 Result Record

```yaml
task_id: MNEMOSYNE-107
task_name: Preserve Fable GF-STEP-2A output and safety-routing incident
task_type: cross_model_greenfield_step_storage_and_provider_incident_record
action_actor: ChatGPT_GitHub_app
started_from: post_MNEMOSYNE_106_after_PR_153_merge
branch: mnemosyne-107-step2a-and-routing-incident
base_branch: master
user_authorization_context:
  - future Fable replies and downloadable files that need GitHub recording may be stored and submitted as PRs without re-asking
  - ordinary ChatGPT Mnemosyne PRs default to ready, not draft
  - current xhigh scope is bounded prompt generation, receipt, structural validation, preservation, incident recording, and PR submission only
source_materials:
  - user-pasted successful Fable GF-STEP-2A chat summary
  - uploaded FABLE5-GREENFIELD-001-STEP2A-research-source-map.md
  - revised GF-STEP-2A prompt generated in this maintenance conversation
  - user screenshots of Fable-to-Opus routing and non-editable PASTED UI
  - user-uploaded partial intermediate output from the interrupted first attempt
files_created:
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-2A/manifest.yaml
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-2A/00-revised-prompt-as-sent.md
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-2A/01-fable-chat-summary.md
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-2A/02-research-source-map.md
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/incidents/INC-001-step2a-safety-routing.md
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/incidents/INC-001-partial-output-before-routing.txt
  - notes/codex-task-results/MNEMOSYNE-107-result.md
files_modified:
  - notes/cross-model-review-results/FABLE5-GREENFIELD-001/manifest.yaml
  - notes/cross-model-review-results/README.md
execution_source_modified: false
current_state_files_modified: false
handoff_files_modified: false
official_083_artifacts_modified: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
regression_formalized: false
operational_build_started: false
codex_task_generated: false
paused_post_handoff_route_resumed_or_closed: false
substantive_fable_review_performed: false
```

## Summary

MNEMOSYNE-107 preserves the successful bounded Fable 5 `FABLE5-GREENFIELD-001 / GF-STEP-2A` output and records the preceding provider safety-routing event as a separate operational incident.

The first attempt was visibly routed from Fable 5 to Opus 4.8 after producing partial intermediate text. It did not deliver the required artifact and is not canonical. The revised prompt was run in a fresh Fable 5 conversation with Research mode off and the same three pinned sources, and it completed successfully.

The incident record deliberately leaves the exact classifier category and trigger unknown. It does not call the task malicious, does not diagnose proprietary safety logic, and does not recommend bypassing safeguards.

## Preconditions and workflow verification

- PR #153 / MNEMOSYNE-106 was confirmed merged before this task began.
- Repository visibility was checked and was public before writing.
- The materials contain research cataloging, methodological boundaries, and UI-routing observations; no credentials or direct personal identifiers were detected.
- Screenshot binaries were not copied into the public repository; their hashes and relevant UI transcriptions are recorded.
- Branch `mnemosyne-107-step2a-and-routing-incident` was created before writes.
- `README.md` was fetched from that branch using an explicit ref before writes.
- Every contents-API write explicitly uses the branch.
- The resulting PR is created ready for review (`draft=false`); no auto-merge is authorized.

## Successful artifact integrity

```yaml
uploaded_filename: FABLE5-GREENFIELD-001-STEP2A-research-source-map.md
canonical_path: notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-2A/02-research-source-map.md
size_bytes: 27200
sha256: ac45e3c4217be8953bb0a2c379aa4e1d2c6bacac5e5f6c6610894f1b4dabb1a1
git_blob_sha_expected: 1c03aa480f90e45dc65542ab3f6c1cad9688e7e3
encoding: utf-8
line_endings: lf
final_lf_present: true
verbatim_status: byte_faithful_utf8_lf_copy
```

## Structural validation

- All 18 required sections are present.
- Eleven active reports are inventoried.
- Eleven research domains are mapped.
- Fifteen preliminary evidence signals are recorded.
- Six PDF visual-review limitations and nine date-sensitivity items are present.
- Four reports are selected for STEP2B; seven are deferred.
- The ending is clean; no artifact-control or tool-status leakage was detected.
- Fable reported approximately 3,397 words after one permitted light compression pass.
- Local counts are 3,433 whitespace-delimited tokens and 2,813 word-pattern matches. The difference reflects counting method and mixed Markdown/Unicode content.

## Routing incident record

The incident record preserves:

- the visible switch to Opus 4.8;
- the edit/retry UI wording;
- the fact that the pasted long task was not editable in place;
- the first attempt's partial intermediate output;
- source hashes for the two screenshots and partial-output text;
- the successful recovery procedure;
- explicit uncertainty about the proprietary classifier.

Public web reporting corroborates that Fable 5 can route some safeguarded requests to Opus 4.8 and that benign requests may be affected. No official Anthropic documentation exposing the exact classifier thresholds was found. External reporting is context only.

## Continuation status

The successful artifact records:

```yaml
GF_STEP_2A_status: GF_STEP_2A_complete_source_map_ready_for_STEP2B
selected_STEP2B_reports:
  - RPT-2026Q2-0001
  - RPT-2026Q2-0003
  - RPT-2026Q2-0004
  - RPT-2026Q2-0005
```

MNEMOSYNE-107 only preserves and indexes this advisory status. It does not execute STEP2B or substantively accept the report prioritization.

## Boundary

This result record is not execution source. It records preservation, structural validation, and provider-routing observations only. It does not approve or reject the STEP2A evidence map, diagnose or bypass a provider safety system, compare or repair the current design, modify execution source/current-state/handoff/official-083 artifacts, create target workspace/material/write/build/regression artifacts, generate a Codex task, authorize auto-merge, execute STEP2B, or resume/close the paused route.
