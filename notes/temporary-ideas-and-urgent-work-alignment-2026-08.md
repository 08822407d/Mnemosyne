# Temporary Ideas and 2026-08 Urgent-Work Alignment

> Non-execution-source synthesis for the user’s temporary ideas added in the current conversation and Issue #265. It does not modify the execution source, launch research, authorize target-repository writes, or adopt a new Mnemosyne/Meta-Agent architecture.

```yaml
record_id: MNEMOSYNE-TEMPORARY-IDEAS-URGENT-ALIGNMENT-001
task_id: MNEMOSYNE-200
repository_ref: 08822407d/Mnemosyne@96d7e9172527f56068404f5561a212b8ddbdd29c
source_issue: https://github.com/08822407d/Mnemosyne/issues/265
source_issue_comments:
  - https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5248414221
  - https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5248467581
  - https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5248547713
  - https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5250223069
additional_source: current_maintenance_conversation_2026_08_11
status: synthesis_and_priority_candidate
execution_source_modified: false
```

## 1. Executive conclusion

The temporary ideas are not a set of unrelated additions. Most converge on one practical architecture:

1. preserve complete sources and design reasons without routinely loading them;
2. maintain a reusable catalogue of Agent operating capabilities;
3. select only the capabilities needed by each target Agent;
4. perform target-specific design and construction primarily in the target repository;
5. keep provider/model/product-surface facts in a separate time-sensitive capability catalogue;
6. validate whether frontier and next-tier models can apply the selected capability package reliably;
7. learn from real target use rather than delaying until the meta-systems appear complete.

This directly supports the urgent Issue #265 route. The highest-leverage immediate addition is the reusable Agent-capability catalogue and a first selection matrix for Meta-Agent plus the two real target needs.

## 2. Idea clusters and current disposition

### I1 — Use before perfection; preserve what cannot be regenerated

User intent:

- Mnemosyne, Meta-Agent and long-lived target systems will never reach a final perfect state;
- real use should start once irreversible information-loss and authority risks are bounded;
- original requirements, complete conversations/reports and design reasons should survive later redesign;
- later upgrades must assess existing target-system work and decide whether migration, recomputation or no change is needed.

Current status:

- source-artifact preservation levels and compact design-rationale capture were adopted through PR #266;
- full historical backfill remains intentionally out of scope;
- a future cross-target impact register is still missing.

Urgent-work alignment:

- Issue #265 TODO 2A: minimum real-use baseline;
- TODO 2D: test/feedback/improvement and migration/rollback;
- TODO 4: complete conversation archives for handoff evaluation.

Disposition: **foundation implemented; use immediately in the first three target designs.**

### I2 — Preserve cold material, but do not routinely read it

User intent:

- one-off task results, old handoffs, completed routes, raw ideas and complete research reports are often valuable for recovery but low-value for ordinary runtime;
- execution/behavior guidance should explicitly prevent indiscriminate reading;
- business Agents should not load Mnemosyne/Meta-Agent construction archives during normal work.

Current status:

- PR #266 adopted `DO_NOT_READ / ON_DEMAND` for complete cold originals;
- PR #267 added a candidate `core + triggered modules` runtime-guidance profile and V0 source mapping;
- active loader behavior has not yet changed and V1 behavioral validation has not run.

Urgent-work alignment:

- TODO 2A: reduce pre-pilot burden;
- TODO 3: next-tier reliability under smaller frozen working sets;
- TODO 4: complete archive is review evidence, not normal handoff input.

Disposition: **directly on the urgent path; validate after the current active-guidance cleanup.**

### I3 — Maintain reusable Agent operating capabilities centrally

User intent:

- many requirements produced during Mnemosyne construction are portable Agent capabilities rather than Mnemosyne-only business rules;
- capabilities should be inventoried, described, versioned and selected like reusable library components;
- project-specific business semantics and temporary platform workarounds must be filtered out before generalization;
- the user should be able to choose from a human-readable capability list instead of remembering every existing design.

Current status:

- Meta-Agent already has a small general methodology and a case-to-method promotion gate;
- Mnemosyne contains many reusable guards/templates but no unified human-readable capability catalogue;
- the Mnemosyne-versus-Meta-Agent ownership boundary remains unresolved.

