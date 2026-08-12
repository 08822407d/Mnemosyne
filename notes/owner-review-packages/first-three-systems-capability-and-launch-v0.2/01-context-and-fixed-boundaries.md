# Context and Fixed Boundaries for OR-02 through OR-09

> Read this before the decision workbook. It distinguishes verified repository state, completed Owner decisions, candidate planner judgments, open Owner choices, current external facts, and matters requiring later Pro/frontier adjudication.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
artifact_role: self_contained_context_for_bounded_owner_review
execution_source: false
source_master: 91efad2f2a2f22e99223c49460d27bd9fcbfdb68
source_OR_01_result: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001
```

## 1. Why this review exists now

The Owner has decided that Mnemosyne, Meta-Agent, and future long-lived Agents should not wait for theoretical completion before real use. The durable minimum is to preserve irreplaceable source and purpose, keep authority clear, retain correction/evolution paths, and learn from actual use.

`OR-01` tested the capability-catalogue approach with a complete human pass. The Owner reviewed all 42 v0.1 entries in six batches, amended their meaning, merged the duplicated `ACAP-035/036`, and accepted a 41-entry active v0.2 working catalogue. The next step is to select a minimum sufficient subset for three systems rather than continue catalogue-wide abstraction.

The three systems are:

1. **Meta-Agent** — the long-lived system for designing Agents, workflows, memory, handoffs, model/tool routing, evaluation, and human-decision boundaries;
2. **work/business-function code-library system** — a target that accumulates real development requirements, business rules, reusable implementation, tests, compatibility, and reuse evidence;
3. **long-term language teacher/practice Agent** — a target that teaches and practices over time, records evidence of ability and progress, adapts plans, and permits correction.

## 2. Verified Mnemosyne state

As of `08822407d/Mnemosyne@91efad2f2a2f22e99223c49460d27bd9fcbfdb68`:

- PR #270 is merged at `214be58743d608f50653933418ae1842fa237633`.
- PR #271 is merged at `91efad2f2a2f22e99223c49460d27bd9fcbfdb68`.
- `notes/reusable-agent-capability-catalog-v0.2.md` is the Owner-reviewed non-execution-source working catalogue.
- v0.2 has 41 active entries; historical `ACAP-036` is retired and merged into `ACAP-035`.
- `notes/first-three-system-capability-selection-v0.2.md` is a Pro/frontier planner candidate pending Owner selection.
- The three OR-01 active-guidance repairs are merged: byte-versus-substantive source change, context-sensitive transfer-format repair, and retained-branch obligation audit.
- `current/human-approved-spec.md` remains Mnemosyne's sole execution source.
- No code-library or language-teacher target repository/store has been created by this route.
- No Meta-Agent pilot, target pilot, external research, model comparison, handoff archive evaluation, or private-material intake has been authorized by these merges.

## 3. Completed Owner decisions from OR-01

These are fixed inputs for this review:

1. The capability catalogue is accepted as a **working inventory and selection aid**, not a final ontology or universal runtime package.
2. Targets choose separately according to their needs; capabilities are not copied wholesale into all three Agents.
3. Catalogue completeness is not a launch gate; real use should refine it.
4. `ACAP-002` means one unambiguous currently adopted authority boundary, not one physical file and not simply the newest artifact.
5. Artifact roles should be reflected in human-navigable storage organization where practical.
6. Byte identity, format normalization, and substantive-content change are distinct.
7. Material long-range requirement conflicts should use frontier/open-ended reasoning; mechanical duplicate checks may be delegated.
8. Material external engineering rationale should be preserved; selective reading, not pre-emptive deletion, controls burden.
9. Raw/research/history are evidence and synthesis inputs, not direct execution source; ordinary runtime keeps them cold.
10. A target may have an identity-pinned non-authoritative recovery snapshot if it cannot become a second writer.
11. Staged intent reconstruction may split preliminary next-tier intake, frontier reconstruction, next-tier follow-up, and frontier adjudication.
12. Long-lived Agents must not infer stable user traits from sparse, contextual, mood-dependent, or changing behavior.
13. Product-specific output topology is a dated provider fact; the portable ability is to distinguish canonical outputs, ancillary summaries, exports, and transfer copies.
14. One canonical PR is a current safety default, not a permanent denial of safe parallel Git work.
15. Early real use should emphasize controlled evolution; rollback is only one possible response.
16. Product/Skills/provider implementation remains separate from portable capability semantics.
17. The working analogy is: **model ≈ CPU; execution source ≈ the currently approved program controlling formal behavior**.

## 4. Capability statuses used in this review

### Required initially

The capability semantics must exist in the first bounded useful version. This does not mean:

- one file per capability;
- every task loads detailed rules;
- full automation;
- proven long-term effectiveness.

Several required semantics may be implemented in one compact target spec, one workflow, or one small set of files.

### Triggered

The capability must be available when a stated action or lifecycle event occurs, but does not burden ordinary turns.

Examples:

- PR controls when a GitHub PR is used;
- research gating when research is proposed;
- answer ledger when several dependent decisions occur.

### Early experiment

The capability is plausible and important enough to test early, but its mechanism or burden is not yet established. The target should record value, failure, and correction evidence.

### Deferred

Do not implement before first use. Reconsider after a real failure, scale threshold, provider choice, or Owner decision creates the need.

### Target-specific object

A business/teaching content structure required by the target but not itself a portable Agent-operating capability—for example requirement-to-code traceability or a learner evidence ledger.

## 5. Meta-Agent authoritative status

The authoritative Meta-Agent repository is `08822407d/Meta-Agent`.

Current facts verified from its target truth and current state:

- sole designated target-truth path: `current/approved-spec.md`;
- Owner disposition: accepted with limitations as an inactive design/governance baseline;
- `effective_for_operational_use: false`;
- operational activation requires a separate exact Owner decision;
- private material, broad writes, RAG, MCP, automation, pilot, prototype, and operational activation remain unauthorized;
- its current active-context safe action is candidate-only P0 v0.2 specification revision, not operational use;
- Meta-Agent-owned behavior guidance and initial memory-system foundation remain deferred to separate Owner review.

Therefore `OR-03` selects candidate capabilities for a later Meta-Agent-owned review/package. It does not activate Meta-Agent or override its current safe action.

## 6. Target-local repository/store candidate

The current planner candidate is:

> A real target normally owns its own target truth, implementation, current state, handoff, tests, evaluation, and migrations in a dedicated repository or approved store. Mnemosyne and Meta-Agent keep bounded design, provenance, capability-selection, feedback, and impact pointers; neither remains a competing writer.

The reason is not merely organization. It reduces:

- unrelated project write-lineage coupling;
- accidental cross-project edits;
- irrelevant runtime loading;
- privacy mixing;
- dual-truth drift;
- the need to serialize all project conversations globally.

This is still a candidate default. Meta-Agent migration is practical evidence, not a general proof of every future cross-repository workflow.

## 7. Storage roles that must not be collapsed

### Structured target truth/current records

Examples:

- approved target behavior;
- current goals/state;
- decisions;
- capability selection;
- compact evidence/ledgers;
- handoff;
- version/change records.

These should be in one approved target-local authority boundary.

### Complete material originals

Examples:

- complete exported conversations;
- research reports;
- task originals;
- private work source;
- customer/confidential materials.

These may be large or sensitive and normally remain in approved private cold storage or under verified pointers. They need not share the same store as runtime truth.

### Working code and business implementation

These belong in the selected work repository/toolchain with exact authority, private-source, customer, credential, dependency, and test boundaries.

### Non-authoritative backup/recovery copy

A recovery snapshot may exist elsewhere only if it is clearly non-authoritative, identity-pinned, read-only/immutable or otherwise prevented from becoming a second writer.

## 8. Preparation versus activation versus bounded real use

The interview must distinguish three different actions:

1. **Preparation** — select capabilities, storage direction, target package structure, questions, and acceptance candidates.
2. **Activation authorization** — explicitly permit Meta-Agent or another system to operate under a frozen scope and authority.
3. **Bounded real use** — perform selected actual tasks with evidence, feedback, stop, and change paths.

Preparing a package does not activate a system. Creating a repository does not activate a system. Selecting a first target does not authorize private-material ingestion or external writes.

## 9. Current-product facts versus Owner choices

The interviewer may ask the Owner what outcomes or constraints matter, such as:

- local versus cloud preference;
- whether voice is important;
- acceptable privacy model;
- whether Skills/module reuse matters;
- which provider should be evaluated first;
- acceptable cost/quota burden.

It must not answer from memory:

- what Claude Skills currently do;
- current ChatGPT/Claude/Fable model lists, plans, quotas, prices, file/context limits, project settings, memory, voice, connector, export, privacy, or data-use behavior;
- current repository/write capabilities of a product;
- which named model is reliably suitable for a task class.

Use `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED` when such a fact affects the decision.

## 10. Impact classes

### Suitable for next-tier clarification

- whether a reviewed capability belongs in required/triggered/experimental/deferred status;
- whether a target-specific object is needed in the first package;
- relative priority and preparation order;
- repository/store preference at the level of Owner goals and constraints;
- questions, caveats, rejection, and deferral.

### Capture preference but return to Pro/frontier before implementation

- Meta-Agent operational activation;
- target truth or writer authority;
- private-material storage approval;
- a new shared/common capability-library owner;
- a new cross-repository trust relationship;
- automatic capability propagation;
- broad migration or completed-work re-evaluation;
- a materially new architecture not analyzed by this package.

### External current fact

- current product/model/plan/Skills/settings/privacy/tool behavior.

## 11. Matters out of scope

- re-reviewing all 41 active catalogue entries from zero;
- building a universal Agent ontology or compiler;
- modifying Mnemosyne execution source;
- modifying Meta-Agent truth or active context;
- creating target repositories or private stores;
- selecting or configuring a provider product;
- launching Fable, Deep Research, Claude, GPT comparison, or handoff evaluation;
- implementing RAG, MCP, automation, vector storage, or automatic cross-target propagation;
- deciding detailed migration schemas before real evidence.

## 12. Pro planner recommendations

These are recommendations, not Owner decisions:

1. Approve the shared floor by six semantic groups, not as 18 separate files or always-loaded rules.
2. Keep empirically immature `ACAP-012`, `022`, and `034` as lightweight required semantics whose detailed mechanisms remain experiments.
3. Accept Meta-Agent additions with `ACAP-040` explicitly marked as a focused design problem, not an already solved prompt format.
4. Keep repository, research, transfer, and provider controls triggered rather than always loaded.
5. Adopt target-local truth with bounded meta-system pointers as the default direction, while preserving a controlled bootstrap exception.
6. Separate compact structured target truth from complete private originals.
7. Distinguish preparation order from pilot/activation order; do not force Meta-Agent activation inside this review.
8. Populate product/provider evidence only for the first concrete target decision, with likely early emphasis on Claude packaging/Skills because the Owner expects near-term Claude-centered work—but verify current facts before use.

The Owner may amend, reject, or defer any recommendation.
