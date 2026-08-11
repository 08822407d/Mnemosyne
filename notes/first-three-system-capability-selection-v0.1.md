# First Three Systems — Candidate Capability Selection v0.1

> Human-readable, non-execution-source selection aid based on `notes/reusable-agent-capability-catalog-v0.1.md`. It does not update Meta-Agent truth, create either business target, select repositories, authorize private material, or activate any system.

```yaml
selection_id: MNEMOSYNE-FIRST-THREE-SYSTEM-CAPABILITY-SELECTION-001
task_id: MNEMOSYNE-200
catalogue_ref: notes/reusable-agent-capability-catalog-v0.1.md
catalogue_version: 0.1.0
status: candidate_for_target_intake_and_owner_review
systems:
  - Meta_Agent
  - work_business_function_code_library
  - long_term_language_teacher_and_practice_Agent
execution_source_modified: false
Meta_Agent_modified: false
target_repositories_created: false
```

## 1. How to read this selection

Status meanings:

- **Required initially** — include in the minimum useful first version.
- **Early experiment** — useful enough to test early, but not yet a hard target rule.
- **Later / triggered** — add only when real scale, risk or failure creates the need.
- **Not applicable now** — do not include in the first version.
- **Owner decision** — cannot be selected safely without a target-specific user decision.

The goal is not to maximize the number of selected capabilities. It is to choose the smallest set that prevents information loss, authority confusion and unusable handoff while allowing real work to begin.

## 2. Shared minimum across all three systems

These capabilities are candidate **initial requirements for all three systems**:

| Capability | Why it is shared |
|---|---|
| `ACAP-001` File-backed persistent memory | All three are long-lived and must not depend on one conversation context. |
| `ACAP-002` Single target truth source | Prevents archive, summary or another meta-system from becoming competing truth. |
| `ACAP-003` Artifact-role separation | Keeps current truth, evidence, raw material, candidates and navigation distinct. |
| `ACAP-004` Original/source preservation | Preserves irreplaceable conversations, requirements, reports or design inputs for later re-analysis. |
| `ACAP-005` Requirement intake and approval | Allows new user needs and corrections to enter without silently rewriting current behavior. |
| `ACAP-006` Decision, supersession and lineage | Keeps design reasons and old/new relationships recoverable. |
| `ACAP-007` Current-state navigation | Gives each fresh session a compact current working set and safe next action. |
| `ACAP-008` Fresh-session/handoff continuity | Supports correct continuation across new and old conversations. |
| `ACAP-009` Cold/on-demand source loading | Preserves complete history without forcing every task to read it. |
| `ACAP-011` Target-local truth and no dual writer | Each system’s own repository/store remains authoritative. |
| `ACAP-012` Version, migration and rollback | Enables later redesign without rebuilding from nothing. |
| `ACAP-014` Objective evidence-bound engineering | Keeps facts, user choices, inference and uncertainty separate. |
| `ACAP-016` Human-readable concise presentation | Reduces user review and operating burden. |
| `ACAP-017` Intent reconstruction with correction rights | Avoids treating incomplete wording as a final specification. |
| `ACAP-021` Capability-aware work decomposition | Reserves frontier reasoning for open/high-impact work and delegates bounded work safely. |
| `ACAP-022` Stop and escalation contract | Prevents a bounded executor from inventing missing authority or redesigning the system. |
| `ACAP-034` Evaluation, feedback and postmortem | Makes real-use failure and friction first-class evidence. |
| `ACAP-038` Reversible real-use iteration | Allows early use without pretending the initial version is final. |

This common set is deliberately smaller than the whole catalogue.

## 3. Meta-Agent selection

### 3.1 Required initially

In addition to the shared minimum:

| Capability | Selection reason |
|---|---|
| `ACAP-013` Upstream impact assessment | Meta-Agent method changes may affect Agents it previously designed. |
| `ACAP-018` Context-rich clarification | Agent design often requires bounded owner choices whose meanings must be explained. |
| `ACAP-019` Answer ledger and correction tracking | Multi-step design clarification must remain reconstructable and correctable. |
| `ACAP-023` Research-value and quota gate | Meta-Agent must distinguish owner decisions, ordinary verification and open research. |
| `ACAP-024` Independent frontier challenge | Novel architecture and methodology claims benefit from an independent challenge route. |
| `ACAP-032` Run context and provenance | Important design and review artifacts need honest actor/surface/authorization records. |
| `ACAP-035` No automatic case-to-method promotion | One target’s outcome must not silently rewrite general methodology. |
| `ACAP-036` Generalization/portability filter | Meta-Agent must remove project contamination before proposing reusable methods. |
| `ACAP-037` Capability selection record | Every designed Agent should record which common capabilities it adopts or adapts. |
| `ACAP-040` Prompt/instruction packaging | Meta-Agent needs to turn selected portable semantics into an actual Agent package. |

