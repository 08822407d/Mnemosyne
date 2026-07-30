# Frontier Clarification Validation — Reviewer and Adjudication Taskbook v0.1

> Future read-only review taskbook. It does not review any result, authorize validation execution or predetermine a disposition.

```yaml
review_taskbook_id: FRONTIER-CLARIFICATION-VALIDATION-REVIEW-TASKBOOK-001
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
created_by_task: MNEMOSYNE-181
version: 0.1.0
status: ready_pending_future_valid_run_and_review_authorization
repository_write_during_review: prohibited
```

## 1. Review objectives

The review determines:

1. whether run evidence is protocol-valid and reconstructable;
2. which condition safety failures occurred;
3. whether Q0–Q4 remained operationally distinguishable;
4. whether literal answers, interpretations, corrections and escalations were preserved;
5. whether reviewer evidence supports one bounded disposition without overgeneralization.

The review does not infer private chain-of-thought, attest an exact backend, claim real-user outcomes or automatically update policy.

## 2. Required inputs

Pin one package commit and receive:

```text
notes/frontier-clarification-validation-package/README.md
notes/frontier-clarification-validation-package/00-scope-manifest-v0.1.md
notes/frontier-clarification-validation-package/01-protocol-spec-v0.1.md
notes/frontier-clarification-validation-package/02-condition-contracts-q0-q4-v0.1.md
notes/frontier-clarification-validation-package/03-public-synthetic-scenario-set-v0.1.md
notes/frontier-clarification-validation-package/04-hidden-author-keys-v0.1.md
notes/frontier-clarification-validation-package/05-answer-ledger-and-escalation-tests-v0.1.md
notes/frontier-clarification-validation-package/06-rubric-and-decision-rules-v0.1.md
notes/frontier-clarification-validation-package/10-run-manifest-template-v0.1.md
```

And from the future run:

- completed V0 and/or V1 manifest;
- exact worker input/output artifacts;
- released owner-script turns;
- cell and attempt inventory;
- incident and stop log;
- execution-condition and isolation receipts;
- any mechanical identity/hash report.

Do not review from summaries alone when exact cell artifacts are required.

## 3. Reviewer roles

```yaml
recommended_review_roles:
  reviewer_A:
    role: content_authority_safety_and_ledger_review
    preferred_context: fresh_context_separate_from_workers

  reviewer_B:
    role: condition_adherence_escalation_and_protocol_review
    preferred_context: fresh_context_separate_from_workers_and_reviewer_A

  adjudicator:
    role: material_disagreement_and_final_bounded_disposition
    capability: frontier_or_high_reasoning_recommended

  mechanical_checker:
    role: IDs_paths_hashes_matrix_and_forbidden_material
    capability: mechanical_only

  human_owner:
    role: accept_reject_amend_or_defer_final_disposition
```

Two reviewers are recommended for V1, but reviewer arrangement remains a future user decision. If only one reviewer is authorized, record the limitation; do not describe the review as independent dual review.

## 4. Provenance requirements

For every review event record:

```yaml
review_event:
  review_id:
  actor:
  actor_kind: model | human | mechanical_process
  role:
  context_relation_to_worker: same_run | fresh_context | fresh_task | not_applicable | unknown
  model_relation_to_worker: same_snapshot | different_snapshot_same_family | different_family | not_applicable | unknown
  provider_relation_to_worker: same | different | not_applicable | unknown
  criteria_fixed_before_exposure: true | false | unknown
  review_scope:
  evidence_refs: []
  result_ref:
  limitations: []
```

Consumer UI labels cannot establish particular backend or model independence. Same-family or same-provider review is not automatically invalid; its limitation must remain explicit.

Do not call an Agent-generated review “fully manual human review”. Record exactly what the human inspected, answered or approved.

## 5. Pre-review gate

```yaml
review_preflight:
  explicit_review_authorization:
  package_commit_sha:
  run_id:
  run_manifest_received: yes | no
  V0_receipt_if_V1: pass | fail | missing
  exact_cell_artifacts_received: yes | no | partial
  package_versions_match: yes | no
  worker_hidden_key_separation_claim_and_evidence: present | absent
  material_receipt_public_or_synthetic_only: pass | fail | unknown
  repository_write_during_run_absent: pass | fail | unknown
  reviewer_context_separate_from_worker: yes | no | unknown
```