Urgent-work alignment:

- TODO 2B/2C: design Meta-Agent plus the two real target systems;
- TODO 3: test consistent application of the same selected capabilities across providers/models;
- added TODO 5 in Issue #265: common Agent-operating methodology.

Disposition: **highest-priority new deliverable; initial catalogue and selection matrix are created by MNEMOSYNE-200.**

### I4 — Build target systems primarily in their own repositories

User intent:

- prior co-location of many projects in Mnemosyne caused authorization, ordering and concurrency burden;
- Meta-Agent migration gives practical evidence that one conversation can work across repositories;
- future target design/build should normally occur in the target repository;
- Mnemosyne and Meta-Agent may still retain bounded generic design, provenance, feedback or impact records, but not duplicate target truth.

Current status:

- Meta-Agent migration passed destination recovery and no-dual-writer checks;
- this demonstrates feasibility for that migration, not a general cross-repository operational validation;
- exact secondary records retained by Mnemosyne and Meta-Agent are not yet decided.

Urgent-work alignment:

- TODO 2B/2C: first real target repositories and truth boundaries;
- TODO 3: cross-provider/tool consistency and repository-write discipline.

Disposition: **prepare a target-local repository operating model and bounded validation before broad use. Do not delay initial target design solely for a universal cross-repository framework.**

### I5 — Agent construction is capability selection plus platform packaging

User intent:

- a large part of Mnemosyne/Meta-Agent output is a package of prompts, Skills, instructions, memory structures and workflows that shape an Agent’s behavior;
- reusable capabilities should not be rewritten from scratch for each Agent;
- platform-specific mechanisms such as Skills require separate understanding and adaptation.

Current status:

- the portable capability layer is partly visible in Mnemosyne guards and Meta-Agent methods;
- no provider-neutral complete Agent Design IR or compiler is approved;
- the exact meaning and operation of Skills across current Claude/ChatGPT products is time-sensitive and not established here.

Urgent-work alignment:

- TODO 2: construct the first target Agents;
- TODO 1: independent research on unresolved platform/packaging questions;
- TODO 3: verify provider-neutral semantic behavior rather than identical files or style.

Disposition: **separate portable capability semantics from provider-specific packaging. Research Skills only when the first target packaging decision is close enough to change implementation.**

### I6 — Maintain a separate provider/model/product-surface capability catalogue

User intent:

- remember which paid models/services can do what;
- preserve software-surface settings, limits and usage procedures;
- use the catalogue during Agent design and model routing rather than depending on human recall.

Current status:

- Mnemosyne has research evidence and scattered capability records, but no unified current catalogue;
- model names, plans, prices, quotas, settings and product behavior are time-sensitive;
- hidden backend identity remains unattestable on consumer chat surfaces.

Urgent-work alignment:

- TODO 3: choose and validate next-tier execution conditions;
- TODO 1: route open or current platform questions to Fable/frontier research when valuable;
- TODO 2: select a practical product surface for each first target.

Disposition: **create a separate catalogue design now; populate only with current verified facts when a decision needs them. Do not mix it with the Agent-capability catalogue.**

### I7 — Human-readable output should be a first-class operating quality

User intent:

- large English-key YAML/code blocks are difficult to absorb;
- most normal explanations should use concise natural language;
- structured blocks remain useful when many explicit human decisions need visual emphasis, but require explanation;
- machine-friendly repository schemas and human-facing conversation output should be separated.

Current status:

- PR #266’s rationale guard already says to explain results in concise natural language rather than pasting large English-key YAML blocks;
- no complete repository-wide human-readability review has been performed.

Urgent-work alignment:

- TODO 2A: reduce real-use maintenance burden;
- TODO 3: compare next-tier model output burden and instruction use;
- first target capability-selection interface.

Disposition: **apply immediately to new user-facing catalogues and future replies; later measure readability/review burden rather than adding another large abstract rule set now.**

### I8 — Upper-level improvements must assess existing target systems

User intent:

- a Mnemosyne or Meta-Agent improvement may require target behavior changes, re-evaluation of completed work, migration or regeneration;
- early designs should preserve enough source/lineage to make later upgrades possible.

