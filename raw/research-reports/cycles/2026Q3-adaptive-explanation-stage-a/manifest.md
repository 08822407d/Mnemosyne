# PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001 — Artifact Manifest

> Non-execution-source receipt and identity manifest for the accepted-with-corrections Stage A research report. This file does not attest the hidden serving model, approve a teaching policy, execute Stage B, assess the user, or authorize persistent learner memory.

```yaml
manifest_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001-MANIFEST-001
created_by_task: MNEMOSYNE-175
research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
repository: 08822407d/Mnemosyne
source_prompt: notes/research-prompts/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001.md
source_design: notes/adaptive-explanation-stage-a-research-design-v0.1.md
stored_report: raw/research-reports/cycles/2026Q3-adaptive-explanation-stage-a/PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001-report.md
evidence_role: accepted_with_maintainer_corrections_non_execution_source
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## Exact received artifact identity

```yaml
received_file:
  operator_filename: deep-research-report (5)(1).md
  bytes: 64304
  lines: 281
  words_whitespace_count: 7792
  sha256: a4d38a426cf1ba5a371a7ad19ae7b8fee16ae33dc539f5bb329066bf4edeca6f
  literal_https_URLs: 39
  citation_groups: 95
  unique_opaque_citation_refs: 56
  portable_source_table_rows: 39
  exact_research_ID_present: true
  exact_topic_present: true
  input_integrity_receipt_present: true
  substantive_research_completed_claimed: true
  final_report_not_plan_only: true
```

The repository copy preserves the received report text as the research artifact. Maintainer corrections are stored separately and do not rewrite the original report.

## Intake anomaly

During receipt, one conversation-level attachment preview exposed stale content from an earlier `PRO-DR-HO-GUIDANCE-001` plan-only artifact. Direct inspection of the uploaded file at the active runtime path showed a different, complete Stage A report with the exact identity above.

```yaml
preview_conflict:
  stale_preview_topic: PRO_DR_HO_GUIDANCE_001
  actual_uploaded_file_topic: PRO_DR_ADAPTIVE_EXPLANATION_STAGE_A_001
  preview_used_as_research_evidence: false
  artifact_selected_for_ingestion: exact_uploaded_file_bytes
  resolution_basis:
    - direct_file_read
    - exact_research_ID_and_topic
    - size_and_hash_inventory
    - substantive_report_content
```

This discrepancy is an input-transport/preview observability issue. It is not evidence of a particular backend or model route.

## Run metadata availability

```yaml
run_metadata:
  pre_run_receipt: not_provided
  start_time: not_provided
  end_time: not_provided
  duration: not_provided
  operator_visible_model_or_mode: not_provided
  visible_reasoning_or_intelligence: not_provided
  usage_counter_before: not_provided
  usage_counter_after: not_provided
  native_plan_text_or_screenshot: not_provided
  source_count_visible_in_product: not_provided
  source_panel_availability: not_provided
  inaccessible_source_list_from_operator: not_provided
  citation_or_export_warnings_from_operator: not_provided
  exact_served_backend: unknown_or_not_attestable
```

Missing run metadata does not invalidate the topic-bound report. It limits provenance and product-incident analysis and must not be silently reconstructed.

## Safety and scope receipt

```yaml
material_preflight:
  repository_visibility_treatment: public_risk
  report_subject: public_educational_research_and_candidate_experiment_design
  current_user_assessed_or_profiled: false
  private_or_customer_material_detected: false
  credentials_secrets_or_tokens_detected: false
  raw_private_chat_or_voice_transcript_included: false
  target_repository_or_connected_service_write_by_research: false
  result: pass_for_public_non_execution_source_storage
```

## Review disposition

```yaml
maintainer_review:
  review: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/01-maintainer-reliability-review.md
  calibration_ledger: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/02-claim-and-evidence-calibration-ledger.md
  Stage_B_decision_preparation: notes/research-batch-reviews/2026-07-adaptive-explanation-stage-a/03-stage-b-decision-preparation.md
  final_disposition: ACCEPT_WITH_CORRECTIONS_AND_PREPARE_STAGE_B_DECISION_PACKAGE
  another_Stage_A_clean_rerun_required: false
  Stage_B_experiment_authorized: false
```
