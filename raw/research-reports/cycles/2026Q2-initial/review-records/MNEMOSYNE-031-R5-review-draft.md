> Status note for repository checkpoint:
> This R5 review draft is preserved as historical draft/review input.
> It is superseded by `MNEMOSYNE-031-research-review-record.md` where final D-01 to D-07 user decisions differ.
> Specifically, D-03, D-04, D-05, D-06, and D-07 were revised during item-by-item user confirmation.

# MNEMOSYNE-031 R5 Review Draft: Confirmation, Candidate Status, and Open Decisions

## file_positioning
- This is the Round 5 review draft for MNEMOSYNE-031.
- It reviews the R4C synthesis and classifies its contents by confirmation status.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should be used for user review before any repository update or promotion into `current/human-approved-spec.md`.

## review_basis
Primary input:
- `MNEMOSYNE-031-R4C-synthesis-candidate-requirements.md`

Underlying R4B inputs:
- 9 R4B main item records.
- 1 R4B addendum record.
- R4B manifest/index.

## R5_purpose
R5 answers the following:
1. Which R4C conclusions are strong enough to treat as confirmed principles?
2. Which are plausible candidate requirements but need more design?
3. Which should remain open because they depend on future practice?
4. Which items require explicit user decision before becoming execution source?
5. What should be given to Codex or another repo-editing Agent next?

---

# 1. Proposed Confirmed Principles

These are strong, repeated, and low-risk enough to be treated as confirmed principles unless the user objects.

## CP-01: Mnemosyne is a persistent-memory-system meta-agent
Mnemosyne's primary role is to design, maintain, review, and evolve persistent memory systems for long-running AI work.

It is not primarily:
- a direct coding Agent;
- a general project implementation Agent;
- a replacement for Codex/Claude Code/Cursor;
- a passive note taker.

It is a meta-agent responsible for memory architecture, memory rules, cooperation rules, and continuity.

## CP-02: Model memory is not the durable truth source
Model-local context, platform memory, and cross-chat memory may be useful as cache or convenience, but they should not be trusted as durable, complete, controllable project memory.

Durable project truth should live in external persistent storage.

## CP-03: Model computes; external state remembers
The model should be treated as the compute/reasoning unit.

External files or other durable storage should hold long-term project memory.

## CP-04: GitHub/Markdown files are the current practical default, not a permanent limitation
Current implementation may prioritize Markdown files in GitHub because they are readable, versioned, diffable, auditable, and usable by Codex Cloud.

However, Mnemosyne should not conceptually require Markdown forever. Storage backend may evolve.

## CP-05: Evidence and execution source must be separated
Raw user text, cleaned records, research reports, summaries, indexes, handoff packages, task logs, and candidate designs are not automatically execution sources.

Execution source means confirmed Agent-readable behavioral guidance that directly influences Agent behavior.

## CP-06: Execution source should require synthesis and confirmation
Material should enter execution source only after:
- source/evidence is identified;
- feasibility is checked;
- conflicts are checked;
- intended behavioral effect is clear;
- high-impact change is confirmed by the user.

## CP-07: Public persistent layer should be stable
Shared memory rules, directory structure, file responsibilities, collaboration rules, and Agent guidance files should remain stable unless requirements or capability boundaries change.

Stability is necessary for consistent Agent behavior.

## CP-08: Ordinary project Agents must not redesign shared memory rules
Ordinary project Agents may read and follow public rules and may write to authorized memory files.

They should not modify:
- `AGENTS.md` / `CLAUDE.md`-like behavior rules;
- memory directory structure;
- public file responsibilities;
- collaboration protocols;
- execution-source boundaries.

## CP-09: Task-private scratch space is allowed but must be separated
Ordinary Agents may create temporary task-private files or directories for current work.

These must not be confused with public persistent memory. They should be cleaned up, deleted, or explicitly archived according to rules.

## CP-10: Requirement conflicts require user decision
If new and old requirements conflict, the system should surface the conflict and ask the user to decide.