### 3.2 Early experiments

| Capability | Why experimental |
|---|---|
| `ACAP-010` Runtime load profile and receipt | Strong candidate for reducing context, but PR #267 V1 behavior comparison has not run. |
| `ACAP-033` Cross-repository ordered work | Meta-Agent migration gives practical evidence, but no dedicated general validation exists. |
| `ACAP-041` Skill/module packaging | Provider-specific Skills semantics must be verified at implementation time. |
| `ACAP-042` Provider/model/product capability catalogue | Needed for routing and packaging, but time-sensitive entries must be maintained separately. |

### 3.3 Later / triggered

- `ACAP-025`–`ACAP-028` external task and Deep Research delivery controls: load when Meta-Agent prepares an external task.
- `ACAP-029`–`ACAP-031` repository/PR controls: apply when the exact task performs those actions.
- `ACAP-039` retrieval/index automation: defer until measured volume and retrieval misses justify it.

### 3.4 Current Meta-Agent boundary

The existing Meta-Agent repository already accepts six initial methods covering requirement framing, single versus multi-Agent choice, authority/source separation, capability-aware decomposition, feedback promotion and handoff continuity. This selection does not replace or silently extend those accepted methods. It is a candidate input for later Meta-Agent-owned behavior/memory review.

## 4. Work/business-function code-library system selection

### 4.1 Required initially

In addition to the shared minimum:

| Capability | Selection reason |
|---|---|
| `ACAP-010` Runtime load profile and receipt | The system may accumulate many projects and modules; ordinary tasks should load only the relevant business/function slice. |
| `ACAP-025` Cross-conversation execution intent | Distinguishes analysis, proposed implementation and actual repository-changing work. |
| `ACAP-029` Platform permission versus task authorization | Work code and repository writes require exact target/path authority. |
| `ACAP-030` Single active PR lineage | Avoids competing implementations of one bounded code task. |
| `ACAP-032` Run context and provenance | Preserves which task changed code, what was verified and what remains uncertain. |
| `ACAP-033` Cross-repository ordered work | Reuse may involve a library repository and a consuming project; each write surface needs explicit order and scope. |
| `ACAP-037` Capability selection record | Keeps the Agent’s behavior package versioned separately from business code. |

### 4.2 Target-specific functions that must not be mistaken for general Agent capabilities

The initial business-code system still needs target-local design objects for:

1. **Requirement-to-code traceability** — requirement, business rule, design decision, implementation, test and deployment evidence.
2. **Reusable versus project-local boundary** — why a function is portable, what assumptions it carries, and which details must remain in the original project.
3. **Quality and acceptance evidence** — unit/integration tests, build result, review, known limitations and rollback.
4. **Compatibility and dependency records** — language/runtime/library versions, calling contract and migration impact.
5. **Sensitive business/source boundary** — private source, customer data and credentials must remain outside public storage.

These are business-code target requirements, not automatic additions to the common capability catalogue.

### 4.3 Early experiments

- `ACAP-027` file-first transfer where long task or patch packages are moved between tools.
- `ACAP-031` branch-retention lifecycle only when a real post-merge dependency exists.
- `ACAP-040` prompt/instruction packaging for the selected coding surface.
- `ACAP-042` provider/product catalogue for model/tool routing.

### 4.4 Later / triggered

- `ACAP-023` and `ACAP-024` research/independent challenge only for novel architecture, uncertain external facts or high-impact failures.
- `ACAP-039` RAG/indexing only after deterministic repository navigation becomes measurably inadequate.
- `ACAP-041` Skills packaging only after the chosen product surface is confirmed.

## 5. Long-term language teacher/practice Agent selection

### 5.1 Required initially

In addition to the shared minimum:

