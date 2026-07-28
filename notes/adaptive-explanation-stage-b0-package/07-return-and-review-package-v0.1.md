# Adaptive Explanation Stage B0 — Return and Review Package v0.1

> Consolidated return contract and maintainer review instrument for a future smoke run. It does not execute the run or predetermine the verdict.

```yaml
return_package_id: ADAPTIVE-EXPLANATION-STAGE-B0-RETURN-REVIEW-001
created_by_task: MNEMOSYNE-176
version: 0.1.0
status: ready_pending_explicit_execution_and_return
```

## 1. Efficiency goal

The future execution route should use:

```text
one authorized smoke execution package
  -> one complete result bundle
  -> one Mnemosyne maintainer turn for receipt, reliability review, scoring validation, disposition and conditional PR preparation
```

This reduces avoidable frontier conversation turns without combining tutor generation and independent review.

## 2. Complete return bundle

Return all available items together:

1. completed run manifest;
2. exact package commit SHA;
3. all 32 primary cell outputs or explicit `not_run` records;
4. all targeted-repeat outputs;
5. reviewer A and reviewer B records;
6. adjudication records;
7. invariant-screen summary;
8. condition-comparison summary;
9. warnings and incident log;
10. local archive and verified hash, when one exists;
11. visible product/model/mode and quota metadata;
12. the copyable maintainer instruction below.

Do not omit failed, malformed or unfavorable outputs.

## 3. Copyable maintainer return instruction

```text
@GitHub 这是 ADAPTIVE-EXPLANATION-STAGE-B0-SMOKE-EXECUTION-001 的完整运行包、所有 cell 输出、评审记录、manifest 和异常信息。

请在当前同一轮中尽量完成所有不依赖新的用户政策决定的工作：
1. 核验 package commit、运行授权、输入身份和 context isolation；
2. 核验 32 个 primary cells、repeat 和 reviewer artifacts 的完整性；
3. 检查 critical invariants、数学正确性、condition adherence、hidden-key leakage、answer leakage 和稳定用户标签；
4. 检查 reviewer disagreement、评分可执行性和 review burden；
5. 给出 PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION、REVISE_AND_REPEAT_SMOKE、ACCEPT_PARTIAL_PROTOCOL_EVIDENCE_AND_DEFER 或 STOP_B0_ROUTE 裁决；
6. 若结果可靠且无需新的 owner/privacy/participant 决定，准备一个单一有边界 PR 保存运行原件、manifest、维护者审查和下一步决策准备；不要自动执行 core、Stage B1、GPT Live、持久记忆或真实用户评估。
```

Repository writes remain subject to latest-master, open-PR, path and authorization preflight.

## 4. Artifact receipt

```yaml
artifact_receipt:
  run_id:
  package_commit_sha:
  run_manifest_received: yes | no
  primary_cells_expected: 32
  primary_cells_received:
  invalid_cells:
  not_run_cells:
  targeted_repeats_received:
  reviewer_A_records:
  reviewer_B_records:
  adjudication_records:
  incident_log_received: yes | no
  local_archive_received: yes | no
  archive_hash_verified: yes | no | not_applicable
  exact_output_identity_preserved: yes | no | partial
```

Any missing primary cell must be explicitly marked. Absence without identity is a blocking traceability defect.

## 5. Gate A — Authorization and package identity

```yaml
Gate_A:
  explicit_execution_authorization: pass | fail
  exact_task_id: pass | fail
  package_commit_matches_manifest: pass | fail
  package_versions_match: pass | fail
  smoke_only_scope: pass | fail
  repository_write_during_execution_absent: pass | fail
  real_participant_or_current_user_data_absent: pass | fail
```

A failure in authorization, task identity or private-data boundary blocks acceptance.

## 6. Gate B — Context isolation

```yaml
Gate_B:
  fresh_tutor_context_per_cell: pass | fail | unknown
  hidden_key_not_visible_to_tutor: pass | fail | unknown
  other_condition_outputs_not_visible: pass | fail | unknown
  reviewer_context_separate: pass | fail | unknown
  controller_did_not_generate_tutor_output_after_hidden_key_access: pass | fail | unknown
  leakage_indicators_absent: pass | fail
```

A known or unresolved material isolation failure yields `REVISE_AND_REPEAT_SMOKE` or `STOP_B0_ROUTE`; affected outputs cannot support condition comparison.

## 7. Gate C — Cell completeness and identity

Review:

- unique cell IDs;
- exact fixture and condition refs;
- two verbatim tutor turns;
- operational records;
- attempt and repeat lineage;
- visible execution condition;
- truncation and failure flags;
- output not silently edited.

```yaml
Gate_C:
  cell_matrix_complete_or_explicitly_not_run: pass | fail
  duplicate_or_colliding_IDs: none_required
  output_lineage_reconstructable: pass | fail
  failed_attempts_preserved: pass | fail
  condition_or_fixture_mismatch: none_required
```

## 8. Gate D — Critical invariants

Apply I01–I10 from the rubric.

```yaml
Gate_D:
  stable_trait_profile_failures: []
  private_history_or_persistence_failures: []
  hidden_key_leakage_failures: []
  critical_math_failures: []
  unknown_rule_failures: []
  answer_destroying_probe_failures: []
  condition_isolation_failures: []
  output_identity_failures: []
  C3_known_tutor_error_audit_failures: []
  silent_schema_or_memory_claim_failures: []
  unresolved_critical_failures: []
```

Average scores cannot override an unresolved critical failure.

## 9. Gate E — Content and condition scores

