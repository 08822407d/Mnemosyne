# Reusable Agent Capability Catalogue — Owner-Reviewed Candidate v0.2

> Human-readable, non-execution-source catalogue of reusable Agent operating capabilities. It is a selection and design aid, not a universal runtime package, execution source, target truth, provider implementation, or proof of empirical effectiveness.

```yaml
catalog_id: MNEMOSYNE-REUSABLE-AGENT-CAPABILITY-CATALOG-001
version: 0.2.0
task_id: MNEMOSYNE-202
status: owner_reviewed_candidate_for_target_selection_and_real_use
supersedes_candidate_version: 0.1.0
source_owner_review: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
source_mnemosyne_ref: 08822407d/Mnemosyne@bd15d62b3111a9f2e55aa64151943f7b4d7f8713
source_meta_agent_ref: 08822407d/Meta-Agent@1fdbd7af9437f72f7c8106714ad1e64908983fb7
active_entry_count: 41
retired_entry_ids:
  - ACAP-036
execution_source_modified: false
Meta_Agent_modified: false
automatic_target_adoption: false
```

## 1. Purpose and use

The catalogue exists so that neither the Owner nor an Agent designer must remember every capability developed across long conversations and projects.

It supports:

1. discovery of existing reusable operating capabilities;
2. plain-language understanding of their purpose and limits;
3. target-specific selection of a minimum sufficient subset;
4. versioned records of adoption, adaptation, experiment, deferral, or rejection;
5. later impact analysis when an upstream capability changes.

A target must reference selected capabilities and implement them locally. It must not load this complete catalogue as routine runtime instructions.

## 2. Status and portability vocabulary

### Maturity/status

- **active-source basis** — semantics already appear in current Mnemosyne execution/behavior guidance;
- **accepted Meta-Agent basis** — semantics appear in the Owner-accepted but operationally inactive Meta-Agent methodology;
- **owner-reviewed candidate** — direction accepted through OR-01 but not yet adopted by a target;
- **provisional / real-use evidence needed** — direction accepted, detailed boundaries not yet established by practice;
- **provider fact/adapter verification needed** — implementation depends on current external product evidence.

### Portability

- **broad core** — likely useful for most long-lived Agents;
- **common optional/triggered** — common but only when a task or lifecycle condition applies;
- **high-risk conditional** — relevant when authority, privacy, writes, or irreversible actions exist;
- **provider adapter** — one product-specific implementation of a portable behavior;
- **target-specific** — business semantics that must remain local.

## 3. Capability inventory

### A. Durable memory, source, authority, and continuity

