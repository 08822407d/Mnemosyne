# MNEMOSYNE-031 Research Review and Restatement Checkpoint Record

## file_positioning

- This is the final MNEMOSYNE-031 research review and user-restatement checkpoint record.
- It summarizes R1-R3 user-confirmed review results, recovered R4B/R4C files, and final R5 user decisions.
- It is not an original requirement.
- It is not a final design.
- It is not an execution source.
- It must not be written directly into `current/human-approved-spec.md`.
- The current execution source remains `current/human-approved-spec.md`.

## source_basis

- User stated that R1, R2, and R3 had already been reviewed and had no major issue.
- R4B recovered records contain 9 main user-restatement files plus 1 addendum.
- R4B manifest marks all R4B records as restatement material, not final design and not execution source.
- R4C synthesis is a complete draft, but is candidate synthesis only.
- Original R5 review draft is preserved only as a draft/review input and is superseded where it conflicts with the final D-01 to D-07 decisions below.

## R1_R2_R3_review_status

### R1 Research Motivation Review

- status: completed before recovery
- user_result: no major issue / acceptable
- user_confirmed: yes
- notes:
  - Research motivation can be treated as accepted for MNEMOSYNE-031 review purposes.
  - Research motivation is not execution source.

### R2 Research Prompts and Report-Topic Mapping Review

- status: completed before recovery
- user_result: no major issue / acceptable
- user_confirmed: yes
- notes:
  - Prompt mapping can be treated as accepted for MNEMOSYNE-031 review purposes.
  - Do not fabricate the missing light research prompts.
  - Prompt mapping, prompts, and reports are not execution source.

### R3 Report Summaries Review

- status: completed before recovery
- user_result: no major issue / acceptable
- user_confirmed: yes
- notes:
  - Current report summaries and seven report summaries can be treated as acceptable temporary text evidence entry points.
  - User is not assumed to have read the full research reports.
  - Do not claim PDF figures, images, tables, or layout have been manually reviewed.

## R4_recovery_status

### R4B User Restatement Records

- status: completed
- main_items_completed: 9
- addenda_completed: 1
- manifest_status: completed
- file_positioning:
  - R4B records are user restatement material.
  - They are not original requirements.
  - They are not final design.
  - They are not execution source.

### R4C Synthesis

- status: complete_draft
- role: candidate requirements and design synthesis
- file_positioning:
  - R4C is not an original requirement.
  - R4C is not final design.
  - R4C is not execution source.
  - R4C must not be written directly into `current/human-approved-spec.md`.

### R5 Review Draft

- status: draft reviewed and superseded where necessary
- notes:
  - Original R5 review draft had `confirmed_by_user: no`.
  - User later reviewed D-01 to D-07 one by one.
  - Final D-01 to D-07 decisions below are authoritative for this checkpoint.
  - Original R5 review draft may be preserved as historical review input, but not as final decision record where it conflicts with this file.

## final_R5_user_decisions

### D-01: Confirm core definition

- decision_status: accepted
- user_confirmed: yes

Confirmed meaning:

Mnemosyne is a persistent-memory-system meta-agent. Its main role is to design, maintain, review, and evolve durable external memory systems for long-running AI work. It is not a direct project implementation Agent, not a coding Agent, and not a replacement for Codex / Claude Code / Cursor.

### D-02: Confirm storage principle

- decision_status: accepted
- user_confirmed: yes

Confirmed meaning:

Accept `model computes; external state remembers`.

Model context is temporary working memory. Model/platform memory may be useful as cache or convenience, but not as durable truth source. Long-term project truth should live in external persistent files or other durable storage. Markdown/GitHub is the current practical default, but not a permanent storage limitation.

### D-03: Confirm execution-source boundary, with handoff revision

- decision_status: accepted_with_wording_revision
- user_confirmed: yes

Confirmed meaning:

Raw records, summaries, indexes, research reports, task logs, candidate designs, and handoff packages cannot automatically become global execution source. Execution source means confirmed Agent-readable behavioral guidance that directly shapes Agent behavior.

Handoff revision:

Handoff is not global project law and should not replace the project's approved Agent behavior guidance.

However, in task recovery / task handoff situations, handoff is a task-local continuation context. It can provide strong operational guidance for resuming the current task correctly.

In the ideal case, global Agent behavior, standing rules, directory responsibilities, and collaboration protocols are already written in the project execution-source files, so handoff should not repeat them.

If a handoff must temporarily override, suspend, or qualify some global behavior rule for the current task, it must describe the exception explicitly, including reason, scope, continuation context, and expected recovery/expiration condition.

Such a local handoff exception must not silently become a permanent project-wide rule or global execution-source change.

Conceptual analogy:

- global Agent behavior guidance = executable program + project data/rule base
- handoff = runtime process context needed to resume a running process correctly

### D-04: Confirm public/private permission boundary, with wording revision

- decision_status: accepted_with_wording_revision
- user_confirmed: yes

Confirmed meaning:

Ordinary target-project Agents may read public memory-system rules. They may write, append, or update project memory content only in authorized files and according to approved memory rules. They must not redesign or modify the shared memory-system design layer itself unless explicitly authorized.

Clarification:

Ordinary project Agents may maintain authorized memory content, but must not redesign the memory system or change its public rules/structure.

Allowed if authorized by project rules:

- read public guidance;
- write to authorized project memory files;
- append permitted records;
- update task records, test records, diagnosis records, documentation drafts, or other approved memory content;
- create task-private scratch files.

Not allowed unless explicitly authorized:

- modify public Agent behavior rules;
- restructure memory directories;
- redefine file responsibilities;
- change collaboration protocols;
- change public/private workspace boundaries;
- change execution-source boundaries;
- silently promote raw / summary / handoff / candidate material into execution source.

### D-05: Confirm original-source preservation principle

- decision_status: accepted_with_principle_revision
- confirmed_title: original-source preservation principle
- user_confirmed: yes

Confirmed meaning:

Original-source materials should be preserved as a durable source layer in all Mnemosyne and target-project memory systems.

Original-source materials include:

- raw user text;
- original requirements;
- original user ideas;
- oral restatements;
- uploaded source materials;
- original prompts where available;
- other first-hand input records.

These materials should not be discarded, overwritten, or replaced by:

- summaries;
- indexes;
- cleaned restatements;
- candidate requirements;
- research syntheses;
- Agent-generated interpretations.

Purpose:

- provide a real basis for later human review, supplementation, correction, and requirement modification;
- help the user remember the original intent and distinguish original ideas from later reinterpretations;
- support model/tool migration and AI-Agent work-guidance upgrades;
- avoid accumulating unpredictable distortion when later work is based only on previous model-generated summaries or syntheses.

Important boundary:

Original-source preservation does not make raw material execution source. Raw/original materials remain evidence/reference layer. Any transformation into confirmed requirements, candidate designs, or Agent-readable execution guidance still requires synthesis, capability checking, conflict checking, and appropriate user confirmation.

Deletion, redaction, or access restriction should not happen automatically as a normal memory-compression strategy. If sensitive material must be removed, redacted, or access-limited, it should be treated as an explicit user-directed action or governed by a separate retention/privacy rule.

### D-06: Confirm memory-system testing / feedback / debugging as research-gated candidate requirement

- decision_status: accepted_with_research_gated_testing_revision
- confirmed_title: memory-system testing / feedback / debugging as research-gated first-class candidate requirement
- user_confirmed: yes

Confirmed meaning:

Memory-system feedback, debugging, troubleshooting, and testing should be promoted from temporary addendum into a first-class candidate requirement.

It is not final design. It is not currently verified capability. It is research-gated and requires later evidence collection, capability-boundary research, industry-practice review, and dry-run validation.

