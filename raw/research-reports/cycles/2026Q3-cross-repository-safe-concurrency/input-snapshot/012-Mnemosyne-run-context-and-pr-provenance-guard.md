# Run Context and Pull-Request Provenance Guard

> User-approved Mnemosyne behavior guard for recording AI execution context in important repository-writing tasks and pull requests. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only execution source. It operationalizes the actor/reviewer/provenance requirements in §§18–19 and the user-approved minimum recommendation derived from FABLE5-GOV-001.

```yaml
guard_id: MNEMOSYNE-RUN-CONTEXT-PR-PROVENANCE-001
created_by_task: MNEMOSYNE-147
current_record_version: v0.2
v0_2_repair_task: MNEMOSYNE-149
status: active_user_approved_behavior_guard
maturity: v0_2_bounded_capability_neutral_review_completed
review_record: notes/run-context-and-pr-provenance-v0.2-review-record.md
historical_version:
  version: v0.1
  merge_commit: e895e586fcda6783af567e3513b2c5f03ebd2d1c
  historical_records_are_not_rewritten: true
applies_to:
  - ordinary_ChatGPT_GitHub_app_repository_writes
  - Codex_repository_writes
  - cross_model_review_storage_and_adjudication_PRs
  - future_Agent_repository_writes
execution_source: current/human-approved-spec.md
research_basis:
  - FABLE5-GOV-001
  - RC-2026Q3-multi-model-adjudication-provenance
```

## 1. Purpose

The guard records what the operator, provider documentation, exact request metadata, and repository can honestly establish about a run without converting a visible product label into a claim about hidden backend identity.

It separates:

- actor and action source;
- product surface and operator-visible or operator-reported selection;
- provider-documented normalization or mapping;
- provider-attested served-model identifiers, when a supported non-consumer surface supplies them;
- hidden backend or weights-level identity;
- output and artifact identity;
- output quality, factual correctness, and architectural judgment assessments;
- reviewer relations, mechanical verification, and human adjudication;
- user authorization.

These dimensions must not be collapsed into a single `model:`, `review_independence:`, or `authorization:` scalar.

## 2. Canonical evidence vocabulary and claim limits

Every evidence-bearing field uses an array of evidence objects. A compound claim uses multiple objects; do not invent concatenated values such as `operator_reported_plus_provider_terminology_normalization`.

```yaml
evidence:
  - class: canonical_evidence_class
    ref:
    observed_or_accessed_at:
    claim_scope:
    detail:
```

The canonical evidence classes are:

```text
direct_user_instruction
operator_observed
operator_reported
provider_documented_mapping
provider_returned_request_metadata
organization_admin_or_audit_record
mechanically_verified_repository_evidence
model_self_report_untrusted
unknown_or_not_attestable
```

Rules:

1. `class`, `ref`, and `claim_scope` are required. `unknown_or_not_attestable` may use `ref: null`, but must state the reason in `detail`.
2. Time-sensitive observations and provider sources require `observed_or_accessed_at`.
3. A UI selection may establish what the operator selected; it does not independently attest the backend that executed the request.
4. Provider documentation may establish the provider's declared mapping at the access date; it does not prove what happened in a particular consumer-chat response.
5. Model self-identification is never identity evidence. Response speed, latency, style, verbosity, perceived intelligence, and displayed reasoning traces are not decisive identity evidence.
6. Artifact hashes establish exact bytes, not producer identity, model identity, factual correctness, or judgment quality.
7. `direct_user_instruction` supports only the authorization or human-decision claim scope stated in the instruction; it cannot support model or backend identity.
8. Claim-level citations, tests, hashes, or quote checks belong in `assessment_refs` or a separately referenced validation record rather than a new open-ended execution-evidence class. They support only the checked claim, do not validate the whole artifact, and cannot support a backend branch.
9. Evidence from different classes remains separate even when it supports adjacent fields.

Normative claim limits are centralized here so v0.2 instances do not repeat boilerplate:

