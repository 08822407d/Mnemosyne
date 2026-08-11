# Capability Feedback Resolution and Real-Use Validation Plan v0.1

> Non-execution-source plan for resolving the OR-01 items that cannot be settled reliably by wording alone. It prepares bounded designs and evidence collection; it does not run external research, activate Meta-Agent, create target repositories, or authorize private material.

```yaml
plan_id: MNEMOSYNE-CAPABILITY-FEEDBACK-RESOLUTION-VALIDATION-001
task_id: MNEMOSYNE-202
status: candidate_plan_for_real_use_and_target_selection
catalogue_ref: notes/reusable-agent-capability-catalog-v0.2.md
owner_review_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
external_execution_or_quota_authorized: false
execution_source_modified: false
```

## 1. Resolution principle

The Owner's review identified three different classes of follow-up. They should not be handled by one generic “more research” route.

1. **Immediate wording/behavior repair** — current intent is clear enough to amend a candidate or active guard now.
2. **Frontier design candidate** — the problem can be structured now, but the mechanism needs controlled validation rather than immediate universal adoption.
3. **Real-use evidence gap** — no amount of abstract explanation can establish thresholds or value; collect target evidence first.
4. **Current provider/product fact** — verify at the time a concrete target decision depends on it.

## 2. Active-guidance repair preparation in MNEMOSYNE-202

MNEMOSYNE-202 does **not** modify active guards. It freezes an implementation-ready proposal for a later separately authorized task covering three bounded repairs:

- `ACAP-004`: distinguish byte transformation from substantive-content change in source-preservation claims;
- `ACAP-027`: add the context-sensitive “排版不对/内容排版不对” transfer-format repair trigger;
- `ACAP-031`: add periodic stale/zombie retention-obligation audit without authorizing deletion.

The exact contract is `notes/proposed-active-guidance-amendments-from-or01-v0.1.md`. Until a later task updates the named `current/*-guard.md` files and that change is accepted, these three repairs remain proposed rather than active behavior. Other catalogue changes remain non-execution-source candidate revisions.

## 3. Coverage gap when no specific rule exists — ACAP-010

### Problem

A runtime profile can load every applicable known module and still encounter a contemplated action with no dedicated rule. Silence must not automatically mean either permission or prohibition.

### Candidate fallback

```text
identify contemplated action
  -> search declared core and task-triggered modules
  -> no specific rule found
  -> classify impact and reversibility
  -> apply general authority/safety/source rules
  -> low-risk and clearly within task: bounded provisional action + disclose assumption
  -> high-impact/authority/privacy/truth/external side effect: stop and escalate
  -> record coverage gap candidate if recurring or material
```

### Minimum receipt

```yaml
uncovered_behavior_receipt:
  contemplated_action:
  specific_rule_found: false
  sources_checked: []
  general_rules_applied: []
  impact_class: low_reversible | moderate | high_or_irreversible | unknown
  disposition: bounded_proceed | stop_for_owner | frontier_reentry | current_fact_check | missing_artifact
  assumptions: []
  candidate_coverage_gap_ref:
```

### Validation

Include at least three cases in the later runtime-guidance comparison:

1. harmless in-scope behavior with no narrow rule;
2. high-impact behavior whose missing rule must block action;
3. recurring gap that should become a candidate module rather than an ad hoc exception.

## 4. Staged intent reconstruction — ACAP-017

### Candidate workflow

#### Stage N0 — next-tier preliminary intake

The next-tier interviewer may:

- restate the rough request;
- distinguish goal, symptom, and proposed solution provisionally;
- ask low-risk factual/context questions;
- capture examples and constraints;
- identify likely high-impact ambiguities.

It must not finalize architecture, authority, privacy, or the user's “true” need.

#### Stage F1 — frontier reconstruction

The frontier planner:

- analyzes N0 answers and source material;
- proposes competing need/problem models;
- identifies hidden dependencies and contradictions;
- distinguishes Owner decisions from external facts and design judgments;
- prepares either a provisional problem frame or a bounded follow-up package.

