# Reusable Agent Capability Catalogue — Candidate v0.1

> Human-readable, non-execution-source inventory of Agent operating capabilities observed or proposed in Mnemosyne and Meta-Agent. It is a selection aid, not a universal package, method library, execution source, provider implementation, or proof that every capability is validated.

```yaml
catalog_id: MNEMOSYNE-REUSABLE-AGENT-CAPABILITY-CATALOG-001
task_id: MNEMOSYNE-200
version: 0.1.0
status: candidate_inventory_for_real_use_and_target_selection
source_mnemosyne_ref: 08822407d/Mnemosyne@96d7e9172527f56068404f5561a212b8ddbdd29c
source_meta_agent_ref: 08822407d/Meta-Agent@1fdbd7af9437f72f7c8106714ad1e64908983fb7
execution_source_modified: false
Meta_Agent_modified: false
automatic_target_adoption: false
```

## 1. Purpose

The catalogue exists so that a human or Agent designer does not need to remember every capability already developed across long conversations and repositories.

It supports four operations:

1. discover existing Agent operating capabilities;
2. understand their purpose, evidence and limits;
3. select a minimum sufficient subset for a target Agent;
4. record which version/scope a target adopted so future upstream changes can be assessed.

The catalogue intentionally separates **portable Agent capabilities** from **provider/product implementation mechanisms**. A capability such as fresh-session continuity may be portable; a particular Claude Skill, ChatGPT Project setting or connector behavior is a time-sensitive implementation option recorded elsewhere.

## 2. Candidate identity and status rules

The `ACAP-*` identifiers below are catalogue-local candidate IDs. They are not issued Mnemosyne execution-source IDs or Meta-Agent method IDs.

Suggested statuses:

- `active_source_rule`: already present in a current Mnemosyne execution source/guard;
- `accepted_meta_method`: present in the Owner-accepted but operationally inactive Meta-Agent methodology;
- `candidate_from_owner_input`: user-confirmed need not yet adopted as standing behavior;
- `validated_bounded`: passed a bounded behavior or mechanical test;
- `partially_validated`: some evidence exists but broader reliability remains open;
- `research_needed`: implementation or value depends on current external evidence;
- `target_specific`: useful capability but not portable as a general Agent rule.

Portability classes:

- `broad_core`: likely needed by most long-lived Agents;
- `common_optional`: common but depends on lifecycle/task type;
- `high_risk_conditional`: only where permissions, privacy, external writes or irreversible actions justify it;
- `provider_adapter`: provider/product-specific implementation layer;
- `target_specific`: business-domain capability that must not be promoted automatically.

## 3. Capability inventory

### A. Memory, source and authority