Current status:

- target-level upgrade/migration contracts exist;
- no central catalogue of deployed target capability selections and affected versions exists.

Urgent-work alignment:

- TODO 2D: iterative improvement and rollback;
- reusable capability catalogue versioning;
- future cross-target impact review.

Disposition: **record selected capability IDs/versions in each first target from the start; defer automated impact propagation.**

## 3. What is “on the way” for the urgent week

### Directly shared work

The following work advances several urgent TODOs at once:

1. **Reusable Agent-capability catalogue** — supports Meta-Agent, both real target Agents and next-tier consistency testing.
2. **Capability selection matrix for the first three systems** — turns abstract methodology into concrete target scope.
3. **Target-local repository operating model** — removes the co-location/concurrency burden before real builds.
4. **Runtime working-set/load profile** — reduces context burden and makes next-tier tests meaningful.
5. **Preservation/rationale/feedback receipts** — enable real-use postmortems and handoff archive evaluation.
6. **Separate provider/product capability catalogue** — supports model/tool routing without contaminating portable Agent capability definitions.

### Related but not the same work

- Fable independent research should challenge unresolved boundaries and alternative architectures; it should not replace the capability inventory or repeat mechanical extraction.
- Handoff archive evaluation uses complete old conversations as evidence but should not turn them into default runtime context.
- Next-tier validation should use frozen capability packages produced by the first two items above.

## 4. Recommended execution order for the remaining urgent window

### Stage A — Current task

- repair the two MNEMOSYNE-199 active-guidance defects;
- create the first reusable Agent-capability catalogue;
- create the first three-system capability selection matrix;
- define the provider/product capability catalogue boundary.

### Stage B — Target-local operating model and first target intake

- freeze which repository owns each target truth and primary write lineage;
- define the bounded records Mnemosyne and Meta-Agent retain;
- run a small public/synthetic cross-repository validation if needed;
- select exact repositories/roots for the business-code library and language-tutor pilots.

### Stage C — Minimum real-use launch baseline

For Meta-Agent, business-code library and language tutor:

- freeze minimum source, authority, memory and feedback files;
- define the first real task set;
- preserve complete conversation/task evidence outside normal runtime;
- start use without waiting for complete automation, RAG or provider-neutral packaging.

### Stage D — Next-tier and cross-provider reliability

- derive frozen bounded tasks from the first target packages;
- test GPT-5.6 Sol and Claude Opus 5 conditions available at execution time;
- measure semantic correctness, authority, escalation, rework and context burden;
- use frontier review for severe or ambiguous failures.

### Stage E — Handoff archive assessment and Fable challenge

- evaluate real old/new conversation handoffs using complete archives;
- distinguish handoff quality from post-hoc recovery by a frontier reviewer;
- assign Fable independent research to unresolved architecture or provider/Skills questions that remain decision-relevant after real-use baselines exist.

## 5. Deferred to avoid another abstraction trap

Do not make the following prerequisites for first real use:

- complete backfill of all historical capabilities;
- a universal Agent compiler or provider-neutral Skills implementation;
- automatic cross-target impact propagation;
- a vector database or RAG layer;
- exact stable IDs for every sentence or section;
- complete research on every provider setting before a target surface is selected;
- a universal concurrency framework for every future repository.

## 6. Design rationale

The selected approach is to build one useful capability catalogue and apply it immediately to the first three systems, rather than first designing a complete universal ontology.

The alternatives considered were:

- continue target design independently and leave reusable capabilities scattered — rejected because it repeats work and prevents deliberate cross-provider consistency testing;
- stop real-use work until a complete common library and provider catalogue exist — rejected because it recreates the slow abstract-construction problem;
- copy the entire Mnemosyne rule set into each target — rejected because it imports project contamination and excessive context;
- use a small candidate catalogue, portability filter and target-specific selection records — selected because it is reversible, testable and directly useful to the urgent real-use route.

Validation comes from using the catalogue in Meta-Agent and the two first real targets, measuring omissions and burden, and revising it from target feedback. The current record is candidate planning evidence, not an execution-source change.