#### Stage N1 — next-tier follow-up and answer capture

A frozen package permits the next-tier model to:

- explain why remaining questions matter;
- answer bounded background questions from the package;
- collect, restate, and confirm answers;
- stop on new high-impact scope.

#### Stage F2 — frontier adjudication

Use only when answers materially change purpose, architecture, authority, privacy, or acceptance. Otherwise a bounded target-intake record may proceed.

### Evidence to collect

- how many frontier turns the staged flow saves;
- whether next-tier questions reveal useful information or create noise;
- interpretation corrections;
- premature framing/anchoring;
- re-entry accuracy;
- user burden compared with direct frontier intake.

## 5. Calibrated persistence versus escalation — ACAP-022

### Problem

A model cannot be trusted to measure its own capability limit merely by “feeling” difficulty. Yet escalating at the first obstacle wastes time and frontier quota.

### Candidate control model

Escalation should be driven primarily by **observable task conditions**, not self-reported confidence.

#### Pre-task routing indicators

- unresolved architecture/authority/privacy/truth decision;
- open-ended problem reconstruction;
- multi-source conflict whose omission changes the result;
- no frozen acceptance criteria;
- missing required artifact;
- novel provider/tool behavior without current evidence.

#### During-task indicators

- repeated failure of the same acceptance check;
- mutually inconsistent candidate answers that cannot be resolved from allowed sources;
- need to invent authority, requirements, facts, or paths;
- expansion outside the frozen scope;
- inability to state a mechanically or semantically reviewable result;
- new high-impact dependency;
- attempt budget exhausted without evidence of progress.

#### Bounded persistence rule

A next-tier task may permit a small, task-specific attempt budget, for example:

- one normal attempt;
- one correction attempt using explicit failure evidence;
- then stop/escalate if the same semantic or boundary failure remains.

This is not a universal numeric rule. The taskbook sets the budget based on risk, cost, and verifiability.

#### Anti-premature-escalation rule

Do not escalate merely because:

- the task is long;
- the first approach failed;
- mechanical work occurs in an important project;
- the model lacks certainty but can identify a conservative reversible path and verification;
- a difficulty can be resolved from an authorized source already named by the task.

### Validation design

Use frozen tasks with hidden difficulty variation. Measure:

- critical missed escalations;
- unnecessary escalations;
- useful bounded recoveries;
- frontier rework saved or created;
- user delay and quota cost;
- whether explicit observable triggers outperform generic “escalate when unsure” wording.

## 6. Real-use evidence work

### ACAP-012 — evolution and migration

Collect from the first targets:

- additive schema change;
- split/merge of one memory object;
- recomputation of a derived view;
- retirement of a rule;
- completed-work re-evaluation;
- failed change and recovery.

Do not build a universal migration service first. Record actual preserve/transform/recompute/retire decisions and later extract the minimum pattern.

### ACAP-013 — upstream impact

Once at least two targets have selection records:

- change one catalogue capability candidate;
- locate affected targets mechanically through version/ID references;
- classify impact separately for behavior, data/schema, derived views, completed artifacts, privacy, and authority;
- measure false positives, missed targets, and review burden.

### ACAP-033 — cross-repository work

Run a public/synthetic test before broad target use:

1. one primary target repository;
2. one bounded evidence pointer back to a meta repository;
3. a deliberately failed first write or stale ref;
4. destination-only recovery;
5. two independent target repositories operating concurrently without writing shared methodology;
6. one deliberate shared-object conflict requiring serialization.

### ACAP-034 — evaluation, feedback, and postmortem

Start with a minimal event record, not a formal report for every task:

- intended value;
- observed result;
- user usefulness/burden;
- source/retrieval/authority/business/teaching/tool/process failure class;
- correction performed;
- recurrence or severity;
- target-only versus reusable-method candidate.

Escalate to a postmortem only for severe, repeated, cross-target, or hard-to-diagnose failures. Measure whether the record changes a later decision; retire fields that do not.