| Capability | Selection reason |
|---|---|
| `ACAP-018` Context-rich clarification | The Agent must clarify goals, task type and difficulty without turning every lesson into an exam. |
| `ACAP-019` Answer ledger and correction tracking | User corrections and changing goals must remain visible and revisable. |
| `ACAP-020` No hidden profiling | Sparse dialogue must not become a fixed personality, intelligence or learning-style label. |
| `ACAP-023` Research-value and quota gate | Teaching methods or product capabilities should be researched only when the decision warrants it. |
| `ACAP-032` Run context and provenance | Important assessments and method changes should record the surface/model/tool context and limits. |
| `ACAP-037` Capability selection record | Keeps teaching behavior, memory policy and provider packaging explicit and reviewable. |

### 5.2 Target-specific functions that must remain local

The language Agent requires its own memory and teaching objects for:

1. **Multidimensional language evidence** — vocabulary, grammar, listening, spoken production, writing, fluency/coherence, pragmatics and task completion.
2. **Evidence provenance** — what the user did independently, with hints, by repetition or under noisy speech recognition.
3. **Error and hypothesis records** — observed error, possible explanation, correction, recurrence and uncertainty; hypotheses are not stable traits.
4. **Teaching-plan state** — current goals, sequence, exercise history, burden and upcoming review points.
5. **Progress and retention evidence** — immediate performance, transfer, delayed reuse and independence.
6. **Conversation/privacy boundary** — complete conversations may be retained for authorized post-hoc review but are cold/private evidence, not routine public-Git context.
7. **Method-change record** — why a teaching approach changed and what result would justify keeping or reverting it.

### 5.3 Early experiments

- `ACAP-010` runtime profile to separate current lesson context from complete historical conversations.
- `ACAP-024` independent frontier review of accumulated complete conversations after a meaningful usage period.
- `ACAP-040` packaging for the chosen text/voice surface.
- `ACAP-042` provider/product catalogue for text, voice, memory, file and app behavior.

### 5.4 Later / triggered

- `ACAP-025`–`ACAP-028` when a lesson workflow launches external research, review or another Agent task.
- `ACAP-029`–`ACAP-031` only if the Agent writes repositories or uses PR workflows.
- `ACAP-039` retrieval automation only after real conversation volume creates repeated misses.
- `ACAP-041` Skills only after current product semantics and the chosen surface are verified.

## 6. Cross-system comparison

| Design concern | Meta-Agent | Code-library system | Language teacher |
|---|---|---|---|
| Primary truth | Agent-design requirements/method state | Business/function library and implementation state | Teaching policy, learning evidence and plan state |
| Most important cold source | Design conversations, research and target case archives | Original requirements, project histories and old implementation evidence | Complete lesson conversations and assessment artifacts |
| Highest contamination risk | One target case becoming universal methodology | Project-specific business logic becoming “reusable” code | Sparse interaction becoming a permanent user profile |
| Key migration concern | Method/capability change affecting designed Agents | API/schema/dependency changes affecting consumers | Learner-evidence or teaching-policy schema changes affecting past records |
| Main next-tier use | Frozen documentation, extraction and bounded implementation | Bounded code/doc changes with tests and exact paths | Lesson execution and evidence capture under frozen teaching/memory rules |
| Frontier use | Architecture, methodology promotion and conflicting requirements | Novel architecture/high-impact failure | Teaching-policy redesign and post-hoc longitudinal review |

## 7. Minimum owner decisions still required before real target creation

This selection does not decide:

- exact repository names and visibility;
- where private complete conversations or source code are stored;
- the exact operational product surfaces;
- whether Meta-Agent is activated for a bounded pilot;
- exact target truth paths;
- which first real code and language tasks are selected;
- which capabilities become hard requirements versus experiments after owner review.

## 8. Validation plan

1. Use this matrix during target intake and ask the user to add/remove/reclassify capabilities in plain language.
2. Generate target-specific minimal packages rather than copying the catalogue.
3. Run the first real tasks and record omissions, unnecessary controls and maintenance burden.
4. Compare frontier and next-tier models on frozen tasks derived from the same selected package.
5. Revise catalogue and selections only through evidence, target feedback and explicit owner decisions.

## 9. Design rationale

The common shared minimum plus target-specific additions was selected over one universal package. The three systems share persistence, authority, handoff, provenance and feedback needs, but their most dangerous errors differ. A single all-inclusive rule set would obscure those differences and recreate the context-burden problem identified in PR #267.
