# MNEMOSYNE-031 R4C Synthesis: Candidate Requirements and Design Structure

## file_positioning
- This is the Round 4C synthesis document for MNEMOSYNE-031.
- It consolidates R4B user restatement records into a structured candidate requirement/design draft.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It must not be written directly into `current/human-approved-spec.md` without later review.
- It is intended as input for R5 review, filtering, and possible promotion into confirmed design/spec material.

## source_inputs
This synthesis is based on:
- `MNEMOSYNE-031-R4B-item01-core-motivation-v2.md`
- `MNEMOSYNE-031-R4B-item02-long-conversation-pain-points.md`
- `MNEMOSYNE-031-R4B-item03-model-context-file-github-roles.md`
- `MNEMOSYNE-031-R4B-item04-execution-source-boundaries.md`
- `MNEMOSYNE-031-R4B-item05-helping-development-agents.md`
- `MNEMOSYNE-031-R4B-item06-meta-agent-proactivity-and-correction.md`
- `MNEMOSYNE-031-R4B-item07-user-confirmation-and-human-review.md`
- `MNEMOSYNE-031-R4B-item08-indexes-summaries-context-saving.md`
- `MNEMOSYNE-031-R4B-item09-multi-project-reuse-and-specialization.md`
- `MNEMOSYNE-031-R4B-addendum01-memory-system-feedback-debugging.md`
- `MNEMOSYNE-031-R4B-manifest-index.md`

## 1. Consolidated Core Definition

Mnemosyne is a persistent-memory-system meta-agent.

Its role is not to directly perform every target task, and not to act as the ordinary development Agent inside each project. Its role is to design, maintain, review, and evolve durable memory systems that allow long-running AI work to survive across:
- conversation boundaries;
- browser/session boundaries;
- model upgrades and model changes;
- tool/vendor boundaries;
- Codex / Claude Code / Cursor / ordinary ChatGPT task boundaries;
- multi-Agent collaboration boundaries;
- human memory and requirement-drift boundaries.

Mnemosyne should convert temporary, scattered, model-local work into durable, auditable, reusable, externally stored project memory.

## 2. Fundamental Architecture Principle

### 2.1 Model computes; external state remembers
The model is treated as the compute unit. It performs:
- natural-language understanding;
- reasoning and analysis;
- generation;
- task execution;
- review;
- synthesis;
- explanation.

The conversation context is temporary working memory.

Model-internal memory or platform-provided cross-chat memory may be useful as cache, but it is not the source of truth.

Persistent project truth should be stored outside the model in external files or other durable storage.

### 2.2 External storage is abstract
“Files” should be understood broadly. The current practical default may be Markdown/GitHub repository files because they are easy for models to read, edit, diff, audit, and version.

However, the design should not hard-code Markdown as the only possible storage form. Future storage backends may include:
- Markdown;
- plain text;
- JSON/YAML;
- tables/spreadsheets;
- databases;
- indexes;
- vector stores;
- hybrid repository/database systems;
- other future model-accessible durable storage.

### 2.3 GitHub as current substrate
GitHub is currently the preferred durable memory substrate because it provides:
- backup;
- version history;
- diff and review;
- auditability;
- repository-based collaboration;
- compatibility with Codex Cloud workflows;
- possible automation through GitHub Actions or related mechanisms.

GitHub automation capacity should be treated as a candidate capability requiring verification, not assumed as unlimited.

## 3. Memory Layer Model

Mnemosyne should distinguish memory layers by authority and purpose.

### 3.1 Raw records
Raw records preserve the user's original wording, requirements, ideas, oral restatements, uploaded research material, and other source material.

They are evidence. They are not directly executable.

Purpose:
- preserve original intent;
- allow later re-analysis;
- prevent loss caused by summary compression;
- support human recall and drift review.

### 3.2 Cleaned/restated records
Cleaned or restated records remove repetition, dictation noise, and obvious speech-to-text artifacts.

They may organize ideas into candidate themes.

They still do not become execution source automatically.

### 3.3 Research and capability evidence
Research reports, model-capability studies, tool-capability studies, and external evidence help judge:
- what is feasible;
- what is outdated;
- what is unrealistic;
- what mature practices exist;
- what current models/tools can support.

Research evidence constrains and informs design, but is not itself a project-specific execution rule.

### 3.4 Indexes and summaries
Indexes and summaries are retrieval aids.