The model must not silently choose one side.

## CP-11: Indexes and summaries are retrieval aids, not authority
Indexes and summaries help locate relevant material and reduce context pressure.

They must not replace raw records, confirmed decisions, or execution sources.

## CP-12: Handoff is local continuation context, not global project law
Handoff helps a new task or conversation continue from the previous one.

It may be operationally important in a local continuation, but it should not override global execution guidance.

## CP-13: Mnemosyne should be active, not passive
Mnemosyne should flag outdated, infeasible, duplicated, inconsistent, or conflicting ideas.

It may propose alternatives, but should distinguish suggestions from confirmed decisions.

## CP-14: Mnemosyne itself is the first validation target
Mnemosyne's own design, review, memory, feedback, and evolution should be used as the first real test case.

---

# 2. Candidate Requirements Needing Further Design

These are plausible and important, but not yet detailed enough to become final rules.

## CR-01: Layered memory architecture
Candidate layers:
1. raw records;
2. cleaned/restated records;
3. research/capability evidence;
4. summaries/indexes;
5. handoff/current context;
6. candidate designs;
7. confirmed execution source.

Needs design:
- file names;
- directory layout;
- update rules;
- cross-reference rules;
- promotion workflow.

## CR-02: Execution-source promotion workflow
R4C proposed a promotion pipeline, but it needs operational form.

Needs design:
- exact approval marker;
- required metadata;
- how to record user confirmation;
- how to handle partial confirmation;
- how to prevent accidental promotion.

## CR-03: Public/private permission model
The distinction is clear, but concrete rules need design.

Needs design:
- default public memory directories;
- default private scratch directories;
- cleanup policy;
- what ordinary Agents may append vs modify;
- how to detect forbidden edits.

## CR-04: Capability versioning
The concept is important but underspecified.

Needs design:
- naming format;
- version file location;
- research cadence;
- model/tool capability matrix;
- upgrade workflow for old projects;
- compatibility notes.

## CR-05: Index and summary system
The principle is confirmed, but the concrete index format should remain provisional.

Needs design:
- minimum useful index schema;
- per-domain indexes;
- references to source files/sections;
- stale index detection;
- model-specific summary density.

## CR-06: Feedback/debugging/troubleshooting system
The addendum should become a candidate requirement, but not yet a confirmed full design.

Needs design:
- issue log format;
- symptom classification;
- debugging workflow;
- evidence collection;
- repair proposal process;
- confirmation boundary for fixes;
- reusable troubleshooting patterns.

## CR-07: Development-project memory template
Software development seems likely to have reusable memory categories.

Needs design:
- minimal template;
- standard template;
- rich long-term template;
- optional modules;
- when to enable each module;
- how to prevent overbuilding small projects.

## CR-08: Upstream Agent-team design document interface
Mnemosyne may receive a design document from another meta-agent.

Needs design:
- expected input format;
- required sections;
- how Mnemosyne validates it;
- how to record upstream assumptions;
- how to handle missing information.

---

# 3. Items to Keep Open / Practice-Dependent

These should not be fixed before real project usage.

## OP-01: Exact index granularity
The user explicitly said this cannot be known yet. Different tasks and models need different index detail.

Status: keep open.

## OP-02: Degree of cross-project reuse
The user expects some reuse, but also warned against premature abstraction.

Status: keep open; extract from Mnemosyne's own use and first real projects.

## OP-03: Which low-risk actions can be fully automatic
Some automatic recording is acceptable, but exact boundaries require practice.

Status: keep open.

## OP-04: How much debugging mechanism should be built initially
The feedback/debugging idea is newly added and not yet mature.

Status: keep open as candidate requirement.

## OP-05: Storage backend abstraction depth
Markdown/GitHub-first is practical, but future database/hybrid storage remains possible.

Status: keep open; do not over-engineer now.

---

# 4. Proposed User Decision List

These are the main decisions the user should confirm in R5.