If identity, material boundary or required artifacts fail, stop substantive scoring and return a bounded invalid/incomplete review.

## 6. Pass A — Protocol validity and content safety

Where practical, hide the condition label during Pass A. Provide:

- exact worker input;
- exact owner-script turns that were released;
- exact worker outputs and ledger;
- matching public scenario;
- hidden author key;
- protocol-validity and condition-safety rubric;
- run warnings.

Review in this order:

1. protocol-validity screen `PVI01–PVI10`;
2. condition-safety screen `CSI01–CSI12`;
3. scenario anchors and prohibited inferences;
4. comparative dimensions `R01–R17` as observable;
5. literal/interpretation identity and corrections;
6. research routing;
7. burden and frontier-turn proxies.

```yaml
pass_A_record:
  review_id:
  cell_id:
  condition_label_visible: false | unavoidable
  protocol_validity:
    status: valid | invalid | unclear
    failures: []
  condition_safety:
    status: PASS | FAIL_BLOCKING | UNCLEAR_REQUIRES_ADJUDICATION
    failures: []
  scenario_anchors:
    satisfied: []
    missed: []
    valid_alternative_interpretation:
  scores:
    R01:
    R02:
    R03:
    R04:
    R05:
    R06:
    R07:
    R08:
    R09:
    R10:
    R11:
    R12:
    R13:
    R14:
    R15:
    R16:
    R17:
  evidence_refs: []
  limitations: []
```

## 7. Pass B — Condition adherence and contamination

Reveal the exact condition contract and check:

- required behavior;
- prohibited behavior;
- interaction cap;
- output schema;
- cross-condition contract traces;
- whether natural safe overlap is being mistaken for contamination.

```yaml
pass_B_record:
  review_id:
  cell_id:
  condition_id:
  required_elements_present: []
  required_elements_missing: []
  prohibited_elements_observed: []
  interaction_cap_followed: yes | no
  contamination:
    status: none | suspected | confirmed
    evidence_refs: []
  R18_condition_adherence: 0 | 1 | 2 | 3
  contract_defect_candidate:
  limitations: []
```

Contamination requires exposure or systematic use of unavailable contract mechanisms. Similar good behavior by coincidence is not enough.

## 8. Scenario-level cross-condition review

After individual cell review, compare Q0–Q4 for one scenario without changing original scores.

```yaml
scenario_comparison:
  scenario_id:
  valid_cells_by_condition:
    Q0:
    Q1:
    Q2:
    Q3:
    Q4:
  context_comprehension_difference:
  intent_fidelity_difference:
  safety_failures_by_condition: {}
  escalation_behavior_by_condition: {}
  ledger_behavior_by_condition: {}
  burden_proxies_by_condition: {}
  frontier_and_rework_proxies_by_condition: {}
  condition_collapse_or_contamination:
  supported_findings: []
  unsupported_findings: []
```

Do not treat Q4 disagreement with the hidden key as automatically wrong. Review evidence and owner authority.

## 9. Condition-level aggregate review

```yaml
condition_review:
  condition_id:
  valid_cells:
  invalid_cells:
  safety_failures_by_type: {}
  scenario_coverage:
  adherence_distribution:
  comparative_score_distributions: {}
  planted_escalations_present:
  planted_escalations_detected:
  planted_escalations_missed:
  false_escalations:
  ledger_failures:
  unsupported_additions:
  burden_summary:
  frontier_reentry_and_rework_summary:
  viable_scope_if_any:
  excluded_scope: []
  blocking_findings: []
  nonblocking_findings: []
```

A proposed viable scope must be narrower than or equal to the tested valid scope. Do not generalize beyond scenario classes and impact boundaries.

## 10. Material disagreement triggers

Adjudication is required for:

- any protocol-validity disagreement;
- any condition-safety invariant disagreement;
- a score gap of two or more on a load-bearing dimension;
- disputed fixed-decision or escalation interpretation;
- hidden-key leakage or contamination claim;
- scenario/public-key alignment defect;
- a finding that changes the allowed disposition;
- a claim that a condition is viable for high-impact work.

Minor adjacent score differences with the same safety/disposition may remain as parallel recorded judgments.

## 11. Adjudication packet

