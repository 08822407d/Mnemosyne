# MNEMOSYNE-031 R4B Manifest: User Restatement Records Index

## file_positioning
- This is the Round 4B manifest/index file.
- It lists all R4B item records completed in the current review round.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It is an index/entry point for later R4C synthesis.

## R4B_scope
Round 4B collected the user's oral restatement of the original motivations, requirements, assumptions, boundaries, and candidate design ideas for Mnemosyne.

The purpose was not to directly generate final rules, but to preserve the user's clarified current understanding before synthesis.

## completed_main_items

| item_id | title | file | status | core_summary |
|---|---|---|---|---|
| R4B-ITEM-01 | Core Motivation | `MNEMOSYNE-031-R4B-item01-core-motivation-v2.md` | complete_for_now | Mnemosyne exists because long-running AI work must survive beyond any single model context, browser window, tool, task, or conversation. It should convert scattered temporary work into durable, auditable, reusable project memory. |
| R4B-ITEM-02 | Long Conversation and Cross-Context Pain Points | `MNEMOSYNE-031-R4B-item02-long-conversation-pain-points.md` | complete_for_now | The core problem is not only long-chat forgetting, but cross-dialogue, cross-task, cross-Agent, and cross-model continuation. External memory is needed to preserve raw content, current state, plans, and handoff context. |
| R4B-ITEM-03 | Model, Context, Files, and GitHub Roles | `MNEMOSYNE-031-R4B-item03-model-context-file-github-roles.md` | complete_for_now | Models compute; context is temporary working memory; model/platform memory is only cache; external persistent storage is the durable truth source. GitHub is the current practical base because of versioning, diff, audit, backup, and Codex Cloud integration. |
| R4B-ITEM-04 | Execution Source Boundaries | `MNEMOSYNE-031-R4B-item04-execution-source-boundaries.md` | complete_for_now | Raw intent, research reports, summaries, and handoff are not execution sources. Execution source means directly Agent-readable behavioral guidance such as `AGENTS.md` / `CLAUDE.md`-like files. |
| R4B-ITEM-05 | Helping Development Agents | `MNEMOSYNE-031-R4B-item05-helping-development-agents.md` | complete_for_now | Mnemosyne is not a coding Agent. It designs persistent-memory organization and cooperation rules for development Agents, including what to record, where to record it, how to index it, and how Agents should use it. |
| R4B-ITEM-06 | Meta-Agent Proactivity and Correction | `MNEMOSYNE-031-R4B-item06-meta-agent-proactivity-and-correction.md` | complete_for_now | Mnemosyne should not be a passive recorder. It should flag outdated, infeasible, duplicated, or conflicting ideas and propose alternatives, especially when turning upstream Agent-team designs into memory-system designs. |
| R4B-ITEM-07 | User Confirmation and Human Review | `MNEMOSYNE-031-R4B-item07-user-confirmation-and-human-review.md` | complete_for_now | High-impact changes require user confirmation. Shared persistent rules and directory structure should remain stable unless requirements or capability boundaries change. Ordinary project Agents should not modify the shared memory-system rules. |
| R4B-ITEM-08 | Indexes, Summaries, and Context Saving | `MNEMOSYNE-031-R4B-item08-indexes-summaries-context-saving.md` | complete_for_now | Index and summary mechanisms should not be over-fixed early. They should start simple and evolve by project, task type, model capability, and usage feedback. Indexes locate source material; they do not replace raw records or execution sources. |
| R4B-ITEM-09 | Multi-Project Reuse and Project Specialization | `MNEMOSYNE-031-R4B-item09-multi-project-reuse-and-specialization.md` | complete_for_now | Reuse should be extracted from practice, not assumed too early. Source-code explanation may be highly reusable; small tasks may need minimal memory; large long-term projects need richer systems. Mnemosyne itself is the first validation case. |

## completed_addenda

| addendum_id | title | file | status | core_summary |
|---|---|---|---|---|
| R4B-ADDENDUM-01 | Memory-System Feedback, Debugging, and Troubleshooting | `MNEMOSYNE-031-R4B-addendum01-memory-system-feedback-debugging.md` | temporary_addendum_only | Mnemosyne should eventually support feedback, correction, testing, debugging, troubleshooting, and fault diagnosis for target-project memory systems when they perform poorly or cause problems. |

## cross_item_themes

### 1. Persistence outside model context
The repeated theme across R4B is that model memory, chat context, and platform memory are not sufficiently durable, controllable, or cross-tool. Persistent project memory must live outside the model in external files or other durable storage.

### 2. Strict separation between evidence and execution
Raw intent, cleaned restatements, research reports, summaries, indexes, and handoff packages all support design, but they should not automatically become execution rules. Agent-readable execution guidance requires additional synthesis, feasibility checking, and confirmation.

### 3. Public shared memory vs task-private workspace
Public persistent memory and rule files are the coordination base for all Agents. Ordinary project Agents may use task-private scratch space, but they should not redesign the shared memory system.

### 4. Gradual evolution
Several areas remain deliberately open: index design, reusable templates, automatic update policy, and debugging workflows. These should evolve through Mnemosyne's own use and the first real target projects.

### 5. Meta-agent responsibility boundary
Mnemosyne is a memory-system designer and maintainer, not a direct project implementation Agent. For development projects, it designs the memory and cooperation rules used by Codex, Claude Code, Cursor, ordinary ChatGPT, and similar Agents.

## R4C_preparation_notes

R4C should synthesize these records into a more structured candidate requirement/design document.

Recommended R4C outputs:
1. consolidated requirement themes;
2. terminology cleanup;
3. proposed architecture of memory layers;
4. execution-source boundary rules;
5. human-confirmation policy;
6. project memory permission model;
7. index/summary design principles;
8. reusable-vs-specialized template strategy;
9. feedback/debugging mechanism as a candidate requirement;
10. unresolved questions and decisions requiring user confirmation.

## R4B_status
- main_items_completed: 9
- addenda_completed: 1
- ready_for_R4C: yes
- caveat: All records are R4B restatement material. They are not final design or execution source.