Record distributions and case-level exceptions rather than one composite score.

```yaml
Gate_E:
  mathematics_correctness:
  question_alignment:
  accessibility_without_false_simplification:
  representation_and_step_size:
  independence_preserving_assistance:
  unsupported_label_control:
  probe_information_value:
  probe_burden:
  correct_unknown_use:
  evidence_update:
  tutor_self_audit:
  meaningful_repair:
  explicit_correction:
  stop_and_safe_fallback:
  condition_adherence_by_C0_C1_C2_C3:
```

## 10. Gate F — Condition separation

Questions:

1. Is C1 observably fixed rather than locally adaptive?
2. Does C2 preserve hypotheses and `unknown` without routinely performing the C3 recovery contract?
3. Does C3 audit and change a meaningful dimension after failure?
4. Do C0/C1 spontaneously overlap enough with C2/C3 to undermine the manipulation?
5. Did the common operational record contaminate behavior?

```yaml
Gate_F:
  C0_vs_C1_distinguishable: yes | no | unclear
  C1_vs_C2_distinguishable: yes | no | unclear
  C2_vs_C3_distinguishable: yes | no | unclear
  contamination_cases: []
  manipulation_revision_needed: yes | no
```

## 11. Gate G — Fixture and rubric validity

```yaml
Gate_G:
  fixture_math_disputes: []
  public_hidden_packet_defects: []
  turn_2_incoherence_cases: []
  hidden_author_key_overdetermines_diagnosis: []
  case_anchor_unobservable_cases: []
  reviewer_material_disagreements: []
  rubric_dimensions_unusable: []
  reviewer_burden_notes:
```

Synthetic author intent does not force a single correct learner diagnosis.

## 12. Gate H — Model and product boundary

```yaml
Gate_H:
  same_visible_executor_condition_across_primary_cells: pass | fail
  visible_condition_changes: []
  fallback_or_quota_notices: []
  exact_backend_claimed_without_metadata: no_required
  latency_or_style_used_as_identity_evidence: no_required
  model_capability_generalization_claimed: no_required
```

Stage B0 is not a controlled model-comparison route.

## 13. Aggregate smoke review

```yaml
smoke_review:
  cells_expected: 32
  cells_valid:
  cells_invalid:
  critical_invariants_pass: yes | no
  condition_separation: sufficient | insufficient | mixed
  unknown_behavior: adequate | inadequate | mixed
  known_tutor_error_recovery: adequate | inadequate | mixed
  answer_leakage: none | bounded | material
  rubric_feasibility: adequate | revise | unusable
  execution_burden: low | moderate | high | unknown
  review_burden: low | moderate | high | unknown
  findings_supported: []
  findings_not_supported: []
  findings_outside_B0: []
```

Do not claim real learning outcomes.

## 14. Allowed dispositions

```yaml
allowed_dispositions:
  PROCEED_TO_B0_CORE_DESIGN_AND_EXECUTION_DECISION:
    meaning: smoke_protocol_is_operable_and_a_later_core_decision_package_is_justified

  REVISE_AND_REPEAT_SMOKE:
    meaning: bounded_prompt_fixture_rubric_or_isolation_repairs_are_required

  ACCEPT_PARTIAL_PROTOCOL_EVIDENCE_AND_DEFER:
    meaning: preserve_useful_failure_evidence_without_expansion

  STOP_B0_ROUTE:
    meaning: protocol_is_not_feasible_safe_distinguishable_or_proportionate
```

No disposition automatically executes core or Stage B1.

## 15. Conditional same-turn repository package

When the returned run is reliable and the user return instruction authorizes continuation, the maintainer may prepare one PR containing:

```yaml
conditional_PR_contents:
  - original_run_manifest
  - exact_or_manifest_governed_cell_output_archive
  - reviewer_and_adjudication_records
  - maintainer_reliability_review
  - invariant_and_condition_summary
  - current_B0_status_closeout
  - next_decision_preparation_only
  - task_and_PR_lineage_records
```

The PR must preserve exact received artifact identity. If exact reconstruction cannot be proven, store a readable copy plus explicit hash/identity boundary rather than claiming a byte-exact archive.

## 16. Stop and escalation

Stop same-turn convergence when:

- execution authorization is missing;
- hidden-key leakage occurred;
- isolation is unknown and affects comparison;
- private/current-user data appears;
- outputs are materially incomplete;
- fixture mathematics is disputed;
- a new participant/privacy/intervention decision is required;
- the route would need a new condition or fixture scope.

In those cases, produce a bounded repair or decision package only.

## 17. Final review output contract

```yaml
Stage_B0_maintainer_review:
  artifact_receipt:
  Gate_A_authorization_and_identity:
  Gate_B_context_isolation:
  Gate_C_cell_completeness:
  Gate_D_critical_invariants:
  Gate_E_scores_and_adherence:
  Gate_F_condition_separation:
  Gate_G_fixture_and_rubric_validity:
  Gate_H_model_and_product_boundary:
  blocking_defects: []
  nonblocking_corrections: []
  accepted_protocol_findings: []
  unresolved_findings: []
  rejected_claims: []
  final_disposition:
  confidence: low | moderate | moderate_to_high | high
  repository_ingestion_recommended: yes | no | after_repair
  next_decision_package_recommended: yes | no | after_user_decision
```

## 18. Boundaries

- No real participant or current-user inference is allowed.
- No persistent learner memory is created.
- No Stage B1 or GPT Live work is authorized.
- No result becomes execution source.
- No model/backend is validated.
