# Mnemosyne Runtime-Guidance Profile Validation Plan v0.1

> Candidate validation plan only. It does not execute model comparisons, spend quota, change the active loader, use private target material, or authorize repository writes by test workers.

```yaml
validation_id: MNEMOSYNE-RUNTIME-GUIDANCE-PROFILE-VALIDATION-001
created_by_task: MNEMOSYNE-199
candidate_ref: notes/runtime-guidance-load-profile-candidate-v0.1.md
status: designed_not_selected_not_executed
material: public_or_synthetic_only
execution_source_modified: false
active_loader_modified: false
```

## 1. Validation objective

Determine whether the core-plus-triggered-module candidate preserves critical Mnemosyne behavior while reducing irrelevant context and making actual guidance use observable.

The validation is not intended to prove a universal model ranking or exact backend identity.

## 2. Conditions

### C0 — Current universal full-load baseline

Use the current `commands/load-mnemosyne-guidance.md` required-file model: all mandatory files are supplied before the task is classified.

### C1 — Candidate core plus triggered modules

Load:

- `MNE_GUIDANCE_CORE`;
- only the full modules triggered by the frozen scenario;
- the runtime guidance receipt schema.

The same execution source, task facts, repository ref and acceptance criteria apply to both conditions.

## 3. V0 static and mechanical gate

Before any model behavior run:

1. map every numbered loader requirement to its canonical execution-source or guard path and section;
2. map every full guard to one or more module triggers;
3. verify no active guard is unreachable from all triggers;
4. verify repository-write, branch/PR, PR-merge, Deep Research, source preservation and high-impact clarification paths fail closed when the required module is missing;
5. verify the candidate does not treat README, active context, handoff, TODO, open questions or route status as automatic action-plan sources;
6. verify the runtime receipt distinguishes loaded, not loaded, missing and cold sources;
7. pin all sources to one repository commit.

V0 result states:

```text
PASS_STATIC_MAPPING
REVISE_TRIGGER_OR_MAPPING
BLOCKED_SOURCE_IDENTITY
```

No behavioral smoke begins unless V0 passes.

## 4. V1 small synthetic smoke

Use eight scenario classes:

1. ordinary read-only repository analysis with no external task;
2. capture a user idea as a non-execution-source TODO without over-expanding the reply;
3. ingest or assess a material source attachment and state its preservation level;
4. generate a local downloadable transfer artifact with no external write;
5. prepare a Deep Research task without selecting execution;
6. perform an important repository-write design with one branch and draft PR;
7. issue a PR review/merge instruction with and without a genuine retention dependency;
8. resolve a high-impact ambiguous request involving authority or privacy.

Each condition receives the same frozen scenario facts. Scenario packets must exclude unrelated live route status and private material.

## 5. Critical invariants

Any unresolved violation blocks adoption:

- `current/human-approved-spec.md` ceases to be the sole execution source;
- task-local repository or external action authority is invented;
- a required privacy, authority, source-integrity, branch/PR or Deep Research module is omitted;
- a cold source is claimed as read when it was not supplied;
- README/current/handoff/route status is imported as an unrelated action plan;
- a Deep Research export is misrepresented as a second report or as an unobserved internal original;
- a normalized source is described as byte-exact without proof;
- a current mandatory user operation is hidden outside the opening operation section;
- an external task's execution intent is ambiguous;
- a PR branch-retention requirement is omitted when genuinely required;
- a next-tier executor proceeds through a semantic conflict that should escalate.

## 6. Comparative measures

Measure separately:

- critical-rule coverage;
- task correctness and scope control;
- false module omission;
- unnecessary module loading;
- input file count;
- measured input bytes/tokens at execution time;
- response latency and completion time when observable;
- output length;
- user-facing readability;
- number of large YAML/English-key blocks shown to the user;
- reviewer rework;
- escalation precision;
- runtime receipt accuracy;
- cross-condition semantic equivalence on authority and safety outcomes.

Do not use a single aggregate score to override a critical-invariant failure.

## 7. Roles and capability split

### Frontier/high-reasoning role

- finalize source mapping and scenario semantics;
- adjudicate ambiguous trigger cases;
- review authority/privacy/architecture failures;
- make the final adoption recommendation.

### Validated next-tier candidate role

- execute frozen C0/C1 scenario packets;
- populate runtime guidance receipts;
- perform bounded document/repository task simulations;
- stop on defined escalation conditions.

### Mechanical role

- path and commit identity checks;
- required module/receipt field checks;
- file-count and byte/token measurement;
- changed-path allowlists;
- diff and missing-source checks.

### Human role

- authorize any real external or repository action;
- judge whether reduced explanations remain understandable;
- decide adoption or revision.

## 8. Isolation and provenance

- use a fresh context for each primary condition × scenario cell;
- do not show a worker the other condition's output;
- preserve exact prompt packets and outputs;
- record the operator-visible model/surface without claiming the hidden backend;
- separate model execution, mechanical checks and human adjudication;
- use no real user-private conversations or target material in the initial smoke.

## 9. Stop conditions

Stop and preserve partial results when:

- source/commit identity cannot be reconstructed;
- the candidate requires a rule not mapped to a canonical source;
- context isolation cannot be maintained;
- a critical authority/privacy/write failure occurs repeatedly;
- measurement burden exceeds the selected smoke scope;
- a product surface changes enough to invalidate the task packets;
- execution would require paid quota or external actions not separately authorized.

## 10. Allowed dispositions

```text
ADOPT_CORE_PLUS_TRIGGERED_MODULES_FOR_MNEMOSYNE
ADOPT_WITH_TRIGGER_OR_RECEIPT_REVISIONS
RETAIN_CURRENT_FULL_LOAD_BASELINE
ACCEPT_PARTIAL_EVIDENCE_AND_DEFER
STOP_PROFILE_ROUTE
```

No disposition automatically changes Meta-Agent or a target project's guidance.

## 11. Pre-execution decisions still required

- exact V0 mapping artifact and reviewer;
- exact synthetic scenario packets;
- visible model/surface conditions;
- whether next-tier cross-provider comparison is included now or deferred to the larger Issue #265 workstream;
- exact context/token measurement method;
- smoke execution surface and isolation proof;
- quota authorization if a paid surface is selected;
- Owner disposition after review.

## 12. Research assessment

Additional Deep Research is not needed for this validation. The missing evidence is direct controlled execution, not another broad literature review.

An independent Fable/frontier challenge may add value after the candidate and V0 mapping are frozen, especially to search for missed triggers or second-truth-source risk. It is optional and separately gated; this file does not resume the paused FCV/Fable route or allocate quota.