| ID | Capability | Plain-language behavior | Maturity | Portability |
|---|---|---|---|---|
| `ACAP-001` | Durable external memory | Keep long-term state in durable files/stores rather than only one model context. | active-source basis | broad core |
| `ACAP-002` | One current adopted authority boundary | Identify which approved source or source set currently controls target behavior when historical, candidate, summary, or handoff artifacts disagree. “Current” means adopted, not merely newest. | active-source and accepted Meta-Agent basis | broad core |
| `ACAP-003` | Artifact-role and storage organization | Separate target truth, decisions, current state, handoff, methods, evidence, raw source, candidates, and inference; reflect roles in human-navigable repository/store organization where practical. | active-source and accepted Meta-Agent basis | broad core |
| `ACAP-004` | Source preservation with byte/semantic distinction | Preserve material originals honestly; distinguish exact byte identity, reconstructability, format normalization, and substantive-content change. A line-ending conversion changes bytes but may leave substantive content unchanged. | active-source basis; terminology repaired by v0.2 | broad core for material sources |
| `ACAP-005` | Requirement intake, approval, and semantic conflict review | Preserve new needs as source/candidates, mechanically detect simple duplication, use frontier reasoning for material long-range semantic conflicts, and require approval before current truth changes. | active-source basis; frontier split owner-reviewed | broad core |
| `ACAP-006` | Decision rationale, supersession, and lineage | Preserve all material external engineering rationale, alternatives actually considered, assumptions, affected artifacts, and old-to-new relationships. Keep hidden chain-of-thought out of scope and read rationale selectively during review. | active-source basis; preservation scope owner-reviewed | broad core |
| `ACAP-007` | Current-state navigation | Maintain a compact non-authoritative view of current phase, completed work, blockers, unknowns, dependencies, and one safe next action. | active-source and accepted Meta-Agent basis | broad core |
| `ACAP-008` | Fresh-session and handoff continuity | Let a qualified fresh session recover target, authority, current stage, boundaries, and next action from explicit sources rather than hidden conversation memory. | active-source and accepted Meta-Agent basis | broad core for long-lived work |
| `ACAP-009` | Cold source as evidence/synthesis input | Preserve raw conversations, research, and history as inputs from which approved control logic is derived; exclude them from ordinary runtime unless reconstruction, dispute, migration, incident, or longitudinal review requires them. | active-source basis; rationale clarified by v0.2 | broad core at scale / common triggered |
| `ACAP-010` | Runtime load profile, receipt, and coverage-gap handling | Load a small core plus task-triggered modules; record what was read/excluded. When no specific rule covers a contemplated behavior, disclose the gap, use general rules only for low-risk reversible work, stop for high-impact gaps, and create a candidate coverage item rather than inventing an active rule. | owner-reviewed candidate; V0 static mapping passed; behavior validation pending | common optional with high value at scale |
| `ACAP-011` | Target-local truth, no dual writer, and non-authoritative backup | Keep target truth/current operation in the target repository/store; prohibit competing live writers. Permit identity-pinned read-only recovery snapshots or backups elsewhere when clearly non-authoritative and not independently edited. | Meta-Agent migration evidence plus owner-reviewed amendment | broad core for repository/store-backed targets |
| `ACAP-012` | Controlled evolution, migration, compatibility, and rollback | Use stable identity, version impact, preserve/transform/recompute/retire decisions, validation, compatibility, and recovery. Migration/evolution is normal; rollback is one optional response. | provisional / real-use evidence needed | common optional; required for long-lived targets |
| `ACAP-013` | Upstream change impact assessment | Identify targets and completed work affected by a changed Mnemosyne capability or Meta-Agent method; classify future-only, review, rebuild, migration, re-evaluation, or authority/privacy effects without automatic propagation. | provisional / multi-target evidence needed | broad for meta-systems; triggered for targets |

### B. Human interaction, intent, and decision quality

| ID | Capability | Plain-language behavior | Maturity | Portability |
|---|---|---|---|---|
| `ACAP-014` | Objective evidence-bound engineering | Separate verified facts, Owner goals/values, model interpretation, and uncertainty; give recommendations without flattering or inventing certainty. | active-source basis | broad core |
| `ACAP-015` | User operation versus explanation separation | Put current human actions prominently and separately from analysis, findings, and later steps. | active-source basis | core for tool-bearing/cross-system work |
| `ACAP-016` | Human-readable concise presentation | Prefer concise natural language; use schemas/structured blocks only when they improve understanding or decision visibility and explain their meaning. | owner-reviewed candidate with active-guidance basis | broad core |
| `ACAP-017` | Staged intent reconstruction with correction rights | Distinguish wording, need, symptom, proposed solution, assumptions, and alternatives. Where useful: next-tier preliminary questions → frontier reconstruction/decision design → frontier-prepared follow-up package → next-tier explanation and answer capture. | active-source and accepted Meta-Agent basis; staged workflow candidate | broad core for design/intake |
| `ACAP-018` | Context-rich clarification | Ask material questions with origin, known state, consequence, option meanings, recommendation, free-form/reject/defer paths, and escalation. | active-source basis | common optional |
| `ACAP-019` | Answer ledger and correction tracking | Preserve user answers separately from model interpretation, corrections, deferrals, conflicts, and residual uncertainty across dependent questions. | active-source basis; current OR-01 exercise supplied practical evidence | common optional for multi-step decisions |
| `ACAP-020` | Evidence-calibrated user-state inference | Do not infer stable personality, intelligence, motivation, learning style, ability, or “frequently changing requirements” trait from sparse/context-dependent behavior. Allow scoped, purpose-relevant, correctable hypotheses with source, uncertainty, and counterevidence. | owner-reviewed broadened candidate | broad core for personal/long-lived Agents; stronger for learning Agents |

### C. Capability routing, research, and external execution

