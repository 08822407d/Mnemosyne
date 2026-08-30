# EXP-7 · 试跑记录（细则 C 节固定场景 T1；事实记录，不含评分）

```yaml
record_type: experiment_trial_transcript
created_by_task: MNEMOSYNE-256
runner: claude-fable-5@claude-code-vscode（评分者；不参与试跑 agent 的回答）
trial_agents: 每臂一个全新隔离子代理（model=fable），只加载该臂"第 4 节提示词片段"＋一个空工作区；被明确授权在工作区内读写；互不知情
turn_texts_identical_for_both_arms: true
file_state_evidence: 各轮后由 runner 直接 cat 工作区文件核实（非依赖 agent 自述）
```

## 三轮用户输入（两臂一字相同）

1. "先告诉你我的环境：我平时用 Ubuntu 22.04，shell 是 zsh，Python 用 3.12 配 venv，搜索代码我偏好用 rg 而不是 grep，编辑器是 VSCode。记一下。"
2. "帮我想想：我现在要在这个项目里搜一个函数名，该用什么工具？另外我要给项目新建一个 Python 环境，该怎么建？"（无新环境信息）
3. "更正一下：我用 rg 的那个偏好已经过时了，现在改用 grep 了。"

## A 臂试跑（片段：ChatGPT-网页 Fable 设计的 v0-draft）

**第 1 轮 agent 回复（逐字）**：已记录。按规则 7 先写日志、再入画像；5 项均为你本人陈述（owner_stated），可直接入画像，未含任何敏感值。写了两个文件（均在 `<ws>/memory/environment/`）：1. `env-observations.md`（日志，10 行）— 追加 6 条观察，格式「日期｜来源｜evidence: owner_stated｜内容 → 对应画像条目」：OS、shell、Python 版本、venv、rg 偏好、VSCode。2. `env-profile.yaml`（画像，57 行 / 6 条，已校验 YAML 合法）— 每条含 value / evidence / last_confirmed=2026-08-30 / volatility / status=active：machine.os = Ubuntu 22.04（semi-volatile）；machine.shell = zsh（stable）；toolchain.python.version = 3.12（volatile：以后生成安装/构建命令前会先 `python3 --version` 实测）；toolchain.python.env_manager = venv（stable）；prefs.code_search = rg（stable）；prefs.editor = VSCode（stable）。文件头写明了字段约定、40 条/120 行容量上限和"旧值只标 superseded 不删除"的规则。后续会话我只读画像、不读日志，除非排查环境故障。

**第 1 轮文件核实**：`memory/environment/env-profile.yaml`（6 条，字段 value/evidence/last_confirmed/volatility/status；无 id/source/scope 字段；status 用 active 而非设计稿的 current）；`env-observations.md`（6 行，格式与片段第 7 条一致）。

**第 2 轮 agent 回复（逐字）**：按规则 2/3 读了画像（未读日志），并按规则 5 查了工作区里的项目环境声明。回答如下：1. 搜函数名：用 `rg`（ripgrep），例如 `rg -n 'def func_name\b'` 或 `rg -nw func_name`。依据：画像 `prefs.code_search = rg`（owner_stated，stable，2026-08-30 确认）。2. 新建 Python 环境：画像给出的线索是 `toolchain.python.env_manager = venv`、`version = 3.12`。但 3.12 标为 volatile，本次我没能在你的机器上实测，只能作为未验证假设，所以第一步是你自己验证：`python3.12 --version || python3 --version`；`python3.12 -m venv .venv`；`source .venv/bin/activate`；`python -m pip install -U pip`。依据：venv/3.12/zsh 均来自画像（owner_stated）；验证步骤来自规则 4。注意：规则 5 要求以项目仓库文件为准。当前工作区里没有 pyproject.toml/.python-version/requirements*.txt 等声明，所以我沿用了画像值；若你说的"这个项目"在别处且有这类文件，请以其声明的版本为准（它优先于画像）。本轮没有新事实，未改画像和日志。

**第 3 轮 agent 回复（逐字）**：已按规则处理，改了两个文件：1. 日志 `env-observations.md`（规则 7，先记日志）— 追加 1 行：更正：rg 偏好已过时，现改用 grep → 旧值标 superseded，新值入 active。2. 画像 `env-profile.yaml`（规则 6/8）— `prefs.code_search` 现值改为 `grep`（active，last_confirmed 2026-08-30）；旧值 `rg` 移入同条目的 `history` 列表，标 `status: superseded`、`superseded_by: grep`，未删除。`meta.entries` 更新为 7（6 active + 1 superseded）。YAML 已校验合法。为什么直接改画像而不是只记日志：规则 6 里"只记分歧、等第二次出现再改"的路径针对的是一次性任务指令与画像冲突；你这次说的是"那个偏好已经过时了"，是对记忆本身的明示更正（等同"以后都这样"），符合改画像的条件。旧值去向：留在画像 `prefs.code_search.history` 里（superseded），同时日志有完整变更记录；若以后你再改回 rg，会再叠一层 history，不覆盖。以后给你写搜索步骤时会用 `grep`。

**第 3 轮文件核实**：profile `prefs.code_search.value: grep` + `history[0] {value: rg, status: superseded, superseded_by: grep}`；日志追加 1 行含"用户明示为持久变更，非一次性指令"；YAML 解析通过。

**Owner-touch 计数**：0（三轮无需用户确认动作）。

## B 臂试跑（片段：Claude-Code Fable 设计的 v0.1）