| ID | Capability | What it does | Current basis/status | Portability |
|---|---|---|---|---|
| `ACAP-001` | File-backed persistent memory | Uses durable files/repositories as long-term state; models remain replaceable computation units. | Mnemosyne execution source §§1–2; active source rule | broad_core |
| `ACAP-002` | Single target truth source | Declares one authoritative target runtime source and prevents newer summaries, handoffs or archives from silently becoming truth. | Mnemosyne §4; Meta-Agent `MA-REQ-0014`, `MA-METHOD-0003` | broad_core |
| `ACAP-003` | Artifact-role separation | Separates target truth, approved decisions, current state, handoff, methods, evidence, raw source, candidates and inference. | Mnemosyne §§4–9; Meta-Agent `MA-REQ-0007`, `MA-METHOD-0003` | broad_core |
| `ACAP-004` | Original/source preservation | Preserves complete material conversations, reports, tasks or documents with honest exact/normalized/receipt-only labels. | `current/source-artifact-preservation-and-design-rationale-guard.md`; active source rule | broad_core for material sources |
| `ACAP-005` | Requirement intake and approval | Captures original input, extracts candidates, checks duplication/conflict and requires user confirmation before approved truth changes. | Mnemosyne §§6–6.1; requirement/self-improvement workflows | broad_core |
| `ACAP-006` | Decision, supersession and lineage | Records why a choice was made, which objects it changes, and how old/new versions relate. | Mnemosyne decision/version/migration patterns; PR #266 rationale guard | broad_core |
| `ACAP-007` | Current-state navigation | Keeps current stage, blockers, pending items and safe next action separate from durable truth. | Mnemosyne active-context/handoff rules; Meta-Agent target file roles | broad_core |
| `ACAP-008` | Fresh-session/handoff continuity | Lets a qualified new conversation resume from explicit files without hidden prior context. | Mnemosyne §15 and handoff guards; Meta-Agent `MA-REQ-0015`, `MA-METHOD-0006` | broad_core for long-lived work |
| `ACAP-009` | Cold/on-demand source loading | Preserves large historical sources but excludes them from normal runtime unless a reconstruction, migration, incident or audit trigger exists. | PR #266 guard; PR #267 load-profile candidate | common_optional becoming core at scale |
| `ACAP-010` | Runtime load profile and receipt | Loads a small core plus task-triggered modules and records what was actually read, missing or intentionally excluded. | PR #267 candidate/V0 mapping; not adopted | common_optional; high value for large systems |
| `ACAP-011` | Target-local truth and no dual writer | Keeps business Agent truth in the target repository and prevents Mnemosyne/Meta-Agent from remaining a competing writer. | Mnemosyne §9; Meta-Agent migration/no-dual-writer evidence | broad_core for repository-backed targets |
| `ACAP-012` | Version, migration and rollback | Uses stable identity, version decisions, old-to-new mapping, validation and rollback/revision plans. | first-target upgrade contract; Meta-Agent `MA-REQ-0010` | common_optional; required for long-lived targets |
| `ACAP-013` | Upstream impact assessment | Determines whether a Mnemosyne/Meta-Agent capability change affects deployed target behavior, completed work, data or migration needs. | owner temporary idea; target upgrade mechanisms only; central register missing | candidate_from_owner_input |

### B. Human interaction and decision quality

| ID | Capability | What it does | Current basis/status | Portability |
|---|---|---|---|---|
| `ACAP-014` | Objective evidence-bound engineering | Separates verified facts, user values, model interpretation and uncertainty; avoids flattery-driven conclusions. | Mnemosyne §11 | broad_core |
| `ACAP-015` | User operation versus explanation separation | Places all current manual actions prominently and keeps them separate from analysis and future steps. | Mnemosyne §12; user-operation guard | common_optional; core for tool-bearing work |
| `ACAP-016` | Human-readable concise presentation | Prefers concise natural language; uses structured blocks only when they improve decisions and explains their meaning. | owner temporary idea; PR #266 user-facing rationale rule | candidate_from_owner_input |
| `ACAP-017` | Intent reconstruction with correction rights | Treats user wording as primary evidence but distinguishes symptom, proposed solution, assumptions and competing interpretations. | user-operation guard §5; Meta-Agent `MA-METHOD-0001` | broad_core for design work |
| `ACAP-018` | Context-rich clarification | Gives background, consequence and option meanings; permits free-form answers, rejection and deferral. | clarification adjudication guard | common_optional |
| `ACAP-019` | Answer ledger and correction tracking | Preserves dependent human answers, model interpretation, corrections, deferrals and residual uncertainty. | clarification guards; not universal for short tasks | common_optional |
| `ACAP-020` | No hidden profiling | Uses scoped evidence and `unknown`; does not turn sparse interaction into stable personality, intelligence, cognitive or learner labels. | Mnemosyne/Meta-Agent boundaries; adaptive explanation research; owner requirements | broad_core for personal/learning Agents |

### C. Work decomposition, research and external execution

