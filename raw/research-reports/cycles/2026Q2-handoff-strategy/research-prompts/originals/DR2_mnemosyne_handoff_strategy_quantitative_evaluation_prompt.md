# Deep Research Prompt — Mnemosyne Handoff Strategy and Quantitative Evaluation

package_id: `DR-MNEMOSYNE-HANDOFF-STRATEGY-2026Q2`
status: research-prompt-draft
intended_use: paste into a Deep Research-capable AI conversation/tool
language: Chinese primary, English terms allowed where useful
repository_context: Mnemosyne external persistent memory meta-agent workspace
not_execution_source: true

---

## 0. Research task title

**Mnemosyne handoff package strategy: definition, quantitative evaluation, and practical starting template for cross-conversation / cross-agent continuation**

中文标题：

**Mnemosyne 交接包策略研究：跨对话 / 跨 Agent 续接的正确性定义、量化评估与可执行起点模板**

---

## 1. Background and motivation

Mnemosyne is an external persistent memory meta-agent system. Its core problem is not just “store information”, but to make long-running AI work recoverable across different conversations, models, tools, and time points.

In current practice, Mnemosyne already uses handoff files, active-context files, startup instructions, replay protocols, Codex task result records, and ordinary ChatGPT ↔ Codex writeback loops. However, after many real self-construction handoffs, the user still cannot reliably answer:

- What exactly counts as a “correct handoff”?
- What information must a handoff package contain?
- How much detail is too little or too much?
- How should a handoff package be evaluated quantitatively?
- How should handoff strategy differ across ordinary ChatGPT, Codex, Claude/Cursor-like coding agents, or different model versions?
- How can a handoff package preserve continuity without blindly importing stale context?
- How can the system distinguish execution source, current state, historical background, task intent, user approvals, and non-execution evidence?
- How should a handoff package prevent a new conversation from repeating old tasks, misreading current gates, or claiming that an uncompleted task already happened?

The user does not know how to specify a quantitatively good handoff package strategy. Therefore, the research goal is to produce a “not too far from correct” quantitative starting framework, even if imperfect. The framework should be usable immediately and then refined through future Mnemosyne dry-runs, self-construction tasks, and real target-project memory-system deployments.

This research should treat Mnemosyne’s own construction history as both:

1. **research sample** — real-world examples of handoffs, failures, repairs, startup guidance, and Codex writeback tasks;
2. **test case** — a practical environment in which a proposed handoff strategy can be evaluated.

---

## 2. Scope boundary

This research is specifically about **handoff package strategy and handoff evaluation**.

Do not broaden into a full memory-system architecture research unless directly needed to define handoff strategy.

In scope:

- Cross-conversation handoff between ordinary ChatGPT conversations.
- Handoff from ordinary ChatGPT planning to Codex task execution.
- Handoff from Codex result back to ordinary ChatGPT verification.
- Handoff from Mnemosyne maintainer conversation to a fresh ordinary Thinking conversation.
- Handoff between different model families or tool interfaces, including ChatGPT, Codex, Claude Code / Cursor-like coding agents, where evidence exists.
- Quantitative / semi-quantitative scoring of handoff correctness.
- Minimum, standard, and extended handoff package structure.
- Evaluation protocols using Mnemosyne self-construction examples.
- Failure modes: stale state, wrong execution source, old task replay, missing user approval, missing current gate, hallucinated repo state, overlong context import, hidden old-conversation contamination, model/version differences.

Out of scope unless directly relevant:

- Full RAG architecture design.
- Automated indexing mechanism design.
- Full multi-agent governance system.
- Target-project memory schema design except as downstream use cases.
- Creating AGENTS.md / CLAUDE.md / GitHub Actions / automation for Mnemosyne.
- Treating any research output as automatically approved execution source.

---

## 3. Required source classes

Use current, reliable sources. Prefer primary or technical sources where available.

### 3.1 External literature / technical sources

Search for current work and best practices in:

- LLM / AI agent memory systems.
- Agent handoff, agent delegation, context transfer, context engineering.
- Long-context and multi-turn agent evaluation.
- Memory benchmarks such as MemoryAgentBench, MemBench, MemoryArena, LoCoMo, LongMemEval, LoCoBench-Agent or similar.
- Context compaction / summarization / replay protocols.
- Claude Code / Cursor / coding-agent instruction files and project memory mechanisms.
- OpenAI Agents SDK handoffs and handoff input filtering.
- LangGraph / LangChain memory concepts: short-term vs long-term memory, thread state, long-term stores.
- LLM-as-judge / human evaluation / rubric design for handoff correctness.
- Software engineering handoff / incident handover / design document review practices, but only where transferable to AI agent handoff.

### 3.2 Mnemosyne internal materials to inspect if provided

When the user provides access to Mnemosyne repository files or excerpts, inspect at least:

- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `commands/load-mnemosyne-guidance.md`
- `notes/first-target-project-fresh-replay-protocol.md`
- `handoff/first-target-project-dry-run-onboarding-package.md`
- `notes/first-target-project-dry-run-manifest-template.md`
- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
- relevant Codex task result records from MNEMOSYNE-034 through MNEMOSYNE-050
- old conversation export excerpts if supplied

Do not treat old conversation exports as current truth. Use them only as historical examples of handoff success/failure and conversation drift.

---

## 4. Central research questions

Answer these questions directly.

### RQ1 — Definition

What does “correct handoff” mean for an AI-agent external persistent memory system?

Define correctness in a way suitable for Mnemosyne, including at least:

- state recovery correctness;
- execution-source recovery;
- task intent recovery;
- boundary recovery;
- authority / user approval recovery;
- next-action recovery;
- stale-state resistance;
- unsupported-assumption handling;
- safety / privacy boundary preservation;
- model/tool provenance recovery;
- ability to continue without re-asking already answered questions.

### RQ2 — Handoff package content

What minimum information should a handoff package contain to allow a fresh agent/session to continue safely?

Distinguish:

1. **minimum handoff package** — short, low-token, enough for ordinary continuation;
2. **standard handoff package** — enough for repository-backed Mnemosyne maintenance;
3. **extended handoff package** — enough for high-risk transitions, model migration, or post-failure recovery.

For each tier, specify fields, examples, and what should explicitly be excluded.

### RQ3 — Quantitative evaluation

How can handoff quality be scored?

Propose a scoring rubric with weights. Include both binary gates and graded dimensions.

At minimum include metrics for:

- execution-source identification;
- current phase / gate recovery;
- file/state reference accuracy;
- current task recovery;
- previous completed task recovery;
- next action correctness;
- forbidden action avoidance;
- user approval / authority recovery;
- stale-context detection;
- unsupported assumption labeling;
- evidence citation/path quality;
- concision vs completeness;
- cross-model robustness;
- token cost / context load efficiency.

Define PASS / FAIL / BLOCKED or equivalent verdict rules.

### RQ4 — Evaluation protocol

How should Mnemosyne evaluate a handoff package strategy in practice?

Design practical tests using Mnemosyne self-construction as sample data.

The protocol should include:

- fresh ordinary ChatGPT replay;
- same-model new conversation replay;
- different-model replay;
- Codex read-only verification;
- post-Codex-result verification;
- corrupted / stale handoff adversarial test;
- missing file test;
- old conversation export contamination test;
- overlong handoff package stress test;
- target-project dry-run handoff test.

For each test, specify input, expected output, scoring method, failure signals, and what to record.

### RQ5 — Handoff generation strategy

How should a handoff package be generated?

Compare:

- fully manual handoff written by the current conversation;
- template-driven handoff;
- file-based handoff generated from repository state;
- multi-part handoff with summary + evidence map;
- current/handoff/startup split;
- task-specific onboarding package;
- long conversation export + extracted selected excerpts;
- replay protocol with fixed prompt.

Recommend a practical Mnemosyne v0.1/v0.2 strategy.

### RQ6 — Model and tool variation

How should handoff strategy account for different models and tool environments?

Discuss:

- model family / visible model label;
- reasoning model vs non-reasoning model;
- ordinary ChatGPT vs Codex vs Claude/Cursor-style coding agents;
- repository access vs pasted file access;
- ability or inability to read files;
- context window and compaction differences;
- hidden memory / platform memory contamination;
- version drift over time.

Recommend what model/tool metadata must be recorded for each handoff test.

### RQ7 — Failure modes and repair

What are common handoff failure modes, and how should Mnemosyne detect and repair them?

Include at least:

- old task replay;
- stale status accepted as current;
- old conversation memory contamination;
- wrong execution-source promotion;
- treating non-execution files as spec;
- hallucinated repo writes;
- claiming dry-run or target selection occurred;
- missing authority approval;
- overlong handoff causing instruction loss;
- too-short handoff causing missing constraints;
- unsupported assumptions silently invented;
- model version/tool capability assumptions not verified.

For each failure mode, propose detection signals and mitigation.

---

## 5. Required output structure

Produce a research report with this structure.

### 5.1 Executive summary

- One-page summary.
- Direct answer: Is Mnemosyne’s current handoff strategy direction basically sound?
- What is the biggest current risk?
- What should be done before first real target-project dry-run?

### 5.2 Operational definition of correct handoff

Give a clear definition and a checklist.

### 5.3 Handoff package tier model

Provide minimum / standard / extended handoff templates.

For each tier, include:

- field list;
- purpose;
- when to use;
- token/length guidance;
- required evidence paths;
- prohibited content;
- example skeleton.

### 5.4 Quantitative scoring rubric

Provide:

- score dimensions;
- weights adding up to 100;
- critical blocking gates;
- PASS / PASS_WITH_WARNINGS / FAIL / BLOCKED rules;
- scoring examples.