## D-01: Confirm core definition
Decision:
- Accept Mnemosyne as a persistent-memory-system meta-agent, not a direct project implementation Agent?

Recommended answer:
- Accept.

## D-02: Confirm storage principle
Decision:
- Accept “model computes; external state remembers” as a core principle?

Recommended answer:
- Accept.

## D-03: Confirm execution-source boundary
Decision:
- Accept that raw records, summaries, indexes, research reports, and handoff cannot automatically become execution source?

Recommended answer:
- Accept.

## D-04: Confirm public/private permission boundary
Decision:
- Accept that ordinary project Agents cannot modify public memory rules and directory organization unless explicitly authorized?

Recommended answer:
- Accept.

## D-05: Confirm conservative preservation
Decision:
- For early stages, should raw user text and original requirements be preserved broadly?

Recommended answer:
- Accept for now.

## D-06: Confirm feedback/debugging as candidate requirement
Decision:
- Should the newly added memory-system feedback/debugging mechanism be promoted from temporary addendum to first-class candidate requirement?

Recommended answer:
- Accept as candidate requirement, not final design.

## D-07: Confirm R4C/R5 repository checkpoint
Decision:
- Should a Codex/repo task now checkpoint R4B records, R4B manifest, R4C synthesis, and R5 review draft into the Mnemosyne repository?

Recommended answer:
- Accept after user review of this R5 draft.

---

# 5. Proposed Promotion Map

This map says what may eventually be promoted, not what is already final.

| source area | proposed status | promotion target |
|---|---|---|
| CP-01 to CP-14 | confirmed principles if user accepts | future `human-approved-spec.md` or equivalent principles section |
| CR-01 to CR-08 | candidate requirements | future design backlog / candidate requirements file |
| OP-01 to OP-05 | open issues | future `open-questions.md` |
| D-01 to D-07 | user decisions | R5 review checklist |
| R4B item files | raw/restated evidence | review-records archive |
| R4C synthesis | candidate synthesis | review-records archive |
| R5 review draft | review classification | review-records archive |

---

# 6. Suggested Repository Checkpoint Structure

If later given to Codex, suggested target paths:

```text
raw/research-reports/cycles/2026Q2-initial/review-records/
  MNEMOSYNE-031-R4B-item01-core-motivation-v2.md
  MNEMOSYNE-031-R4B-item02-long-conversation-pain-points.md
  MNEMOSYNE-031-R4B-item03-model-context-file-github-roles.md
  MNEMOSYNE-031-R4B-item04-execution-source-boundaries.md
  MNEMOSYNE-031-R4B-item05-helping-development-agents.md
  MNEMOSYNE-031-R4B-item06-meta-agent-proactivity-and-correction.md
  MNEMOSYNE-031-R4B-item07-user-confirmation-and-human-review.md
  MNEMOSYNE-031-R4B-item08-indexes-summaries-context-saving.md
  MNEMOSYNE-031-R4B-item09-multi-project-reuse-and-specialization.md
  MNEMOSYNE-031-R4B-addendum01-memory-system-feedback-debugging.md
  MNEMOSYNE-031-R4B-manifest-index.md
  MNEMOSYNE-031-R4C-synthesis-candidate-requirements.md
  MNEMOSYNE-031-R5-review-draft.md
```

Potential updates after checkpoint:
- `current/active-context.md`: mark R4B complete, R4C complete, R5 draft generated, awaiting user review/confirmation.
- `current/todo.md`: mark R4B and R4C complete; mark R5 draft generated; add review decisions pending.
- `current/open-questions.md`: add D-01 to D-07 and OP-01 to OP-05.
- `handoff/handoff-current.md`: next step is user review of R5 decisions, not regenerating R4B/R4C.

---

# 7. R5 Status

- R5_classification_status: draft_complete
- confirmed_by_user: no
- ready_for_user_review: yes
- ready_for_repo_checkpoint: only after user approval
- execution_source_status: not_execution_source