| Field or evidence group | Does not prove |
|---|---|
| product surface, operator selection, or provider normalization | particular-request backend identity |
| provider-attested served-model identifier | weights-level identity or absence of routing/serving-stack change |
| artifact ref, Git object ID, or file hash | producer identity, correctness, or quality |
| review event | independence on an unrecorded dimension, human adjudication, or user authorization |
| human adjudication | factual correctness or technical completeness |
| user authorization | review, quality, correctness, or authorization for a later task |

### 2.1 Backend status

Consumer Chat always uses:

```yaml
backend:
  status: unknown_or_not_attestable
  reason:
```

Do not upgrade a Consumer Chat picker label, regenerate label, model self-report, behavioral inference, or ordinary admin event into backend attestation.

On another surface, a provider-attested served-model identifier may be recorded only when exact-request metadata and a provider contract define the returned field's semantics:

```yaml
backend:
  status: provider_attested_served_model_identifier
  served_model_identifier:
  exact_request_ref:
  evidence:
    - class: provider_returned_request_metadata | organization_admin_or_audit_record
      ref:
      observed_or_accessed_at:
      claim_scope: provider_attested_served_model_identifier_for_exact_request
  provider_field_name:
  provider_field_semantics:
  provider_contract_ref:
  provider_contract_accessed_at:
  does_not_prove:
    - weights_level_identity
    - absence_of_routing_or_serving_stack_change
```

An organization admin or audit record qualifies only when it identifies the exact request or event and the provider contract gives the relevant field semantics. The open-ended phrase `equivalently strong source` is not an allowed attestation path. If any required element is absent, use `unknown_or_not_attestable`.

## 3. Applicability, precedence, and burden

The most demanding applicable class takes precedence.

### 3.1 Low-risk work

Natural-language disclosure is sufficient only when the operation faithfully performs a mechanical action whose input, content, role, and destination are already fixed, and it involves no:

- selection among candidate inputs;
- interpretation, judgment, acceptance, or prioritization;
- current-state or reusable-behavior update;
- checkpoint, handoff, validation, review, research-interpretation, or downstream decision record;
- task prompt or artifact whose framing may materially guide a later agent.

Typo-only, formatting-only, link repair, and exact-byte storage can qualify. A mechanical substep inside an important task does not make the task low-risk.

### 3.2 Important repository-writing work

A compact v0.2 run record is required when a task:

- modifies current-state or reusable behavior guidance;
- creates or modifies a checkpoint, handoff, validation result, research interpretation, review result, or task prompt used by later agents;
- performs substantive acceptance, rejection, prioritization, or architecture judgment;
- modifies or proposes modifying the execution source;
- is explicitly designated by the user as important, high-risk, or intended for later review.

If any important trigger applies, the important classification wins even when part of the work is mechanical.

### 3.3 High-impact work

Execution-source changes and trust-boundary changes require heterogeneous review before final substantive acceptance unless the user explicitly approves a task-local exception. Mechanical verification and explicit human decision remain required; heterogeneous model review is evidence, not authority. This rule does not require heterogeneous review for every PR.

A task-local exception must use:

```yaml
heterogeneous_review_exception:
  decision_ref:
  exact_scope:
  reason:
  expires_with_task: true
  compensating_controls:
    mechanical_verification_refs: []
    human_adjudication_ref:
  residual_risk: []
  not_future_precedent: true
```

Platform permission, a previous exception, or a generic authorization statement is not an exception for the current task.

## 4. Compact v0.2 run-record schema

Important task result records contain the eight required core groups below. Core groups must not be omitted.

```yaml
run_context:
  schema_and_task:
    record_version: v0.2
    task_id:
    record_id:

  date_or_window:
    started_at:
    completed_or_recorded_at:

  action:
    actor:
    actor_kind: human | model | agent | mechanical_process | mixed
    source:
    switch_history:
      status: confirmed_none | recorded | unknown
      evidence: []

  product_surface:
    value:
    evidence: []

  operator_selection:
    verbatim:
    evidence: []

  backend:
    status: unknown_or_not_attestable
    reason:

  artifacts:
    status: recorded | confirmed_none | unknown
    refs:
      - ref:
        relation: created | modified | produced | stored | reviewed
        immutable_identity:
          status: recorded | not_available_before_merge | unknown
          type: git_commit_sha | git_blob_sha | sha256 | other
          value:

  user_authorization:
    status: authorized | not_authorized | unknown
    actor:
    decision_ref:
    authorized_actions: []
    excluded_actions: []
    evidence: []
    expires_with_task: true
    not_future_precedent: true

  limitations: []
  omissions: []
```

