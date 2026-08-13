# First Three Systems — Owner-Confirmed Capability Selection v0.3

> Consolidated target-selection record derived from the Owner-confirmed OR-02 through OR-09 result. This is a non-execution-source design and adoption candidate. It does not implement capabilities, modify target truth, activate a target, or select a provider product.

```yaml
selection_id: MNEMOSYNE-FIRST-THREE-SYSTEM-CAPABILITY-SELECTION-003
version: 0.3.0
task_id: MNEMOSYNE-205
catalogue_ref: notes/reusable-agent-capability-catalog-v0.2.md
owner_review_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md
supersedes_planner_candidate_for_selection_scope: notes/first-three-system-capability-selection-v0.2.md
status: owner_confirmed_selection_with_target_adaptations_and_deferrals
execution_source: false
automatic_target_adoption: false
```

## 1. Status vocabulary

- `required_default_active` — the target's first bounded design must preserve the semantic requirement without depending on a runtime trigger classifier.
- `adapted_required` — required, but the selected target uses the specific adaptation stated here.
- `provisional_target_review` — plausible, but applicability or mechanism requires target-domain review.
- `frontier_refinement_required` — purpose or boundary is open enough that a later frontier design must refine it.
- `deferred_not_selected` — not selected for the target by this review; may be reconsidered later.

`required_default_active` does not mean the related external action runs every turn. For example, the research gate is always part of the governing capability package, but research executes only when its own decision and authorization conditions are met.

## 2. Capability matrix

| ID | Meta-Agent | Code-library Agent | Natural-language learning Agent | Owner-confirmed notes |
|---|---|---|---|---|
| 001 | required_default_active | required_default_active | required_default_active | durable external memory |
| 002 | required_default_active | required_default_active | required_default_active | one adopted authority boundary, not one physical file |
| 003 | required_default_active | required_default_active | required_default_active | human-navigable role organization |
| 004 | required_default_active | required_default_active | required_default_active | exact/normalized/substantive change distinction |
| 005 | required_default_active | required_default_active | required_default_active | approved requirement change and frontier semantic-conflict review |
| 006 | required_default_active | required_default_active | required_default_active | preserve material external rationale and lineage |
| 007 | required_default_active | required_default_active | required_default_active | current-state navigation |
| 008 | required_default_active | required_default_active | required_default_active | fresh-session/handoff continuity |
| 009 | required_default_active | required_default_active | required_default_active | cold source as evidence/synthesis input |
| 010 | adapted_required | adapted_required | adapted_required | receipt + coverage-gap required; selective loading deferred |
| 011 | required_default_active | required_default_active | required_default_active | target-owned truth, no competing writer, non-authoritative backup allowed |
| 012 | required_default_active | required_default_active | required_default_active | evolution semantics required; mechanism grows from practice |
| 013 | required_default_active | frontier_refinement_required | deferred_not_selected | code target must separate Agent-internal, business, and API evolution |
| 014 | required_default_active | required_default_active | adapted_required | language-domain evidence/measurement differs |
| 015 | required_default_active | required_default_active | required_default_active | promoted from triggered planner status |
| 016 | required_default_active | required_default_active | provisional_target_review | likely not applicable or materially different for language teaching |
| 017 | required_default_active | required_default_active | adapted_required | language goal/plan reconstruction needs domain-specific form |
| 018 | required_default_active | required_default_active | required_default_active | promoted from triggered planner status |
| 019 | required_default_active | required_default_active | required_default_active | promoted from triggered planner status |
| 020 | required_default_active | deferred_not_selected | required_default_active | evidence-calibrated user/learner inference |
| 021 | required_default_active | required_default_active | adapted_required | language task/model routing details differ |
| 022 | required_default_active | required_default_active | provisional_target_review | may be unnecessary or require different stop indicators |
| 023 | required_default_active | required_default_active | required_default_active | gate always present; research still conditional and human-authorized |
| 024 | required_default_active | required_default_active | required_default_active | independent challenge semantics always available; runs remain selective |
| 025 | required_default_active | required_default_active | required_default_active | external-task execution intent |
| 026 | required_default_active | required_default_active | required_default_active | complete visible operator flow |
| 027 | required_default_active | required_default_active | required_default_active | file-first transfer and format-repair shortcut |
| 028 | required_default_active | required_default_active | required_default_active | canonical output versus export/representation separation |
| 029 | required_default_active | required_default_active | required_default_active | platform access is not task authorization |
| 030 | required_default_active | required_default_active | required_default_active | current one-canonical-PR safety default |
| 031 | required_default_active | required_default_active | required_default_active | retained-branch obligation and audit |
| 032 | required_default_active | required_default_active | required_default_active | honest run/provenance context |
| 033 | required_default_active | required_default_active | required_default_active | ordered cross-repository work; mechanism still evidence-limited |
| 034 | required_default_active | required_default_active | adapted_required | language evaluation standards require domain research |
| 035 | required_default_active | deferred_not_selected | deferred_not_selected | Meta-Agent methodology-promotion filter |
| 037 | required_default_active | required_default_active | required_default_active | explicit capability selection/adoption record |
| 038 | required_default_active | required_default_active | adapted_required | language target may use a more aggressive bounded-real-use cadence |
| 039 | required_default_active | required_default_active | required_default_active | RAG/retrieval automation still needs real failure evidence |
| 040 | required_default_active | required_default_active | required_default_active | packaging need active; implementation unresolved |
| 041 | required_default_active | required_default_active | required_default_active | provider Skill/module adapter requires current verification |
| 042 | required_default_active | required_default_active | required_default_active | decision-driven provider/product entries; no prebuilt encyclopedia |

Historical `ACAP-036` remains retired into `ACAP-035` and is not selected separately.

## 3. Adapted ACAP-010 contract

For all three systems:

```text
Required now:
- record the important current sources/rules/materials actually used;
- disclose a material coverage gap;
- use general rules only for low-risk reversible gaps;
- stop/escalate high-impact gaps;
- preserve the gap as a candidate improvement item.

Deferred:
- automatic small-core + trigger-based selective rule loading;
- automatic context/retrieval routing not supported by real-use evidence.
```

For the language target, complete old conversations remain on-demand evidence under ACAP-009 even while capability rules are default-active.

## 4. Target-specific objects

### Meta-Agent

- method registry and version/impact links;
- target case/evidence pointers;
- design package and acceptance record;
- methodology-promotion history;
- designed-target index without target authority.

### Code-library Agent

Confirmed:

- requirement/business-rule source;
- requirement-to-decision-to-implementation-to-test trace;
- reusable/project-local boundary and rejected-reuse cases;
- function/API/dependency/compatibility record;
- private-source/customer/credential boundary;
- useful-result/rework/failure record.

Not adopted now:

- exhaustive library-side consuming-project/API reverse index.

### Natural-language learning Agent

Provisional education/SLA starting objects:

- multidimensional task-supported language evidence;
- evidence provenance;
- error/alternative explanation/correction/recurrence/uncertainty;
- goals/plan/exercise history/burden.

Confirmed higher-level objects:

- immediate versus delayed/transfer/independent performance;
- complete-conversation evidence archive;
- teaching-method change rationale and keep/revise criteria;
- user correction/deletion/dispute path.

## 5. Target implementation boundary

This file selects capability semantics only. Each target must later:

1. create or use its approved target-owned repository/store;
2. convert selected capabilities into target-specific instructions and records;
3. define target-domain measurements and privacy;
4. verify current provider/product facts at the decision that needs them;
5. obtain separate authorization for activation, writes, private material, or external runs.
