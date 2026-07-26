# Model-Capability-Aware Work Planning Preparation v0.1

> Preparation and evidence-planning note only. This file is not execution source, a model-routing policy, a task schema, a benchmark result, or implementation authorization.

```yaml
preparation_id: MODEL-CAPABILITY-PLANNING-PREP-001
created_by_task: MNEMOSYNE-163
source_raw: raw/chatgpt-discussion-058.md
open_question: current/model-capability-aware-work-planning-open-question.md
status: preparation_complete_future_research_or_controlled_validation_not_started
repository_write_authorized_beyond_MNEMOSYNE_163: false
execution_source_change_authorized: false
```

## 1. Preparation objective

Prepare Mnemosyne to investigate a practical operating constraint:

- frontier-model capacity is valuable and limited;
- key architecture, policy, adjudication and large-scale synthesis may justify frontier execution;
- small, temporary or routine Agent work often should not consume frontier quota;
- Mnemosyne outputs should not depend implicitly on permanent frontier availability;
- task planning should make high-reasoning stages visible and concentrate them rather than mixing them throughout routine work;
- lower-tier execution should be validated rather than assumed.

The purpose of this note is to organize the future inquiry and the user interaction. It deliberately stops before proposing a final policy.

## 2. Why existing mechanisms are insufficient

### 2.1 Provenance is retrospective

The run-context guard answers:

- who or what acted;
- which product surface and visible/reported selection were used;
- what can and cannot be attested about the backend;
- what review and authorization occurred.

It does not answer:

- what level of reasoning the task actually needed;
- whether the task could have been decomposed;
- whether a lower-tier executor would have passed;
- when escalation should have occurred.

### 2.2 Surface selection is not capability allocation

The current Work assessment distinguishes Chat, Work and Codex by workflow surface. A surface can still expose several model or reasoning choices, and the same model tier may behave differently depending on tools, context, task framing and verification.

Therefore future guidance must avoid equations such as:

```text
Work = high intelligence
Codex = lower intelligence
Chat = simple
Pro = always required
```

### 2.3 Staged high-cost prompt generation is narrower

Execution-source §17 already prevents silent generation of high-risk prompt packs in a low-strength context and requires staged dependency handling. It does not yet cover the whole lifecycle:

```text
problem framing
→ architecture or policy reasoning
→ task decomposition
→ routine implementation
→ mechanical validation
→ substantive review
→ human decision
```

## 3. Provisional task-allocation model for investigation

The following is a hypothesis to test, not an approved workflow.

```text
High-value reasoning envelope
  - ambiguous goals and requirement interpretation
  - architecture and policy alternatives
  - cross-source synthesis
  - safety / authority / privacy trade-offs
  - adjudication and acceptance criteria
  - decomposition and escalation design

Bounded execution envelope
  - applying a frozen specification
  - filling an approved template from supplied evidence
  - localized document repair
  - routine implementation with explicit acceptance tests
  - evidence extraction under a fixed schema
  - deterministic transformation

Mechanical envelope
  - hashes, exact anchors, diffs, schema parsing, tests
  - inventory and allowlist checks
  - reproducible comparison

Human envelope
  - resource-budget choice
  - final policy and product decisions
  - approval of external or repository actions
```

Future evidence may show that some items move between envelopes depending on context scale, novelty, ambiguity, safety impact and available verification.

## 4. Design properties to investigate

A task artifact intended for next-tier execution may need to be:

- self-contained enough to avoid relying on the frontier planner's hidden context;
- explicit about execution source, authority and forbidden actions;
- bounded to one decision or transformation surface;
- equipped with literal inputs, examples or references when ambiguity is costly;
- equipped with acceptance criteria and negative cases;
- fail-closed on missing, conflicting or stale inputs;
- explicit about what must be returned for stronger review;
- separated from any user decision the executor is not authorized to make;
- independently verifiable where possible.

However, adding too much detail can increase context length and instruction dilution. The study must therefore test **minimum sufficient specification**, not assume that more instructions always help lower-tier models.

## 5. Proposed evidence inventory

Before external research or controlled testing, a maintainer should sample prior Mnemosyne work across these classes:

| Class | Candidate examples | What to examine |
|---|---|---|
| Architecture/adjudication | Fable GF5 Stage A/B, Pro adjudications, run-context guard repair | ambiguity, cross-source reasoning, missed semantic relations |
| Frozen exact implementation | MNEMOSYNE-157 and -160 | whether specification quality reduced executor capability demand |
| Small GitHub repair | route status and finalization PRs | whether strong models added value beyond careful process |
| Research prompt authoring | Pro/Deep Research task packs | whether prompt framing needs frontier reasoning |
| Handoff/continuation | receive/guidance and live-wayfinding repairs | authority and context-contamination sensitivity |
| Target-project design | Meta-Agent controlled dry-run | incomplete requirements, truth-source and safety reasoning |

