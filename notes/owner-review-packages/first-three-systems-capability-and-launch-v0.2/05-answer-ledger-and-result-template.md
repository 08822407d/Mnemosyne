# Answer Ledger and Clarification Result Template — OR-02 through OR-09

> The interviewer maintains a concise visible ledger in chat. This structured form is used only for the final clarification result or a later separately authorized repository record. It is not an execution source and does not approve, activate, create, or modify any system.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
template_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-TEMPLATE-002
question_range: OR-02_through_OR-09
repository_write_during_interview: false
```

## 1. Status vocabulary

Use one status per question or sub-question:

- `CONFIRMED` — the Owner explicitly confirmed the recorded interpretation;
- `PROVISIONAL` — current preference with a condition, experiment, or later review;
- `DEFERRED` — no decision now; safe default and revisit trigger recorded;
- `REJECTED` — option, group, item, or premise rejected;
- `NOT_APPLICABLE` — does not apply under the confirmed scope;
- `FRONTIER_REENTRY_REQUIRED` — package insufficient for a high-impact design/authority/privacy/activation decision;
- `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED` — decision depends on a current external fact;
- `MISSING_ARTIFACT_BLOCKS_DECISION` — an exact unavailable artifact is necessary.

Do not use `CONFIRMED` merely because the Owner did not object immediately.

## 2. Visible ledger format

Keep the chat-facing view short:

```text
人工抉择进度 — MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002

已确认：
- OR-02-A：<自然语言结果>

暂定：
- OR-03-C：<实验条件>

延期：
- OR-07-C：<安全默认与重访条件>

已拒绝：
- OR-08-A：<原因>

需当前事实核验：
- OR-09-C：<事实及影响>

需 Pro/frontier：
- OR-06：<原因>

当前问题：OR-02-B
剩余：OR-02-C 至 OR-09
```

Only display sections that contain items.

## 3. Per-sub-question capture

```yaml
subquestion_result:
  question_id:
  short_label:
  status:

  owner_answer:
    verbatim_or_safe_ref:
    message_or_time_ref:

  interviewer_interpretation:
  interpretation_confirmed: yes | no | provisional
  confirmation_ref:

  selected_items: []
  item_dispositions:
    - item_id_or_plain_name:
      disposition: required | adapted | triggered | experimental | deferred | rejected | not_applicable
      owner_reason_or_condition:
      interviewer_note:

  target_specific_objects:
    - object_name:
      disposition:
      condition_or_adaptation:

  selected_options: []
  rejected_options: []
  conditions_or_exceptions: []

  corrections:
    - previous_interpretation:
      correction:
      correction_ref:
      changed_preference_or_interviewer_misunderstanding:

  deferred:
    value: true | false
    safe_default:
    revisit_trigger:

  residual_uncertainty: []
  affected_later_questions: []

  external_fact_checks_required:
    - fact:
      decision_it_can_change:
      desired_owner_outcome_or_constraint:
      verification_route: ordinary_current_verification | bounded_behavior_test | Deep_Research_candidate | Fable_or_frontier_research_candidate
      execution_authorized: false

  missing_artifacts:
    - artifact:
      why_needed:
      safe_request_after_storage_or_authority_approval:

  frontier_reentry:
    required: true | false
    reason:
    affected_decision:
```

## 4. Expected sub-question inventory

The interviewer may add item-level children when the Owner requests OR-01-style review.

```yaml
question_inventory:
  OR-02:
    - OR-02-A durable_source_and_current_authority
    - OR-02-B continuity_cold_source_and_target_local_truth
    - OR-02-C controlled_evolution
    - OR-02-D objective_readable_correctable_interaction
    - OR-02-E capability_routing_and_safe_limits
    - OR-02-F real_use_learning_and_controlled_improvement
    - OR-02-TRIGGER common_triggered_modules
  OR-03:
    - OR-03-A Meta_Agent_required_additions
    - OR-03-B Meta_Agent_triggered_additions
    - OR-03-C Meta_Agent_early_experiments
    - OR-03-D Meta_Agent_target_specific_objects
  OR-04:
    - OR-04-A code_required_portable_additions
    - OR-04-B code_target_specific_objects
    - OR-04-C code_triggered_modules
    - OR-04-D code_experiments_and_deferrals
  OR-05:
    - OR-05-A language_required_portable_additions
    - OR-05-B language_target_specific_objects
    - OR-05-C language_triggered_modules
    - OR-05-D language_experiments_and_deferrals
  OR-06:
    - OR-06 target_repository_or_store_default
  OR-07:
    - OR-07-A structured_target_truth
    - OR-07-B work_source_customer_and_credentials
    - OR-07-C private_conversation_and_source_originals
    - OR-07-D non_authoritative_recovery_snapshots
  OR-08:
    - OR-08 preparation_and_bounded_real_use_order
  OR-09:
    - OR-09-A Meta_Agent_product_fact_priorities
    - OR-09-B code_toolchain_fact_priorities
    - OR-09-C language_surface_fact_priorities
    - OR-09-D verification_timing_and_order
