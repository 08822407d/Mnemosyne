# MNEMOSYNE-031 R4B Item 05 Record: Helping Development Agents

## file_positioning
- This is a Round 4B user oral restatement record.
- It records the user's current restated intent for one prompt-list item.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should not be written directly into `current/human-approved-spec.md`.
- It may later be used as input for R4C.

## item
- item_id: R4B-ITEM-05
- category: helping_codex_claude_code_cursor
- question: How should Mnemosyne help Codex, Claude Code, Cursor, and similar development Agents?

## dictation_cleanup_notes
- “Cloud Code / cloud 的 code” was interpreted as “Claude Code” where development-Agent context fits.
- “Fable, Mesos” were preserved as uncertain references to possible other AI tools/models.
- “原 Agent / 原理 Agent” was interpreted as “meta-agent”.
- “AGENTS.md / CLAUDE.md” were treated as examples of Agent behavior-guidance files.
- Repetitions, filler words, and oral restarts were removed.

## user_restatement_summary

For software development projects, Mnemosyne is not intended to directly participate in coding as one of the project development Agents. Its main role is to design the persistent-memory and collaboration rules that project development Agents should follow.

When given a project requirement, Mnemosyne should help generate project-level guidance files such as `AGENTS.md`, `CLAUDE.md`, or similar instruction files. These files should tell the actual development Agents what project information must be persistently recorded, where it should be stored, how it should be organized, and how Agents should use it.

The user wants this because complex development projects include much more than coding. They may require requirement intake, raw requirement preservation, requirement analysis, domain or industry knowledge collection, feasibility judgment, architecture design, detailed design, API design, test data design, test cases, test frameworks, error-code explanations, update logs, performance optimization notes, developer API documentation, and user-facing documentation. These materials should not be scattered randomly across a project, nor should they be placed as one undifferentiated pile in a single folder. They should be organized with clear file roles, directory structure, and indexes.

Mnemosyne should also guide how project Agents preserve domain knowledge. For specialized domains, an Agent may need to collect and store industry, professional, or subject-matter knowledge related to requirements. Such knowledge may be too large or too important to rely on model-local memory. It should be stored in project files so later Agents and tasks can reuse it.

For design and architecture, Mnemosyne should ensure that decisions are recorded so later Agents or human users do not need to rediscover the whole design by re-reading all source code. This supports both Agent continuation and user understanding. The same applies to detailed design, API design, testing, error handling, documentation, and performance-related work.

For later requirement changes, persistent memory should help identify whether a new request is a new feature, an enhancement to an existing requirement, a duplicate, a similar idea, or a conflict. It should help compare new and old requirements accurately and quickly, avoiding forgotten prior work.

In multi-Agent collaboration, each Agent or task context should ideally focus on a specific type of work, such as requirements, architecture, testing, documentation, explanation, or performance optimization. These Agents may be from different tools or vendors, and they cannot be assumed to communicate through shared model memory. They should communicate through project files and indexes.

Therefore, Mnemosyne's development-project role is to design a persistent-memory system and Agent cooperation rules for each target project. The desired result is that the user can start a new Agent task with a short instruction, and the Agent can then read the project guidance and memory files to understand how to work accurately.

## raw_intent_points
- Mnemosyne should not be treated as a direct coding Agent for target projects.
- It should design memory and collaboration rules for development Agents.
- It should generate or help generate project guidance files such as `AGENTS.md` / `CLAUDE.md`.
- It should specify what content must be persistently recorded.
- It should specify file organization, directory structure, index design, style, and detail level.
- Persistent records should cover raw requirements, requirement analysis, domain knowledge, architecture, detailed design, APIs, tests, error codes, updates, documentation, and performance notes.
- Project memory should not be scattered randomly or flattened into an unstructured folder.
- Domain/professional knowledge should be stored externally when relevant.
- Later Agents should be able to understand design without re-parsing the entire source code.
- Requirement evolution should be tracked so duplicates, enhancements, and conflicts can be identified.
- Multiple Agents should coordinate through files because they may not share model memory.
- The system should reduce human prompt burden: a short user instruction should be enough to start a correctly guided Agent task.

## candidate_design_implications
- Target project memory systems need explicit file layout design.
- Project guidance should include rules for what to write, where to write it, and how to update it.
- Memory systems should include indexes to reduce context load.
- Development memories should include both technical design artifacts and human-facing explanation artifacts.
- Requirement history and change comparison should be first-class capabilities.
- Multi-Agent workflows should be designed around file-based communication.
- Mnemosyne should generate project-specific guidance from reusable patterns rather than manually written prompts each time.

## possible_tensions_or_risks
| issue | description | why_it_matters |
|---|---|---|
| Meta-agent vs coding Agent | Mnemosyne designs the memory system but does not directly code the target project. | Keeps responsibility boundaries clear. |
| Rich memory vs project clutter | Many artifact types may be useful, but too many files can become chaotic. | File layout and index design are essential. |
| Specialized domain knowledge | Some projects require domain knowledge beyond code. | Memory design must support non-code knowledge records. |
| Agent focus vs coordination | Agents should focus on one task type, but their work must integrate. | File-based communication and handoff rules are needed. |
| One-sentence startup goal | The user wants short task startup prompts. | Project guidance must be strong enough to carry detailed instructions. |

## R4C_input_status
- item_discussion_status: complete_for_now
- ready_for_R4C_input: yes
- may_accept_later_additions: yes