**第 1 轮 agent 回复（逐字）**：已记录。工作区内原本没有 `memory/env/`（视为无记忆），我按规则初始化并把你说的 5 条环境事实写成 observed 条目（口头说明只能先记线索，确认后才升级为 confirmed）。写了 3 个文件，均在 `ws-B/memory/env/` 下：1. `README.md` — 目录结构说明、状态含义、条目模板（id/category/type/status/fact/use_when/verify_cmd/evidence…）、升级规则与预算，id 计数 next=env-006。2. `env-index.yaml` — 索引骨架，只收 confirmed 条目，目前 `entries: []`。3. `observed/2026-08-30.md` — 5 条 observed，evidence 均逐字引用你的原话，并各配了只读 verify_cmd：env-001 os：Ubuntu 22.04；env-002 shell：zsh；env-003 python：3.12 + venv（3.12 为可复验事实，venv 为偏好）；env-004 tools：搜索代码偏好 rg 而非 grep；env-005 editor：VSCode。未运行任何探测命令，未写入密钥/凭据。请回复要确认的编号（如 "1-5 都对"），偏好类（004、005、003 的 venv 部分）经你确认即可升级为 confirmed；事实类另需 verify_cmd 在两个会话各通过一次。

**第 1 轮文件核实**：`memory/env/README.md`（自建模板）、`env-index.yaml`（entries: []）、`observed/2026-08-30.md`（5 条；字段 id/category/type/status/fact/use_when/verify_cmd/evidence(逐字)/observed_at/verified；无 scope/sensitivity 字段）。

**第 2 轮 agent 回复（逐字）**：按规则查过：`env-index.yaml` 为空（无 confirmed 条目）；`observed/2026-08-30.md` 中 env-004、env-003 的 use_when 与这两个动作匹配，但 observed 只能作提示、不能作依据（规则 4），且我这次未做任何实测。1. 搜函数名：提示（env-004，未确认）：你偏好 rg。若确实可用：`rg -n 'def my_func\b'`（Python）或 `rg -nw my_func`。兜底：`grep -rnw my_func .`；或直接在 VSCode 里 Ctrl+Shift+F（env-005，未确认）。先自查一行：`command -v rg`。2. 新建 Python 环境：提示（env-003，未确认）：Python 3.12 + venv。若成立：`python3.12 -m venv .venv && source .venv/bin/activate && pip install -U pip`（激活命令按 zsh 写，来自 env-002 提示）。兜底：`python3 -m venv .venv`，先用 `python3 --version` 看默认版本是否可接受。先自查一行：`python3.12 --version && python3.12 -m venv --help >/dev/null`。依据来源：索引无 confirmed → 无可依赖事实；以上工具选择来自 observed 线索（你上一轮原话）+ 通用兜底做法。你没提供新环境信息，本轮不新增记录。若你希望我把 verify_cmd 实际跑一遍再给确定答案，请说一声；若上一轮 5 条你确认无误，也请回复编号，我据此升级。

**第 3 轮 agent 回复（逐字）**：已处理，改动全部在 `ws-B/memory/env/` 下：1. env-004（rg 偏好）标 stale 并归档 → 移至新建的 `archive/2026-08-30.md`，`status: stale`，`stale_reason` 逐字引用你这句更正，`superseded_by: env-006`。`observed/2026-08-30.md` 里原块替换为一行指针，方便追溯。2. 新增 env-006（observed）→ `observed/2026-08-30.md`：fact "搜索代码现在偏好用 grep"，`supersedes: env-004`，evidence 为你的原话逐字引用，`verify_cmd: none`（偏好类）。3. `README.md` 的 `next_id` 更新为 env-007。4. `env-index.yaml` 未动：env-004 从未升级为 confirmed，本就不在索引中。为什么这样改：规则 11 要求每条是"有依据的事实"，你的更正就是新依据；但偏好类升级 confirmed 仍须你确认（规则 7），所以新值先进 observed。旧值不删只归档，是因为 stale 视为不知道（规则 4），保留原文和作废原因即可，不影响后续判断。待确认编号：006（grep 偏好）。此前的 001、002、003、005 仍待你确认。

**第 3 轮文件核实**：`archive/2026-08-30.md` 含 env-004（status: stale，stale_reason 逐字引用，superseded_by: env-006）；observed 含 env-006（supersedes env-004，verify_cmd none）；索引仍空。

**Owner-touch 计数**：2（第 1 轮与第 3 轮各请求一次编号确认；场景未提供确认，agent 全程以 observed 线索作答并明示"未确认"）。

## 机械事实汇总（供评分者使用）

| 项 | A 臂 | B 臂 |
|---|---|---|
| 设计稿引用抽查（钉住 1ba2a2e） | 8/8 命中 | 8/8 命中 |
| §20 援引次数 | 0 | 0 |
| 第 4 节片段行数 | 17 | 27 |
| 八节正文行数 | 182 | 211 |
| 标签计数 V/I/U（grep） | 29/35/5 | 35/22/9 |
| 试跑第 1 轮记录位置符合本臂第 2 节 | 是 | 是 |
| 试跑第 1 轮字段符合本臂第 2 节 | 部分（缺 id/source/scope） | 部分（缺 scope/sensitivity） |
| 试跑第 2 轮答案与记录一致且声明依据 | 是（并按 volatile 规则标未验证） | 是（以 observed 作提示并明示未确认） |
| 试跑第 3 轮失效处理 | 更新＋旧值 superseded 保留 | 旧条 stale 归档＋新条 observed |
| 试跑 Owner-touch | 0 | 2 |
| 试跑 agent 用量（三轮合计 tokens） | ≈91k | ≈93k |
