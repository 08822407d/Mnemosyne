# Deep Research Prompt — DR5 v2: First real target-project dry-run evaluation framework

execute_in: new Pro Deep Research task/conversation
do_not_execute_in_current_maintainer_thread: true
stage: pre_real_target_project_dry_run_optional_but_recommended
repository_context: Mnemosyne first real target-project dry-run evaluation and memory-system validation
output_primary: full report body in the Deep Research final report/chat itself
output_file_backup: optional export only; not canonical

---

## Prompt to paste into Pro Deep Research

你正在为 Mnemosyne 进行 Deep Research。

请用中文撰写最终报告；必要的技术术语可保留英文。

## Critical output-delivery rule / 关键输出规则

完整研究报告正文必须直接出现在 Deep Research 最终报告 / 最终回答正文中。

不要把最终回答设计成“简短摘要 + 下载链接”。不要要求报告另写入、只写入或主要写入一个可下载文件。可下载文件或导出文件只能作为备份；不能作为唯一 canonical report original。

如果报告太长，请在最终回答中使用明确分片正文：

```yaml
package_id: DR5-v2-first-real-target-dry-run-evaluation-framework
chunk: N / total
instruction: wait for all chunks before ingestion/review
```

## Research title

**DR5 v2 — 首个真实 target-project dry-run 的评测框架：长期 Agent 记忆、handoff continuity、authority boundary、user-input governance 与 dry-run evidence 的验证方法**

## Background

Mnemosyne 是一个“记忆系统元 Agent”工作仓库，用于为目标项目设计、演化和交付 AI Agent 外部持久记忆系统。当前状态：

- post-MNEMOSYNE-053 fresh replay 已 reviewed PASS；
- target-project workspace principle 已进入 execution source；
- DR4 user-input governance 已完成；
- PRO-01 / PRO-02 / PRO-03 / PRO-04 已完成；
- B1 hardening 已完成，包括 synthetic-vs-real separation、approval conflict resolution、redaction manifest gate、external pointer safety gate、manual-import artifact classification、target workspace skeleton；
- 当前下一步可能是选择第一个真实 target project，并在 no-target-write / authority / safe input / run manifest 批准后进行 first real target-project dry-run；
- 目前仍没有 target selected、没有 real dry-run、没有 target materials ingested、没有 target repository written。

在真实需求验证前，Mnemosyne 需要一个外部证据支持的、可操作的评测框架，用于判断 first real target-project dry-run 到底算不算“成功”，并避免把 synthetic smoke test、draft design 或单次模型输出误认为真实验证。

## Research goals

请研究并提出一个适用于 Mnemosyne 的 **first real target-project dry-run evaluation framework**。重点不是泛泛介绍 AI agent memory，而是把当前工程状态转化为可执行评测方案。

请回答：

1. 真实 target-project dry-run 应验证哪些能力？
2. 如何区分：
   - synthetic smoke test；
   - tabletop dry-run；
   - real target-project dry-run；
   - real target delivery；
   - target repository write？
3. 如何评估长期外部记忆系统是否在真实需求场景中“有用且安全”？
4. 如何评估 handoff / continuity / replay 在真实 target 场景中是否有效？
5. 如何评估 authority/source-map recovery、target runtime truth source、no-target-write、user input storage policy 是否被正确遵守？
6. 如何设计 pass/fail / PASS_WITH_WARNINGS / REPAIR_RECOMMENDED / BLOCKED 判定？
7. 哪些检查应是 deterministic checklist，哪些可以使用 LLM-as-judge，哪些必须由用户确认？
8. 如何避免模型把漂亮的 delivery artifact 误判为真实项目成功？
9. 如何把 dry-run 结果转化为 Mnemosyne self-improvement candidates，而不污染 execution source？
10. 如何避免 target-specific lesson 被直接推广为 global rule？
11. 如何设计最小 postmortem 和 regression test record？
12. 如何在没有 target repository write 的前提下评估 delivery package 可用性？

## Sources to prioritize

优先使用当前、可靠来源：

- AI agent memory / long-term memory evaluation；
- multi-session continuity / handoff evaluation；
- requirements engineering validation；
- software acceptance testing / user acceptance testing；
- design review / architecture decision record practice；
- incident postmortem / runbook validation；
- data governance and privacy/redaction validation；
- LLM-as-judge reliability and evaluator bias；
- benchmark studies for agent memory, long-context continuity, task completion, stale context, and conflict handling.

可搜索并比较这些或同类 benchmark / methods：

```text
LoCoMo
LongMemEval
MemoryAgentBench
MemBench
MemoryBank-style evaluations
agent memory benchmarks
LLM-as-judge evaluation reliability
software UAT acceptance criteria
architecture review checklists
incident handoff/postmortem practices
```

如果某些 benchmark 名称不准确或已有更新，请使用最新可核实来源并说明。