They help humans and Agents locate relevant source files, sections, decisions, research evidence, and execution sources without loading all material into context.

They are not authority layers and must not replace raw records or execution sources.

### 3.5 Handoff / continuation packages
Handoff records are local continuation context for a task or conversation.

They are analogous to interrupt context: useful for resuming a specific task, but not global project law.

A new Agent/task should first read the global execution guidance, then read handoff/current-context material.

### 3.6 Candidate design / organized requirements
Candidate design documents transform raw intent and research evidence into structured proposals.

They may be close to “source code” in the programming analogy, but still require review before they become execution guidance.

### 3.7 Execution source
Execution source means directly Agent-readable behavioral guidance that controls how Agents work.

Examples:
- `AGENTS.md`;
- `CLAUDE.md`;
- equivalent project instruction files;
- explicitly approved project memory rules;
- approved Agent cooperation protocols.

Execution sources are analogous to compiled executables in the user's programming analogy. They should be generated only after synthesis, feasibility checking, and confirmation.

## 4. Execution-Source Boundary Rules

### 4.1 Materials that must not automatically become execution source
The following are not execution sources by default:
- raw user requirements;
- raw project ideas;
- oral restatement records;
- cleaned requirement notes;
- research reports;
- summaries;
- indexes;
- handoff packages;
- task logs;
- temporary scratch files;
- unreviewed Agent suggestions;
- debugging observations;
- candidate alternatives.

### 4.2 Materials that may inform execution source
The following may inform execution-source generation:
- user-confirmed requirements;
- research-supported capability boundaries;
- mature practices discovered in research;
- repeated real-project patterns;
- confirmed design decisions;
- resolved conflict decisions;
- confirmed upgrade decisions;
- validated feedback/debugging results.

### 4.3 Promotion rule
A material should enter execution source only after:
1. the source/evidence layer is identified;
2. the intended behavioral effect is clear;
3. feasibility is checked against current model/tool capability;
4. conflicts with existing rules are checked;
5. the user confirms the change when the change is high-impact;
6. the change is written into the correct public rule file or memory-system rule file.

## 5. Project Memory Permission Model

### 5.1 Public persistent layer
The public persistent layer includes:
- Agent behavior guidance files;
- memory directory structure;
- file responsibility definitions;
- indexes;
- public collaboration rules;
- rules for reading/writing memory;
- project-wide memory organization;
- execution-source files.

This layer is shared infrastructure. It is what allows different Agents, tasks, and conversations to cooperate consistently.

### 5.2 Ordinary project-Agent restrictions
Ordinary project Agents may:
- read public rules;
- follow public memory rules;
- write to authorized project memory files;
- append permitted records;
- create task-private temporary files;
- produce candidate updates or suggestions.

Ordinary project Agents should not:
- rewrite public behavior rules;
- redesign the memory directory structure;
- change file responsibilities;
- change collaboration protocols;
- silently promote raw material into execution source;
- mix private scratch material into the public persistent layer;
- modify `AGENTS.md` / `CLAUDE.md`-like rules unless explicitly authorized.

### 5.3 Mnemosyne authority
Mnemosyne or a designated memory-system-maintenance task may propose and apply changes to the public persistent layer, but high-impact changes require user confirmation.

### 5.4 Task-private workspace
Task-specific Agents may create temporary files, drafts, scratch directories, and auxiliary artifacts for local work.

These should have lifecycle rules:
- create only when useful;
- keep separate from public persistent memory;
- clean up, delete, or explicitly archive after use;
- do not treat scratch material as confirmed memory.

## 6. Human Confirmation Policy

### 6.1 Must be confirmed
The following should require user confirmation:
- changes to execution-source files;
- changes to Agent behavior rules;
- changes to directory structure;
- changes to file responsibilities;
- changes to memory-system collaboration protocols;
- resolution of conflicting requirements;
- adoption of new capability-version rules;
- upgrading old project memory systems to new capability assumptions;
- adding research-derived best practices as binding rules;
- removing or suppressing previously confirmed requirements;
- major simplification or expansion of a target project's memory system.

### 6.2 May be automatic if clearly marked non-execution
The following may usually be automatic:
- saving raw user text;
- saving raw requirement records;
- receiving newly provided research reports;
- producing summaries;
- producing indexes;
- producing preliminary analysis;
- saving task logs;
- saving handoff drafts;
- generating candidate alternatives.

