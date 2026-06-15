# MNEMOSYNE-031 R4B Item 03 Record: Model, Context, Files, and GitHub Roles

## file_positioning
- This is a Round 4B user oral restatement record.
- It records the user's current restated intent for one prompt-list item.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It should not be written directly into `current/human-approved-spec.md`.
- It may later be used as input for R4C.

## item
- item_id: R4B-ITEM-03
- category: model_context_file_github_roles
- question: What roles should the model, conversation context, external files, and GitHub repository play?

## dictation_cleanup_notes
- “阿方罗一版模型” was interpreted as a computer architecture / von Neumann style analogy.
- “异式性存储器” was interpreted as cache or temporary storage.
- “文件” was interpreted broadly as external persistent state carrier, not only Markdown.
- “CloudCode” was interpreted as Claude Code only where the development-Agent context fits.
- Filler words, oral restarts, and repeated fragments were removed.

## user_restatement_summary

The user decided to separate memory from the model because model-provided memory is limited, compressed, selectively retained, and not fully controllable by the user. Even when ChatGPT-like systems provide cross-chat memory, the platform decides what to remember and how to compress it. Such memory may be useful as an auxiliary feature, but it should not be treated as the reliable truth source for a persistent memory system. It also does not solve multi-Agent or multi-tool collaboration, because ordinary chat memory does not automatically extend to Codex, Claude Code, other vendors' models, or project-specific task environments.

The user therefore frames the architecture using a computer-system analogy. The model is like the compute unit: it receives natural language, analyzes it, reasons, generates outputs, and performs current tasks. The conversation context is like temporary working memory: useful for the active session, but not durable. Model-internal memory or platform memory can be treated like cache: it may speed up access or provide convenience, but it must not be treated as authoritative persistent storage.

Durable memory should be stored externally. The term "file" should be understood broadly. It does not only mean Markdown. It refers to any external persistent state carrier in a file system or storage layer: Markdown, text, JSON, YAML, database records, tables, or future storage forms that models may handle well. The user initially considered databases because they seemed more professional, but later realized that current AI coding and chat tools often work more naturally with repository files, especially Markdown. Therefore, Markdown/GitHub files are the current practical default, not a permanent restriction.

GitHub was chosen as the current storage and memory base for practical reasons. It provides backup, version history, diff, auditability, and a familiar workflow. It also provides possible automation mechanisms such as GitHub Actions, although their real capability boundaries should not be assumed too broadly without verification. Codex Cloud can work directly against a GitHub repository, which makes GitHub a natural shared substrate for AI-assisted work.

In each target project memory system, the model should be explicitly instructed that persistent truth comes from the external files, not from the model's own local context or platform memory. The model may use its context for current reasoning, but it should read, update, and respect the external memory files according to the project's rules.

## raw_intent_points
- Platform or model memory is limited and not fully user-controlled.
- Cross-chat memory may be compressed or selectively retained by the platform.
- Model memory should be treated as auxiliary cache, not durable truth.
- Multi-Agent and cross-tool collaboration cannot rely on one model's internal memory.
- The model's primary role is computation: language understanding, analysis, reasoning, generation, task execution.
- Conversation context is temporary working memory.
- External persistent storage should hold durable project memory.
- “File” is a broad term and should not be limited to Markdown.
- Markdown/GitHub files are currently preferred because they are easy for models to read, edit, diff, and audit.
- Database or other storage backends may become suitable later as model/tool capabilities evolve.
- GitHub is useful because of backup, versioning, diff, audit, and Codex Cloud integration.
- GitHub automation is a possible future advantage, but its capability boundary must be verified.
- Target project instructions should explicitly tell Agents that external files are the persistent memory source.

## candidate_design_implications
- Mnemosyne should preserve the principle: model computes, external state remembers.
- Persistent memory backend should be abstract enough to allow future storage evolution.
- Current implementation may prioritize Markdown/GitHub, but should avoid hard-coding Markdown as the only possible form.
- Project-specific memory systems should include explicit model-behavior rules about reading and trusting external memory.
- GitHub can be treated as the current audit and collaboration substrate.
- Model/platform memory should be optional convenience, never the execution source.
- Future database, index, RAG, or automation layers should be treated as capability extensions requiring verification.

## possible_tensions_or_risks
| issue | description | why_it_matters |
|---|---|---|
| Markdown default vs storage abstraction | Current tools favor Markdown, but future tools may handle databases better. | The system should not overfit to one storage format. |
| Model memory convenience vs truth source | Platform memory may be helpful but is not controllable enough. | Agents must not silently treat model memory as authoritative. |
| GitHub automation expectations | GitHub has automation features, but their boundaries are uncertain. | Automation should be verified before being designed as a default capability. |
| External files vs database professionalism | Databases may seem more professional, but may be less accessible to current models. | Practical model accessibility matters more than abstract elegance at this stage. |
| Cache vs durable storage | Model/context memory may speed work but can disappear or distort. | Persistent files must remain the durable source of continuity. |

## R4C_input_status
- item_discussion_status: complete_for_now
- ready_for_R4C_input: yes
- may_accept_later_additions: yes
