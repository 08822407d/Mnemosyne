# MNEMOSYNE-031 User Design Intent Restatement

## file_positioning

- this_is_user_restatement: yes
- not_original_requirement: yes
- not_final_design: yes
- not_execution_source: yes
- may_differ_from_original_due_to_time_and_prior_discussion: yes
- source_records:
  - 9 R4B main records
  - 1 R4B addendum
  - R4B manifest/index
  - R4C synthesis
  - final R5 D-01 to D-07 user decisions

## user_restatement_summary

The user wants Mnemosyne to exist because long-running AI work must survive beyond any single model context, browser window, tool, task, conversation, vendor, model version, or human memory state.

Mnemosyne is intended as a persistent-memory-system meta-agent. It is not primarily a coding Agent or direct project execution Agent. Its mature role is to design, maintain, review, and evolve external persistent memory systems, memory rules, cooperation rules, and continuity mechanisms for target projects and recurring work scenarios.

The user's motivation evolved from ordinary ChatGPT continuity problems, to long-term learning and technical study, to complex multi-Agent AI-assisted software development. In all cases, the key need is the same: preserve original intent, current state, decisions, evidence, and working context in an external durable layer that later humans and Agents can inspect, audit, update, and reuse.

## raw_intent_points

- preserve long-running AI work beyond any single chat/model/tool/session;
- reduce repeated prompt-writing when starting new conversations or tasks;
- preserve raw user text and original requirements as a durable source layer;
- support human recall and requirement-drift review;
- allow work to survive model switching and model upgrades;
- use external files or other durable storage as the long-term truth source;
- treat model context as temporary working memory;
- treat model/platform memory as cache or convenience, not authoritative truth;
- use GitHub/Markdown as the current practical substrate because of diff, versioning, audit, backup, and Codex Cloud integration;
- avoid hard-coding Markdown/GitHub as the only possible future backend;
- distinguish raw records, cleaned records, research evidence, summaries/indexes, handoff, candidate designs, and execution source;
- keep evidence layers and execution source separate;
- allow summaries and indexes to help retrieval but not become authority;
- treat handoff as task-local continuation context, not global project law;
- allow handoff to contain explicit local continuation exceptions when required for task recovery;
- allow ordinary project Agents to maintain authorized memory content;
- prevent ordinary project Agents from redesigning public memory-system rules and structure unless explicitly authorized;
- keep high-impact changes under user confirmation;
- use research reports as high-weight evidence for feasibility, capability boundaries, and modernization suggestions;
- make Mnemosyne active in flagging outdated, infeasible, duplicated, inconsistent, or over-idealized ideas;
- keep memory-system testing / feedback / debugging as a first-class but research-gated candidate capability;
- let reuse and templates emerge from practice instead of over-fixing them too early.

## explicit_user_needs

- A persistent external memory layer for long-running AI work.
- A method for preserving original-source materials and not losing raw user intent.
- A way to transform raw intent into structured candidate requirements and then into confirmed execution guidance only after review.
- A system that can support Codex, Claude Code, Cursor, ordinary ChatGPT, and other Agents by giving them durable project memory and cooperation rules.
- A GitHub/repository-based current substrate for versioned, auditable, model-readable memory.
- Clear file roles, directory roles, and authority boundaries.
- Human confirmation for high-impact rule, structure, execution-source, or conflict-resolution changes.
- Research-informed capability boundary checks.
- Active correction when user ideas are outdated, infeasible, duplicated, conflicting, inefficient, over-idealized, or speculative.
- A future path for memory-system testing, debugging, troubleshooting, and feedback.

## desired_meta_agent_behavior

Mnemosyne should not be a passive recorder.

It should:

- preserve original user intent faithfully;
- organize raw intent into structured candidate material;
- distinguish raw, candidate, confirmed, and execution-source layers;
- flag conflicts and require user decisions;
- identify infeasible or outdated assumptions;
- propose alternatives or compromises;
- distinguish suggestions from confirmed decisions;
- use research/capability evidence to constrain design;
- help design memory systems for target projects;
- help define how ordinary Agents read/write project memory;
- protect shared memory rules and directory structure;
- support user review and auditability;
- avoid silently upgrading raw/suggested material into execution source.

## user_assumptions

- External durable state is necessary for long-running AI work.
- Model context is not a durable truth source.
- Model/platform memory is cache/convenience, not authority.
- GitHub/Markdown is currently practical for model-readable persistent memory.
- Future storage backends may become better and should remain conceptually possible.
- Project memory systems need layered authority.
- Indexes and summaries should evolve through practice.
- Reuse should be extracted from actual target projects.
- Small tasks may need minimal memory.
- Large long-term projects need richer memory systems.
- Capability boundaries change and may require version-aware updates.
- Original-source preservation is important for model migration and later work-guidance upgrades.
- Memory-system testing/debugging is desirable but currently unverified.

## possible_conflicts_or_tensions