## Required output structure

请按以下结构输出完整报告：

1. Executive summary
2. Direct recommendation for Mnemosyne before first real target dry-run
3. Evaluation object model
   - synthetic smoke test
   - tabletop dry-run
   - real target-project dry-run
   - target delivery
   - target repository write
4. Capability dimensions to evaluate
5. Safety / authority / governance dimensions to evaluate
6. Deterministic checks vs LLM-as-judge vs user-confirmation split
7. Pass/fail semantics and severity taxonomy
8. Evidence requirements
9. First real target dry-run scorecard v0.1
10. Dry-run postmortem template
11. Regression test record schema
12. How to route findings into Mnemosyne self-improvement without execution-source contamination
13. Comparison to existing memory / continuity / agent benchmarks
14. Recommendations for Mnemosyne v0.1
15. Deferred v0.2+ recommendations
16. Evidence table with citations
17. Known uncertainty and limits

## Required deliverable A — Evaluation dimensions

给出一个表格，至少包含：

```text
dimension_id
dimension_name
what_it_tests
evidence_required
deterministic_check
llm_judge_allowed
user_confirmation_required
failure_examples
severity_if_failed
```

必须包含这些维度：

```text
target selection validity
authority/source-map completeness
target runtime truth source status
safe input/user originals storage policy
redaction manifest / external pointer safety
no-target-write preservation
synthetic-vs-real evidence separation
memory schema fit to target needs
handoff package usability
unsupported assumptions handling
stale/conflicting context handling
delivery package completeness
target-specific/global lesson separation
postmortem quality
```

## Required deliverable B — Scorecard v0.1

提出一个 100 分或权重制 scorecard。必须有 critical blockers。建议包含：

```yaml
critical_blockers:
  - target_not_selected
  - authority_missing
  - no_target_write_not_confirmed
  - unsafe_material_ingested
  - target_repository_written_without_approval
  - synthetic_evidence_reported_as_real_dry_run
  - target_workspace_treated_as_execution_source
  - target_runtime_truth_source_invented
  - user_originals_stored_unsafely
  - missing_run_manifest_approval
```

分数维度可包括：

```text
context recovery
authority/source map
input safety
memory design fit
handoff/delivery usability
evidence/provenance
assumption discipline
postmortem/actionability
```

## Required deliverable C — Result semantics

定义：

```yaml
dry_run_result_verdict:
  PASS:
  PASS_WITH_WARNINGS:
  REPAIR_RECOMMENDED:
  FAIL:
  BLOCKED:
```

必须明确：`PASS` 不等于 production-ready，不等于 target repository write approved，不等于 global Mnemosyne rule update approved。

## Required deliverable D — Postmortem template

提供 Markdown/YAML 模板：

```yaml
first_target_dry_run_postmortem:
  dry_run_id:
  target_project_id:
  run_kind: real_target_project
  target_repository_write_performed: false
  target_materials_ingested:
  materials_safety_status:
  verdict:
  score:
  critical_blockers:
  what_worked:
  what_failed:
  unsupported_assumptions_found:
  stale_context_found:
  authority_conflicts_found:
  user_input_storage_issues:
  handoff_continuity_issues:
  delivery_package_issues:
  target_specific_lessons:
  mnemosyne_global_lesson_candidates:
  required_repairs:
  user_decisions_needed:
  evidence_paths:
```

## Required deliverable E — Regression test record schema

提供：

```yaml
mnemosyne_regression_test_record:
  test_id:
  source_event:
  target_scope:
  model_or_tool:
  repository_ref:
  input_package:
  expected_recovery:
  forbidden_claims:
  deterministic_checks:
  llm_judge_checks:
  user_confirmation_checks:
  result:
  score:
  evidence:
  failure_class:
  follow_up_task:
```

## Required deliverable F — Integration recommendations

把建议分为：

```text
use_before_first_real_target_dry_run
add_to_non_execution_source_support_instruments
candidate_for_execution_source_later
defer_until_after_first_real_target
do_not_do_in_v0.1
```

## Constraints

- 不要把研究报告当作 Mnemosyne execution source。
- 不要建议 v0.1 必须自动化、MCP、RAG、GitHub Actions 或 auto-writeback。
- 不要建议在 first dry-run 中写 target repository。
- 不要把 synthetic smoke test 当作 real target dry-run evidence。
- 不要假设 private repo 自动允许敏感原文入库。
- 不要忽视 Git history exposure。
- 不要把 LLM-as-judge 当作唯一评审者。
- 不要假设一次 target 成功就能更新 global execution source。
- 明确区分 facts、research evidence、engineering recommendations、Mnemosyne-specific recommendations。

## Final answer requirement

最终回答必须直接包含完整报告正文。可以有短摘要开头，但不能只有摘要。不要把报告主体藏在下载链接中。