### ACAP-039 — retrieval automation

Before adding RAG/index automation, measure:

- repeated misses where relevant information was preserved but not found;
- time/context cost of deterministic lookup;
- false retrieval and stale-source incidents;
- archive size and update frequency;
- privacy/permission constraints;
- whether improved layout/source maps solve the problem first.

No fixed numeric threshold is adopted before target evidence.

## 7. Provider packaging and capability catalogue evidence

### ACAP-040 — capability-to-instruction packaging

This is a design problem, not merely prompt writing. A target package must preserve:

- selected capability semantics and IDs;
- target-specific adaptations;
- source/authority precedence;
- always-loaded core versus triggered modules;
- provider/tool assumptions;
- context/loading behavior;
- version and update path;
- test and receipt requirements.

Evaluate at least two packaging strategies for one real target:

1. compact project/system instructions plus referenced files;
2. modular Skills/commands/configuration where the product supports them.

Compare semantic coverage, context burden, updateability, portability, and model compliance.

### ACAP-041 — Skills/modules

Do not research every provider in advance. When Claude becomes the selected surface:

- verify current official Skill semantics, scope, loading, inheritance, precedence, file format, tool access, versioning, and security;
- record actual user setup and observed behavior;
- run a bounded semantic-equivalence test against the portable capability package;
- keep a dated adapter record and recheck trigger.

### ACAP-042 — provider/model/product catalogue

Populate only decision-relevant entries. Each entry separates:

- official provider claim with access date;
- operator-observed UI/settings;
- bounded task evidence;
- failure evidence;
- exact backend status (normally unknown in consumer chat);
- freshness/recheck trigger.

Initial entries should be driven by the first target's concrete surface decision, not by an attempt to document every subscribed product.

## 8. Product output topology — ACAP-028

The portable schema should allow products to differ:

```yaml
output_topology_record:
  provider_product_surface:
  task_type:
  observed_at:
  substantive_canonical_outputs: []
  ancillary_execution_or_process_summaries: []
  downloadable_or_exported_representations: []
  transfer_copies: []
  official_source_refs: []
  operator_observation_refs: []
  bounded_test_refs: []
  limitations_and_recheck_trigger: []
```

The Owner's current observations about ChatGPT Deep Research and Claude are preserved as unverified/time-sensitive operator observations until a concrete task requires current verification.

## 9. Capability and model split

```yaml
frontier_required_or_recommended:
  - staged_intent_problem_reconstruction
  - material_requirement_conflict_analysis
  - escalation_policy_design_and_adjudication
  - cross_target_generalization_or_impact_decisions
  - capability_packaging_architecture

next_tier_candidate:
  - frozen_intake_interview
  - answer_ledger_and_bounded_explanation
  - target_selection_record_drafting
  - exact_application_of_an_approved_package
  - structured_real_use_event_capture

mechanical:
  - ID_and_version_mapping
  - source_ref_and_path_checks
  - task_acceptance_checks
  - selection_and_impact_index_lookup
  - hashes_diffs_and_tests

human_only:
  - purpose_and_value_selection
  - target_truth_authority_and_privacy
  - operational_activation
  - provider_subscription_or_quota_trigger
  - common_method_promotion
```

## 10. Priority order

1. Use the v0.2 catalogue to prepare target-specific selections.
2. Begin bounded real use after target authority/storage decisions.
3. Collect ACAP-012/013/033/034/039 evidence from those targets.
4. Research and test ACAP-040/041/042 only when a concrete provider packaging decision is imminent.
5. Use independent Fable/frontier research for ownership/lifecycle or alternative packaging architecture, not for mechanical inventory updates.

## 11. Stop conditions

Do not:

- promote provisional capabilities to execution source merely because this plan exists;
- create provider-fact entries from model memory;
- interpret successful artifact creation as real-use value;
- allow a next-tier model to make a new authority/privacy/architecture decision;
- automatically propagate a capability update into existing targets;
- create RAG/automation before preserving a deterministic baseline and evidence of need.
