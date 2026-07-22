# Run Context and Pull-Request Provenance Guard

> User-approved Mnemosyne behavior guard for recording AI execution context in important repository-writing tasks and pull requests. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only execution source. It operationalizes the actor/reviewer/provenance requirements in §§18–19 and the user-approved minimum recommendation derived from FABLE5-GOV-001.

```yaml
guard_id: MNEMOSYNE-RUN-CONTEXT-PR-PROVENANCE-001
created_by_task: MNEMOSYNE-147
status: active_user_approved_behavior_guard
maturity: provisional_pending_reliable_Pro_or_stronger_model_review
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

The guard records what the operator and repository can honestly establish about a run without converting a visible product label into a claim about hidden backend identity.

It separates:

- actor/action source;
- product surface and operator-visible or operator-reported selection;
- provider-documented mapping between a visible selection and a named model;
- per-request backend identity;
- output/artifact identity;
- reviewer identity and review independence;
- user authorization.

These dimensions must not be collapsed into a single `model:` field.

## 2. Evidence vocabulary

Use one of the following evidence classes for every model/surface field:

```text
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

1. A UI selection may establish what the operator selected; it does not independently attest the backend that executed the request.
2. Provider documentation may establish the provider's current declared mapping; it does not prove what happened in a particular consumer-chat response.
3. Model self-identification is never sufficient identity evidence.
4. Response speed, latency, style, verbosity, perceived intelligence, or displayed reasoning traces are not decisive identity evidence.
5. Artifact hashes establish exact bytes, not model identity, factual correctness, or judgment quality.
6. A backend identity may be recorded as attested only when provider-returned request metadata, an applicable admin/audit record, or an equivalently strong source supports the particular run. Otherwise use `UNKNOWN_OR_NOT_ATTESTABLE`.

## 3. Applicability and burden

### 3.1 Low-risk work

For typo-only, formatting-only, link repair, mechanical storage, or other low-impact work, a concise natural-language execution-context disclosure in the PR body is sufficient. Do not create a large per-turn manifest.

### 3.2 Important repository-writing work

A compact structured run record is required when a task:

- modifies current-state or reusable behavior guidance;
- creates or modifies a checkpoint, handoff, validation result, research interpretation, review result, or task prompt used by later agents;
- performs substantive acceptance, rejection, prioritization, or architecture judgment;
- modifies or proposes modifying the execution source;
- is explicitly designated by the user as important, high-risk, or intended for later cross-model review.

### 3.3 High-impact work

Execution-source changes and trust-boundary changes require heterogeneous review before final substantive acceptance unless the user explicitly approves a task-local exception. Mechanical verification and explicit human decision remain required; heterogeneous model review is evidence, not authority.

This rule does not require heterogeneous review for every PR.

## 4. Compact run-record schema

Important task result records must include the applicable fields below:

```yaml
run_context:
  record_version: v0.1
  task_id:
  recorded_at:
  action_actor:
  provider_product_surface:
  surface_evidence: operator_observed | operator_reported | verified_platform_record | unknown
  operator_visible_or_reported_selection:
  selection_evidence: operator_observed | operator_reported | unknown
  operator_visible_or_reported_reasoning_level:
  reasoning_level_evidence: operator_observed | operator_reported | unknown
  provider_documented_model_mapping:
  provider_mapping_source:
  provider_mapping_accessed_at:
  backend_model_identity: UNKNOWN_OR_NOT_ATTESTABLE
  backend_identity_evidence: unknown_or_not_attestable
  model_self_report_used_as_identity_evidence: false
  model_or_surface_switches_during_task: []
  artifact_or_commit_refs: []
  output_hashes: []
  reviewer_or_adjudicator:
  review_independence_class:
  user_authorization_evidence:
  limitations: []
```

Fields may be omitted only when genuinely inapplicable. Unknown values must be recorded as `unknown`, not guessed.

## 5. Pull-request body disclosure

Every important PR must contain a compact `Execution context` section. It should normally include:

```yaml
execution_context:
  action_actor:
  product_surface:
  operator_selected_option:
  provider_documented_model_mapping:
  backend_model_identity: UNKNOWN_OR_NOT_ATTESTABLE
  review_independence:
  later_stronger_model_review:
```

The PR body may point to the full result-record path instead of duplicating every field.

Avoid wording such as:

```text
implemented under GPT-X
written by GPT-X
verified by GPT-X
```

when the only evidence is a consumer UI selection or model self-report.

Prefer wording such as:

```text
The operator reports selecting <official UI option>. Current provider documentation maps that option to <official model name>. The particular response's backend identity was not independently attested.
```

## 6. Official naming and freshness

Model and reasoning names are time-sensitive product facts.

Before writing a current name into a PR/result record:

1. use the exact current official product/model terminology where it can be verified;
2. record the official source URL and access date for any UI-option-to-model mapping;
3. preserve the operator's actual visible selection separately from the normalized official model name;
4. do not silently carry old labels such as `Thinking Standard`, `Thinking Extended`, or `Thinking Heavy` into current records after the provider has renamed them;
5. when current official naming cannot be verified, record the user's wording verbatim as `operator_reported` and leave the normalized mapping unknown.

Historical records retain the terminology that was visible or reported at their execution time. They are not rewritten solely because product naming later changes.

## 7. Model or surface switches within one task

If the operator changes model option, reasoning level, conversation, product surface, or execution agent during the task:

- record each known segment;
- associate commits/artifacts with the best-supported segment where possible;
- do not collapse multiple segments into a single model label;
- mark uncertain attribution explicitly;
- use the least-privileged evidentiary claim that fits the available record.

Example:

```yaml
model_or_surface_switches_during_task:
  - segment: task_design
    selection: High
    evidence: operator_reported
  - segment: repository_write
    selection: Extra High
    evidence: operator_reported
```

## 8. Reviewer and independence recording

For review, adjudication, validation, or acceptance work, record:

- actual reviewer/actor;
- human decisions separately from model analysis;
- same-run, same-conversation, fresh-same-family, different-family/provider, mechanical-verification, and human-adjudication roles separately;
- limitations when producer and reviewer share a model family or provider.

A later stronger-model review must not erase the original record. It should add a reviewed/superseding record and preserve the original execution context.

## 9. Current adoption and later review boundary

MNEMOSYNE-147 adopts this guard for immediate use based on explicit user authorization and the convergent DR07/FABLE5-GOV-001 evidence. The guard is deliberately marked provisional because the user intends to have it reviewed and improved when a reliably available `GPT-5.6 Sol Pro` or stronger model route exists.

Until that review occurs:

- the guard is active;
- its claims remain limited to honest recording and risk-based review;
- it must not be treated as backend attestation;
- it must not trigger automatic rollback or policy adoption;
- later review should check field burden, false confidence, model-switch handling, and consistency with current provider terminology.

## 10. Boundaries

This guard does not:

- prove backend model identity;
- require a heavy cryptographic provenance stack;
- require heterogeneous review for every change;
- authorize repository writes, merges, auto-merge, execution-source edits, target-project work, or checkpoint activation;
- make PR metadata or result records execution source;
- replace `current/github-single-active-pr-lineage-guard.md`;
- replace mechanical diff/hash verification, human authorization, or substantive review.
