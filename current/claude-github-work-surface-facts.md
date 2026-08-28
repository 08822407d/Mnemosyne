# Claude GitHub Work-Surface Facts — Current

> Current, time-sensitive product-surface record for Mnemosyne work that uses Claude with GitHub-backed persistent storage. This file is not an execution source and does not authorize Claude, Fable, Claude Code, Research, quota use, repository writes, target adoption or connector activation. `current/human-approved-spec.md` remains the only Mnemosyne execution source.

```yaml
fact_record_id: MNEMOSYNE-CLAUDE-GITHUB-WORK-SURFACE-FACTS-001
created_by_task: MNEMOSYNE-219
observed_and_checked_at: 2026-08-15
product_account_condition: user_reported_Claude_Max_5x_100_USD_monthly
status: current_fact_with_operator_observation_and_official_documentation
fact_classes:
  - official_current_documentation
  - operator_observed_current_account_UI
  - engineering_inference
exact_backend_identity: unknown_or_not_attestable
execution_source_modified: false
```

## 1. Operator-observed Claude web Project UI

The Owner completed the `MNE-DR-005` Project-knowledge folder-selection preflight on the current Claude web UI.

```yaml
observed_surface: Claude_web_Project_add_context_from_GitHub
ordinary_repository_selection_exposed_branch_list: false
successful_non_default_branch_route:
  - click_the_hyperlink_icon
  - paste_the_full_GitHub_branch_URL
  - browse_the_supplied_branch
  - select_the_required_folder_once
observed_folder: project-knowledge/MNE-DR-005/
observed_Project_knowledge_file_count: 30
folder_selection_preflight: PASS
Research_started_during_preflight: false
claim_scope: this_account_and_current_rollout_only
```

Current operator rule:

- when a Claude Project needs content from a non-default branch, do not instruct the Owner to expect a branch dropdown after ordinary repository selection;
- first use the hyperlink/URL entry route and paste the complete branch URL;
- then select the exact task-specific folder;
- confirm the resulting file count before starting Research;
- recheck this behavior after a material Claude UI change.

## 2. Official Claude Project GitHub boundary

Current Anthropic documentation states that Claude Project GitHub integration can:

- search accessible repositories or accept a repository URL;
- select specific files and folders;
- synchronize previously selected content;
- add content from multiple repositories when it fits within the available context/retrieval capacity.

The synced Project model provides file names and contents from a specific branch. It does not provide commit history, pull requests or other Git metadata as Project knowledge.

Consequences:

- a path list alone does not make those files readable unless they are actually selected or otherwise supplied;
- branch URL entry and folder selection are input-configuration work, not repository development;
- a branch chip or repository link does not attest an exact commit unless separately verified;
- Project knowledge is suitable for bounded read-only evidence packets, not as a complete Git working environment.

## 3. Claude Code boundary

Current Anthropic documentation describes Claude Code on the web as a separate work surface that:

- clones the selected GitHub repository into an isolated remote environment;
- reads and edits repository files;
- runs setup commands, tests and other shell commands;
- pushes changes to a new branch;
- supports pull-request creation/review workflows;
- permits several isolated tasks to run in parallel.

Claude Max includes access to Claude Code. Claude Code in a terminal/IDE is recommended by Anthropic for exploratory work, frequent course correction and work involving local uncommitted changes; Claude Code on the web is recommended for well-defined delegated tasks.

## 4. Current Mnemosyne work-surface decision

```yaml
Claude_Project_GitHub_context:
  recommended_for:
    - bounded_read_only_research
    - Fable5_independent_evidence_packets
    - one_run_Project_knowledge_snapshots
  not_recommended_as_primary_surface_for:
    - ongoing_branch_and_PR_maintenance
    - commit_history_or_PR_metadata_review
    - repeated_write_heavy_meta_Agent_development

Claude_Code_web_or_terminal:
  candidate_for:
    - Mnemosyne_repository_maintenance
    - Meta_Agent_repository_maintenance
    - target_repository_build_and_documentation_changes
    - branch_commit_test_and_PR_workflows
  adoption_status: requires_bounded_document_centric_pilot_before_becoming_default

repository_files:
  role: durable_cross_product_memory_and_truth
  examples:
    - current_truth_and_authority_files
    - task_and_handoff_packages
    - CLAUDE.md_or_equivalent_repo_local_guidance
    - validation_and_result_records
```

## 5. Answer to the current portability question

Claude can support GitHub-backed long-term Agent construction, but not with the same convenience when Claude Project GitHub context is used as the only surface.

The closest functional comparison is:

- Claude Project GitHub context ↔ bounded read-only repository context;
- Claude Code on the web/terminal ↔ repository-working Agent with branch, command and PR capabilities;
- Fable 5 Research ↔ independent high-capability research/adjudication surface.

Therefore the current recommendation is a split workflow rather than forcing every task through Claude Project context.

## 6. Recheck triggers

Reverify this record when any of the following occurs:

- the Claude Project GitHub UI adds an ordinary branch picker;
- the hyperlink/branch-URL entry route changes or disappears;
- Project knowledge begins exposing commit/PR metadata;
- Claude Code repository, branch, PR or plan behavior changes;
- a real Mnemosyne/Meta-Agent Claude Code pilot reveals different permissions, task isolation or operator burden;
- Anthropic changes Max-plan inclusion, quotas or data-retention terms;
- the user changes the preferred Claude work surface.

## 7. Official sources checked

Checked on 2026-08-15:

- Anthropic Help Center — `Use the GitHub integration`
- Anthropic Help Center — `Claude Code on the web`
- Anthropic Help Center — `What is the Max plan?`

The exact current UI route in §1 is Owner-observed evidence and is intentionally not represented as an official universal product guarantee.

## 8. GitHub-side app authorization vs installation（addendum 2026-08-28, MNEMOSYNE-251）

Owner-observed on the Owner's account（截图证据，2026-08-28）：

- GitHub 对 App 有两个独立层：**Authorized GitHub Apps**（授权 App 代表用户行动）与 **Installed GitHub Apps**（安装进账号并圈定仓库范围）。Anthropic 的 `Claude` App（slug `claude`，owner `anthropics`——经 `gh api /apps/claude` 核实）在仅完成 claude.ai 连接器 OAuth 时只出现在前者。
- 公开仓库：仅授权层即可被 Claude 网页读取（Owner 此前对 Mnemosyne 的文件夹选择即在此状态下成功）。
- **私有仓库：需要安装层的仓库授予**——经 <https://github.com/apps/claude> 安装、选 "Only select repositories" 并勾选目标私库；此后该 App 与仓库范围在 Installed GitHub Apps 页可配置。Owner 已于 2026-08-28 按此为私库 Alaya 完成配置。
- 各厂商 App 的安装与仓库范围**互不相通**（ChatGPT 的连接器授权不覆盖 Claude，反之亦然）。
- claim scope：本节为该账号当期观察＋GitHub 文档化模型；产品接入流程属时效事实，复核触发同 §6。
