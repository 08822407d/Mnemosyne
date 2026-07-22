# Run-Context and PR-Provenance Adoption Record

> User-decision and implementation-scope record. This file is not execution source. The active behavior instrument is `current/run-context-and-pr-provenance-guard.md`; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
decision_id: MNEMOSYNE-RUN-CONTEXT-PR-PROVENANCE-ADOPTION-001
decision_task: MNEMOSYNE-147
decision_actor: user
implementation_actor: ChatGPT_GitHub_app
decision_status: approved_for_immediate_behavior_guard_implementation
research_basis:
  - FABLE5-GOV-001
  - DR07_independent_research_pair
```

## User-approved objective

Adopt the useful minimum recommendation from FABLE5-GOV-001 for Mnemosyne-related pull requests and important repository-writing tasks:

- record the current product/model selection honestly;
- use current official names rather than informal or stale labels when the mapping can be verified;
- distinguish operator-visible or operator-reported selection from hidden backend identity;
- use a compact structured run record for important tasks;
- disclose model/surface switches and reviewer independence;
- mark this initial implementation for later review and improvement by a reliably available Pro or stronger model.

## Adopted in this task

```yaml
adopted:
  - active_run_context_and_PR_provenance_behavior_guard
  - natural_language_disclosure_allowed_for_low_risk_work
  - compact_structured_run_record_required_for_important_repository_writes
  - PR_body_execution_context_section_for_important_PRs
  - current_official_model_and_reasoning_terminology_when_verifiable
  - operator_selection_separated_from_provider_documented_mapping
  - backend_identity_UNKNOWN_OR_NOT_ATTESTABLE_by_default
  - model_self_report_style_latency_and_verbosity_not_identity_evidence
  - model_or_surface_switch_segmentation
  - reviewer_and_independence_recording
  - heterogeneous_review_requirement_for_high_impact_execution_source_or_trust_boundary_acceptance_unless_user_exception
  - future_reliable_Pro_or_stronger_model_review_marker
```

## Deliberately deferred

The user authorization is implemented as a focused first slice, not as automatic adoption of every candidate in the research report.

```yaml
deferred:
  - full_T0_through_T5_governance_framework_as_a_global_schema
  - automatic_checkpoint_activation
  - complete_checkpoint_field_expansion
  - mandatory_heterogeneous_review_for_every_change
  - heavyweight_cryptographic_provenance
  - mandatory_API_or_admin_log_execution_for_ordinary_work
  - GF_STEP_5_substantive_adjudication
  - any_target_project_action
```

## Current official naming normalization

The user described the current selection as `gpt5.6sol thinking very high`. OpenAI's current official standard-ChatGPT terminology, verified on 2026-07-22, is:

```yaml
product_surface: standard_ChatGPT_conversation
official_reasoning_option: Extra High
provider_documented_model_mapping: GPT-5.6 Sol
higher_separate_option: Pro
provider_documented_Pro_model_mapping: GPT-5.6 Sol Pro
```

Official sources:

- https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes

The former `Thinking Heavy` label was renamed `Extra High`. This record does not claim that the particular response's backend was independently attested.

## Later review requirement

```yaml
later_review:
  required: true
  preferred_reviewer: reliably_available_GPT_5_6_Sol_Pro_or_stronger_heterogeneous_or_human_assisted_review
  review_targets:
    - field_burden_and_omission_rules
    - false_confidence_risk
    - official_naming_refresh_behavior
    - model_switch_segmentation
    - reviewer_independence_classes
    - high_impact_heterogeneous_review_exception_handling
  original_record_preserved: true
```

Later review may amend or supersede this guard through a new reviewed task and PR; it must not erase this original execution context.

## Boundary

This decision does not prove backend identity, activate a quality-incident checkpoint, adjudicate Fable GF-STEP-5, authorize target-project work, approve auto-merge, or adopt the deferred research candidates.
