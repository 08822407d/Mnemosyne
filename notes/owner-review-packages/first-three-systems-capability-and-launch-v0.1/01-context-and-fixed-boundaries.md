# Context and Fixed Boundaries

> Read this before the decision workbook. It distinguishes verified repository state, accepted Owner direction, candidate design judgments, open Owner choices, external facts, and matters that require later frontier adjudication.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
artifact_role: self_contained_context_for_bounded_owner_review
execution_source: false
source_master: ee3a9fc1acc67e2efd5f7269fd77f097d055a97e
```

## 1. Why this review exists now

The Owner has decided not to wait for Mnemosyne, Meta-Agent, or future long-lived Agents to become theoretically complete. The immediate objective is to begin bounded real use while preserving enough source information, authority, lineage, and rollback capacity to improve later without losing the original purpose.

MNEMOSYNE-200 converted that direction into four connected candidate artifacts:

- a 42-entry reusable Agent capability catalogue;
- candidate capability selections for Meta-Agent, a work/business-function code-library system, and a long-term language teacher/practice Agent;
- a target-local repository/store operating model;
- a minimum real-use launch baseline.

Those artifacts are intentionally candidates. The present review asks the Owner which parts should guide the first real target packages and which parts should be simplified, deferred, or rejected.

## 2. Verified repository state

As of `08822407d/Mnemosyne@ee3a9fc1acc67e2efd5f7269fd77f097d055a97e`:

- PR #268 is merged.
- `notes/reusable-agent-capability-catalog-v0.1.md` contains 42 candidate `ACAP-*` entries.
- `notes/first-three-system-capability-selection-v0.1.md` proposes a shared minimum and target-specific additions.
- `notes/target-local-repository-operating-model-candidate-v0.1.md` proposes target-local truth and bounded meta-system pointers.
- `notes/minimum-real-use-launch-baseline-candidate-v0.1.md` defines a small hard floor and deliberately deferred complexity.
- `notes/provider-product-capability-catalog-candidate-v0.1.md` defines how current model/product/Skills facts may later be recorded, but it does not populate or verify those facts.
- `current/human-approved-spec.md` remains the only Mnemosyne execution source.
- Meta-Agent remains in its dedicated repository and is not effective for operational use.
- No work/business-function code-library target repository or long-term language-teacher target repository has been created by this route.
- No Fable, Deep Research, Claude, GPT comparison, handoff-archive evaluation, or target pilot was launched by PR #268.

## 3. Owner directions treated as fixed inputs

The interviewer must not ask the Owner to reconfirm these unless a later answer directly conflicts with them:

1. **Use before perfection.** Long-lived systems should enter bounded real use before they are complete.
2. **Preserve irreplaceable source.** Complete conversations, task prompts, research reports, and other material originals should be preserved honestly when possible so later redesign can recover original intent.
3. **Preservation is not routine loading.** Large historical sources should normally remain cold/on-demand.
4. **Real use is primary evidence.** Actual tasks, failure, friction, and user feedback should drive improvement more than indefinite abstract simulation.
5. **Frontier reasoning is scarce.** Open problems, architecture, authority, privacy, methodology promotion, and severe failures should use the strongest suitable reasoning; frozen bounded work should be delegated when reliable.
6. **Portable capabilities and provider mechanisms differ.** A capability such as handoff continuity is portable; a particular Skill, Project setting, prompt surface, or connector behavior is a time-sensitive implementation mechanism.
7. **Target-specific business truth is not a universal method.** Project details must not silently become Mnemosyne or Meta-Agent common rules.
8. **Human readability matters.** Ordinary explanations should use concise natural language rather than long blocks of unexplained English schema terms.

## 4. Existing accepted boundaries

### Mnemosyne

- sole execution source: `current/human-approved-spec.md`;
- raw, research, candidates, current state, handoff, and task results do not automatically become execution source;
- user confirmation is required before approved execution-source change;
- public or unverified repository visibility permits only public, synthetic, or explicitly redacted material;
- platform permission is not task authorization.

### Meta-Agent

- authoritative repository: `08822407d/Meta-Agent`;
- designated target truth: `current/approved-spec.md` in that repository;
- current status: Owner-accepted inactive design/governance baseline;
- operational activation requires a separate exact Owner decision;
- no private material, automatic methodology promotion, broad write authority, RAG, MCP, automation, or pilot is implied by repository existence;
- Mnemosyne is not a second Meta-Agent writer.

### Future target systems

The target-local operating model is still a candidate, but any target must eventually have:

- an identified owner;
- one declared target truth source/store;
- a material/source and privacy policy;
- exact write authority;
- a current-state/handoff mechanism;
- feedback and change history;
- a rollback or revision route proportionate to impact.

## 5. Terms used in the review

### Capability

A reusable behavioral or operational ability an Agent/system may need, such as preserving original requirements, continuing across fresh conversations, or stopping on missing authority.

A capability does not imply one exact file, prompt, Skill, tool, or implementation.

### Provider adapter

A current product-specific way to implement a capability, such as a prompt, project instruction, Skill, command, repository file, setting, or tool integration. Provider adapters are time-sensitive.

### Required initially

The capability semantics should be present in the first bounded useful version. This does not require heavy infrastructure. Several capabilities may be implemented in one compact file or workflow.

### Triggered

The capability must be available and loaded/applied when a stated situation occurs, but it need not burden every ordinary task.

### Early experiment

The capability is plausible and useful enough to test early, but it should remain reversible and may be removed if cost exceeds value.

### Deferred

Do not implement before first use. Reconsider only when a real task, failure, scale threshold, or product decision creates the need.

### Target truth

The single approved source/store that controls current target behavior or state. Evidence, archives, summaries, handoffs, and meta-system pointers do not become target truth merely by being newer or more detailed.

### Cold source

Preserved material used only when a task-specific reconstruction, migration, dispute, audit, or longitudinal-review trigger applies.

## 6. Uncertainty routing

The interviewer should classify new uncertainty as follows:

| Type | Examples | Route |
|---|---|---|
| Owner decision | capability priority, repository preference, privacy tolerance, launch order | ask with context and record answer |
| External current fact | what Claude Skills currently do, current ChatGPT plan/file/model limits, current product setting behavior | do not guess; mark for current verification/research |
| Frontier design judgment | ownership of shared capability definitions, Meta-Agent operational activation, a new trust boundary, major schema change | stop affected item and return to Pro/frontier |
| Missing artifact | exact code repository, complete conversation export, target-specific requirements | request or defer; do not invent |
| Mechanical check | file existence, IDs, path, exact selection count | verify mechanically when authorized |

## 7. Impact classes for the questions

### Low or moderate impact — suitable for next-tier clarification

- catalogue wording, grouping, omissions, and duplicates;
- whether a candidate capability is required, triggered, experimental, deferred, or not applicable;
- relative priority among the three first systems;
- recording preferences, caveats, and questions.

### High impact — interviewer may explain and capture, but final implementation needs frontier/human re-entry

- target repository/store and visibility when private material is involved;
- Meta-Agent operational activation;
- target truth or write-authority changes;
- permission to ingest complete personal conversations or work source;
- changing Mnemosyne or Meta-Agent common methodology;
- automatic propagation or migration across targets.

### External fact — not an Owner preference

- present-day product, model, subscription, quota, context, file, connector, Voice, Project, Memory, Skills, or privacy behavior.

The interviewer must not ask the Owner to guess these facts. It may ask which outcome matters, then route the factual question to current verification.

## 8. Matters deliberately out of scope

- designing a complete universal Agent ontology;
- assigning permanent provider/model rankings;
- implementing Skills or provider adapters;
- creating target repositories or ingesting target materials;
- activating Meta-Agent;
- running PR #267 V1 model comparisons;
- launching Fable/Deep Research;
- evaluating archived handoffs;
- modifying execution source or target truth;
- building RAG, MCP, automation, a vector database, or cross-target auto-propagation.

## 9. Planner's provisional recommendations

These are recommendations, not fixed Owner decisions:

1. Accept the 42-entry catalogue as a **working inventory**, not a final ontology; correct omissions and confusing entries without blocking real use.
2. Approve the shared minimum by **semantic groups**, not by treating every capability as a separate file or mandatory per-turn procedure.
3. Reclassify some repository/research/provenance controls from unconditional first-version requirements to **triggered capabilities** where the relevant action is absent.
4. Use target-local truth with bounded Mnemosyne/Meta-Agent pointers as the default direction; allow a temporary bootstrap exception only with an explicit cutover/no-dual-writer gate.
5. For language learning, keep compact structured target truth in a private approved store and complete conversation exports in a private cold archive or verified pointer rather than public Git.
6. Use a hybrid first-use order: narrowly bounded Meta-Agent design work plus an early low-risk language-teacher pilot, while the code-library target waits only for a safe repository/storage and representative task choice—not for theoretical completion.
7. Defer current provider/Skills selection until a concrete target package needs it, then verify the smallest relevant product facts.

The Owner may reject or modify any recommendation.