The inventory must use visible selection and task records only as provenance. It must not infer hidden backend identity or attribute every defect to the model tier.

## 6. Controlled validation outline

### Phase 0 — rubric and input freeze

- select a representative, read-only or synthetic task;
- pin all repository refs and source files;
- define correct outputs, forbidden claims, stop conditions and scoring before either model sees the task;
- prevent target/repository writes;
- record visible model/reasoning selections verbatim.

### Phase 1 — monolithic comparison

Run the same task independently under:

- one user-selected frontier condition;
- one user-selected next-tier condition.

Compare:

- requirement and authority recovery;
- evidence completeness;
- correctness;
- fabricated facts or permissions;
- scope discipline;
- uncertainty handling;
- self-detected need for escalation;
- usability of the returned artifact;
- human review and repair time.

### Phase 2 — decomposed workflow comparison

Compare:

1. frontier model performs the complete task;
2. frontier model frames, decomposes and freezes criteria; next-tier model performs bounded execution; mechanical checks validate; frontier or human reviews only the high-impact result.

The relevant cost is not only model quota. Measure total rework, review burden, latency and risk.

### Phase 3 — instruction portability

Test whether the same behavior guidance remains usable when:

- the model/provider changes;
- the product surface changes;
- context is reduced to the intended handoff package;
- a low-risk task omits unnecessary Mnemosyne maintenance context.

## 7. Candidate evaluation dimensions

```yaml
candidate_evaluation:
  task_contract_recovery:
  authority_and_forbidden_action_adherence:
  evidence_recovery_and_citation:
  factual_and_logical_correctness:
  uncertainty_calibration:
  escalation_precision:
  acceptance_criteria_coverage:
  mechanical_verifiability:
  repair_or_review_burden:
  context_and_quota_cost:
  portability_across_surfaces_and_providers:
```

No weights or pass threshold are approved. Critical authority, safety or truth-source violations may need to override aggregate scores, but that is a future design decision.

## 8. External research candidates

A future Pro/Deep Research task, if separately selected, should examine:

- model cascades and routing;
- budget-aware inference and agent planning;
- task decomposition between planner and executor models;
- weak-to-strong supervision and verifier architectures;
- model capability evaluation under real task contracts;
- prompt/specification complexity versus instruction-following reliability;
- escalation and abstention calibration;
- mixed-model software/Agent development workflows;
- cost-quality-risk trade-offs.

The prompt should distinguish current provider product tiers from stable design principles and should not assume that benchmark rankings directly predict Mnemosyne task performance.

No such research task is generated or selected by this preparation note.

## 9. Inputs expected from the user

### Needed now

Only the already planned action:

1. execute the four isolated Pro Deep Research tasks;
2. return each complete report body and any generated file;
3. record the visible task/model/mode label verbatim if available;
4. report any truncation, source-access or citation failure.

The new model-capability planning issue does not require a fifth research run now.

### Needed later, after a concrete validation package exists

The user will be asked to:

1. identify the visible frontier option available at that time;
2. identify the visible next-tier option they realistically intend to use for routine work;
3. approve a bounded read-only or synthetic two-condition replay;
4. select or approve representative task classes;
5. state the acceptable review/rework burden and any tasks that should never be delegated below the frontier tier.

The user does not need to provide stable provider names, backend claims or quota numbers now.

## 10. Interim authoring discipline

Until this question is resolved, future Mnemosyne taskbooks and target-Agent guidance should avoid:

- saying or implying that Pro, Fable 5 or any named frontier model is always available or mandatory;
- using the construction model as an undocumented runtime dependency;
- calling a task “low difficulty” without explicit scope and verification;
- delegating architecture or authority decisions merely because a routine executor has repository tools;
- treating a model label as evidence that the task will be performed correctly.

They may, when warranted:

- state that a phase contains high-impact synthesis or adjudication and recommend the user select a stronger model;
- separate frozen bounded execution from architecture judgment;
- include explicit escalation and stop conditions;
- use mechanical checks to reduce—but not erase—the need for reasoning and review.

These interim statements restate current boundaries and the present user constraint; they are not a new mandatory schema or global routing policy.

## 11. Stop conditions

Stop and return to user or stronger review when:

- the task requires an unapproved architecture, policy, truth-source or authority decision;
- evidence conflicts or the task's scope cannot be made self-contained;
- next-tier output fails critical boundaries;
- verification cost exceeds the expected quota saving;
- current product tiers cannot be identified reliably enough for the proposed test;
- a test would require real target materials or writes not separately authorized.

## 12. Completion criterion for this preparation

```yaml
preparation_completion:
  raw_input_preserved: true
  existing_rules_and_idea_mapped: true
  provenance_vs_capability_planning_distinction_recorded: true
  research_and_validation_questions_defined: true
  user_actions_separated_into_now_and_later: true
  model_routing_policy_adopted: false
  execution_source_modified: false
  research_executed: false
  controlled_replay_executed: false
```
