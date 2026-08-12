# Capability-Selection and Q&A Guide for OR-02 through OR-09

> Primary explanation reference for the next-tier interviewer. It is deliberately more detailed than the decision workbook so ordinary Owner questions can be answered without reconstructing the entire repository or consuming another Pro turn. It does not establish current provider/product facts, approve target selections, activate Meta-Agent, or authorize repository/private-material actions.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
artifact_role: bounded_next_tier_answer_and_explanation_guide
execution_source: false
catalogue: notes/reusable-agent-capability-catalog-v0.2.md
selection_candidate: notes/first-three-system-capability-selection-v0.2.md
current_product_facts_verified_here: false
```

## 1. How the interviewer should answer a checklist question

When the Owner asks “这一项是什么意思”“为什么需要”“能不能删”“是不是太重”“三个 Agent 都需要吗”, answer in this order:

1. **Plain meaning** — what behavior the capability or object supplies.
2. **Problem prevented** — the concrete failure it is intended to reduce.
3. **Smallest first-version form** — how it can exist without heavy infrastructure.
4. **Why this target needs it** — shared, Meta-Agent, code-library, or language-teacher relevance.
5. **Boundary and maturity** — required, triggered, experimental, deferred, or target-specific; state evidence limits.
6. **Effect of omission** — what becomes harder or unsafe if it is left out.
7. **Decision freedom** — the Owner may accept, adapt, trigger, experiment, defer, reject, or reject the premise.
8. **Escalation** — identify whether the issue is an Owner choice, current product fact, missing artifact, or frontier architecture question.

Do not answer by merely repeating an `ACAP-*` label. Do not turn a provisional capability into a proven rule. Do not claim that “required” means one file, one prompt paragraph, or always-loaded detailed text.

## 2. Distinctions that resolve most questions

### 2.1 Capability versus implementation

A capability describes **what behavior is needed**. An implementation describes **how one target and one current product realize it**.

Example:

- capability: a fresh conversation can continue correctly;
- possible implementation: target files, a startup instruction, a Project instruction, a Skill, a command, or another product-specific mechanism.

The Owner can accept the capability while deferring the implementation. A current provider mechanism must not be promoted into a permanent universal rule.

### 2.2 Required initially versus always loaded

“Required initially” means the semantics must not be absent from the first bounded useful version. It does not mean:

- one file per capability;
- every turn reads every detailed rule;
- every response mentions it;
- automation must exist;
- the detailed mechanism has already been empirically validated.

One compact target spec can cover purpose, authority, source roles, selected capabilities, and stop boundaries. Task-specific modules can remain triggered.

### 2.3 Portable capability versus target-specific object

A portable capability is reusable across targets, such as preserving sources or handling handoff.

A target-specific object contains domain information, such as:

- requirement-to-code/test traceability;
- a language learner evidence ledger;
- dependency compatibility records;
- current teaching plan.

A target-specific object may be essential for one Agent without becoming a universal catalogue capability.

### 2.4 Source preservation versus routine reading

A complete conversation, report, or task can be worth preserving while remaining cold during normal work. It is read when original intent, migration, dispute, incident, or longitudinal review requires it.

Preserving source protects future correction. Excluding it from routine runtime protects attention and prevents old evidence from acting like current control logic.

### 2.5 Execution source versus target truth

Working analogy accepted by the Owner:

- model ≈ CPU;
- execution source ≈ the currently approved program controlling formal Agent behavior.

Target truth may be broader because it can also include authoritative current data, configuration, or business state. Raw evidence, research, candidates, current-state navigation, and handoff support the system but do not automatically control behavior.

### 2.6 Preparation versus activation versus use

- **Preparation:** design/select/package the system.
- **Activation authorization:** explicitly permit operation under a scope and authority.
- **Bounded real use:** perform actual tasks and collect results.

A package, repository, or selected capability list does not activate anything by itself.

### 2.7 Owner preference versus current external fact

The Owner decides goals, acceptable risk, preferred workflow, privacy tolerance, and priorities.

The interviewer must verify rather than guess current facts about models, plans, prices, quotas, Skills, Projects, Voice, Memory, connectors, exports, context limits, and privacy behavior.

---

# 3. OR-02 shared-floor answer guide

## 3.1 Durable source and current authority — ACAP-001 through ACAP-006

### What the group accomplishes

This group ensures that a long-lived Agent does not depend on one chat, does not lose the original goal, does not let drafts or summaries become authority accidentally, and can explain why its current design exists.

### Smallest practical form

A small target can implement the group through:

- one compact approved target spec and authority map;
- one source/requirements record or source-map section;
- one decision/change-history record;
- source pointers that distinguish exact, normalized, or external originals.

It does not require six services or six large files.

### Item explanations

**ACAP-001 — Durable external memory**  
Keeps long-term state outside one model context. Without it, the system effectively ends when the conversation ends. Storage can be Git, files, a database, or another approved store.

**ACAP-002 — One current adopted authority boundary**  
Specifies which approved source or source set controls current behavior when old versions, candidates, summaries, and handoffs disagree. “One” means one unambiguous authority system, not one physical file.

**ACAP-003 — Artifact-role and storage organization**  
Separates truth, decisions, current state, handoff, methods, evidence, raw source, candidates, and inference. Where practical, the storage layout should help a human see these roles rather than relying only on metadata.

**ACAP-004 — Source preservation with byte/semantic distinction**  
Preserves material originals honestly and distinguishes exact bytes, reconstructable archives, normalized copies, and substantive edits. A line-ending change alters bytes without necessarily changing meaning.

**ACAP-005 — Requirement intake, approval, and semantic conflict review**  
New ideas enter as source/candidates; simple duplication can be mechanical, but material long-range semantic conflict should use frontier reasoning. Approved truth changes only after the required human decision.

**ACAP-006 — Decision rationale, supersession, and lineage**  
Preserves externally stated engineering reasons, meaningful alternatives, assumptions, affected artifacts, and old-to-new relationships. It does not require hidden chain-of-thought. The Owner has chosen preservation rather than premature deletion; later review reads selectively.

### Why all three systems need it

- **Meta-Agent:** its design choices may influence many later targets.
- **Code library:** business rules and code must remain traceable to original requirements and decisions.
- **Language teacher:** goals, evidence, plan changes, and user corrections must not silently drift.

### What can be adapted

The exact filenames, schemas, and approval burden should differ by target. A trivial correction does not need the same process as a target-purpose change.

### Omission risk

Removing one item may be reasonable only with a replacement mechanism. Removing the entire group recreates dependence on conversation memory and ambiguous authority.

## 3.2 Current work, handoff, cold source, and target-local truth — ACAP-007, 008, 009, 011

### What the group accomplishes

It lets a new conversation know where work stands without reading the full archive, while keeping the target itself—not Mnemosyne or Meta-Agent—as the active writer.

### Smallest practical form

- one short current-state/handoff file or section;
- one source map identifying cold archives;
- one declared active target writer;
- optional read-only recovery snapshot with an exact identity.

### Item explanations

**ACAP-007 — Current-state navigation**  
Answers “现在做到哪里、有什么阻塞、下一步是什么”. It is a work map, not the program or truth source.

**ACAP-008 — Fresh-session and handoff continuity**  
A qualified new session should recover target, authority, current state, boundaries, and next action from explicit sources instead of hidden old-chat assumptions. A handoff is not proof; recovery should eventually be tested.

**ACAP-009 — Cold source as evidence/synthesis input**  
Raw conversations and research were created to be analyzed and synthesized into approved control logic, not to act as control logic themselves. They remain available for reconstruction and review but are excluded from normal runtime.

**ACAP-011 — Target-local truth, no dual writer, and non-authoritative backup**  
The target repository/store owns current target operation. Mnemosyne and Meta-Agent may keep bounded pointers and generalized evidence, but not competing editable truth. A backup is allowed only if it cannot become an independent writer.

### Why target-local does not mean isolated

The target can reference common capabilities, Meta-Agent design rationale, and Mnemosyne memory-system records. The rule prevents competing authority, not useful references.

### Why a backup does not violate single truth

A backup can preserve recovery bytes without controlling current behavior. It must be identity-pinned, non-authoritative, and not independently edited.

### Omission risk

Without the group, fresh sessions rescan history, old handoffs reappear as current, and multiple repositories can drift into competing writers.

## 3.3 Controlled evolution — ACAP-012

### Plain meaning

Important target objects retain enough identity and version history to change safely. A real change can preserve, transform, recompute, retire, or re-evaluate existing objects. Rollback is one option, not the central purpose.

### Why it is proposed before mature migration evidence exists

The first version need not predict every future migration. It should merely avoid anonymous overwrite and preserve enough history for later improvement.

### Smallest practical form

- stable IDs for important objects;
- one compact version/change record;
- previous-state or commit reference;
- a short effect statement when a material change occurs.

### Owner decision choices

- required semantic floor, experimental mechanism;
- triggered only at the first material change;
- deferred until a real change;
- alternative formulation.

### What would be too heavy now

A universal migration service, event sourcing, automatic dual-write, or a large compatibility framework without a real target need.

## 3.4 Objective, readable, and correctable interaction — ACAP-014, 016, 017

**ACAP-014 — Objective evidence-bound engineering**  
Separates facts, Owner values, model interpretation, and uncertainty. It permits recommendations but prohibits flattering certainty.

**ACAP-016 — Human-readable concise presentation**  
Uses natural language for the human interface and structured blocks only when they improve comparison or decision visibility. Machine schemas may remain structured in repository files.

**ACAP-017 — Staged intent reconstruction with correction rights**  
Distinguishes wording, symptom, goal, proposed solution, assumptions, and alternative interpretations. Major ambiguity may use next-tier preliminary questions, frontier reconstruction, next-tier follow-up, and frontier adjudication. Ordinary tasks need not use all stages.

### Why this is a shared floor

All three systems depend on understanding human goals. A technically correct system can still fail by optimizing the wrong interpretation or making its explanation unusable.

### Omission risk

- unsupported conclusions become persistent truth;
- the user cannot understand or correct the system;
- an incomplete sentence becomes a permanent specification.

## 3.5 Work routing and calibrated stop/escalation — ACAP-021, 022

**ACAP-021 — Capability-aware work decomposition**  
Separates frontier/open reasoning, validated bounded execution, mechanical checks, and human-only decisions. Named models are not permanently assigned to tiers.

**ACAP-022 — Bounded effort and calibrated stop/escalation**  
Uses observable triggers rather than model self-confidence alone. Examples: missing authority, unresolved architecture, repeated acceptance failure, need to invent facts, scope expansion, or exhausted bounded attempts.

### Why “escalate when unsure” is insufficient

A model may overestimate or underestimate itself. The mechanism should rely on task contracts, acceptance checks, and observable failure evidence.

### Why “never give up” is also insufficient

Persistent effort is useful only while it remains within authority and produces reviewable progress. Repeated semantic failure can waste time and hide risk.

### Smallest practical form

- task-class label;
- explicit acceptance and stop conditions;
- one correction attempt when appropriate;
- a return route to stronger reasoning or human decision.

### Maturity

The purpose is accepted; calibration remains experimental and should be measured through actual next-tier tasks.

## 3.6 Real-use evaluation and controlled improvement — ACAP-034, 038

**ACAP-034 — Real-use evaluation, feedback, and postmortem**  
Records usefulness, burden, omissions, errors, corrections, and recurring failures—not merely artifact completion. Formal postmortems are reserved for severe, repeated, cross-target, or difficult failures.

**ACAP-038 — Early bounded use with controlled evolution**  
Starts useful work before theoretical completion while preserving source, authority, privacy, feedback, and change paths. Evolution is normal; rollback is optional.

### Smallest practical form

After a representative task, record:

- intended value;
- observed result;
- user usefulness/burden;
- correction or failure class;
- whether the issue appears target-local or potentially reusable.

### Why this is not premature bureaucracy

The first record can be a few lines. The purpose is to keep “PR merged” from being mistaken for “system valuable.” Fields that do not change later decisions should be removed after experience.

## 3.7 Why other capabilities are shared triggered modules

The following are common, but their detailed rules need not be loaded when their triggering action is absent:

- `015`: current human operations;
- `018`–`019`: material multi-step clarification;
- `023`–`024`: research or independent challenge;
- `025`–`028`: cross-conversation/external-task output and transfer;
- `029`–`033`: connected-service/repository actions;
- `039`–`042`: retrieval scale or provider packaging.

Making them triggered reduces irrelevant context without deleting the capability. The Owner may move a named item into the shared floor if a target's ordinary work nearly always triggers it.

---

# 4. OR-03 Meta-Agent answer guide

## 4.1 Why Meta-Agent needs more than the shared floor

Meta-Agent does not merely perform one business task. It designs Agents and methods that may affect several targets. Its special risks are:

- one case becoming universal methodology;
- a method change affecting already designed Agents;
- producing abstract designs that cannot be packaged into usable instructions;
- becoming an unapproved target writer;
- spending research/frontier quota without decision value.

## 4.2 Proposed required additions

**ACAP-013 — Upstream impact assessment**  
When a common method changes, identify targets that used the old version and classify future-only, review, rebuild, migration, completed-work re-evaluation, privacy, or authority effects. The first index can be lightweight.

**ACAP-018 — Context-rich clarification**  
Meta-Agent often asks architecture and workflow questions. The Owner needs origin, consequences, options, free-form response, rejection, and deferral—not unexplained IDs.

**ACAP-019 — Answer ledger**  
Several Agent-design decisions depend on one another. The ledger prevents tentative answers or model interpretations from silently becoming final.

**ACAP-023 — Research-value and quota gate**  
Meta-Agent should distinguish Owner preference, ordinary verification, Deep Research, and independent frontier challenge. It cannot authorize quota itself.

**ACAP-032 — Run context and provenance**  
Important designs should record actor, visible surface, artifacts, review relation, authorization, and limitations without claiming hidden backend identity or correctness.

**ACAP-035 — Controlled generalization and method promotion**  
Separates business truth, target-type constraints, user/organization specifics, provider workarounds, and portable semantics before a case changes common methodology.

**ACAP-037 — Capability selection/adoption record**  
Every designed target should state which catalogue version/capabilities it requires, adapts, triggers, experiments with, defers, or rejects.

**ACAP-040 — Capability-to-instruction packaging**  
Meta-Agent's design must eventually become usable prompts, instructions, files, commands, or provider adapters. Accepting the need does not approve a particular prompt format or Skill mechanism; the design problem remains open.

## 4.3 Why independent frontier challenge is triggered, not universal

`ACAP-024` is valuable for novel, disputed, high-impact, or acceptance-critical work. Requiring it for every bounded design would duplicate effort and consume quota without proportional value.

## 4.4 Why Skills and provider catalogue are experiments

`ACAP-041` and `042` depend on current product facts. The portable semantics are known, but actual loading, precedence, context cost, security, and product reliability must be verified at the time of use.

## 4.5 Does selecting these capabilities activate Meta-Agent?

No. Meta-Agent remains operationally inactive. The selection becomes input to a later Meta-Agent-owned package and Owner decision. Its current P0 candidate work and activation gates remain separate.

## 4.6 Could Meta-Agent own the common capability catalogue?

That is an unresolved architecture/ownership question. The interviewer may record the Owner's preference but must mark:

`FRONTIER_REENTRY_REQUIRED — shared capability-library ownership and lifecycle`.

---

# 5. OR-04 code-library answer guide

## 5.1 Why only ACAP-029 and ACAP-037 are proposed as additional required portable capabilities

The shared floor already covers memory, authority, source, continuity, evolution, reasoning, and feedback. Most additional code-system needs are domain objects, not universal Agent behaviors.

- `ACAP-029` is required because connected repository access is not permission to modify arbitrary work code.
- `ACAP-037` is required so the Agent behavior package/version remains distinct from the code/business asset catalogue.

GitHub PR, branch retention, provenance, transfer, and cross-repository rules become required when the actual workflow triggers them.

## 5.2 Target-specific objects

**Requirement and business-rule source**  
Preserves what the function should do and who decided it. Prevents code from becoming the only surviving specification.

**Requirement → decision → implementation → test/acceptance trace**  
Allows a future correction to identify which code and tests are affected.

**Reusable versus project-local boundary and rejected reuse**  
Records not only successful reuse but cases where assumptions differ and reuse is unsafe.

**Function/API/dependency/compatibility record**  
Supports discoverability, version effects, and consuming-project impact.

**Private source/customer/credential boundary**  
Prevents a reusable library process from pulling confidential or secret material into an inappropriate repository or model context.

**Consuming-project links and migration impact**  
Identifies where a shared function is used and what a change could affect.

**Useful-result, rework, and failure record**  
Shows whether the asset reduced work or created maintenance burden.

## 5.3 Why PR controls are triggered

A local or non-PR coding workflow does not need GitHub PR lineage rules. Once GitHub PRs are used, `ACAP-030` applies. The current one-canonical-PR default is a safety control; explicitly designed parallel variants remain possible with reconciliation.

## 5.4 Why research is not an everyday coding rule

Ordinary frozen implementation should use tests and exact authority. Research/frontier review triggers on novel architecture, disputed business rules, external facts, severe failures, or uncertain reuse—not on every code edit.

## 5.5 Can the first code task use private work code?

Not from this interview alone. Private source, customer material, repository visibility, credentials, and Agent access require a later exact storage/authority preflight and Owner authorization.

## 5.6 Can code-library preparation start without Meta-Agent activation?

Yes. Mnemosyne/Pro can prepare a target intake and minimal package. Using Meta-Agent to design it is a separate bounded pilot/activation decision.

---

# 6. OR-05 language-teacher answer guide

## 6.1 Why the four additional portable capabilities are proposed

**ACAP-018 — Context-rich clarification**  
Learning goals, task difficulty, plan changes, and assessment meaning need understandable choices and free correction.

**ACAP-019 — Answer ledger**  
Goals and preferences can change; the system must distinguish new correction, temporary preference, and earlier misunderstanding.

**ACAP-020 — Evidence-calibrated user-state inference**  
Sparse lessons, mood, topic familiarity, hints, transcription errors, or changing focus must not become permanent personality, learning-style, or ability labels.

**ACAP-037 — Capability selection record**  
Keeps the teaching behavior/memory package and its version explicit so later changes can be assessed.

## 6.2 Target-specific teaching/memory objects

**Multidimensional language evidence**  
Record only dimensions the activity actually tests: vocabulary, grammar, comprehension, spoken/written production, coherence, pragmatics, task completion, and other justified dimensions.

**Evidence provenance**  
Distinguish independent production from hinted, repeated, translated, or speech-recognition-affected performance.

**Error, alternative explanation, correction, recurrence, uncertainty**  
An observed error may arise from language knowledge, task misunderstanding, noise, fatigue, or transcription. Preserve competing explanations and later correction.

**Current goals, teaching plan, exercise history, and burden**  
Keeps teaching adaptive without treating every session as a permanent learner trait.

**Immediate performance versus delayed retention/transfer/independence**  
Fluent repetition immediately after explanation is not the same as later independent use.

**Private complete-conversation archive or verified pointer**  
Supports longitudinal review and stronger-model re-analysis without loading every old conversation in ordinary lessons.

**Teaching-method change rationale and keep/revise criteria**  
Makes plan changes reviewable rather than opaque.

**User correction, deletion, and dispute path**  
The user must be able to correct evidence interpretation and challenge or remove inappropriate records according to the target's policy.

## 6.3 Why stable profiling is deferred

A profile can be useful only when the teaching purpose, repeated evidence, correction rights, uncertainty, and counterevidence justify it. “The user frequently changes requirements” or “the user is a visual learner” must not arise from a few contextual observations.

## 6.4 Why full conversations should be private and cold

They may contain personal information, are large, and are rarely needed per lesson. Compact current teaching truth belongs in an approved target store; complete exports can remain in separate private cold storage or under verified pointers.

## 6.5 Why formal assessment and voice policy may need Pro/frontier

They change the learner model, evidence interpretation, and potentially high-impact claims. Current voice/transcript behavior is also a time-sensitive product fact.

## 6.6 Can the first version teach without claiming a stable proficiency level?

Yes. It can conduct low-risk practice, record task-local evidence, adapt exercises provisionally, and collect user feedback while deferring formal longitudinal claims.

---

# 7. OR-06 and OR-07 repository/storage answer guide

## 7.1 Why target-local truth is the default recommendation

It reduces irrelevant loading, accidental cross-project edits, global PR serialization, privacy mixing, and competing writers. Mnemosyne and Meta-Agent still keep bounded pointers and generalized evidence.

## 7.2 Does one repository per target create too much fragmentation?

It adds navigation overhead, but a target index and stable pointers can manage it. The alternative—many live target truths in one meta repository—creates stronger authority, privacy, and concurrency coupling.

## 7.3 Can different target projects proceed concurrently?

Potentially yes when each writes a different target repository/truth and neither edits shared methodology or capability files. Shared truth objects still require serialization or reconciliation.

## 7.4 What is a bootstrap exception?

A temporary target workspace inside a meta-system before a destination exists. It must be labelled non-final, have a planned destination, pass destination-only recovery, and end with a no-dual-writer cutover.

## 7.5 Why not keep a live mirrored copy in Mnemosyne for safety?

A live editable mirror becomes a second writer and creates ambiguity. Use immutable or read-only identity-pinned backups instead.

## 7.6 Is private Git always the best store?

No. It may be appropriate for structured versioned truth, but large sensitive conversation exports may be better in a private local or cloud archive with verified pointers and backups. The Owner chooses the desired properties; current service privacy facts require verification.

## 7.7 Can the interview approve a concrete storage service?

No. It can capture desired properties and preferences. Concrete private-material ingestion or a new trust/permission relationship requires Pro/frontier preflight and current product verification.

## 7.8 Why separate structured truth from complete originals?

They have different runtime, size, privacy, and retrieval needs. Structured truth is frequently read and edited; complete originals preserve evidence and are read on demand.

## 7.9 What makes a recovery backup non-authoritative?

It has a declared source/version identity, is immutable or read-only, is not independently edited, and is used only for recovery. It cannot override the target's current adopted authority.

---

# 8. OR-08 order and launch answer guide

## 8.1 Why preparation order and pilot order differ

A system can be designed and reviewed before it is allowed to operate. This lets work proceed without accidentally activating Meta-Agent or ingesting private data.

## 8.2 Must Meta-Agent be ready before either target begins?

No. Requiring full Meta-Agent readiness would recreate the “wait until complete” pattern. A target package can be prepared directly while Meta-Agent's own bounded-use package is developed separately.

## 8.3 Why the planner recommends parallel preparation

It avoids idle time and lets the first target whose storage/material/task preflight becomes ready generate real evidence. It does not mean parallel writes to shared capability/method truth.

## 8.4 What blocks the language target?

At minimum: private storage/correction path, allowed evidence scope, target truth, first low-risk task, and any required current text/voice/product facts.

## 8.5 What blocks the code target?

At minimum: safe repository/toolchain, allowed non-sensitive representative tasks, private/customer/credential boundary, target truth, and write authority.

## 8.6 What blocks Meta-Agent operational use?

Its current target truth is inactive. Separate Owner authorization, current blocker/health-review disposition, exact pilot scope, acceptance/stop criteria, authority, and no-private-material conditions are required.

## 8.7 Can the Owner choose only one target?

Yes. The three-system plan is a candidate sequence, not a requirement. The Owner may defer or reject any target.

---

# 9. OR-09 current-product answer guide

## 9.1 Why product facts are not included in this package

They change rapidly and require current official evidence or bounded tests. Storing them as permanent capability truth would make the design stale and provider-specific.

## 9.2 What may the interviewer explain without web verification?

It may explain the decision logic and which facts matter. It must not claim current model lists, prices, quotas, limits, Skills behavior, settings, privacy, or connector actions.

## 9.3 What should be verified first?

Only the smallest facts that can change the first selected target decision. Examples:

- for near-term Claude-centered work: current instruction/Skill/project/file/repository behavior relevant to the chosen package;
- for language use: current text/voice/transcript/export/privacy facts;
- for code use: repository, testing, private-source, and artifact behavior.

This is a priority suggestion, not a claim about current product capability.

## 9.4 Does choosing Claude-first approve Claude Skills?

No. It only prioritizes verification. Current Skill semantics, loading, precedence, context cost, tool access, versioning, and security must be checked.

## 9.5 When is a bounded behavior test needed?

When official documentation does not establish actual reliability for the exact task class, or observed behavior conflicts with documentation.

## 9.6 When is Deep Research justified?

When evidence is distributed, recent, contested, and can materially change a high-impact choice. A simple current product lookup usually needs ordinary official-document verification, not Deep Research.

## 9.7 When is Fable/frontier research justified?

For open architecture, ownership, lifecycle, adversarial alternatives, or high-impact acceptance—not for simple product fact lookup or mechanical catalogue population.

## 9.8 Required marker

Use:

`CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED — <fact and affected OR question>`.

Continue unrelated Owner choices when possible; do not force the Owner to guess the fact.

---

# 10. Frequently asked questions

### Q1. Does accepting the shared floor approve all 41 capabilities?

No. It approves a compact common semantic floor. Other capabilities remain target-specific, triggered, experimental, deferred, or not applicable.

### Q2. Does accepting a target selection modify that target?

No. The answer becomes clarification evidence. A later authorized task must apply it to the correct target repository/store.

### Q3. Why not load the entire catalogue into every Agent?

The catalogue is a design index, not runtime instructions. Targets reference selected IDs and implement only the relevant semantics locally.

### Q4. Can a capability be both required and experimental?

Yes. The semantic safeguard may be required while the detailed implementation or threshold remains experimental—for example migration, escalation calibration, or feedback records.

### Q5. Why keep ACAP-012 in the floor when migration is speculative?

Because stable identity and non-destructive change are durable minima. The heavy mechanism is deferred; real changes supply the detailed pattern.

### Q6. Why keep ACAP-022 when models may not know their limits?

The v0.2 definition avoids relying on self-confidence alone and uses observable task triggers and acceptance failures. Its calibration remains a real-use experiment.

### Q7. Why keep ACAP-034 when evaluation thresholds are unknown?

Without any outcome/burden record, real use cannot improve the system. The initial record can be tiny; formal postmortems remain rare.

### Q8. Why is ACAP-015 not always required?

Its semantics matter when the user must act. A short informational lesson or internal bounded step may have no user operation to separate.

### Q9. Why are repository controls not universal?

They are action-specific adapters. An Agent not writing repositories should not load PR and branch rules.

### Q10. Why does Meta-Agent need ACAP-040 if packaging is unresolved?

Because producing usable instructions is part of its value. The requirement identifies the design problem; it does not pretend the solution is known.

### Q11. Could ACAP-040 and ACAP-041 be the same?

No. `040` is the general need to convert capabilities into executable instructions. `041` is one product-specific Skill/module adapter.

### Q12. Does OR-03 approve Meta-Agent's common-library ownership?

No. Ownership and lifecycle of a shared capability library require frontier architecture review.

### Q13. Does OR-03 activate Meta-Agent?

No. Its authoritative spec remains inactive and activation is separately gated.

### Q14. Why does the code target need an explicit rejected-reuse record?

Because knowing where reuse is unsafe prevents later models from applying a function outside its assumptions merely because it looks similar.

### Q15. Is source code itself the code target's execution source?

Not necessarily. Code is authoritative implementation, while Agent behavior instructions and business truth may be separate target-truth components. The target must define the authority map.

### Q16. Why does the language target need evidence provenance?

A correct answer after a hint, translation, repetition, or faulty transcription is different evidence from independent production.

### Q17. Can the language Agent adapt after one lesson?

It may make scoped provisional adaptations, but should not create stable proficiency, personality, or learning-style claims from weak evidence.

### Q18. Do complete conversations need to be in the same repository as learner truth?

No. The recommended direction is compact structured truth in an approved private target store and complete conversations in private cold storage or verified pointers.

### Q19. Can a private repository safely store every private original?

Not automatically. Size, Git history persistence, access, provider exposure, backup, and privacy requirements must be assessed.

### Q20. Why not choose exact repository names now?

Repository/store names are easy; visibility, authority, private-material policy, and tool access are the consequential decisions. The interview may record naming preferences but should not create anything.

### Q21. Can Mnemosyne keep a compact target backup?

Only as a clearly non-authoritative, identity-pinned, non-editable recovery copy. It must not become target truth or a live writer.

### Q22. Can two target conversations work simultaneously?

Yes when they own different target truth and do not edit shared method/capability objects. Shared objects require serialization or reconciliation.

### Q23. Why not start with Meta-Agent only?

That is an available option, but it delays real target evidence and may recreate indefinite preparation. The planner therefore favors parallel preparation, not automatic activation.

### Q24. Why might the language target be a good early pilot?

It can provide frequent low-risk feedback and direct value. Its privacy, evidence-noise, voice, and product-surface boundaries must be handled first.

### Q25. Why might the code target be a good early pilot?

It produces concrete artifacts and mechanical tests. Private work/customer/credential boundaries may make the first safe task harder to select.

### Q26. Does selecting a first target authorize the first task?

No. The exact task, materials, repository/store, model/tool actions, acceptance, and stop conditions remain separately gated.

### Q27. Which named model is the next tier?

The durable rule is task-class based. Current named-model suitability requires dated evidence and can change.

### Q28. Can the next-tier interviewer make recommendations?

It may state the Pro planner's recommendations and explain trade-offs. It must not invent a new high-impact recommendation or silently choose for the Owner.

### Q29. What if the Owner proposes a new shared database or automatic propagation?

Record the idea and return `FRONTIER_REENTRY_REQUIRED`; do not finalize the architecture in the next-tier interview.

### Q30. What if the Owner asks a current Claude/ChatGPT/Fable question?

Mark `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED`, identify which decision it affects, and do not answer from memory.

### Q31. What if an exact target repository or source artifact is missing?

Mark `MISSING_ARTIFACT_BLOCKS_DECISION` only when the answer actually depends on it. Do not ask the Owner to recreate facts that an available artifact can establish.

### Q32. What if the guide does not answer a question?

Use the on-demand source map, read only the named authoritative source, disclose the extra path, and avoid indiscriminate repository loading.

### Q33. Is ACAP-031's periodic branch audit active now?

Yes for Mnemosyne after PR #271 merged. The catalogue v0.2 was authored before that merge and contains a stale maturity phrase saying the audit was proposed. The current guard `current/pr-merge-branch-disposition-guard.md` controls active Mnemosyne behavior. This status correction does not automatically propagate to another target.

### Q34. Does accepting the target-local model mean all materials go to GitHub?

No. “Target-local” means one target-owned authority boundary; that boundary can combine a repository for structured truth with a private archive or safe pointers for complete originals.

### Q35. Must every choice be final before the review completes?

No. `PARTIAL_WITH_DEFERRALS` is valid. Record the safe default and revisit trigger instead of manufacturing certainty.

## 11. When to read an additional source

Use this guide first. Read an on-demand source only for exact wording, status, source identity, repository role, or target-authority questions. State:

> 为回答 OR-XX 的这个问题，我额外读取了 `<path>`；没有读取其他冷历史材料。

Do not claim an unread file influenced the answer.

## 12. Stop and escalation summary

Use `FRONTIER_REENTRY_REQUIRED` for:

- new execution source, target truth, authority, privacy, trust, or writer relationship;
- Meta-Agent activation;
- common capability-library ownership;
- automatic propagation/shared runtime state;
- broad irreversible migration or completed-work re-evaluation;
- materially new target purpose or architecture;
- conflict with fixed OR-01 decisions.

Use `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED` for current product facts.

Use `MISSING_ARTIFACT_BLOCKS_DECISION` when an exact missing source is necessary.

Independent low-impact questions may continue if the escalation does not invalidate them.