| ID | Capability | What it does | Current basis/status | Portability |
|---|---|---|---|---|
| `ACAP-021` | Capability-aware work decomposition | Splits frontier reasoning, bounded next-tier execution, mechanical checks and human-only decisions. | Mnemosyne user-operation guard; Meta-Agent `MA-REQ-0011`, `MA-METHOD-0004` | broad_core for complex work |
| `ACAP-022` | Stop and escalation contract | Stops on ambiguity, authority, privacy, missing input or high-impact change and returns to the correct reviewer/owner. | multiple active guards; Meta-Agent methods | broad_core |
| `ACAP-023` | Research-value and quota gate | Runs external research only when the question is researchable, decision-relevant and sufficiently frozen; human retains cost/run authorization. | user-operation and clarification guards | common_optional |
| `ACAP-024` | Independent frontier challenge | Uses a separate high-capability reviewer for alternative problem reconstruction, adversarial challenge or high-impact acceptance when useful. | Issue #265 TODO 1; provenance/review rules | common_optional |
| `ACAP-025` | Cross-conversation execution intent | Declares analysis/preparation/launch status and current versus later actions before presenting external-task details. | cross-conversation execution-intent guard | common_optional |
| `ACAP-026` | Complete operator flow | Makes an external task executable without forcing the user to discover steps in repository files. | artifact and cross-conversation guards | common_optional |
| `ACAP-027` | File-first transfer artifact | Delivers long structured prompts/packages as verified files while keeping necessary visible operating steps in chat. | artifact-delivery guard; behavior validation complete for bounded cases | common_optional |
| `ACAP-028` | Deep Research one-report semantics | Treats the complete report as the one canonical substantive output and uses supported exports as representations of it. | Deep Research correction guard; repaired by MNEMOSYNE-200 | provider_adapter with portable semantic intent |

### D. Repository, action authority and provenance

| ID | Capability | What it does | Current basis/status | Portability |
|---|---|---|---|---|
| `ACAP-029` | Platform permission versus task authorization | Separates app/repository access from current task authority, target/path scope and expiry. | Mnemosyne §§14, 18; object templates; Meta-Agent write rule | high_risk_conditional |
| `ACAP-030` | Single active PR lineage | Prevents multiple overlapping PRs for one task and requires a unique merge target. | current PR-lineage guard | provider/repository adapter; high_risk_conditional |
| `ACAP-031` | Branch-retention lifecycle | Shows retention only when a verified post-merge dependency exists and explicitly releases prior obligations. | current branch-disposition guard | provider/repository adapter |
| `ACAP-032` | Run context and provenance | Records actor, visible surface/selection, artifacts, reviewer relations and authorization without claiming hidden backend identity. | current run-context guard | common_optional; important for audits |
| `ACAP-033` | Cross-repository ordered work | Allows one task/conversation to read or write multiple repositories with explicit per-surface authority, order, truth boundaries and result records. | Meta-Agent migration practical evidence; no dedicated general validation | candidate_from_owner_input; high_risk_conditional |

### E. Evaluation, evolution and reuse

| ID | Capability | What it does | Current basis/status | Portability |
|---|---|---|---|---|
| `ACAP-034` | Evaluation, feedback and postmortem | Captures outcomes, failures, burden, correction and regression candidates rather than only artifact completion. | first-target evaluation instruments; Meta-Agent `MA-METHOD-0005` | broad_core for real-use systems |
| `ACAP-035` | No automatic case-to-method promotion | Keeps target feedback scoped until abstraction, competing explanations, validation and user approval support generalization. | Mnemosyne/Meta-Agent requirements and method gate | broad_core for meta-systems |
| `ACAP-036` | Generalization/portability filter | Removes business semantics, target-type constraints and temporary platform workarounds before promoting a reusable capability. | Issue #265 TODO 5; partly covered by Meta-Agent promotion gate | candidate_from_owner_input |
| `ACAP-037` | Capability selection record | Records which catalogue capabilities and versions a target adopts, adapts, rejects or defers. | owner temporary idea; created as candidate by MNEMOSYNE-200 | candidate_from_owner_input |
| `ACAP-038` | Reversible real-use iteration | Starts a bounded useful version early, preserves evidence, and changes it through tested feedback rather than waiting for completion. | Issue #265 TODO 2; first-target upgrade contract | broad_core |
| `ACAP-039` | Conditional retrieval/index automation | Adds RAG/indexing/automation only after measured deterministic-file retrieval burden justifies it. | Mnemosyne and Meta-Agent non-goals/candidate memory design | common_optional; deferred |