The following groups are conditional:

```yaml
provider_normalization:
  normalized_selection:
  normalized_reasoning_level:
  provider_documented_model_mapping:
  evidence: []

operator_reasoning_setting:
  verbatim:
  evidence: []

segments: []

review_events: []

human_adjudication:
  status: pending | recorded | not_required | unknown
  actor:
  decision:
  evidence: []
  limitations: []

assessment_refs: []

recovery_refs:
  checkpoint_ref:
  incident_assessment_ref:
  activation_record_ref:

lineage:
  review_disposition: accept_as_is | amend | supersede_for_scope | reject | defer
  reviews: []
  amends: []
  supersedes_for_scope: []
  preserves: []

heterogeneous_review_exception:
  decision_ref:
  exact_scope:
  reason:
  expires_with_task: true
  compensating_controls:
    mechanical_verification_refs: []
    human_adjudication_ref:
  residual_risk: []
  not_future_precedent: true
```

Conditional triggers:

- `provider_normalization`: when a normalized provider name or selection is claimed;
- `operator_reasoning_setting`: when the operator reports a reasoning setting distinct from the selected option;
- `segments`: when `action.switch_history.status` is `recorded`;
- `review_events`: when review, validation, reproduction, or mechanical verification occurred;
- `human_adjudication`: when a human decision is required, pending, or recorded;
- `assessment_refs`: when quality, correctness, or architectural assessment exists outside the provenance record;
- `recovery_refs`: only when a separately authorized checkpoint, incident assessment, or activation record actually exists;
- `lineage`: when the record reviews, amends, supersedes, or preserves another record;
- `heterogeneous_review_exception`: only when §3.3 applies and the user explicitly grants the exception.

When a triggered conditional group is unavailable or withheld, record:

```yaml
omissions:
  - field:
    reason: not_applicable | not_available | withheld
    detail:
```

Several `not_applicable` fields may be grouped only when they share the same precise reason. Core fields remain present; unknown values are written as `unknown`, never guessed. `unknown`, `confirmed_none`, and `not_available_before_merge` are distinct states and must not be interchanged. Historical v0.1 instances are preserved and are not required to validate against v0.2.

## 5. Pull-request body disclosure

Every important PR contains a compact `Execution context` section and points to the full result record:

```yaml
execution_context:
  action_actor:
  product_surface:
  operator_selection_verbatim:
  provider_normalization_ref:
  served_model_identifier_status: unknown_or_not_attestable
  review_record_ref:
  human_adjudication_status:
  authorization_ref:
  full_run_record:
```

Do not use wording such as `implemented under GPT-X`, `written by GPT-X`, or `verified by GPT-X` when the only evidence is a consumer UI selection or model self-report.

Prefer:

```text
The operator reports selecting <verbatim option>. A separately cited provider source maps or normalizes that option as of <date>. The particular response's backend identity was not independently attested.
```

If no operator selection was reported or observed, say so; do not manufacture a disclosure from the apparent response behavior.

## 6. Official naming and freshness

Model and reasoning names are time-sensitive product facts.

Before claiming a current normalized name:

1. preserve the operator's actual wording verbatim in `operator_selection`;
2. record official normalization separately in `provider_normalization`;
3. use an evidence object with the official source, access date, and exact mapping claim;
4. do not silently carry a stale product label into a current normalization field;
5. when official naming cannot be verified, preserve the user's wording and omit the normalization with an auditable reason.

Historical records retain the terminology visible or reported at their execution time. Later renaming does not rewrite those records.

## 7. Model, surface, conversation, or actor segments

`action.switch_history.status` is required for every important run record and has explicit semantics:

- `confirmed_none`: available evidence supports that no relevant switch occurred;
- `recorded`: one or more known segments exist and `segments` is required;
- `unknown`: the available evidence cannot establish whether or where switching occurred.

