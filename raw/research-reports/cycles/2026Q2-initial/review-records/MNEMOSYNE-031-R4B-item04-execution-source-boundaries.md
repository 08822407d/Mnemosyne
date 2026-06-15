# MNEMOSYNE-031 R4B Item 04 Record: Execution Source Boundaries

## file_positioning
- This is a Round 4B user oral restatement record.
- It records the user's current restated intent for one prompt-list item.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should not be written directly into `current/human-approved-spec.md`.
- It may later be used as input for R4C.

## item
- item_id: R4B-ITEM-04
- category: execution_source_boundaries
- question: Which materials can become executable guidance for Agents, and which materials should remain evidence, raw records, summaries, handoff, or intermediate design material?

## dictation_cleanup_notes
- “执行员” was interpreted as “执行源 / directly Agent-readable behavioral guidance”.
- “Cloud.md” was treated as a likely reference to `CLAUDE.md` or a similar Claude Code instruction file.
- “summary” was interpreted broadly as index/summary material for raw intent, research reports, and other evidence.
- “handoff” was interpreted as a local continuation package or task handoff context.
- Repetitions and oral restarts were removed, but the programming analogy was preserved.

## user_restatement_summary

The user did not originally think carefully about execution-source boundaries. This distinction became clearer during later design discussion.

The user's current view is that an execution source is the material that directly guides an AI Agent's behavior. Examples include files such as `AGENTS.md`, `CLAUDE.md`, or similar project-level instruction files that an Agent reads when entering a repository and that strongly influence what it does, what rules it follows, and what it should avoid.

Raw requirements and raw design ideas are not execution sources. They are like user requirements, early design notes, or large explanatory comments in source code. They preserve what the user originally imagined, but they may be incomplete, duplicated, inconsistent, unrealistic, or based on insufficient understanding of current model/tool capabilities.

Research reports are also not execution sources. They are like the programming language manual, library documentation, and platform capability documentation. They help determine what is actually feasible, what the toolchain supports, and which user ideas should be corrected, rejected, adjusted, or supplemented. They can constrain or inform the execution source, but they do not themselves tell a specific Agent exactly what to do in a specific project.

Cleaned or organized requirement versions are closer to source code: they transform raw ideas into something more structured, de-duplicated, internally consistent, and compatible with current capabilities. But even this is not necessarily the final execution source until it has been reviewed, checked against research/capability boundaries, and confirmed for Agent use.

The execution source is analogous to the compiled executable program. It is the version that Agents actually read and act on. In Mnemosyne or target-project memory systems, this may be files like `AGENTS.md`, `CLAUDE.md`, or other explicit behavioral guidance files.

Summaries and indexes are not execution sources either. Their purpose is to help the model and the human quickly locate relevant raw records, research evidence, prior decisions, and design discussions without loading everything into context. They reduce context pressure and accelerate both reading and later updating, but they should not be treated as final rules.

Handoff packages are local continuation context. They are similar to an interrupt context in operating-system terms: useful when the same task is resumed in a new conversation or new task session. Within a local continuation, a handoff may have strong operational guidance. But for the whole project, it is not the global execution source. A new Agent should first read the global execution source, then use the handoff to understand the current task state.

## programming_analogy
- Raw requirements / raw ideas: user requirements, early design sketches, or explanatory source comments.
- Research reports: language syntax, library documentation, platform capability documentation.
- Organized requirement/design version: source code that has been made syntactically and semantically viable for the target language, libraries, and platform.
- Execution source: compiled executable program, or in the Agent system case, directly Agent-readable behavioral guidance such as `AGENTS.md` / `CLAUDE.md`-like files.
- Handoff: interrupt context or task continuation context, not the global executable program.

## raw_intent_points
- Execution source means the files or rules that directly guide Agent behavior.
- Raw requirements and original ideas must be preserved but cannot be executed directly.
- Raw ideas may contain duplication, inconsistency, unrealism, or insufficiently researched assumptions.
- Research reports inform feasibility and capability boundaries but are not project-specific execution rules.
- Organized requirements help reconcile duplicates, conflicts, and weak assumptions.
- Summaries/indexes are for locating material and reducing context pressure.
- Handoff is for local continuation of a task, not global project authority.
- A new task should first read global execution guidance, then read handoff/current task context.
- Execution-source generation should involve transformation from raw intent through research/capability checking into Agent-usable guidance.

## candidate_design_implications
- Mnemosyne should keep a strict boundary between raw evidence, research evidence, summaries, handoff, and execution source.
- It should preserve raw user intent while preventing raw intent from directly controlling Agents.
- It should use research/capability boundaries to filter unrealistic or unsafe execution-source requirements.
- It should support transformation stages: raw intent -> organized/candidate requirements -> reviewed design -> Agent-readable execution guidance.
- Handoff should be treated as task-local continuation material, not global project law.
- Index/summary files should help retrieval and update, not become behavioral authority by accident.

## possible_tensions_or_risks
| issue | description | why_it_matters |
|---|---|---|
| Raw evidence vs executable rules | Raw user ideas are valuable but may be inconsistent or infeasible. | Direct execution could make Agent behavior unstable. |
| Research evidence vs project instructions | Research reports describe feasibility and practices, not a specific project's rules. | Reports should constrain design, not replace design. |
| Handoff authority | Handoff is useful for local continuation but can be stale or partial. | It should not override global execution source. |
| Summary convenience | Summaries are easy for models to read quickly. | They must not be mistaken for complete or authoritative rules. |
| Compilation analogy | Execution source should be the checked and confirmed version. | The system needs an explicit transformation and approval process. |

## R4C_input_status
- item_discussion_status: complete_for_now
- ready_for_R4C_input: yes
- may_accept_later_additions: yes
