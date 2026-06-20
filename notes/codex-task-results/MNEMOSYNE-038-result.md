# MNEMOSYNE-038 Result Record

task_id: MNEMOSYNE-038
task_name: Recover Light Research Prompt Originals

task_claims_completion: yes

## files_created

- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/01_non_dev_long_term_memory_cases.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/02_chatgpt_claude_conversation_memory_boundaries.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/03_local_coding_agents_file_memory.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/04_cloud_coding_agents_github_memory_writeback.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/05_theory_engineering_basis_external_memory.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/06_transfer_dev_memory_to_general_dialogue.md`
- `notes/codex-task-results/MNEMOSYNE-038-result.md`

## files_modified

- `raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/current/current-report-summaries.md`
- `current/active-context.md`
- `current/todo.md`
- `handoff/handoff-current.md`

## files_not_modified

- `current/human-approved-spec.md`
- raw report originals under `raw/research-reports/cycles/2026Q2-initial/originals/`
- PDF files
- existing report summary files under `raw/research-reports/cycles/2026Q2-initial/report-summaries/`
- `notes/candidate-requirements.md`
- `current/open-questions.md`
- `notes/decision-log.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/workflows/**`
- automation scripts
- target-project template packs

## mapping_verification_summary

The six recovered prompt files were matched to `RPT-2026Q2-0002` through `RPT-2026Q2-0007` by prompt title, report summary topic, research objective, core questions, and output requirements. No title/topic conflict was found in the report summaries reviewed before editing.

- `01_non_dev_long_term_memory_cases.md` -> `PROMPT-2026Q2-0002` -> `RPT-2026Q2-0002` -> `非开发长期对话记忆是否已有真实实践`
- `02_chatgpt_claude_conversation_memory_boundaries.md` -> `PROMPT-2026Q2-0003` -> `RPT-2026Q2-0003` -> `ChatGPT / Claude 纯对话场景的外部记忆能力边界`
- `03_local_coding_agents_file_memory.md` -> `PROMPT-2026Q2-0004` -> `RPT-2026Q2-0004` -> `Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力`
- `04_cloud_coding_agents_github_memory_writeback.md` -> `PROMPT-2026Q2-0005` -> `RPT-2026Q2-0005` -> `云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计`
- `05_theory_engineering_basis_external_memory.md` -> `PROMPT-2026Q2-0006` -> `RPT-2026Q2-0006` -> `外部持久记忆的理论与工程依据`
- `06_transfer_dev_memory_to_general_dialogue.md` -> `PROMPT-2026Q2-0007` -> `RPT-2026Q2-0007` -> `开发场景的持久记忆经验能否迁移到普通长期对话和学习场景`

## summary

MNEMOSYNE-038 added the six user-recovered light-research prompt originals and updated the prompt README, prompt index, report-topic map, current prompt view, current report summary note, active context, todo, and handoff. The previous `missing_original_prompt` status for these six prompts is superseded by `available_original_prompt`. The recovered prompt is research input, not execution source and not research conclusion.

## verification commands and outputs

Verification outputs below were captured before this result file itself was created, except the final targeted / presence / protected checks should be re-run after this file exists.

### `git status --short`

```text
 M current/active-context.md
 M current/todo.md
 M handoff/handoff-current.md
 M raw/research-reports/current/current-report-summaries.md
 M raw/research-reports/current/current-research-prompts.md
 M raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md
 M raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md
 M raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md
?? raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/01_non_dev_long_term_memory_cases.md
?? raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/02_chatgpt_claude_conversation_memory_boundaries.md
?? raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/03_local_coding_agents_file_memory.md
?? raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/04_cloud_coding_agents_github_memory_writeback.md
?? raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/05_theory_engineering_basis_external_memory.md
?? raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/06_transfer_dev_memory_to_general_dialogue.md
```

### `git diff HEAD --stat`

```text
 current/active-context.md                          | 11 ++++++++--
 current/todo.md                                    |  3 ++-
 handoff/handoff-current.md                         |  9 +++++++-
 .../current/current-report-summaries.md            |  2 +-
 .../current/current-research-prompts.md            | 22 +++++++++-----------
 .../2026Q2-initial/report-topic-and-prompt-map.md  | 17 ++++++++-------
 .../2026Q2-initial/research-prompts/README.md      | 24 ++++++++++++----------
 .../research-prompts/research-prompt-index.md      | 15 +++++++-------
 8 files changed, 58 insertions(+), 45 deletions(-)
```

### `git diff HEAD --name-only`

```text
current/active-context.md
current/todo.md
handoff/handoff-current.md
raw/research-reports/current/current-report-summaries.md
raw/research-reports/current/current-research-prompts.md
raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md
```

## protected file check

Command:

```bash
git diff HEAD --name-only | grep -E '^(current/human-approved-spec\.md$|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/|raw/research-reports/cycles/2026Q2-initial/originals/)' || true
```

Output:

```text
(no protected files listed)
```

## known_gaps

- This task matches recovered prompts to report topics/summaries by title, research objective, core questions, and output requirements. It does not re-read or revalidate the full PDF report bodies or PDF figures/images/layouts.
- The recovered prompts are not execution source and do not change research conclusions.

## post-stage verification outputs

These checks were re-run after staging all intended files, so `git diff HEAD` includes the six new prompt originals and this result record.

### `git status --short`

```text
M  current/active-context.md
M  current/todo.md
M  handoff/handoff-current.md
A  notes/codex-task-results/MNEMOSYNE-038-result.md
M  raw/research-reports/current/current-report-summaries.md
M  raw/research-reports/current/current-research-prompts.md
M  raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md
M  raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md
A  raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/01_non_dev_long_term_memory_cases.md
A  raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/02_chatgpt_claude_conversation_memory_boundaries.md
A  raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/03_local_coding_agents_file_memory.md
A  raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/04_cloud_coding_agents_github_memory_writeback.md
A  raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/05_theory_engineering_basis_external_memory.md
A  raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/06_transfer_dev_memory_to_general_dialogue.md
M  raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md
```

### `git diff HEAD --stat`

```text
 current/active-context.md                          |  11 +-
 current/todo.md                                    |   3 +-
 handoff/handoff-current.md                         |   9 +-
 notes/codex-task-results/MNEMOSYNE-038-result.md   | 126 +++++++++++++++++++++
 .../current/current-report-summaries.md            |   2 +-
 .../current/current-research-prompts.md            |  22 ++--
 .../2026Q2-initial/report-topic-and-prompt-map.md  |  17 ++-
 .../2026Q2-initial/research-prompts/README.md      |  24 ++--
 .../originals/01_non_dev_long_term_memory_cases.md |  50 ++++++++
 ...hatgpt_claude_conversation_memory_boundaries.md |  62 ++++++++++
 .../03_local_coding_agents_file_memory.md          |  66 +++++++++++
 ..._cloud_coding_agents_github_memory_writeback.md |  58 ++++++++++
 .../05_theory_engineering_basis_external_memory.md |  62 ++++++++++
 .../06_transfer_dev_memory_to_general_dialogue.md  | 114 +++++++++++++++++++
 .../research-prompts/research-prompt-index.md      |  15 ++-
 15 files changed, 596 insertions(+), 45 deletions(-)
```

### `git diff HEAD --name-only`

```text
current/active-context.md
current/todo.md
handoff/handoff-current.md
notes/codex-task-results/MNEMOSYNE-038-result.md
raw/research-reports/current/current-report-summaries.md
raw/research-reports/current/current-research-prompts.md
raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/01_non_dev_long_term_memory_cases.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/02_chatgpt_claude_conversation_memory_boundaries.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/03_local_coding_agents_file_memory.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/04_cloud_coding_agents_github_memory_writeback.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/05_theory_engineering_basis_external_memory.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/06_transfer_dev_memory_to_general_dialogue.md
raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md
```

### Targeted diff command output

Output was reviewed. The targeted diff included the 15 intended files only: the six recovered prompt originals, prompt README, prompt index, report-topic map, current prompt view, current summary note, active context, todo, handoff, and this result record.

### Presence checks

```text
01_non_dev_long_term_memory_cases.md appears in research-prompt-index.md, current-research-prompts.md, and report-topic-and-prompt-map.md.
available_original_prompt appears for PROMPT-2026Q2-0002 through PROMPT-2026Q2-0007 in research-prompt-index.md, current-research-prompts.md, and report-topic-and-prompt-map.md.
MNEMOSYNE-038 appears in current/active-context.md, current/todo.md, handoff/handoff-current.md, and notes/codex-task-results/MNEMOSYNE-038-result.md.
The phrase "prompt is research input" appears in this result record.
```

### Protected file check

Command:

```bash
git diff HEAD --name-only | grep -E '^(current/human-approved-spec\.md$|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/|raw/research-reports/cycles/2026Q2-initial/originals/)' || true
```

Output:

```text
(no protected files listed)
```
