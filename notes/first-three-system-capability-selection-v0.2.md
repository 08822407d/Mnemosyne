# First Three Systems — Planner Candidate Capability Selection v0.2

> Frontier-planned selection candidate derived from the Owner-reviewed catalogue v0.2. It prepares OR-02 through OR-05; it does not update Meta-Agent truth, create target repositories, authorize private material, or activate any system.

```yaml
selection_id: MNEMOSYNE-FIRST-THREE-SYSTEM-CAPABILITY-SELECTION-002
version: 0.2.0
task_id: MNEMOSYNE-202
catalogue_ref: notes/reusable-agent-capability-catalog-v0.2.md
catalogue_version: 0.2.0
owner_review_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
status: planner_candidate_pending_owner_selection
systems:
  - Meta_Agent
  - work_business_function_code_library
  - long_term_language_teacher_and_practice_Agent
execution_source_modified: false
Meta_Agent_modified: false
target_repositories_created: false
```

## 1. Selection rule

A target should adopt the smallest set that protects source, authority, continuity, user correction, and evolution while allowing real use.

Statuses:

- **required initially** — semantics must exist in a compact first bounded version;
- **triggered** — available and applied only when its condition occurs;
- **early experiment** — test early, preserve reversibility/evolution, and measure burden/value;
- **deferred** — do not implement until evidence or a product choice creates the need;
- **target-specific object** — required business/teaching content that is not a portable common capability.

“Required” does not mean one file per capability or always-loaded detail.

## 2. Shared initial semantic floor

The following remain the planner's candidate shared minimum for all three systems:

| Capability group | IDs | Compact implementation intent |
|---|---|---|
| Durable source and current authority | `001`–`006` | one compact target spec/authority map plus source, requirement, and decision lineage; exact/normalized source roles remain explicit |
| Current work and fresh-session continuity | `007`–`009`, `011` | current state/handoff, cold-source policy, target-local truth, and no competing writer; optional non-authoritative recovery snapshot |
| Evolution | `012` | lightweight version/change/compatibility path; migration evidence grows with real changes |
| Objective and understandable interaction | `014`, `016`, `017` | evidence-bound reasoning, concise human output, and correctable intent reconstruction |
| Capability routing and safe limits | `021`, `022` | task-class split plus observable stop/escalation triggers and bounded attempt policy |
| Real-use learning and evolution | `034`, `038` | minimal outcome/burden/failure capture and controlled improvement after use |

The following are not shared always-on rules but are common triggered modules:

- `ACAP-015` when current human operations could be hidden in analysis;
- `ACAP-018` and `019` for material multi-step clarification;
- `ACAP-023` and `024` for research/independent challenge;
- `ACAP-025`–`028` for cross-conversation/external task output and transfer;
- `ACAP-029`–`033` for connected-service/repository work;
- `ACAP-039`–`042` only when retrieval scale or provider packaging decisions require them.

## 3. Meta-Agent

### Required initially beyond the shared floor

| ID | Reason |
|---|---|
| `ACAP-013` | A changed method/capability may affect Agents previously designed by Meta-Agent. Keep the first impact record lightweight and provisional. |
| `ACAP-018` | Material Agent-design choices need contextualized questions. |
| `ACAP-019` | Multi-step Owner answers, corrections, and deferrals must remain reconstructable. |
| `ACAP-023` | Meta-Agent must distinguish Owner preference, ordinary fact verification, and decision-relevant research. |
| `ACAP-032` | Important design/review artifacts need honest actor/surface/authorization and limitation records. |
| `ACAP-035` | Target cases must pass the combined promotion and portability filter before changing common methodology. |
| `ACAP-037` | Every designed Agent should receive a versioned capability-selection record. |
| `ACAP-040` | Meta-Agent's practical value depends on converting selected capabilities into an executable target package; the packaging method remains a focused design problem. |

### Triggered

- `ACAP-020` when Meta-Agent models recurring user/organization patterns; no unsupported stable profiling.
- `ACAP-024` for novel, disputed, high-impact, or acceptance-critical design—not every ordinary design.
- `ACAP-025`–`028` when preparing external research/review or cross-conversation tasks.
- `ACAP-029`–`031` when performing actual connected repository/PR work.

### Early experiments

- `ACAP-010`: small core + triggered modules + uncovered-behavior receipt.
- `ACAP-033`: ordered target/meta repository plan and bounded evidence pointer.
- `ACAP-041`: current provider Skill/module adapter after official verification.
- `ACAP-042`: decision-driven provider/product entries rather than a broad encyclopedia.

### Target-specific objects

- method registry and version/impact links;
- target case/evidence pointers;
- design package and acceptance record;
- methodology promotion decision history;
- designed-target index without target authority.

## 4. Work/business-function code-library system

### Required initially beyond the shared floor

| ID | Reason |
|---|---|
| `ACAP-029` | Exact repository/path/action authority is required for work code and external writes. |
| `ACAP-037` | Keep the Agent behavior package/version separate from the business-code catalogue and implementation. |

### Target-specific initial objects

1. requirement and business-rule source;
2. requirement → design decision → implementation → test/acceptance trace;
3. reusable versus project-local scope and rejected-reuse cases;
4. function/API/dependency/compatibility record;
5. private source/customer/credential boundary;
6. consuming-project links and migration impact;
7. useful-result, rework, and failure record.

### Triggered by actual workflow