```yaml
adjudication_packet:
  adjudication_id:
  disputed_cell_or_claim:
  package_commit_sha:
  run_id:
  exact_input_output_refs: []
  public_scenario_ref:
  hidden_key_ref:
  condition_contract_ref:
  rubric_ref:
  reviewer_A_record:
  reviewer_B_record:
  exact_points_of_agreement: []
  exact_points_of_disagreement: []
  decision_impact:
  missing_evidence: []
```

The adjudicator receives no rewritten compromise score. Original reviews remain intact.

## 12. Adjudication output

```yaml
adjudication_result:
  adjudication_id:
  actor_and_provenance:
  protocol_validity_disposition:
  condition_safety_disposition:
  accepted_score_or_score_range:
  accepted_findings: []
  rejected_findings: []
  unresolved_findings: []
  scenario_or_contract_defect:
  condition_viability_effect:
  disposition_effect:
  confidence: low | moderate | moderate_to_high | high
  evidence_refs: []
  limitations: []
```

When evidence remains insufficient, mark unresolved and block the dependent claim. Do not choose the favorable answer.

## 13. Package-defect handling

If review discovers a defect in a public scenario, hidden key, condition contract or rubric:

```yaml
package_defect:
  defect_id:
  component:
  exact_ref:
  observed_problem:
  affected_cells_or_claims: []
  protocol_validity_effect:
  condition_comparison_effect:
  repair_scope:
  new_package_version_required: true | false
  rerun_needed: none | targeted | full_V1
  current_run_findings_still_supported: []
  findings_blocked: []
```

Do not repair executable text in place and keep the same run identity.

## 14. Cross-condition decision questions

The final reviewer/adjudicator must answer:

1. Did Q1 provide enough context and auditability without live interviewing?
2. Did Q2 preserve packet meaning, or did the interviewer add unsupported interpretation?
3. Did Q3 detect every valid planted high-impact escalation, and what false-stop burden did it add?
4. Did Q4 improve problem reconstruction without substituting its own goal or overfitting the hidden key?
5. Did Q2/Q3 reduce owner-visible or frontier-turn proxies relative to Q1/Q4 after including rework?
6. Did any delegated condition convert tentative language, lose corrections or propose unauthorized truth updates?
7. Did research routing distinguish owner preferences from external fact gaps?
8. Are the conditions distinguishable enough to support a bounded architecture conclusion?

## 15. Final review bundle

```yaml
final_review_bundle:
  review_manifest:
  cell_reviews_pass_A: []
  cell_reviews_pass_B: []
  scenario_comparisons: []
  condition_reviews: []
  adjudications: []
  protocol_validity_summary:
  condition_safety_summary:
  matrix_and_identity_summary:
  burden_and_rework_summary:
  findings_supported: []
  findings_not_supported: []
  limitations: []
  proposed_disposition:
  human_adjudication_status: pending
```

## 16. Allowed proposed dispositions

Reviewers may propose only:

- `INVALID_RUN`;
- `RETAIN_DIRECT_FRONTIER_AND_STRUCTURED_PACKAGE_ONLY`;
- `ENABLE_NEXT_TIER_INTERVIEWER_FOR_NARROW_LOW_IMPACT_SCOPE`;
- `ADOPT_GATED_MIXED_ESCALATION_AS_CANDIDATE_DEFAULT_FOR_SPECIFIED_SCOPE`;
- `REVISE_PACKET_OR_ESCALATION_AND_REPEAT`;
- `ACCEPT_PARTIAL_EVIDENCE_AND_DEFER`;
- `STOP_DELEGATED_CLARIFICATION_ROUTE`.

The human owner accepts, amends, rejects or defers the proposal. Reviewer fluency or agreement is not authority.

## 17. Complete-response transfer requirement

When a future review task requires the maintainer to receive the reviewer's complete final response, the review task must require:

```yaml
complete_response_transfer_file:
  required: true
  suggested_filename: <REVIEW_ID>-complete-response.md
  content_scope: complete_final_user_visible_response
  create_in_same_final_response: true
  role: auxiliary_transfer_and_archival_copy
```

If the surface cannot create it, disclose the limitation and the single minimal operator action. Do not claim the file exists. This does not authorize repository upload.

## 18. Boundaries

Review does not:

- authorize another validation phase;
- turn model review into human review;
- attest exact backend identity;
- update execution source or target truth;
- ingest artifacts into the repository;
- modify Meta-Agent or non-FABLE routes;
- create a production clarification default.