Automatic outputs must remain clearly labeled as records, summaries, indexes, drafts, or candidates. They must not silently become execution source.

### 6.3 Stability principle
If user requirements and model/tool capability boundaries have not changed, public rules and memory organization should remain stable.

Stable rules and stable file organization are a mechanism for keeping Agent behavior consistent across tasks and conversations.

## 7. Mnemosyne Workflow with Upstream Project/Agent-Team Design

The user expects a two-stage workflow for complex projects.

### 7.1 Upstream project/Agent-team design
A separate meta-agent may first discuss:
- the concrete project requirement;
- Agent team structure;
- task allocation;
- required Agent capabilities;
- cooperation model;
- project implementation strategy.

The output is an AI-Agent team organization/design document.

### 7.2 Mnemosyne memory-system design
Mnemosyne then receives that design document and focuses on:
- what the target project should remember;
- how project memory should be organized;
- what files/directories/indexes should exist;
- how Agents should read/write memory;
- what parts are public persistent memory;
- what parts are task-private workspace;
- what behavior guidance should be generated for project Agents.

### 7.3 Active review during dialogue
Mnemosyne should not be a passive recorder.

It should flag:
- outdated assumptions;
- infeasible requirements;
- repeated requirements;
- conflicts;
- unrealistic memory expectations;
- excessive complexity;
- missing confirmation points;
- places where a research report or capability boundary should constrain the design.

It may suggest alternatives or compromises, but should distinguish suggestions from confirmed decisions.

## 8. Development-Agent Support Model

For software development projects, Mnemosyne supports development Agents indirectly.

It should not be treated as the coding Agent.

It should design the memory and cooperation rules used by:
- Codex;
- Claude Code;
- Cursor;
- ordinary ChatGPT;
- other development or explanation Agents.

### 8.1 Typical memory categories for development projects
Candidate categories include:
- raw requirements;
- requirement analysis;
- user-confirmed decisions;
- domain/industry knowledge;
- dependency/library usage;
- configuration knowledge;
- architecture drafts;
- architecture rationale;
- detailed design;
- API design;
- core API documentation;
- test strategy;
- test cases;
- test data;
- expected outputs;
- error-code explanations;
- debugging records;
- performance notes;
- update/change logs;
- developer documentation;
- user documentation;
- handoff/current-task records;
- indexes.

### 8.2 Goal of project guidance
The target goal is that the user can start a new Agent task with a short instruction, and the Agent can read the project guidance and memory files to understand how to work accurately.

## 9. Index and Summary Principles

Index and summary design is not mature enough to be fixed early.

### 9.1 Why indexing is hard
The value of a detail depends on:
- task perspective;
- future use;
- Agent role;
- project domain;
- model capability;
- context size;
- retrieval capability;
- user question.

The same raw detail may be useless for one task and critical for another.

### 9.2 Gradual index strategy
Mnemosyne should:
1. start with a simple usable index;
2. preserve raw records separately;
3. add richer indexes as real use reveals needs;
4. support multiple views when needed;
5. avoid allowing indexes to become authority layers.

### 9.3 Possible index types
Future target projects may need:
- requirement index;
- architecture index;
- API index;
- testing index;
- error-code index;
- decision index;
- research evidence index;
- domain knowledge index;
- handoff index;
- change-log index;
- troubleshooting index.

## 10. Reuse and Specialization Strategy

Reusable patterns should be extracted from practice rather than assumed too early.

### 10.1 Likely high-reuse category
Source-code explanation workflows may be highly reusable. For example, Linux kernel source explanation may reuse the same memory and behavior pattern across different subsystems at the same abstraction level.

### 10.2 Minimal-memory category
Small one-off development tasks may need only:
- raw requirement preservation;
- minimal output/result record;
- perhaps one task note.

They may not justify a full memory system.

### 10.3 Rich-memory category
Large long-term projects need richer memory systems, including requirement history, architecture, API, test, domain knowledge, documentation, handoff, and debugging records.

### 10.4 Category-specific templates
Potential broad categories:
- software development;
- source-code/module explanation;
- foreign-language learning;
- other future recurring work types.

These categories may need separate templates because their goals and memory structures differ substantially.

### 10.5 Mnemosyne self-validation
Mnemosyne itself should be the first validation case.