- `ACAP-015`: when user operations/approvals exist.
- `ACAP-025`: when analysis and implementation cross conversations or tools.
- `ACAP-027`: when long patch/task packages are transferred.
- `ACAP-030`: when GitHub PR workflow is used; explicitly designed parallel variants remain possible.
- `ACAP-031`: only when a real live-branch dependency exists; include periodic obligation audit.
- `ACAP-032`: important change/review provenance.
- `ACAP-033`: when both library and consuming project are read/written.
- `ACAP-040`: after a coding surface/package is selected.

### Early experiments

- `ACAP-010`: relevant-module loading and coverage-gap receipt across growing project/function areas.
- `ACAP-012`, `013`, `033`, `034`: collect real migration, impact, cross-repository, and value/burden evidence rather than adding infrastructure first.

### Deferred

- `ACAP-023`/`024` for ordinary bounded implementation; trigger only for novel architecture, disputed reuse, current external facts, or severe failures.
- `ACAP-039` until deterministic repository navigation repeatedly misses preserved information.
- `ACAP-041` until the chosen coding product exposes a useful current Skill/module mechanism.
- broad `ACAP-042` population beyond facts needed for the selected toolchain.

## 5. Long-term language teacher/practice Agent

### Required initially beyond the shared floor

| ID | Reason |
|---|---|
| `ACAP-018` | Goals, task difficulty, assessment meaning, and plan changes need understandable context and free-form correction. |
| `ACAP-019` | User answers, corrections, changing goals, and deferrals must remain visible and revisable. |
| `ACAP-020` | Sparse lessons, mood, context, transcription error, or changing focus must not become unsupported stable learner/personality labels. |
| `ACAP-037` | Keep the teaching behavior/memory package and its capability version explicit. |

### Target-specific initial objects

1. multidimensional language evidence by task-supported dimension;
2. evidence provenance: independent, hinted, repeated, translated, or affected by speech recognition/noise;
3. observed error, alternative explanations, correction, recurrence, and uncertainty;
4. current goals, teaching plan, exercise history, and burden;
5. immediate performance versus delayed retention/transfer/independence;
6. private complete-conversation archive or verified pointer;
7. teaching-method change rationale and keep/revise criteria;
8. user correction, deletion, and dispute path.

### Triggered

- `ACAP-015` when the user must perform a current learning/technical operation.
- `ACAP-023` for external teaching-method/product facts that can change a decision.
- `ACAP-024` after enough longitudinal evidence exists for an independent high-capability review.
- `ACAP-025`–`028` when an external review/research/export task is prepared.
- `ACAP-032` for important formal assessment, teaching-policy change, or cross-model review.

### Early experiments

- `ACAP-010`: separate current lesson context from complete cold archives and record actual loaded sources.
- `ACAP-017`: staged next-tier intake/frontier reconstruction/next-tier clarification for major goal or plan changes, not every ordinary lesson.
- `ACAP-034`: minimal useful/burdensome/misleading event records; only repeated/severe cases become postmortems.
- `ACAP-040`: packaging for the selected text/voice surface.
- `ACAP-042`: populate only text, voice, memory, file, transcript/export, privacy, and quota facts that change the target decision.

### Deferred

- repository/PR modules unless the target actually uses such workflows;
- `ACAP-039` until real conversation volume produces repeated retrieval misses;
- `ACAP-041` until current provider Skill semantics are verified and useful for the chosen surface;
- stable user-profile features unsupported by repeated evidence and a clear teaching purpose.

## 6. Cross-system planner comparison

| Concern | Meta-Agent | Code-library system | Language teacher |
|---|---|---|---|
| Primary target truth | Agent-design requirements/method state | business rules, function/code assets, implementation state | teaching policy, learning evidence, plan state |
| Highest contamination risk | one target case becomes common methodology | project-local business logic becomes reusable code without evidence | context/mood/noise becomes stable learner/user profile |
| Main provisional capability evidence | impact, packaging, cross-repository, next-tier execution | migration, reuse, cross-repository, retrieval, value | longitudinal assessment, retrieval, teaching-policy adaptation, provider surface |
| Main frontier work | architecture, promotion, true-need reconstruction | novel architecture, disputed business rules/reuse, severe failure | learner-model/assessment/policy redesign, longitudinal review |
| Main next-tier work | frozen intake/explanation, package drafting, record maintenance | bounded code/doc changes with tests and exact authority | lesson execution and evidence capture under frozen policy |

## 7. Owner decisions still required

This planner candidate does not decide:

- whether the shared floor is accepted as a group or narrowed;
- which required/triggered/experimental status the Owner chooses for each target;
- target repository/store names, visibility, and private-original storage;
- Meta-Agent operational pilot scope;
- first real tasks and allowed materials;
- provider/product surfaces and quota;
- exact acceptance, stop, evolution, and migration criteria.

## 8. Next review strategy

The remaining Owner review should not repeat all 41 active catalogue entries. It should ask only:

1. approve or amend the shared semantic floor;
2. approve or amend Meta-Agent additions;
3. approve or amend code-library additions;
4. approve or amend language-teacher additions;
5. decide target-local repository/private storage and launch order;
6. route current product facts to later verification.

Major capability ownership or Meta-Agent activation remains frontier/human work. The bounded selection interview and result capture may use a next-tier model after a refreshed self-contained package is prepared.

## 9. Design rationale

v0.2 selects stable reviewed semantics as the shared floor, moves action-specific controls to triggered modules, and labels practice-dependent capabilities as experiments rather than proven hard requirements. This preserves the Owner's direction to start real use while preventing the first target packages from inheriting the entire Mnemosyne maintenance rule set.