### F. Provider and packaging adapters

| ID | Capability | What it does | Current basis/status | Portability |
|---|---|---|---|---|
| `ACAP-040` | Prompt/instruction packaging | Converts selected capabilities into platform-appropriate prompts, project instructions, commands or configuration. | practical pattern; no complete provider-neutral packaging standard adopted | provider_adapter; partially validated |
| `ACAP-041` | Skill/module packaging | Maps selected capabilities into current provider mechanisms such as Skills where the product supports them. | user temporary idea; exact current product semantics not reviewed here | research_needed; provider_adapter |
| `ACAP-042` | Provider/model/product capability catalogue | Records current model strengths, limits, plans, settings, surfaces, tools and freshness evidence separately from portable Agent capability semantics. | user temporary idea; scattered research evidence exists | research_needed; provider_adapter |

## 4. Portability filter

Before promoting a project-derived behavior into this catalogue, review four layers separately:

1. **business truth** — domain goals, data, rules and user-specific operational facts; normally not portable;
2. **target-type adaptation** — constraints shared by a class such as learning Agents or code repositories; portable only by stated scope;
3. **portable operating capability** — source, handoff, authority, evaluation or similar semantics that survive across targets;
4. **provider workaround/adapter** — current UI, tool, model or packaging behavior; time-sensitive and never treated as a universal Agent law.

Promotion requires:

- source and target-case references;
- scope and assumptions;
- at least one competing explanation or counterexample review;
- evidence of value or a clearly labelled experiment status;
- user decision for general methodology changes;
- version/compatibility effect and rollback/revision path.

## 5. Target selection record

A target should reference catalogue capabilities without copying the whole catalogue into runtime context.

```yaml
capability_selection_record:
  target_id:
  target_truth_ref:
  catalogue_version:
  selected:
    - capability_id:
      adoption: required | adapted | experimental | deferred | rejected | not_applicable
      target_implementation_ref:
      adaptation_reason:
      validation_ref:
  unresolved_dependencies: []
  provider_adapter_refs: []
  owner_decision_ref:
```

This schema belongs in repository records, not necessarily in user-facing chat. Human review should use a concise explained checklist.

## 6. Immediate candidate use

MNEMOSYNE-200 uses this catalogue to prepare a first selection matrix for:

1. Meta-Agent;
2. the work/business-function code-library Agent/system;
3. the long-term language teacher/practice Agent.

The matrix is evidence for target design and does not update any target truth source.

## 7. Maintenance and anti-bloat rules

- Keep one concise human-readable catalogue entry per capability; detailed source evidence remains linked and on demand.
- Do not duplicate a capability merely because a new provider packages it differently.
- Do not make every capability universal; record applicability and target selection.
- Preserve rejected, superseded and narrowed capabilities sufficiently to prevent resurrection without review.
- Provider/product facts require observation date and recheck trigger.
- Add stable global IDs only after real use shows the catalogue identity scheme is useful; current IDs are candidate inventory labels.
- Measure whether the catalogue reduces design time and omissions. Retire or simplify entries whose maintenance burden exceeds their value.

## 8. Known gaps

- The Mnemosyne-versus-Meta-Agent ownership boundary for reusable capability definitions is unresolved.
- `ACAP-033` cross-repository ordered work has migration evidence but no dedicated general validation.
- `ACAP-041` Skills packaging and `ACAP-042` provider/product catalogue need current official product research before implementation claims.
- Human-readable capability selection has not yet been tested with the user.
- The catalogue does not yet include target feedback from real business-code or language-tutor use.

## 9. Design rationale

A small explicit catalogue was selected instead of either copying the entire Mnemosyne rule set into targets or designing a complete universal Agent ontology first.

The decisive trade-off is immediate usefulness versus premature standardization: the catalogue must be detailed enough to prevent human-memory omissions and support deliberate selection, but still remain a candidate that real target use can correct.