```

## 5. Package-level result

```yaml
clarification_result:
  result_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002
  package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
  source_repository: 08822407d/Mnemosyne
  source_master_commit:
  OR_01_result_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
  catalogue_ref: notes/reusable-agent-capability-catalog-v0.2.md
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
    - question_id: OR-02
      subresults: []
    - question_id: OR-03
      subresults: []
    - question_id: OR-04
      subresults: []
    - question_id: OR-05
      subresults: []
    - question_id: OR-06
      subresults: []
    - question_id: OR-07
      subresults: []
    - question_id: OR-08
      subresults: []
    - question_id: OR-09
      subresults: []

  selected_shared_floor:
    required: []
    adapted: []
    triggered: []
    experimental: []
    deferred: []
    rejected: []

  target_selections:
    Meta_Agent:
      required: []
      triggered: []
      experimental: []
      deferred: []
      rejected: []
      target_specific_objects: []
    work_business_function_code_library:
      required: []
      triggered: []
      experimental: []
      deferred: []
      rejected: []
      target_specific_objects: []
    long_term_language_teacher_and_practice_Agent:
      required: []
      triggered: []
      experimental: []
      deferred: []
      rejected: []
      target_specific_objects: []

  repository_and_storage_preferences:
    target_local_default:
    structured_truth_preferences: []
    work_source_constraints: []
    private_original_preferences: []
    non_authoritative_backup_preferences: []
    implementation_authorized: false

  preparation_and_use_order:
    package_preparation_order: []
    first_bounded_use_preference:
    parallel_preparation_allowed:
    activation_or_pilot_authorized: false
    prerequisites_and_blockers: []

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
  target_repository_created: false
  private_material_ingested: false
  external_research_or_quota_used: false
```

## 6. Human-readable final summary

Before completion, show the Owner:

1. **共同最低能力：** confirmed/adapted/triggered/experimental/deferred items;
2. **Meta-Agent：** additions, objects, and unresolved activation/ownership items;
3. **代码库 Agent：** portable capabilities and target-specific records;
4. **外语教师 Agent：** portable capabilities and teaching/memory records;
5. **仓库与存储：** preferences, safe defaults, and unresolved privacy/authority decisions;
6. **准备顺序与首次真实使用：** clearly separated from activation authorization;
7. **当前产品事实核验：** facts, decisions affected, and timing;
8. **需要 Pro/frontier 的事项：** exact reasons;
9. **延期事项及安全默认：** revisit triggers;
10. **未授权/未改变：** repositories, targets, activation, private materials, external runs.

Ask the Owner to correct the summary. Silence is not confirmation.

## 7. Mapping after later save authorization

A later saved result remains evidence and routes changes to the correct owner:

| Result category | Candidate destination/role |
|---|---|
| shared-floor selection | Mnemosyne capability-selection/adoption candidate; not execution source |
| Meta-Agent selection | separate Meta-Agent-owned review/change candidate |
| code/language selection | target-intake and target-package candidate |
| target-local preference | architecture/intake decision candidate requiring exact preflight |
| private storage preference | privacy/storage decision requiring current fact and authority review |
| preparation/use order | urgent-route priority and activation-preparation evidence |
| provider fact needs | dated provider/product verification TODO |
| activation preference | separate Owner activation decision package |
| common-library ownership | frontier architecture question |

One result file must not directly modify every affected repository.

## 8. Suggested later save path

```text
notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md
```

This is a suggestion only. No file is created during the interview.

## 9. Later save preflight

Before any later repository write:

- verify latest `master` and open PR lineage;
- assign a new task ID rather than reusing MNEMOSYNE-204;
- confirm the result contains no private source or complete personal conversations;
- confirm whether only the result is saved or any candidate files are amended;
- preserve operator-visible model selection without backend claim;
- obtain exact allowed paths/actions and prohibited paths;
- create one branch and at most one draft PR;
- do not update Meta-Agent or targets without separate authorization.

## 10. Completion rule

`PARTIAL_WITH_DEFERRALS` is a valid outcome. A useful result narrows and routes the next work; it does not manufacture answers to privacy, product, activation, or missing-artifact questions.
