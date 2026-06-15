# MNEMOSYNE-031 R4B Item 02 Record: Long Conversation and Cross-Context Pain Points

## file_positioning
- This is a Round 4B user oral restatement record.
- It records the user's current restated intent for one prompt-list item.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should not be written directly into `current/human-approved-spec.md`.
- It may later be used as input for R4C.

## item
- item_id: R4B-ITEM-02
- category: long_conversation_pain_points
- question: What pain points in long ChatGPT conversations and cross-context work make external file/GitHub state necessary?

## dictation_cleanup_notes
- “间入提示词” was interpreted as “输入提示词”.
- “剩下文臃肿” was interpreted as “上下文臃肿”.
- “CloudCode / cloud 的 code” was interpreted as “Claude Code” where context fits.
- “原理人 / 原理 Agent” was interpreted as “元 Agent”.
- Filler words, repetitions, and oral restarts were removed.
- Overlap with Item 01 was preserved where it clarifies pain points.

## user_restatement_summary

The user's main long-conversation pain point is not only that one chat becomes long or that the model forgets details. The deeper problem is maintaining one coherent long-running work stream across multiple conversations, tasks, Agents, and models.

When a new conversation starts, the user must repeatedly input prompts explaining what the work is, what has already been done, what the current state is, and what should happen next. If the previous conversation summary is too short, important details are lost and the new conversation cannot continue accurately. If the summary is too detailed, it consumes too much of the new conversation's context window, making the new conversation quickly become long again. This creates an accumulating problem: each handoff either loses information or consumes too much context.

Therefore, external persistent memory is needed. It should preserve original content, current state, confirmed plans, versioned results, and other durable records outside the model's temporary context. These records should not merely be one large summary. They should form a structured external memory that supports lookup, handoff, review, and later transformation into Agent-usable instructions.

Another pain point is multi-Agent and multi-task collaboration. In complex projects, different Agents may not be in a simple parent-child continuation relationship. They may be parallel collaborators working on requirement analysis, architecture, code design, testing, documentation, explanation, performance optimization, or other supporting tasks. Codex, Claude Code, ordinary ChatGPT, and other tools do not automatically share reliable context with each other. Different vendors' tools cannot directly communicate through their own model memory, and even tasks within the same tool may not reliably share state unless the project files or GitHub repository provide the communication layer.

The user also emphasized that drift is not only an Agent problem. Humans also forget, reinterpret, or change earlier ideas. External records are therefore needed not only to keep Agents aligned, but also to help the user review their own earlier thinking. Old ideas and new ideas may need to be compared, merged, revised, or rejected. Requirement changes are not always errors, but the system should preserve enough history to tell what was originally intended, what later changed, and what still needs a decision.

A further pain point is model migration. The user may close one conversation and open another not only because of context bloat or browser performance, but also because a new model is released, a better model becomes available, or another vendor's model is better suited to a task. The system must allow work to survive model changes. For that reason it should preserve multiple layers: original requirement or idea text, a structured analysis version, and an Agent-usable execution or instruction version. The original text should be preserved because later analysis may be wrong; the structured version is needed because raw text is not directly executable; the Agent-usable version is needed because actual Agents need concise operational instructions.

Finally, the user does not want to manually design a complex memory and coordination prompt for every project. Many projects need similar memory-system capabilities, while others need simplified or specialized versions. A meta-agent is needed to analyze a project description and decide what memory files, organization, detail level, and cooperation rules are appropriate for that project.

## raw_intent_points
- New conversations require repeated prompt input to explain the same work.
- Handoff summaries have a size/detail dilemma: too short loses information; too long consumes context.
- External memory should preserve raw content, current state, confirmed plans, and versioned results.
- Multi-Agent project work needs a communication layer beyond model-local memory.
- Codex, Claude Code, ChatGPT, and other tools cannot be assumed to share context automatically.
- GitHub/project files can act as the shared communication and audit layer.
- Humans also forget or drift, so external records help the user review and reconcile old and new ideas.
- Requirement changes may be legitimate, but the system should show what changed and why.
- Model switching is a normal workflow need, not an exception.
- The system needs layered records: raw requirement text, analyzed/structured version, and Agent-usable version.
- A meta-agent is needed because manually designing memory systems for each project is too complex.
- Different projects may reuse similar patterns but require different simplification or customization.

## candidate_design_implications
- Mnemosyne should support explicit handoff records instead of relying on chat summaries alone.
- It should preserve raw user expressions separately from refined requirements.
- It should support comparison between old and new ideas.
- It should track current state, confirmed decisions, pending questions, and avoided actions.
- It should treat GitHub/project files as a communication layer for cross-Agent collaboration.
- It should support model migration by making project state readable by different models.
- It should generate project-specific memory systems from reusable patterns.
- It should distinguish Mnemosyne's own memory from target-project memory.
- It should include mechanisms for drift review, conflict review, and user re-confirmation.

## possible_tensions_or_risks
| issue | description | why_it_matters |
|---|---|---|
| Summary detail dilemma | Too little summary loses information; too much summary consumes context. | External memory must be structured and queryable rather than a single huge handoff. |
| Drift vs legitimate change | Old ideas may change for valid reasons. | The system should not freeze old requirements as absolute truth. |
| Raw text vs Agent instructions | Raw user text is important but not directly executable. | A transformation process is required from raw intent to structured requirement to Agent-usable rules. |
| Cross-Agent collaboration vs platform limits | Different tools do not share model memory. | Project files/GitHub must carry shared state. |
| Reusable pattern vs per-project customization | Many projects share patterns but differ in complexity. | Mnemosyne should generate tailored memory systems, not a rigid universal template. |

## R4C_input_status
- item_discussion_status: complete_for_now
- ready_for_R4C_input: yes
- may_accept_later_additions: yes
