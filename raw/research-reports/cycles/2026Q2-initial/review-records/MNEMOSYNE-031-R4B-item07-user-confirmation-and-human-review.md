# MNEMOSYNE-031 R4B Item 07 Record: User Confirmation and Human Review

## file_positioning
- This is a Round 4B user oral restatement record.
- It records the user's current restated intent for one prompt-list item.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should not be written directly into `current/human-approved-spec.md`.
- It may later be used as input for R4C.

## item
- item_id: R4B-ITEM-07
- category: user_confirmation_and_human_review
- question: Which changes require user confirmation, and which records may be generated automatically?

## dictation_cleanup_notes
- “执行员” was interpreted as “execution source / Agent-readable behavioral guidance”.
- “A阵 / AI智能私” was interpreted as “Agent / AI Agent”.
- “公共的公用的持久部分” was interpreted as shared public persistent memory/rule layer.
- “私有的部分” was interpreted as task-private temporary workspace.
- Filler words, repetitions, and oral restarts were removed.

## user_restatement_summary

The user considers this area still somewhat immature because it will become clearer through the first few real projects. However, several principles are already clear.

High-impact changes require user confirmation. These include changes to Agent behavior rules, project memory directory structure, file responsibilities, collaboration rules, and execution-source files such as `AGENTS.md` / `CLAUDE.md`. Such changes should normally occur only when there is a real trigger: user requirement changes, project goal changes, model/tool/platform capability changes, model upgrades, or explicit user request for redesign. During normal project execution, ordinary project Agents should not modify these rule-like files or the public memory organization.

Stability itself is a goal. If user requirements and model/tool capability boundaries have not changed, then rules, directory structure, and file responsibilities should remain stable. Stable rule files and stable memory organization are what allow different Agents, tasks, and conversations to behave consistently over time.

The user distinguishes between a public persistent layer and task-private temporary workspace. The public persistent layer includes Agent guidance files, memory directory structures, file responsibility definitions, indexes, public collaboration rules, and rules for reading/writing project memory. This layer is the shared basis for all Agents to cooperate consistently. Ordinary project Agents should not modify it on their own.

A project Agent may create temporary files, temporary directories, drafts, or auxiliary materials when needed for its own task. These belong to the task's private workspace. They should be cleaned up, deleted, or explicitly archived according to rules after use. Temporary private materials should not be mixed into the public persistent memory layer by accident.

Only Mnemosyne or the specific memory-system-design/maintenance task has authority to modify the shared persistent memory rules and organization. Ordinary project Agents may read public guidance and may write to authorized memory files according to the rules, but they should not redesign the memory system itself.

Requirement conflicts require user review. If old and new requirements conflict, the system should explicitly show the conflict and let the user decide how to resolve it. The model should not silently choose one side.

Research reports are evidence and capability-boundary references. They may show that some user ideas are unrealistic, outdated, or infeasible; they may also provide current feasible industry practices and mature examples. The system may use such research to suggest modifications or new execution-source rules, but changes to rules, functions, or existing project memory systems should be confirmed by the user.

Capability versions should be tracked. Periodic research, such as every few months, and major new model releases may change the known capability boundary. Research results should be marked with time/version information. The user should decide whether new projects should adopt the new capability version and whether old projects should be upgraded.

At the same time, some low-risk work can be automatic. Raw user text, raw requirement records, newly provided research reports, initial summaries, indexes, and preliminary analysis may be saved or generated automatically. They do not require review each time because they are records or support materials, not execution source. However, they must not automatically become behavior rules.

The user also recognizes that not all execution-source content must originate directly from the user's own wording. Mature practices and feasible patterns discovered in research may be absorbed by Agents and proposed as execution-source content. But since the exact boundary is still unclear, this should be refined through real project practice.

## raw_intent_points
- Rule changes usually require real triggers such as requirement changes or model/tool capability changes.
- Normal project execution should not change Agent behavior rules or memory organization.
- Stable rules and stable directory structures help keep Agent behavior consistent.
- Public persistent memory/rule layers should be protected from ordinary project-Agent modification.
- Ordinary Agents may create private temporary files for task-local work.
- Temporary files should be cleaned up, archived, or deleted according to rules.
- Public shared memory organization should be modified only by Mnemosyne or designated memory-system maintenance tasks.
- Requirement conflicts must be shown to the user for decision.
- Deep research reports constrain feasibility and provide reference practices, but do not automatically modify execution rules.
- Capability research results should be versioned or time-marked.
- Upgrading old project memory systems to new capability versions requires user initiation/confirmation.
- Raw records, summaries, indexes, and preliminary analyses can often be generated automatically.
- Automatically generated support materials cannot automatically become execution source.
- Agent-proposed mature practices may later become execution-source content after appropriate review.

## candidate_design_implications
- Mnemosyne should define a permission boundary between public persistent memory and task-private workspace.
- Agent guidance should explicitly forbid ordinary project Agents from changing public rules, directory layout, file roles, and collaboration protocols.
- Public persistent files should be treated as shared coordination infrastructure.
- Task-local scratch space should have lifecycle rules: create, use, clean up/archive/delete.
- Execution-source updates should require clear trigger, rationale, and user confirmation.
- Capability-boundary updates should carry version/time labels.
- Research-derived best practices may be proposed as rules but should be distinguishable from confirmed rules.
- Early implementations should use conservative preservation of raw text because the precise keep/drop policy is not yet mature.

## possible_tensions_or_risks
| issue | description | why_it_matters |
|---|---|---|
| Stability vs adaptation | Rules should stay stable unless requirements or capabilities change. | Prevents accidental behavior drift while still allowing planned upgrades. |
| Public layer vs private workspace | Agents need freedom for task work but must not damage shared memory structure. | Supports both flexibility and coordination. |
| Automatic recording vs execution authority | Raw records and indexes can be automatic, but rules cannot silently change. | Prevents unreviewed material from controlling Agents. |
| Research-derived rules | Best practices may come from research, not the user directly. | The system needs a path for Agent-proposed improvements with review. |
| Immature policy boundary | Some details will only become clear in real projects. | Early design should stay principle-based and conservative. |

## R4C_input_status
- item_discussion_status: complete_for_now
- ready_for_R4C_input: yes
- may_accept_later_additions: yes