| issue | description | why_it_matters | needs_user_decision |
|---|---|---|---|
| raw preservation vs privacy/retention | Original-source materials should be preserved, but sensitive material may require redaction or access limits. | A preservation policy needs a privacy exception mechanism. | yes |
| stable public rules vs adaptation | Stable rules keep Agents consistent, but model/tool capabilities and requirements change. | Need promotion and upgrade workflows. | yes |
| ordinary Agent autonomy vs protected memory system | Ordinary Agents should update authorized memory content but not redesign public rules. | Need concrete file-level permission rules. | yes |
| handoff local authority vs global execution source | Handoff can guide local task recovery but must not silently become global law. | Need local-exception and promotion policy. | yes |
| rich memory vs overbuilding | Large projects need rich memory; small tasks may not. | Need minimal/standard/rich templates. | yes |
| research evidence vs user-confirmed rules | Research should constrain design but not automatically override execution source. | Need clear synthesis/confirmation workflow. | yes |
| testing/debugging aspiration vs feasibility | User wants software-test-like memory validation, but current feasibility is unverified. | Need research and dry-runs. | yes |

## assumptions_to_check_against_research

| assumption | related_research_area | check_needed | priority |
|---|---|---|---|
| Current models can reliably follow repository-based memory rules. | AI Agent external persistent memory and coding-agent workflows | capability-boundary check | high |
| Current models can maintain layered memory without confusing authority levels. | multi-Agent memory systems, instruction following, repository state management | capability-boundary check | high |
| GitHub/Markdown workflows scale for complex multi-Agent memory. | tool capability, repository-based AI workflows | engineering practice review | high |
| Ordinary project Agents can safely update authorized memory content. | coding-agent reliability, file-editing safety | dry-run validation | high |
| Handoff can act as task-local continuation context without overriding global rules. | long-context continuation, handoff design | dry-run validation | high |
| Memory-system testing/debugging can be performed by current models. | AI evals, software testing analogies, multi-Agent observability | deep research required | high |
| Source-code explanation workflows have high template reuse. | reusable AI workflows, codebase explanation | practice validation | medium |
| Language learning memory systems need separate templates. | long-term tutoring memory | later research/practice | medium |

## likely_outdated_or_weak_assumptions

| assumption | why_potentially_outdated_or_weak | suggested_research_or_design_check |
|---|---|---|
| GitHub/Markdown will remain the best substrate. | Future tools may handle databases, vector stores, or hybrid memory better. | Keep backend abstract and periodically reassess. |
| All useful memory can be organized manually in files. | Large projects may need automated indexing/retrieval. | Test index/search needs during dry-runs. |
| Memory-system debugging can resemble software testing. | AI memory behavior may be harder to test deterministically than code. | Research eval patterns and build small test cases. |
| Ordinary Agents can reliably respect permission boundaries. | File-editing Agents may over-edit unless constraints are explicit and checked. | Use dry-run and diff review. |
| One meta-agent can design all memory systems from project descriptions. | Different domains may require specialized templates and research. | Extract templates from practice rather than assume universality. |

## speculative_or_unverified_ideas

- software-test-like memory-system test cases;
- automated root-cause diagnosis for memory-system failures;
- broad memory-system troubleshooting workflow;
- periodic capability-version research process;
- target-project memory-system issue logs;
- reusable templates across source-code explanation, software development, and language learning;
- future storage backends beyond Markdown/GitHub;
- upstream Agent-team design document interface as a normal input pipeline.

## candidate_requirements_to_consider

- layered memory architecture;
- execution-source promotion workflow;
- public/private memory permission model;
- original-source preservation policy;
- handoff local-exception policy;
- authorized memory content update policy for ordinary project Agents;
- index and summary system;
- capability versioning and upgrade workflow;
- development-project memory template;
- upstream Agent-team design document interface;
- memory-system testing / feedback / debugging / troubleshooting workflow;
- privacy/redaction/access policy for original-source materials;
- target-project memory-system issue log.

## open_questions

- What exact approval form is required before candidate material becomes execution source?
- How abstract should the first storage backend design be?
- What default directory names and lifecycle rules should task-private workspaces use?
- What minimum index format should be used first?
- Should each target project have a memory-system issue log and troubleshooting record?
- How often should capability research be performed, and how should capability versions be named?
- Which first reusable template should be built after Mnemosyne itself: software development, source-code explanation, or language learning?
- What privacy/redaction/access-control rule should govern original-source materials if sensitive content appears?
- Can current models reliably perform memory-system testing / debugging / root-cause diagnosis?
- Are there mature industry practices or successful examples for memory-system testing/debugging in AI-Agent teams?
- When should handoff-local exceptions be promoted into global execution-source changes, and what approval form is required?

## codex_writeback_instructions

- Create this user design restatement record only as a clearly marked restatement/synthesis record.
- Suggested path: `raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md`.
- Do not write this directly into `current/human-approved-spec.md`.
- Do not treat this as original requirement or final design.
- Add candidate requirements only when clearly marked as candidate.
- Add open questions for uncertain assumptions.
