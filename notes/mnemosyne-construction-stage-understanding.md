# Mnemosyne Construction-Stage Understanding

This file is not an execution source. It is a non-execution-source construction-stage understanding note for preserving user supplemental explanations, candidate rationale, open-question material, and idea-buffer material.

`current/human-approved-spec.md` remains the only execution source. If this note conflicts with `current/human-approved-spec.md`, the spec wins and the conflict should be recorded as an open question rather than silently resolved here.

## 1. Mnemosyne as prototype-stage exploratory engineering

Mnemosyne is currently closer to a prototype-stage exploratory system than a mature conventional software project. The current goal is not perfect architecture or complete process formalization.

The initial goal is to establish a usable external persistent memory framework that is better than relying only on model context or platform-internal memory. Real maturity should come from using Mnemosyne to design persistent memory systems for real target projects, observing problems, and feeding those problems back into Mnemosyne.

Defects are acceptable at this stage because both the human user and AI agents have some intelligence and can work around imperfect memory-system behavior.

Core problems remain:

- model context is limited and lossy;
- platform/internal memory is not a stable truth source;
- new conversations/tasks need more reliable handoff;
- long-term projects need AI help to compensate for limited human memory.

## 2. Ordinary ChatGPT to Codex repository writeback loop

Ordinary ChatGPT conversations are generally read-only with respect to GitHub repositories. Ordinary ChatGPT conversations may and often should generate strict Codex tasks when a discussion result needs to be landed in the repository.

Codex tasks are the reviewed writeback mechanism: Codex edits repository files, opens PRs, the user reviews and merges, and then a ChatGPT/Codex read-only verification can confirm the result on master.

Therefore "do not write the repository in this conversation" must not be misread as "do not generate Codex tasks." The correct distinction is:

- discussion / planning stage;
- Codex task prompt generation stage;
- Codex execution / PR stage;
- user review and merge stage;
- post-merge verification stage.

## 3. Evidence-guided self-improvement

Mnemosyne does not improve only through self-use and project feedback. It should also use periodic deep research and current best practices in adjacent fields.

Mnemosyne-affiliated AI conversations/tasks should actively compare research findings with:

- current open questions;
- failure modes;
- target-project feedback;
- template gaps;
- capability boundaries;
- outdated assumptions.

The user is not expected to read all research reports or manually identify every applicable best practice.

Research evidence is evidence, not execution source. It can generate candidate improvements, open questions, or research-gated items, but cannot directly override `current/human-approved-spec.md`.

## 4. Human-readable basis materials vs agent-operational artifacts

Two broad material classes are useful for discussing Mnemosyne artifacts.

Human-readable basis materials:

- raw user text;
- original requirements and feedback;
- Human-Approved Design Basis / HADB;
- research prompts and research reports.

Agent-operational artifacts:

- startup instructions;
- handoff;
- active context;
- commands;
- templates;
- task prompts;
- delivery manifests;
- verification checklists;
- Codex task result records;
- other model/agent-facing operational files.

Human-readable basis materials preserve human intent, user reviewability, model-migration evidence, and design grounding.

Agent-operational artifacts are generated for later agents to load, follow, transform, or verify. Agent-operational artifacts are similar to software source code, intermediate representations, or compiled artifacts in the sense that they should be structured, role-specific, and used consistently by agents.

They are still natural-language/Markdown artifacts, so they are not deterministic machine code, but they should be designed to maximize reproducibility and reduce interpretation drift. They must not be invented or silently reinterpreted by later agents.

## 5. Human-Approved Design Basis / HADB

Human-Approved Design Basis (HADB), Chinese: 人类确认设计依据稿.

HADB is a human-readable settled design-basis text formed after discussion, contradiction resolution, feasibility analysis, research-evidence checking, and user confirmation.

HADB is not the raw original record. HADB is not automatically the execution source. HADB is the direct input for generating agent-operational artifacts and later design documents.

After user confirmation, a HADB version should not be silently modified within the same design round. If later generation of operational artifacts reveals missing details, the agent should request clarification and record a clarification addendum or next revision rather than inventing missing details.

## 6. Indexing / retrieval acceleration as research-gated performance optimization

The user's "index" idea was borrowed from PC hardware / operating-system / file-system analogies. It has not been verified as suitable for AI agent external memory.

It should not be treated as a core Mnemosyne requirement. It should be classified as a research-gated performance optimization candidate.

It may later be studied as a retrieval acceleration mechanism when persistent memory grows large. Risks include stale indexes, misleading indexes, and agents treating indexes as authority rather than retrieval aids.


## 7. Near-term target-project readiness priority

The current near-term construction priority is to make Mnemosyne capable of designing and helping build persistent-memory frameworks for other target projects as soon as reasonably possible.

Mnemosyne should avoid getting trapped in endless refinement of its own internal protocols before serving real target-project memory needs. Internal onboarding reliability, command conventions, and behavior guidance remain important, but they should primarily support real target-project readiness.

The practical near-term success condition is not a perfect internal system. It is a usable framework that can:

- intake a target project's context and constraints;
- propose an external persistent-memory structure;
- distinguish execution source, evidence, candidate material, handoff, and operational artifacts;
- produce a deliverable starter memory framework for the target project;
- receive feedback from target-project use and feed it back into Mnemosyne.

This priority remains non-execution-source construction understanding unless later promoted through approved workflow.