| ID | Capability | Plain-language behavior | Maturity | Portability |
|---|---|---|---|---|
| `ACAP-021` | Capability-aware work decomposition | Split frontier/open reasoning, validated next-tier bounded execution, mechanical verification, and human-only decisions; do not permanently bind named models to tiers. | active-source and accepted Meta-Agent basis | broad core for complex work |
| `ACAP-022` | Bounded effort and calibrated stop/escalation | Stop or escalate on authority/privacy/architecture/missing-input/high-impact conflicts, but do not rely on model self-confidence alone. Use observable task triggers, bounded attempt budgets, acceptance checks, and repeated-failure signals to balance persistence against premature escalation. | provisional / controlled validation needed | broad core |
| `ACAP-023` | Research-value and quota gate | Research only when an external question is decision-relevant, sufficiently frozen, not answerable by ordinary verification, and worth cost/delay; human controls provider/surface/quota/run. | active-source basis | common optional |
| `ACAP-024` | Independent frontier challenge | Use a separately framed high-capability review for alternative reconstruction, adversarial failure search, or high-impact acceptance when its distinct value justifies it. | owner-reviewed candidate with provenance basis | common triggered |
| `ACAP-025` | Cross-conversation execution intent | State whether an external task is analysis, prepared, optional/required, now/after gate, and whether execution/quota is authorized. | active behavior guard | common optional |
| `ACAP-026` | Complete visible operator flow | Make external work executable from the user-facing response: surface, mode, files, preflight, launch, stop, return, and separate-context requirements. | active behavior guard | common optional |
| `ACAP-027` | File-first transfer and context-sensitive format repair | Deliver long structured transfer content as verified files while keeping visible operating steps. If the user says “排版不对” or equivalent immediately after transfer content, treat structural Markdown/YAML/code-block damage as the leading repair hypothesis. | active behavior basis; repair shortcut owner-reviewed | common optional |
| `ACAP-028` | Canonical output and representation-role separation | For each provider/task type, distinguish substantive canonical output(s), ancillary execution summary, exported/downloadable representations, and transfer copies. Do not assume ChatGPT's or Claude's current output topology is universal or permanent. | owner-reviewed generalized semantic; provider facts need dated verification | portable semantic with provider-adapter implementations |

### D. Repository action, authority, lineage, and provenance

| ID | Capability | Plain-language behavior | Maturity | Portability |
|---|---|---|---|---|
| `ACAP-029` | Platform permission versus task authorization | Connected access is not current authority. Bind repository/service, target/path, action, scope, expiry, and prohibited actions to the current task. | active-source and accepted Meta-Agent basis | high-risk conditional |
| `ACAP-030` | Canonical PR lineage and controlled parallel variants | Default to one canonical branch/PR per task; allow explicitly designed parallel variants only with scope separation, reconciliation, and one final merge target. Treat the current default as a safety control, not a permanent denial of multi-contributor Git workflows. | active guard plus owner-reviewed future boundary | provider/repository adapter; high-risk conditional |
| `ACAP-031` | Branch-retention obligation, release, and audit | Retain a merged-PR branch only for a verified dependency; record reason, release gate, responsible route, and status; explicitly release it; periodically audit active obligations for stale/zombie branches without automatic unauthorized deletion. | active guard amended by v0.2 | provider/repository adapter |
| `ACAP-032` | Run context and provenance | Record actor, visible surface/selection, artifact identity, review relation, authorization, and limitations without claiming hidden backend or correctness from provenance alone. | active behavior guard | common optional; required for important audited work |
| `ACAP-033` | Cross-repository ordered work | Declare a primary write repository and separate per-repository read/write scope, order, authority, no-dual-writer rule, partial-failure handling, and result references. | provisional; Meta-Agent migration evidence only | high-risk conditional |

### E. Evaluation, generalization, selection, and evolution

| ID | Capability | Plain-language behavior | Maturity | Portability |
|---|---|---|---|---|
| `ACAP-034` | Real-use evaluation, feedback, and postmortem | Record usefulness, burden, omissions, errors, corrections, repeated failures, and regression candidates—not only artifact/task completion. Scale formality to impact and repeated evidence. | provisional / real-use thresholds needed | broad core for real-use systems |
| `ACAP-035` | Controlled generalization and method-promotion filter | Do not automatically promote one case into common method. Separate business truth, target-type constraints, user/organization specifics, current provider workarounds, and portable operating semantics; review competing explanations/counterexamples and require Owner approval for common-method change. | owner-reviewed merge of v0.1 `ACAP-035` and `ACAP-036` | broad core for meta-systems |
| `ACAP-036` | **Retired in v0.2** | Merged into `ACAP-035`; ID retained only for history and must not be reused. | retired | not applicable |
| `ACAP-037` | Capability selection and adoption record | Record which catalogue version and capabilities a target requires, adapts, experiments with, defers, rejects, or treats as not applicable; use it for package generation, review, impact, and future discovered purposes. | owner-reviewed candidate | broad for first targets |
| `ACAP-038` | Early bounded use with controlled evolution | Begin useful real work before theoretical completion while preserving source, authority, privacy, evidence, change paths, compatibility, migration, and optional rollback. Treat evolution—not rollback—as the normal path. | owner-reviewed renamed candidate | broad core |
| `ACAP-039` | Evidence-triggered retrieval/index automation | Add RAG, embeddings, vector/index automation, or automatic loading only after measured deterministic retrieval failures/burden justify their privacy, synchronization, evaluation, and maintenance cost. | provisional / no threshold evidence yet | common optional, deferred |

