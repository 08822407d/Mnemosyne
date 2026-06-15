# MNEMOSYNE-031 R4B Item 08 Record: Indexes, Summaries, and Context Saving

## file_positioning
- This is a Round 4B user oral restatement record.
- It records the user's current restated intent for one prompt-list item.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should not be written directly into `current/human-approved-spec.md`.
- It may later be used as input for R4C.

## item
- item_id: R4B-ITEM-08
- category: indexes_summaries_context_saving
- question: How should Mnemosyne design indexes and summaries so Agents do not need to load all memory files into context every time?

## dictation_cleanup_notes
- “约上下文” was interpreted as “节约上下文”.
- “索引” was preserved broadly as index/retrieval aid, not a fixed technical structure.
- The user's computer-system analogy was preserved, but not over-specified.
- Repetitions, filler words, and oral restarts were removed.

## user_restatement_summary

The user does not yet have a clear fixed design for the index and context-saving mechanism. This part is partly inspired by computer-system concepts such as caches, directories, lookup structures, and memory hierarchy, but those concepts cannot be copied directly.

The main difficulty is deciding what information should be preserved in an index or summary. A piece of raw material may seem unimportant from one angle, but important from another. Its value may depend on the future task, topic, Agent role, or user question. Therefore, there is no simple universal rule for what must be indexed and what can be omitted.

Different models may also need different index detail levels. For a stronger model, a relatively compact summary may be enough. For another model, the same summary may omit too much context. Tool capabilities, context window size, retrieval ability, and comprehension ability all affect the usable index design.

The user therefore prefers a gradual approach. At the beginning, Mnemosyne may create a basic useful index. As the project is used for longer and more workflows appear, the index can become richer, more layered, and more task-specific. Different task divisions may require different indexes, such as requirement indexes, architecture indexes, API indexes, testing indexes, error-code indexes, decision indexes, and handoff indexes.

The index should not replace the original records. Its purpose is to help Agents and the user quickly locate the relevant raw records, design documents, evidence, decisions, and execution sources without loading everything into the active context. It should reduce context pressure and support reading, updating, and cross-task continuation.

## raw_intent_points
- The user currently has no fixed detailed index design.
- Index design is inspired by computer-system concepts, but should not be mechanically copied from them.
- Which content should be indexed depends on task angle, topic, future use, and Agent role.
- The same raw content may have different value under different perspectives.
- Different models may require different levels of index detail.
- Index design should evolve with project practice.
- Early projects may start with a simple index.
- Later projects may need multi-layer, multi-theme, and task-specific indexes.
- Indexes are for lookup, retrieval, context saving, reading, updating, and handoff support.
- Indexes and summaries must not replace original records or final execution sources.

## candidate_design_implications
- Mnemosyne should not hard-code a single universal index format too early.
- It should support progressive index refinement.
- It should preserve raw records separately from summaries/indexes.
- It should allow multiple index types for different project domains or Agent roles.
- Indexes should point to source files, sections, decisions, or evidence rather than becoming authority themselves.
- Indexes should reduce context pressure by helping Agents select what to read.
- Index quality should be reviewed through real project usage and adjusted over time.

## possible_tensions_or_risks
| issue | description | why_it_matters |
|---|---|---|
| Too little index detail | Compact indexes may omit information needed by weaker models or future tasks. | Agents may fail to find or understand relevant records. |
| Too much index detail | Overly rich indexes may consume context and become hard to maintain. | The index may recreate the same context-bloat problem it was meant to solve. |
| Perspective dependence | A detail may be unimportant for one task but important for another. | Index design needs multiple views or later refinement. |
| Model capability variation | Different models may use the same index differently. | The index should be adaptable rather than fixed for one model. |
| Index vs authority | Indexes are convenient and easy to read. | They must not be mistaken for original records or execution rules. |

## R4C_input_status
- item_discussion_status: complete_for_now
- ready_for_R4C_input: yes
- may_accept_later_additions: yes