Do not infer `confirmed_none` from an empty array. It requires supporting evidence. When status is `unknown`, describe the unresolved range in `limitations`.

```yaml
action:
  switch_history:
    status: recorded
    evidence: []

segments:
  - segment_id:
    order:
    time_window:
    action_actor:
    product_surface:
      value:
      evidence: []
    operator_selection:
      verbatim:
      evidence: []
    operator_reasoning_setting:
      verbatim:
      evidence: []
    provider_normalization_ref:
    conversation_or_run_ref:
    artifact_or_commit_refs: []
    attribution_status: direct | best_supported | unknown
    limitations: []
```

When `recorded`, include every known segment needed to reconstruct attribution, not only the moment of switching. Associate artifacts and commits with the best-supported segment. Uncertain attribution must not be labeled `direct`.

## 8. Review, adjudication, authorization, and lineage

Review events are component records, not a single independence label:

```yaml
review_events:
  - review_id:
    actor:
    actor_kind: model | human | mechanical_process
    role:
    context_relation_to_producer:
      same_run | same_conversation | fresh_conversation | fresh_task_project | not_applicable | unknown
    model_relation_to_producer:
      same_snapshot | different_snapshot_same_family | different_family | not_applicable | unknown
    provider_relation_to_producer:
      same | different | not_applicable | unknown
    criteria_fixed_before_exposure: true | false | unknown | not_applicable
    review_scope:
    evidence: []
    result_ref:
    limitations: []
```

Rules:

1. Mechanical verification, fresh context, heterogeneous review, and human adjudication may coexist; none substitutes for another.
2. Consumer Chat UI labels cannot establish `model_relation_to_producer` when the particular backends are not attested.
3. Same-family or same-provider review is not automatically invalid, but its limitations must be explicit.
4. Human decisions, model analysis, mechanical checks, and task authorization remain separate objects.
5. One user message may support both `human_adjudication` and `user_authorization` only when it explicitly expresses both; each object uses its own `claim_scope`.
6. `reviews` does not automatically mean `amends` or `supersedes_for_scope`.
7. `amends` requires a disposition and decision reference. `supersedes_for_scope` names the old artifact and exact superseded scope. Everything else remains under `preserves`.
8. A stronger product option does not by itself establish review independence.

## 9. v0.2 review and future review triggers

The v0.1 guard and MNEMOSYNE-147 records remain preserved historical records. Version v0.2 is a bounded repair informed by a fresh-task-project, same-provider review with mechanical and multi-agent cross-checks; it is not represented as heterogeneous-provider review. The user's task-local disposition is recorded separately from that review.

Future review is triggered by material schema-use defects, provider-semantics changes, an execution-quality incident, execution-source or trust-boundary work, or explicit user direction. It is not triggered merely by the availability of a named product tier.

Future review must add a new review or amendment record. It must not erase historical execution context or silently reinterpret a v0.1 instance as v0.2.

## 10. Recovery cross-references

`recovery_refs` is a lightweight link to separately authorized records. A checkpoint reference does not create an incident, activate a checkpoint, prove provider failure or model substitution, authorize recovery, or authorize a repository write.

`incident_assessment_ref` and `activation_record_ref` must point to records that actually exist. If a checkpoint is activated in the future, contamination windows, affected-artifact inventories, evidence tiers, downstream dependencies, restart actors/reviewers, and re-entry criteria belong in that separate activation record rather than this general guard.

## 11. Boundaries

This guard does not:

- prove hidden or weights-level backend model identity;
- turn provider-returned identifiers into broader claims than the provider contract supports;
- evaluate output quality, factual correctness, or architectural judgment merely by recording provenance;
- require a heavy cryptographic provenance stack;
- require heterogeneous review for every change;
- authorize repository writes, merges, auto-merge, execution-source edits, target-project work, recovery, or checkpoint activation;
- make PR metadata, review records, run records, or status files execution source;
- replace `current/github-single-active-pr-lineage-guard.md`;
- replace mechanical diff/hash verification, user authorization, substantive review, or human adjudication.