Its own design, review, feedback, debugging, and evolution should provide evidence about which patterns are reusable and which are project-specific.

## 11. Feedback, Debugging, and Troubleshooting Mechanism

A new candidate requirement was added during R4B: Mnemosyne should support feedback and troubleshooting for target-project memory systems.

### 11.1 Problem
A designed memory system may later work poorly:
- Agents may fail to find records;
- indexes may be insufficient;
- rules may be confusing;
- public/private boundaries may be violated;
- handoff may be stale;
- execution-source rules may be too vague;
- records may become chaotic;
- users may not get useful continuity;
- Agents may misuse or ignore memory.

### 11.2 Candidate mechanism
Mnemosyne may need a process analogous to software testing/debugging:
1. collect failure reports;
2. identify symptoms;
3. locate possible cause;
4. inspect rules, indexes, file structure, handoff, and Agent behavior;
5. propose fixes;
6. mark fixes as candidate changes;
7. obtain confirmation for high-impact changes;
8. update the target memory system;
9. record the troubleshooting result as reusable knowledge when appropriate.

### 11.3 Open status
This mechanism is only a candidate requirement. It needs later design and validation.

## 12. Capability Versioning and Upgrades

Model/tool capability boundaries change over time.

Mnemosyne should support the idea of capability versions:
- research time/version;
- model/tool version considered;
- capability assumptions;
- known limitations;
- recommended memory-system practices for that capability version.

When new research or model releases change assumptions, the user may decide:
- whether new projects should use the new version;
- whether old project memory systems should be upgraded;
- whether execution-source rules should be revised.

Capability updates should not silently rewrite old project rules.

## 13. Candidate Terminology Cleanup

Recommended terms:

| term | meaning |
|---|---|
| Mnemosyne | The persistent-memory-system meta-agent. |
| Target project | A project for which Mnemosyne designs a memory system. |
| Ordinary project Agent | An Agent doing actual target-project work, such as coding, testing, explaining, or documenting. |
| Upstream Agent-team design meta-agent | A separate meta-agent that designs project Agent roles and task division before Mnemosyne designs memory. |
| Public persistent layer | Shared project memory/rules used by all Agents. |
| Task-private workspace | Temporary files/directories used by one Agent or task. |
| Raw record | Original user text, requirement, report, or unprocessed source material. |
| Cleaned record | Lightly processed and organized raw material. |
| Research evidence | Reports or evidence about feasibility, model capability, tool capability, and mature practices. |
| Index / summary | Retrieval aid, not authority. |
| Handoff | Local continuation context for a task. |
| Candidate design | Structured proposal not yet confirmed. |
| Execution source | Confirmed Agent-readable guidance that directly shapes behavior. |
| Capability version | Time/model/tool-bounded set of assumptions about what is feasible. |

## 14. R5 Review Tasks

R5 should decide what to do with this synthesis.

Recommended R5 tasks:
1. Review terminology and correct any wrong terms.
2. Decide whether the memory-layer model is acceptable.
3. Decide whether the execution-source boundary rules are acceptable.
4. Decide whether the public/private permission model is acceptable.
5. Decide whether human-confirmation policy should be strict or relaxed.
6. Mark which sections are candidate requirements vs confirmed principles.
7. Identify unresolved questions requiring more user input.
8. Decide whether the feedback/debugging addendum should become a first-class requirement.
9. Decide whether to ask Codex to add R4B/R4C records to the repository.
10. Decide whether any part is ready to become `human-approved-spec` material.

## 15. Unresolved Questions

### 15.1 Execution-source promotion
What exact approval form is required before candidate material becomes execution source?

### 15.2 Storage backend abstraction
How abstract should the first implementation be? Should it be Markdown/GitHub-first with future backend abstraction, or should storage abstraction be designed immediately?

### 15.3 Public/private workspace layout
What default directory names and lifecycle rules should task-private workspaces use?

### 15.4 Index format
What minimum index format should be used first?

### 15.5 Debugging mechanism
Should each target project have a memory-system issue log and troubleshooting record?

### 15.6 Capability versioning
How often should capability research be performed, and how should versions be named?

### 15.7 Template categories
Which first reusable template should be built after Mnemosyne itself: software development, source-code explanation, or language learning?

## R4C_status
- synthesis_status: complete_draft
- ready_for_R5_review: yes
- execution_source_status: not_execution_source
- user_confirmation_required_before_promotion: yes