### F. Provider packaging and current capability evidence

| ID | Capability | Plain-language behavior | Maturity | Portability |
|---|---|---|---|---|
| `ACAP-040` | Capability-to-instruction packaging | Convert selected portable capabilities into a platform-usable prompt/instruction/configuration/file package while preserving scope, authority, versions, and testability. | focused design and real-use research needed | provider adapter with portable design problem |
| `ACAP-041` | Skill/module packaging adapter | Map selected capabilities into current provider Skill/module/command mechanisms only after verifying loading, scope, precedence, tool relation, versioning, context cost, and security. | provider fact/adapter verification needed; expected early Claude use evidence | provider adapter |
| `ACAP-042` | Dated provider/model/product capability catalogue | Maintain current evidence about subscribed products, visible models/modes, settings, tools, Skills, limits, quotas, privacy, and bounded task results; separate official facts, operator observation, and tests, with recheck triggers. | provider fact verification and repeated tests needed | provider adapter/support catalogue |

## 4. Portability and promotion filter

Before a capability or project lesson becomes reusable common method, separate:

1. **business truth** — local goals, data, rules, implementation, and user decisions;
2. **target-type adaptation** — requirements shared only by a class of Agents;
3. **portable operating semantics** — behavior that survives target/provider changes;
4. **provider adapter/workaround** — dated implementation behavior;
5. **evidence maturity** — observation, bounded validation, repeated real use, or open question.

Promotion requires proportional source references, counterexample/alternative review, scope, assumptions, evidence, target impact, version effect, and explicit Owner decision. A target-local fix may proceed without waiting for common promotion.

## 5. Target capability selection record

```yaml
capability_selection_record:
  target_id:
  target_truth_ref:
  catalogue_id: MNEMOSYNE-REUSABLE-AGENT-CAPABILITY-CATALOG-001
  catalogue_version: 0.2.0
  selected:
    - capability_id:
      adoption: required | adapted | triggered | experimental | deferred | rejected | not_applicable
      target_implementation_ref:
      adaptation_reason:
      evidence_or_validation_ref:
      unresolved_dependency:
  provider_adapter_refs: []
  impact_review_contact_or_route:
  owner_decision_ref:
```

The selection record is an index and design input. It does not substitute for target-local executable instructions or load the entire catalogue into runtime context.

## 6. Anti-bloat and preservation rules

- Preserve all material source/rationale/history; optimize runtime loading rather than deleting evidence solely to save context.
- Keep catalogue entries concise and link detailed designs/validation evidence on demand.
- Do not duplicate a portable capability for every provider implementation.
- Preserve retired/narrowed IDs and mappings; never silently reuse them.
- Recheck product facts at decision time.
- Allow real use to merge, split, rename, or retire candidate entries through explicit version mapping.

## 7. Immediate open evidence work

The highest-value evidence gaps are:

1. calibrated next-tier persistence/escalation under difficult bounded tasks (`ACAP-022`);
2. target-local and cross-repository real work, concurrency, and partial failure (`ACAP-012`, `013`, `033`);
3. practical evaluation/feedback burden and thresholds (`ACAP-034`);
4. deterministic retrieval failure thresholds before automation (`ACAP-039`);
5. capability packaging across prompts, instructions, and provider Skills (`ACAP-040`, `041`);
6. dated provider/product behavior and output topology (`ACAP-028`, `042`).

These gaps do not block bounded target design; they control whether a capability is hard-required, triggered, experimental, or deferred.

## 8. Design rationale

v0.2 preserves the catalogue as a practical checklist rather than expanding it into a universal ontology. It integrates the Owner's complete 42-item human review, merges the only clear duplicate, separates portable semantics from current product facts, and marks practice-dependent claims as provisional. The objective is to begin target-specific selection and real use while keeping future correction inexpensive and traceable.