The rubric should be concrete enough that a future ChatGPT or Codex verification task can apply it.

### 5.5 Mnemosyne self-construction test suite

Design a test suite using Mnemosyne’s own construction history.

Include at least 8 test cases:

1. fresh startup from current repository files;
2. handoff after a Codex task result;
3. handoff after a failed or stale Codex branch scenario;
4. handoff after a long old conversation export;
5. handoff before first target-project dry-run;
6. handoff across model/tool labels;
7. handoff with missing current/handoff file;
8. handoff with deliberately stale next-step instruction.

### 5.6 Recommended v0.1 implementation

Recommend what Mnemosyne should do now, without overengineering.

Include:

- which current files should carry current state;
- which files should not be execution source;
- what a handoff package should include now;
- what metadata to add to replay records;
- what not to automate yet;
- what to defer until real target-project dry-runs.

### 5.7 Future research / improvement backlog

List what should be deferred to later research or future versions.

---

## 6. Required concrete deliverables

The report must include these deliverables.

### Deliverable A — Correct handoff definition

A concise definition, suitable for later inclusion as candidate wording.

### Deliverable B — Mnemosyne handoff scoring rubric v0.1

A table with dimensions, weights, pass thresholds, blocking failures, and evidence requirements.

### Deliverable C — Handoff package templates

Provide three templates:

1. `minimum_handoff_package_v0.1`
2. `standard_handoff_package_v0.1`
3. `extended_handoff_package_v0.1`

Each template should be in YAML or Markdown structure.

### Deliverable D — Replay / verification prompt

Provide a fixed prompt that can be pasted into a fresh ordinary ChatGPT conversation to test whether a handoff package works.

### Deliverable E — Handoff failure taxonomy

Provide failure modes with detection and mitigation.

### Deliverable F — Model/tool provenance schema

Provide a minimal schema for recording the model/tool context of a handoff test:

```yaml
handoff_test_provenance:
  tested_at:
  source_conversation_or_task:
  target_conversation_or_task:
  tool_or_interface:
  visible_model_label:
  reasoning_effort_if_visible:
  repository_ref_or_commit:
  files_available:
  files_read:
  user_supplied_context:
  hidden_prior_context_expected: yes/no/unknown
  limitations:
```

### Deliverable G — Immediate Mnemosyne recommendations

A short ordered list of changes or checks Mnemosyne should perform before first real target-project dry-run.

Do not say “perform more research” as the only recommendation. The report must produce a usable starting strategy.

---

## 7. Evaluation requirements for the research report itself

The final report should be evaluated against these criteria:

- Does it define “correct handoff” operationally, not vaguely?
- Does it provide a numeric or semi-numeric rubric?
- Does it distinguish critical blocking gates from ordinary quality issues?
- Does it avoid assuming that a long summary is always better?
- Does it account for stale-state and old-conversation contamination?
- Does it account for different models and tool interfaces?
- Does it produce templates that can be used immediately?
- Does it provide a practical test protocol using Mnemosyne’s own construction history?
- Does it identify what should be done now vs deferred?
- Does it avoid promoting research conclusions directly into execution source?

---

## 8. Important constraints

- Do not assume repository writes are allowed unless explicitly authorized.
- Do not propose fully automated writeback as a current requirement.
- Do not treat old conversation exports as current truth.
- Do not treat research reports as execution source.
- Do not assume that `AGENTS.md`, `CLAUDE.md`, GitHub Actions, MCP, RAG, or automatic indexing already exist.
- If recommending any of those mechanisms, classify them as future/candidate/research-gated and explain required evidence.
- Do not overfit to one model vendor.
- Record uncertainty when current model/tool behavior cannot be verified.
- Separate facts from recommendations.
- Separate immediate v0.1 actions from future v0.2+ improvements.

---

## 9. Suggested search terms

Use combinations of the following:

- “LLM agent handoff evaluation”
- “AI agent context transfer”
- “agent memory handoff”
- “context engineering agent memory”
- “conversation summarization handoff LLM evaluation”
- “multi-session agent benchmark memory”
- “MemoryAgentBench”
- “MemBench LLM agents memory”
- “MemoryArena multi-session agent memory”
- “LoCoBench-Agent long-context software engineering agents”
- “Claude Code memory CLAUDE.md effective instructions”
- “OpenAI Agents SDK handoffs input filters”
- “LangGraph memory short-term long-term state checkpointer”
- “LLM-as-judge rubric evaluation agent handoff”
- “software engineering handoff checklist incident handover”

---

## 10. Expected final answer style

Write the final research report in Chinese, but keep technical terms in English when they are clearer.

Use this output style:

1. Start with direct conclusions.
2. Then provide the framework.
3. Then provide templates and scoring rubric.
4. Then provide test protocol.
5. End with immediate recommendations for Mnemosyne.

Avoid vague advice. The goal is to give Mnemosyne a quantitative starting point that can be imperfect but usable.
