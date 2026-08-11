# Capability and Q&A Reference for the Owner Review

> This is the next-tier interviewer's primary explanation reference. It translates the candidate capability catalogue and first-three-system selection into concise natural language. Read the full source files only when the Owner asks for exact source/status details or this reference is insufficient.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
artifact_role: bounded_interviewer_explanation_reference
execution_source: false
current_product_facts_verified_here: false
```

## 1. Four distinctions to preserve

### Capability versus implementation

A capability says **what behavior is needed**. An implementation says **how one current product realizes it**.

Example:

- capability: continue correctly in a fresh conversation;
- possible implementations: repository files, project instructions, a Skill, a startup prompt, or another tool-specific mechanism.

Do not reject a useful capability merely because the current implementation is uncertain. Do not promote one provider's implementation into a universal capability.

### Required versus always loaded

“Required initially” means the semantics must exist in the first useful version. It does not mean:

- one file per capability;
- every task must load the full rule;
- every response must mention it;
- the capability must be automated.

A compact target spec may cover several capabilities, while detailed modules remain triggered.

### Source preservation versus runtime context

A complete conversation or report can be worth preserving without being read during ordinary work. Normal runtime should use compact current truth and state; complete originals are read only when a reconstruction, migration, incident, dispute, or longitudinal review needs them.

### Candidate versus approved truth

The catalogue, selection matrix, target-local operating model, and launch baseline are candidates. The Owner's interview answers become clarification evidence. They do not modify execution source or target truth until a separately authorized write/adoption task records the decision in the appropriate repository.

## 2. Compact reference for all 42 candidate capabilities

### Memory, source, and authority

| ID | Plain-language meaning | Typical need | Important limit |
|---|---|---|---|
| `ACAP-001` | Keep long-term state in durable files/stores, not only one model context. | nearly every long-lived system | does not require Git or a database specifically |
| `ACAP-002` | Declare one current target truth source. | all three systems | archive, summary, handoff, and evidence remain non-authoritative |
| `ACAP-003` | Label truth, decision, current state, handoff, method, evidence, raw source, candidate, and inference separately. | all three | roles must not change silently |
| `ACAP-004` | Preserve material original conversations/reports/tasks honestly as exact, reconstructable, normalized, receipt-only, or unavailable. | all three where sources matter | exactness requires mechanical evidence and safe storage |
| `ACAP-005` | Let new needs enter as source/candidates and require approval before current truth changes. | all three | not every minor remark needs a heavy workflow |
| `ACAP-006` | Record important choice rationale and old-to-new supersession/lineage. | all three | no hidden chain-of-thought required |
| `ACAP-007` | Keep current stage, blockers, and next action in a compact non-truth navigation view. | all three | current state cannot override target truth |
| `ACAP-008` | Let a qualified fresh session resume without hidden previous-chat assumptions. | all long-lived work | requires actual receive/recovery validation |
| `ACAP-009` | Keep large history cold and read it only on a clear trigger. | systems with growing archives | a summary error must still be traceable to source |
| `ACAP-010` | Load a small core plus task-specific modules and record what was read/excluded. | large or multi-purpose systems | candidate; behavior comparison not yet run |
| `ACAP-011` | Keep target truth in the target repository/store and prevent Mnemosyne/Meta-Agent from remaining competing writers. | repository/store-backed targets | bootstrap exceptions need cutover/no-dual-writer gates |
| `ACAP-012` | Use stable identity, version impact, migration mapping, validation, and rollback/revision. | long-lived targets | first version can be lightweight; no need for event sourcing |
| `ACAP-013` | When an upstream capability/method changes, identify affected targets and completed work. | Meta-Agent/Mnemosyne ecosystems | automatic propagation is not approved |

### Human interaction and decision quality

| ID | Plain-language meaning | Typical need | Important limit |
|---|---|---|---|
| `ACAP-014` | Separate verified facts, Owner values, model interpretation, and uncertainty. | all three | objective does not mean refusing to recommend |
| `ACAP-015` | Put current human actions in a clear operation section, separate from explanation and future steps. | tool-bearing/cross-system work | need not make every short reply rigid |
| `ACAP-016` | Prefer concise natural language; use structured blocks only when they improve understanding/decisions. | all three | repository machine schemas may remain structured |
| `ACAP-017` | Reconstruct the likely need without replacing the Owner's goal; preserve corrections and alternatives. | design/intake work | no mind-reading or stable profiling |
| `ACAP-018` | Ask material questions with background, consequence, option meaning, free-form/reject/defer paths. | design and learning | unnecessary for trivial questions |
| `ACAP-019` | Keep a visible ledger of answers, interpretations, corrections, deferrals, and conflicts. | multi-step decisions | external persistence is conditional |
| `ACAP-020` | Do not turn sparse behavior into stable personality, intelligence, learning-style, or ability labels. | especially language/personal Agents | evidence-based task-local hypotheses remain allowed |

### Work decomposition, research, and external execution

| ID | Plain-language meaning | Typical need | Important limit |
|---|---|---|---|
| `ACAP-021` | Split frontier reasoning, bounded next-tier execution, mechanical checks, and human-only decisions. | complex work | model names are not permanent tier assignments |
| `ACAP-022` | Stop and escalate on missing input, authority, privacy, architecture, or high-impact conflict. | all three | stopping must identify the correct return route |
| `ACAP-023` | Research only when external evidence can change a sufficiently frozen decision; human controls quota/run. | research-capable systems | important topic alone is not enough |
| `ACAP-024` | Use an independent frontier challenge when alternative reconstruction/adversarial review adds value. | high-impact/novel work | not required for every task; review is evidence, not authority |
| `ACAP-025` | State whether another task is analysis, prepared, optional, required, now, or after a gate. | cross-conversation work | not needed when no external task is discussed |
| `ACAP-026` | Give the user the complete operating flow rather than only a repository pointer. | external tasks | long body may stay file-first; steps must remain visible |
| `ACAP-027` | Deliver long structured transfer artifacts as verified files. | prompts, handoffs, taskbooks | do not generate files for every small answer |
| `ACAP-028` | Treat Deep Research as one complete canonical report with supported exports of the same report. | Deep Research adapter | current surface capabilities must be observed; no invented second report |

### Repository actions, authority, and provenance

| ID | Plain-language meaning | Typical need | Important limit |
|---|---|---|---|
| `ACAP-029` | Connected access/permission is not current task authorization; specify repository/path/action/scope/expiry. | code and repository work | high-risk conditional capability |
| `ACAP-030` | One task has one canonical branch and at most one open canonical PR. | GitHub PR workflow | provider/repository adapter, not universal Agent law |
| `ACAP-031` | Tell the user to retain a branch only for a verified dependency; explicitly release prior retention later. | selected Git workflows | ordinary deletion needs no routine notice |
| `ACAP-032` | Record actor, visible surface/selection, artifacts, review, and authorization without claiming hidden backend. | important audit/review work | provenance does not prove correctness |
| `ACAP-033` | Order per-repository reads/writes with separate authority and no-dual-writer semantics. | library+consumer or meta+target work | migration evidence exists; general validation remains open |

### Evaluation, evolution, and reuse

| ID | Plain-language meaning | Typical need | Important limit |
|---|---|---|---|
| `ACAP-034` | Record usefulness, failure, burden, corrections, postmortem, and regression candidates. | all real-use systems | model self-evaluation alone is insufficient |
| `ACAP-035` | One case cannot automatically become general methodology. | meta-systems | target-specific fixes may proceed locally |
| `ACAP-036` | Remove business details, target-type constraints, and temporary provider workarounds before generalization. | Meta-Agent/Mnemosyne | requires evidence, counterexamples, and Owner approval for common method changes |
| `ACAP-037` | Record which catalogue version/capabilities a target required, adapted, experimented with, deferred, or rejected. | all first targets | should reference, not copy, the whole catalogue into runtime |
| `ACAP-038` | Start a reversible useful version early and improve from real evidence. | all three | does not waive source, authority, privacy, or rollback floor |
| `ACAP-039` | Add RAG/indexing/automation only after measured deterministic retrieval burden justifies it. | later at scale | explicitly deferred before evidence |

### Provider and packaging adapters

| ID | Plain-language meaning | Typical need | Important limit |
|---|---|---|---|
| `ACAP-040` | Turn selected portable capabilities into prompts, instructions, commands, configs, or files for the chosen surface. | Meta-Agent and targets | no provider-neutral packaging standard yet |
| `ACAP-041` | Map capabilities into current Skill/module mechanisms where supported. | selected provider products | current Skills semantics require official verification |
| `ACAP-042` | Maintain a dated catalogue of model/product/plan/settings/tools/limits and bounded task results. | routing and packaging | must remain separate from portable capability truth and be rechecked |

## 3. Why the shared minimum can still be small in practice

The 18 shared entries are semantic safeguards, not an 18-component software platform.

A small target might implement them through:

- one compact approved spec covering purpose, truth, roles, authority, and selected capabilities;
- one source/requirements record;
- one current state and handoff;
- one decision/version/history record;
- one feedback/evaluation log;
- one private source/archive policy or pointer.

The first version does not need:

- a database;
- automatic indexing;
- automatic writeback;
- autonomous migration;
- a multi-Agent runtime;
- a universal schema;
- a full provider catalogue.

## 4. Target-specific explanation reference

### Meta-Agent

Primary concern: it creates designs and methods that may affect multiple future targets.

Most important additions:

- impact assessment (`ACAP-013`);
- explanation/answer ledger (`ACAP-018`, `019`);
- research and independent challenge routes (`023`, `024`);
- honest run evidence (`032`);
- case-to-method and portability gates (`035`, `036`);
- target capability selections (`037`);
- packaging (`040`).

Most important danger: one target's outcome becomes a universal method or Meta-Agent becomes an unapproved writer for targets.

### Work/business-function code library

Primary concern: preserve requirements/business rules/implementation/tests while distinguishing reusable functions from one project's local truth.

Most important target-specific needs:

- requirement-to-code traceability;
- reuse assumptions and rejected-reuse cases;
- compatibility/dependencies;
- test/acceptance/rollback evidence;
- private source/customer/credential boundary.

Most important danger: project-specific code is generalized without evidence, or cross-repository work changes the wrong truth source.

Repository controls (`ACAP-025`, `029`–`033`) should be triggered by the actual toolchain rather than automatically loaded in every task.

### Long-term language teacher/practice Agent

Primary concern: sustain useful teaching while preserving multidimensional evidence and allowing correction.

Most important target-specific needs:

- vocabulary/grammar/comprehension/production/coherence/pragmatics/task evidence;
- hint/repetition/transcription provenance;
- error/hypothesis/correction history;
- current teaching plan;
- delayed retention/transfer evidence;
- private complete-conversation archive;
- method-change rationale.

Most important danger: sparse conversation or speech-recognition noise becomes a permanent learner/personality label.

Research/provenance controls should be triggered by formal assessment, method changes, product decisions, or longitudinal review rather than burden every lesson.

## 5. Frequently asked questions

### Q1. Does approving the catalogue approve all 42 capabilities?

No. It approves using the catalogue as a working selection aid. Each target still chooses a minimum subset and target-specific adaptations.

### Q2. Does “required initially” mean a capability must be automated before use?

No. The first version may be manual, file-based, and human-reviewed. Required means the safety/continuity semantics should not be absent.

### Q3. Why preserve complete conversations if normal tasks should not read them?

Because later redesign, dispute, migration, longitudinal review, or stronger-model analysis may need the exact source. Routine loading would waste context and create irrelevant interference.

### Q4. Why not rely only on a summary of the original conversation?

Summaries are useful derived views but can omit or distort goals. Preserving source keeps future correction possible.

### Q5. Why must there be one target truth source?

Without one declared authority, a newer summary, handoff, Meta-Agent output, or copied repository may silently conflict with current behavior. One truth source does not mean one file contains all evidence.

### Q6. Why separate target repositories from Mnemosyne and Meta-Agent?

Target-local truth reduces cross-project write conflicts, irrelevant context, privacy leakage, and competing writers. Mnemosyne and Meta-Agent can still retain bounded pointers and generalized evidence.

### Q7. Can several target conversations work at the same time?

Potentially yes when each has a different primary repository/truth and they do not edit the same shared capability/method files. Shared truth objects still require serialization or reconciliation.

### Q8. Does cross-repository capability mean one task has permanent permission to all repositories?

No. Each task needs exact per-repository read/write scope, order, authorization, and expiry. Connected access is not authority.

### Q9. Why not put complete language-learning conversations in public Git?

They may contain private personal data, are large, persist in Git history, and are rarely needed in normal runtime. Private cold storage with safe pointers is the current recommended direction.

### Q10. Is a private Git repository always the best archive for complete conversations?

Not necessarily. A private local/cloud archive may be better for large sensitive exports, while compact structured truth/ledgers use a private repository or store. The Owner chooses the privacy/backup model.

### Q11. Why is Meta-Agent still inactive if it already has an approved spec?

The Owner accepted an inactive design/governance baseline, not operational readiness. Activation needs a separate bounded scope, blocker disposition, acceptance/stop/rollback criteria, and exact authority.

### Q12. Can the next-tier interviewer approve Meta-Agent activation?

No. It may explain and capture the Owner's preferred scope. Final activation planning and repository change require frontier/human re-entry.

### Q13. Is independent frontier review required for every Meta-Agent design?

No. Meta-Agent should have a triggered independent-challenge route for novel, high-impact, disputed, or acceptance-critical work. Ordinary bounded work need not spend another frontier run.

### Q14. Why is `ACAP-030` not a universal first-version capability for the code system?

It is specifically a GitHub PR lineage control. If the chosen toolchain uses GitHub PRs, it becomes required for those actions. It should not burden a local/non-PR workflow.

### Q15. Why is research gating not necessarily an everyday language-teacher rule?

Ordinary lessons should not continually evaluate research value. The capability should trigger when the system proposes a teaching-method change, current product claim, or evidence-dependent high-impact decision.

### Q16. Why not build RAG or a vector database immediately?

The first version can use deterministic files, current-state summaries, and source maps. RAG adds complexity, privacy, evaluation, and staleness risks. Add it only after real retrieval failures justify it.

### Q17. What is the difference between prompt packaging and Skills packaging?

Prompt packaging is the portable need to turn selected capabilities into usable instructions/configuration. Skills packaging is one provider-specific mechanism whose current semantics must be verified. They must not be assumed equivalent.

### Q18. What do Claude Skills currently support?

This package intentionally does not answer. It is a time-sensitive product fact. Record the decision it would affect, then verify current official documentation and, if necessary, run a bounded behavior check.

### Q19. Which current model should be used for each task?

The portable rule is task-class based: frontier for novel/high-impact judgment, validated next-tier for frozen bounded work, mechanical tools for exact checks, human for authority/privacy/acceptance. Current named model suitability requires dated evidence and may change.

### Q20. Does a capability selection force the same behavior forever?

No. The selection records required/adapted/experimental/deferred/rejected status and version. Real-use evidence can produce a target-specific change, migration, or catalogue/method candidate through review and Owner decision.

### Q21. Can an upstream capability update automatically modify targets?

No. It should identify affected target selections, classify impact, create target-specific candidates, and require target authority to adopt/migrate/rollback.

### Q22. What if the Owner does not know which repository/storage option is best?

Record the desired privacy, portability, backup, collaboration, and tool behavior. Defer the exact service/path and route current external facts to verification. Safe default is no private material ingestion before approval.

### Q23. What does “hybrid first-use order” really mean?

It means Meta-Agent may be tested in a narrow design-only role without becoming the only gate, while a low-risk language pilot begins after storage rules; code work waits only for a safe repository/task, not for all abstract design to finish.

### Q24. Does choosing language first mean code-library work is abandoned?

No. It means language supplies earlier low-risk real-use evidence while code storage/task selection is prepared. The Owner may instead choose code first or parallel work.

### Q25. Can the next-tier interviewer save the final result?

Only after a separate exact repository-write instruction. During the interview it should maintain the visible ledger in chat and return the completed result package without writing GitHub.

## 6. Source-status answers

When asked whether a capability is already “implemented,” answer precisely:

- `active source rule`: already present in current Mnemosyne execution/behavior guidance for its scope;
- `accepted Meta-Agent method`: accepted in the inactive Meta-Agent baseline, not operationally active;
- `candidate`: proposed by Owner input or recent design, not approved standing behavior;
- `partially validated`: some bounded evidence exists but broad reliability remains open;
- `provider adapter/research needed`: current product facts or implementation have not been verified.

Never collapse these into a simple yes/no unless the scope is clear.

## 7. Questions that must not be answered from this package alone

- current provider/model/plan pricing, quota, context, file, setting, tool, connector, Voice, Memory, Project, Skills, or data-use behavior;
- exact private repository/storage legal or employer compliance;
- whether current hidden backend identity matches a visible UI label;
- whether Meta-Agent is implementation-ready after its pending candidate revision work;
- whether a new shared capability library should be owned by Mnemosyne, Meta-Agent, or another repository;
- whether a target may ingest private source/personal conversations;
- whether an external research run should begin now without explicit authorization.

The interviewer should identify the decision these facts affect and return the appropriate verification/frontier route.