Ideal long-term capability:

After a target project's AI-Agent team and memory system have been designed and established, Mnemosyne should eventually be able to use test-case-like scenarios to verify whether the memory system's actual working results match expected behavior.

Possible test targets:

- whether project Agents can find the right records;
- whether Agents follow memory rules;
- whether public/private boundaries are respected;
- whether handoff is used correctly;
- whether only authorized memory files are updated;
- whether summaries/indexes are not treated as authority;
- whether original-source records are preserved;
- whether conflicts are surfaced;
- whether work can continue across tasks or models.

Possible diagnosis targets:

- Agent behavior problem;
- memory-rule problem;
- file-organization problem;
- index-quality problem;
- handoff-quality problem;
- execution-source ambiguity;
- model/tool capability limit;
- ambiguous or conflicting user requirement.

Research-gated status:

This is an aspirational candidate capability. Current MNEMOSYNE-031 review does not prove that current models can perform this reliably. It does not prove that mature industry solutions or successful implementation patterns already exist. Later research and small dry-runs are required before any concrete testing/debugging workflow is promoted into execution source or target-project template rules.

### D-07: Confirm repository checkpoint / Codex writeback scope

- decision_status: accepted_with_checkpoint_scope_revision
- user_confirmed: yes

Confirmed meaning:

A Codex/repo writeback task may checkpoint the MNEMOSYNE-031 review materials into the repository after this user confirmation round. However, the original R5 review draft must not be treated as final if it conflicts with later D-01 to D-07 user-confirmed revisions.

Checkpoint scope:

Codex may checkpoint:

- R4B user restatement records;
- R4B manifest/index;
- R4C synthesis candidate-requirements document;
- original R5 review draft as historical draft/review input if useful;
- a new combined MNEMOSYNE-031 review/writeback record containing final user-confirmed D-01 to D-07 decisions and wording revisions.

The original R5 review draft:

- may be preserved as a draft/review input;
- must be marked superseded / reviewed / revised where it conflicts with the final decisions;
- must not be used as the authoritative final R5 decision record.

The new combined writeback record:

- should be the authoritative MNEMOSYNE-031 review result;
- still remains non-execution-source unless separately promoted through the approved process.

## agent_usage_expectations

- Reports are high-weight evidence layer for Mnemosyne meta-agent use.
- User is not required to master all full research reports.
- Meta-agent should evaluate feasibility.
- Meta-agent should confirm capability boundaries.
- Meta-agent should identify outdated, weak, over-idealized, or speculative assumptions.
- Meta-agent should suggest modern feasible practices.
- No report / motivation / prompt / summary / R4B / R4C / R5 file is execution source.
- Current execution source remains `current/human-approved-spec.md`.

## pdf_figure_review_status

- still_pending: yes
- notes:
  - Do not claim PDF figures, images, tables, or layout have been manually reviewed.
  - R3 acceptance applies only to summary/text evidence entry, not PDF visual/layout verification.

## files_that_must_not_be_modified_in_MNEMOSYNE_031

- research report originals
- pro prompt original
- missing light research prompts
- `current/human-approved-spec.md`
- PDF files
- `AGENTS.md`
- `CLAUDE.md`
- GitHub Actions files
- automation files

## next_route_recommendation

Recommended order:

1. Complete repository checkpoint for MNEMOSYNE-031.
2. Then choose one next route:
   - first dry-run of Mnemosyne on itself or a small target scenario;
   - PDF figure/table/image review planning;
   - Idea Capture Buffer / candidate requirements cleanup;
   - small fixes to tracking files if repository consistency issues are found.

Preferred next route after checkpoint:

- small Mnemosyne self-validation dry-run.

Reason:

The current work has accumulated enough review and intent material. Dry-run practice will help validate layered memory, original-source preservation, handoff behavior, index needs, public/private permission boundaries, and research-gated testing/debugging assumptions.
