# Answer Ledger and Clarification Result Template

> The interviewer maintains a concise visible ledger in chat and uses this structured form only for the final clarification result or a later separately authorized repository record. The template is not an execution source and does not itself approve any decision.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
template_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-TEMPLATE-001
repository_write_during_interview: false
```

## 1. Status vocabulary

Use one status per question or sub-question:

- `CONFIRMED` — Owner explicitly accepted the recorded interpretation;
- `PROVISIONAL` — Owner selected a current preference but left a condition or future review;
- `DEFERRED` — no decision now; safe default and trigger are recorded;
- `REJECTED` — Owner rejected the option, group, or premise;
- `FRONTIER_REENTRY_REQUIRED` — package is insufficient for a high-impact decision;
- `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED` — decision depends on a current external fact;
- `MISSING_ARTIFACT_BLOCKS_DECISION` — exact source/target material is absent;
- `NOT_APPLICABLE` — the question does not apply under confirmed scope.

Do not use `CONFIRMED` merely because the Owner did not object immediately.

## 2. Visible ledger after each question

The chat-facing ledger should remain short:

```text
人工抉择进度 — MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001

已确认：
- OR-01：<plain-language result>

暂定：
- OR-02-A：<condition>

延期：
- OR-07A：<safe default and trigger>

需外部事实核验：
- OR-09：<fact>

需 Pro/frontier 复核：
- OR-06：<reason>

当前问题：OR-02-B
剩余问题：OR-02-C ... OR-09
```

Only show sections that contain items.

## 3. Per-question capture

```yaml
question_result:
  question_id:
  short_label:
  status:

  owner_answer:
    verbatim_or_safe_ref:
    answer_time_or_message_ref:

  interviewer_interpretation:
  interpretation_confirmed: yes | no | provisional
  confirmation_ref:

  selected_options: []
  rejected_options: []
  conditions_or_exceptions: []
  corrections:
    - previous_interpretation:
      correction:
      correction_ref:

  deferred:
    value: true | false
    safe_default:
    revisit_trigger:

  residual_uncertainty: []
  affected_later_questions: []

  external_fact_checks_required:
    - fact:
      decision_it_can_change:
      verification_route: ordinary_current_verification | bounded_behavior_test | Deep_Research_candidate | Fable_or_frontier_research_candidate
      execution_authorized: false

  missing_artifacts:
    - artifact:
      why_needed:
      safe_request_after_approval:

  frontier_reentry:
    required: true | false
    reason:
    affected_decision:
```

## 4. Package-level result

```yaml
clarification_result:
  result_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-001
  package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
  source_repository: 08822407d/Mnemosyne
  source_master_commit:
  package_paths_loaded: []
  on_demand_source_paths_loaded: []
  cold_sources_deliberately_not_read: []

  interviewer:
    actor: ChatGPT
    product_surface: standard_ChatGPT_conversation_with_GitHub_connector_reads
    operator_visible_selection_verbatim:
    exact_backend: unknown_or_not_attestable
    same_conversation_model_switch_reported: true

  started_at:
  completed_at:
  completion_status: COMPLETE | PARTIAL_WITH_DEFERRALS | BLOCKED | ESCALATED

  question_results:
    - question_id: OR-01
      result_ref: embedded_below
    - question_id: OR-02
      result_ref: embedded_below
    - question_id: OR-03
      result_ref: embedded_below
    - question_id: OR-04
      result_ref: embedded_below
    - question_id: OR-05
      result_ref: embedded_below
    - question_id: OR-06
      result_ref: embedded_below
    - question_id: OR-07
      result_ref: embedded_below
    - question_id: OR-08
      result_ref: embedded_below
    - question_id: OR-09
      result_ref: embedded_below

  confirmed_decisions: []
  provisional_decisions: []
  deferred_items: []
  rejected_options_or_premises: []
  corrections_to_planner_interpretation: []
  external_fact_checks_required: []
  missing_artifacts: []
  frontier_reentries_required: []

  proposed_next_safe_action:
  repository_write_performed: false
  execution_source_modified: false
  Meta_Agent_modified: false
  target_repository_modified: false
  external_research_or_quota_used: false
```

## 5. Human-readable final summary

Before treating the interaction as complete, show the Owner a compact summary organized as:

1. **What you confirmed**
2. **What you changed from the planner's proposal**
3. **What remains provisional**
4. **What you deferred and the safe default**
5. **What needs current product verification**
6. **What must return to Pro/frontier**
7. **What the next concrete task would be**
8. **What was not authorized or changed**

Ask the Owner to correct this summary.

## 6. Candidate decision-record mapping

If the Owner later separately authorizes repository storage, the saved record should map decisions without automatically promoting them:

| Owner-review result | Candidate destination/role |
|---|---|
| catalogue wording/scope corrections | catalogue amendment candidate, not automatic overwrite |
| shared/target capability selections | target capability-selection candidate |
| target-local repository model preference | architecture/target-intake decision candidate |
| private storage preference | privacy/storage decision requiring exact target preflight |
| launch order | urgent-route priority/activation-preparation candidate |
| product fact needs | provider/product catalogue verification TODO |
| Meta-Agent activation preference | separate Meta-Agent Owner decision package |
| new common-library ownership idea | frontier architecture question |

One result file should not directly modify every affected source. Later tasks should apply changes to the correct owner repository with exact scope.

## 7. Suggested repository path after later authorization

```text
notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-001.md
```

This path is a suggestion only. During the interview no file is created.

## 8. Required storage preflight for a later save

Before a later repository write:

- verify execution-time latest `master`;
- verify no active duplicate task/PR lineage;
- assign a new task ID rather than reusing MNEMOSYNE-201;
- confirm the result contains no private source or complete personal conversation content;
- confirm whether only the result is stored or catalogue/selection files are also amended;
- preserve the operator-visible next-tier selection as reported, without backend claim;
- obtain exact allowed paths/actions and prohibited paths;
- create one branch and at most one draft PR;
- do not update Meta-Agent or targets unless separately authorized.

## 9. Completion rule

The interview can end with `PARTIAL_WITH_DEFERRALS`. It is not necessary to force decisions whose source, privacy, product facts, or consequences are not ready.

A useful result is one that makes the next task safer and clearer, not one that fills every field with false certainty.
