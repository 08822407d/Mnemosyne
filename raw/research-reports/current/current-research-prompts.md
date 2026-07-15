# Current Research Prompts / 当前研究课题索引（派生视图）

## 文件定位

本文件是 current 派生视图，用于索引当前激活研究轮次的 research prompts / prompt availability。

- active_cycles: RC-2026Q2-initial; RC-2026Q2-memory-testing (supplemental); RC-2026Q2-handoff-strategy (supplemental); RC-2026Q2-user-input-governance (supplemental); RC-2026Q2-first-target-dry-run-evaluation (supplemental); RC-2026Q3-platform-context-apps-delta (supplemental)
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- prompt 原文是研究输入，不是研究报告结果；
- pro prompt 原文当前可用；
- 6 个用户找回的轻度研究 prompt 原文当前可用；
- 原始 prompt 文件位于各 cycle 的 `research-prompts/originals/`；
- prompt index 与 report-topic mapping 位于各 cycle 目录；
- prompt 是 research input，不是 report conclusion 或 execution source。

## Current Prompt Index

| prompt_id | related_report_id | prompt_status | prompt_file | topic_title | notes |
|---|---|---|---|---|---|
| PROMPT-2026Q2-0001 | RPT-2026Q2-0001 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/AI_agent_external_persistent_memory_deep_research_prompt_pro.md` | AI agent external persistent memory / AI agent 长期记忆系统 | 用户保留的 pro 深度研究课题原文；用于理解研究输入，不是执行源。 |
| PROMPT-2026Q2-0002 | RPT-2026Q2-0002 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/01_non_dev_long_term_memory_cases.md` | 非开发长期对话记忆是否已有真实实践 | recovered user-provided light-research prompt original; prompt is input, not report conclusion or execution source. |
| PROMPT-2026Q2-0003 | RPT-2026Q2-0003 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/02_chatgpt_claude_conversation_memory_boundaries.md` | ChatGPT / Claude 纯对话场景的外部记忆能力边界 | recovered user-provided light-research prompt original; prompt is input, not report conclusion or execution source. |
| PROMPT-2026Q2-0004 | RPT-2026Q2-0004 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/03_local_coding_agents_file_memory.md` | Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力 | recovered user-provided light-research prompt original; prompt is input, not report conclusion or execution source. |
| PROMPT-2026Q2-0005 | RPT-2026Q2-0005 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/04_cloud_coding_agents_github_memory_writeback.md` | 云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计 | recovered user-provided light-research prompt original; prompt is input, not report conclusion or execution source. |
| PROMPT-2026Q2-0006 | RPT-2026Q2-0006 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/05_theory_engineering_basis_external_memory.md` | 外部持久记忆的理论与工程依据 | recovered user-provided light-research prompt original; prompt is input, not report conclusion or execution source. |
| PROMPT-2026Q2-MT-0001 | RPT-2026Q2-MT-0001 | available_original_prompt | `raw/research-reports/cycles/2026Q2-memory-testing/research-prompts/originals/DR1_memory_testing_debugging_evidence_review_prompt.md` | AI Agent external persistent memory system testing/debugging/evaluation/failure diagnosis | DR1 prompt; research input only, not report conclusion or execution source. |
| PROMPT-2026Q2-0007 | RPT-2026Q2-0007 | available_original_prompt | `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/06_transfer_dev_memory_to_general_dialogue.md` | 开发场景的持久记忆经验能否迁移到普通长期对话和学习场景 | recovered user-provided light-research prompt original; prompt is input, not report conclusion or execution source. |

## Review Notes

- MNEMOSYNE-038 已将 `PROMPT-2026Q2-0002` through `PROMPT-2026Q2-0007` 从 missing status 更新为 available recovered originals。
- 如 prompt 与 report / summary / motivation 存在差异，可登记 delta / review note；但 prompt 本身不作为研究结论或执行源。
- MNEMOSYNE-040 normalized and indexed DR1 memory-testing prompt under supplemental cycle `RC-2026Q2-memory-testing`。

## PROMPT-2026Q2-HO-0001 — DR2 handoff strategy / 交接包策略量化研究

- prompt_id: PROMPT-2026Q2-HO-0001
- cycle_id: RC-2026Q2-handoff-strategy
- file_path: `raw/research-reports/cycles/2026Q2-handoff-strategy/research-prompts/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_prompt.md`
- topic: Mnemosyne handoff package strategy and quantitative evaluation
- prompt_type: deep_research_prompt
- status: original_available
- note: Research input only; not a report conclusion and not execution source.

## DR4 user-input governance prompt status

```yaml
prompt_id: PROMPT-2026Q2-UIG-0001
report_id: RPT-2026Q2-UIG-0001
cycle_id: RC-2026Q2-user-input-governance
status: original_available
prompt_path: raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md
prompt_type: corrected_deep_research_prompt
note: Research input only; not a report conclusion and not execution source. This corrected prompt requires the full Deep Research report body in the final answer and forbids summary+download-only report delivery.
```

## Supplemental prompt — DR5 first real target-project dry-run evaluation

| prompt_id | related_report_id | prompt_status | prompt_file | topic_title | notes |
|---|---|---|---|---|---|
| PROMPT-2026Q2-FTDRE-0001 | RPT-2026Q2-FTDRE-0001 | original_available | `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/research-prompts/originals/DR5_v2_first_real_target_dry_run_evaluation_framework_prompt.md` | DR5 first real target-project dry-run evaluation framework | Prompt is research input/provenance, not report evidence or execution source. |

## Supplemental prompt — DR6 2026Q3 platform/context/apps delta

| prompt_id | related_report_id | prompt_status | prompt_file | topic_title | notes |
|---|---|---|---|---|---|
| PROMPT-2026Q3-PLATFORM-DELTA-0001 | RPT-2026Q3-PLATFORM-DELTA-0001 | original_available | `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/research-prompts/originals/DR6_2026Q3_platform_memory_apps_capability_delta_prompt.md` | Project memory, apps/plugins, GitHub, Deep Research, Work/Codex/Agent, provenance, no-write and handoff delta | Research input only; report accepted with corrections by MNEMOSYNE-123. |

## DR6 review notes

- DR6 report-level Deep Research citation markers may not resolve in GitHub; use the cycle `source-manifest.md` for load-bearing official URLs.
- 有依赖关系的后续 Deep Research 应遵守 §17 分阶段生成，不一次性启动全部下游课题。
- DR6 prompt and report do not close Issues #170/#171, resolve `HO-GUIDANCE-001`, or modify the execution source.
