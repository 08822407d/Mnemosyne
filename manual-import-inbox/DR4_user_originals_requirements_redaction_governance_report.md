# DR4 — 用户原始构想、需求原文、整理版、用户决策、脱敏版与外部指针的治理模式研究

## 执行摘要

对 Mnemosyne 的 v0.1 来说，最稳妥、最可执行、也最符合 requirements engineering、privacy engineering 与 Git 风险现实的结论是：**用户原始构想与原始需求默认不进入 Git 仓库；仓库中只放经过审批的决策、经过验证的脱敏材料、以及指向外部受控存储的 provenance 指针与治理元数据。** 原因并不抽象：requirements engineering 本来就区分 stakeholder needs、derived/system requirements、approval baseline 与 change control；privacy engineering 要求 inventory、mapping、data minimization、disassociability 与 documented review；而 Git/GitHub 的官方文档明确表明，一旦敏感内容进入历史，后续清除是高协调成本、高副作用、且不能保证彻底的，特别是在已有 clone、fork、PR 引用和可见性切换的情况下。citeturn8view5turn8view4turn8view6turn12view2turn12view3turn11view0turn9view1turn9view3turn10view2

这意味着 Mnemosyne 不应把 AI restatement 当作 original requirement，也不应把 private repo 误判成“可安全存原文”的同义词。根据 SEBoK，对 stakeholder needs 的记录、requirements 的转化、baseline 的批准与 change control 是不同工件；根据 NIST AI RMF，文档化的作用是提升 transparency、human review 和 accountability，而不是让模型输出自动升级为 authoritative source；根据 ICO 与 HHS，脱敏/去标识化不是“删几个词”这么简单，而是要有方法说明、风控假设、可识别性测试与持续复核。citeturn8view5turn8view4turn8view6turn16view0turn12view4turn15view3turn14view0turn8view14

因此，本报告建议 Mnemosyne 采用五层治理：**原始证据层、解释层、决策层、披露层、指针与谱系层**。其中只有“用户批准后的决策层”可成为项目执行的正式依据；“原始证据层”只在 provenance 争议、审计、回访时具有证据权威，但不直接充当执行 baseline；“AI restatement”只是解释工件，必须被追溯并被显式批准后，才能派生出 authoritative decision。citeturn8view6turn16view0turn8view7turn12view5turn13view0

在仓库可见性上，v0.1 最小可行政策应采用**visibility pessimism**：凡是仓库可见性未验证、可能变化、未来可能开源、或需要与外部协作者切换访问模式的项目，一律按“可能公开”的最坏情形处理。GitHub 官方说明表明，从 private 变 public 后，代码、Actions 日志都会对所有人可见，任何人都可 fork；从 public 变 private 后，现有 public forks 不会自动变私有；即便重写历史，旧 clone、fork、PR references 与 cached views 仍可能保留敏感内容。citeturn10view2turn9view6turn9view1turn9view2turn9view5

## 直接回答与核心判断

### Mnemosyne 应把什么放在仓库里

直接回答研究问题一与四：**raw user input、requirements originals、敏感原文、会议原录、用户私密材料，默认不存入 Git；AI restatements 只可在 private 且 visibility 已验证稳定的仓库中作为草稿存在；真正应进入仓库并承担执行权威的，是“用户已批准的 decision record / approved requirement baseline”；面向更广共享场景的，只能是 redacted excerpts、synthetic substitutes，以及不会泄露敏感位置与访问路径的 external pointers。** 这个分离方式同时满足 requirements traceability、privacy minimization 与 Git exposure containment。citeturn8view4turn8view6turn12view2turn11view0turn11view1turn9view1turn10view2

如果只说一句政策化结论，那就是：**原件在受控外部系统，决策在仓库，脱敏版在可共享层，指针和谱系在治理层。** NIST Privacy Framework 要求对系统、数据动作、目的、数据元素、处理环境以及 owner/operator 进行 inventory 与 mapping；这正好支持把“内容本体”和“说明其来源、位置、责任与用途的元数据”分开管理。citeturn12view2

### 为什么不能把 originals 当作普通文档塞进 Git

requirements engineering 的基本出发点不是“谁先说出来谁就是 baseline”，而是把 stakeholder needs 作为输入，再经过定义、验证、追踪与基线化，形成后续设计与执行使用的 requirements 与 approved baselines。SEBoK 明确区分 stakeholder needs、system requirements、requirements management、validation/verification 与 configuration baselines；这说明“原始说法”“整理说法”“批准后的执行要求”本来就不应混成一个文件夹里权威相同的文本集合。citeturn8view5turn8view4turn8view6turn8view7turn8view8turn16view0

与此同时，Git 的问题不只是“误提交”而是“历史可追溯且难彻底消除”。GitHub 官方文档说明，敏感数据进入仓库后，即便重写历史并 force-push，内容仍可能存在于 clones、forks、通过 SHA-1 直接访问的 cached views，以及引用该提交的 pull requests 中；历史重写还会带来 changed commit hashes、签名失效、PR diff 破坏、以及 recontamination 风险。`.gitignore` 也无济于事，因为它只影响未跟踪文件，已经被跟踪的文件不受影响。citeturn8view0turn9view1turn9view2turn9view3turn9view5turn8view3

### private repo 也不等于安全区

“private repo 就可以存 originals”这个前提，在治理上不成立。GitHub 官方文档明确写到：从 private 切到 public 后，代码、push activity、Actions history 与 logs 都会对所有访问 GitHub.com 的人可见，且任何人都可以 fork；反过来，从 public 切回 private 时，现有 public forks 仍保持 public，不会自动跟着变私有。换言之，只要项目存在 visibility switch 的现实可能，就不能把“当前 private”视为对未来暴露风险的充分控制。citeturn10view2turn9view6

因此，对 Mnemosyne v0.1，**“visibility unverified = treat as public-risk”** 应成为默认规则，而不是例外规则。这不是法律口号，而是被 Git 的历史模型和平台 fork 机制直接逼出来的工程结论。citeturn9view1turn9view6turn10view2

## 分层模型与权威模型

### 建议的层模型

建议 Mnemosyne 采用如下五层模型：

**原始证据层**保存用户真的说过、发过、上传过、批准保留的原始材料，但该层默认放在仓库外的 access-controlled system 中，只在 repo 中留下 pointer、classification、retention、owner、approval 与 provenance 说明。这样做符合 NIST Privacy Framework 的 inventory/mapping 思路，也符合 data minimization 与 storage limitation：保留“知道它存在、知道谁负责、知道为什么留着”的信息，但不把敏感本体无差别复制进 Git。citeturn12view2turn11view0turn11view1

**解释层**保存 human restatement、AI restatement、requirement extraction notes、open questions 等派生工件。它可帮助项目工作，但不拥有原始权威。SEBoK 把 stakeholder needs 视为输入，把 system requirements 视为经过转化和追踪的 design input；NIST AI RMF 则强调 documentation 用于 human review 与 accountability。这两者叠加的含义就是：解释工件应被保留和追溯，但它们本身不能冒充原文或自动升级为批准后的 baseline。citeturn8view5turn8view4turn12view5

**决策层**保存 user-approved decisions、approved requirement baselines、accepted assumptions、change approvals。这个层才是项目执行的 authoritative source。SEBoK 对 baselining 和 configuration baseline 的定义都强调“formally approved snapshot”以及后续变更控制；因此，Mnemosyne 应把“正式执行依据”绑定到批准后的 decision artifact，而不是绑定到聊天原文或 AI 改写文本。citeturn8view6turn16view0

**披露层**保存 redacted excerpts、synthetic substitutes、public summaries、limited-access disclosure variants。这个层的目标不是“还原全部真实”，而是“在满足共享目的的前提下，尽量降低识别性和泄露面”。ICO 明确区分 anonymisation 与 pseudonymisation，并强调 motivated intruder test；NIST Privacy Framework 也把 disassociability、de-identification、tokenization 与 selective disclosure 列为核心实践。citeturn8view13turn8view14turn12view3

**指针与谱系层**保存 external pointers、source maps、authority notes、redaction manifests、approval manifests。这个层不替代内容，但负责说明“内容在哪里、谁负责、谁批准、从哪里派生、允许怎么用”。NIST SSDF 要求保护 provenance data 的完整性并使其可验证；GenAI Profile 也强调 content provenance、origin tracing、human review 与 lineage tracking。citeturn8view9turn13view0

### 建议的权威模型

Mnemosyne 应把“权威”拆成五类，而不是只有“存了/没存”两种状态。

原始证据层的权威是**evidentiary authority**。它回答“用户当时到底说了什么/交了什么”，因此在争议解决和回溯中权重最高；但它不是日常执行的 baseline，因为原话可能含糊、变化中、未确认、带情绪化表述或互相矛盾。SEBoK 对 stakeholder needs 的定位正是“输入与来源”，而不是自动成为 technical baseline。citeturn8view5turn8view4

解释层的权威是**interpretive authority**，也就是“说明团队或模型如何理解原始输入”。它必须可追溯，但不具备独立执行权威。换句话说，AI restatement 能帮助梳理，却不能代替 original，也不能代替 approval。NIST AI RMF 对 documentation、human review 与 accountability 的强调，支持这种“可留痕、不可自动执法”的定位。citeturn12view5turn13view0

决策层的权威是**operative authority**。一旦某个 decision record 被用户批准，它就成为项目执行、评审、变更与交付的直接依据，后续所有 restatement 都必须向它追踪，而不是反过来让它追踪模型文字。SEBoK 的 requirements baseline、validation matrix 和 configuration baseline 都支持这种机制。citeturn8view6turn8view7turn16view0

披露层的权威是**disclosure authority**。它只回答“什么可以被谁看到”，不回答“原件完整内容是什么”。也就是说，redacted excerpt 与 synthetic substitute 对共享行为有效，但对原始事实并不拥有替代性真值。ICO 和 HHS 都强调 residual risk、anticipated recipient 与可识别性评估，这说明披露层的充分性必须按接收者和场景而定。citeturn8view14turn14view0turn14view3

指针与谱系层的权威是**provenance authority**。它管理 lineage、ownership、location、retention、access status、approval chain 与 method history。它不承载业务本体，却决定系统能否回答“这份内容从哪里来、谁同意了、脱敏是否复核、外部原件是否仍可访问”。citeturn12view2turn8view9turn13view0

### 存储决策矩阵

下表是基于 requirements 基线化、data minimization、storage limitation、anonymisation governance 以及 Git 历史暴露后果综合形成的 **Mnemosyne v0.1 recommendation matrix**。它是建议矩阵，不是外部标准原文。citeturn8view6turn16view0turn11view0turn11view1turn15view3turn9view1turn10view2

| item | store_in_repo_public | store_in_repo_private | store_if_visibility_unverified | authority_level | redaction_required | approval_required | preferred_path |
|---|---|---|---|---|---|---|---|
| original user idea | 否 | 否 | 否 | 原始证据权威 | 如需任何共享则必须先脱敏 | 保留需显式同意 | `outside-git` + `01-user-input/originals/<id>.pointer.yaml` |
| raw requirement | 否 | 原则上否 | 否 | 原始证据权威 | 摘录入 repo 前必须脱敏 | 是 | `outside-git` + `01-user-input/originals/<id>.pointer.yaml` |
| AI restatement | 否 | 是，限 draft | 否 | 解释权威，非原文、非基线 | 若源自敏感内容则是 | 用于执行前必须批准 | `01-user-input/restatements/<id>.md` + meta |
| user-approved decision | 仅在内容已披露安全时可 | 是 | 仅可存脱敏版 | 执行权威 | 若进入 public / unverified 则必须 | 是，且需可追溯 | `01-user-input/decisions/<id>.md` |
| redacted excerpt | 是，前提是已验证 | 是 | 是，按保守规则 | 披露权威 | 已内含 | 是 | `01-user-input/redactions/<id>.md` |
| synthetic substitute | 是，前提是不可逆回推 | 是 | 是 | 披露/分析代理权威 | 需做再识别风险评估 | 是 | `01-user-input/redactions/<id>.synthetic.md` |
| external pointer | 仅可存不暴露敏感位置的粗粒度版本 | 是 | 是，需最小化 | 谱系权威 | 常常需要 | 视敏感度与所有权而定，v0.1 建议是 | `01-user-input/pointers/<id>.pointer.yaml` |
| source map | 否 | 是 | 否 | 审计与谱系权威 | 对外共享前需重写 | 是 | `01-user-input/governance/source-maps/<id>.yaml` |
| authority note | 是，若不含敏感引用 | 是 | 是 | 治理权威 | 如出现敏感上下文则是 | 进入 public 时建议审批 | `01-user-input/governance/authority-notes/<id>.md` |

## 按仓库可见性划分的存储政策

### public、private、unverified、changing visibility 的处理规则

**Public repo** 的规则应最简单：不允许 originals、不允许 raw requirements、不允许 source maps、不允许含敏感定位信息的 external pointers；只允许经过验证的 redacted excerpt、synthetic substitute、generic authority note，以及在内容本身已披露安全的前提下的 approved decision summary。因为一旦仓库是 public，代码与日志都可能被所有人看到，也允许被 fork。citeturn10view2

**Verified private repo** 也不应成为原文仓库。v0.1 更稳妥的政策是：private repo 可以存 draft restatements、approved decisions、redacted artifacts 和 governance metadata，但 originals 与 raw requirements 仍默认留在 Git 外部的受控存储。这样做的原因不是 private repo 毫无安全价值，而是为了避免后续 visibility switch、clone 扩散、历史重写与误提交后的不可逆后果。citeturn10view2turn9view1turn9view5

**Visibility unverified** 或 **visibility may change** 的项目，应按 public-risk 处理。Mnemosyne 若在 v0.1 就允许“先放 private，以后再说”，那实际上等于把未来治理债务预埋到 Git 历史里。GitHub 对 visibility change 的说明已经足够说明风险：从 private 变 public 时，可见面立即扩大；从 public 变 private 时，历史 public forks 依旧存在。citeturn10view2turn9view6

**Changing visibility** 的项目还应被视作高风险治理场景。这里的正确做法不是加强 `.gitignore`，因为 `.gitignore` 对已跟踪文件无效；也不是寄希望于事后 cleanup，因为 GitHub 官方明确说明 cleanup 需要改写历史、协调 clones/forks，并伴随 commit hash、diff、signature 和 recontamination 问题。citeturn8view3turn9view1turn9view3

### 推荐路径政策

Mnemosyne 可以保留用户给出的基本目录框架，但应把它改造成“**content-light repo, provenance-heavy governance**”的结构。推荐如下：citeturn12view2turn8view9turn15view3

```text
target-projects/<target_project_id>/01-user-input/
  originals/
    README.md
    pointers/
      src-*.pointer.yaml
  restatements/
    rst-*.md
    rst-*.meta.yaml
  decisions/
    dec-*.md
    dec-*.approval.yaml
  redactions/
    red-*.md
    red-*.manifest.yaml
    syn-*.md
  governance/
    source-maps/
      map-*.yaml
    authority-notes/
      auth-*.md
    visibility-status.yaml
```

其中最关键的一条是：**`originals/` 在 repo 中只放 pointer 与说明，不放 raw content 本体。** 如果某个项目后来被证明完全不含敏感信息，也不应在 v0.1 里破例把 originals 回填到 Git；这类例外应推迟到 v0.2，在完成 classification、retention、visibility policy 和 removal playbook 之后再讨论。这个保守设计更符合 data minimization 与 storage limitation，也更容易向用户解释。citeturn11view0turn11view1turn15view3

### 外部指针政策

external pointer 的本质不是“链接”而是“**受控引用**”。它至少要记录 source_id、location_type、location_description、owner、access_status、authority_level、sensitivity、allowed_use 和 not_stored_in_repo_reason，这些字段与 NIST Privacy Framework 的 owners/operators、processing environment、purposes、data elements mapping，以及 provenance integrity 的要求是对齐的。citeturn12view2turn8view9turn13view0

对 Mnemosyne 来说，pointer 应遵守三个规则。第一，**pointer 不得泄露比内容摘要更多的敏感信息**；例如不要在 public repo 中写出客户内部盘符、私有 bucket 名称、未公开产品代号或账户路径。第二，**pointer 必须说明“为什么不存 Git”**，让未来维护者知道这不是遗漏，而是治理决策。第三，**pointer 必须说明 allowed_use**，避免下游把“只可核对来源”的指针当作“可自由抓取原文”的许可。citeturn12view2turn15view3

基于上述原则，建议采用如下 schema：citeturn12view2turn8view9turn13view0

```yaml
external_source_pointer:
  source_id:
  location_type:
  location_description:
  owner:
  access_status:
  authority_level:
  sensitivity:
  allowed_use:
  not_stored_in_repo_reason:
```

## 脱敏、合成替代与 Git 历史暴露

### 脱敏与 synthetic substitute 的政策

Mnemosyne 不应把 redaction 理解为“简单打码”，而应把它视为一个**有方法、有审查、有残余风险判断的治理过程**。ICO 强调 anonymisation governance、responsibility、identification testing、training 和 documented rationale；HHS 在 Expert Determination 模式下要求记录方法与分析结果，并评估 anticipated recipient 结合其他合理可得信息后的识别风险。citeturn15view0turn15view1turn15view3turn14view0

这直接支持两条操作规则。第一，**redacted excerpt 与 synthetic substitute 必须分开**。前者仍是原文的删节版，后者是重新表述、抽象化、替换具体上下文后的代理文本；两者风险不同，权威也不同。第二，**pseudonymisation 不能被误判为 anonymisation**。ICO 明确指出，pseudonymised data 在持有附加信息的人手里仍是 personal data；因此，把姓名换成项目代号、把客户名换成缩写，并不自动让文本适合进入 public repo。citeturn8view13turn11view3turn8view14

对 v0.1，建议把 redaction verification 做成显式步骤，而不是“作者自行判断”。最少应有：确定接收者场景、枚举去除类别、记录方法、二次复核、残余风险说明，以及必要时进行 motivated intruder style 检查。美国联邦法院关于 redaction 的实践也提醒，源文件中可能存在隐藏数据与元数据，因此“另存为可共享版本”往往比在原文件上黑框遮盖更安全。citeturn8view14turn15view3turn8view17

### 红action manifest schema

下列 schema 是根据 ICO 对责任、文档化、培训与 identifiability testing 的要求，以及 HHS 对方法与结果记录的要求综合形成的建议。citeturn15view3turn15view0turn14view0

```yaml
redaction_manifest:
  source_item_id:
  original_storage_status:
  redacted_file_path:
  redaction_method:
  removed_categories:
  reviewer:
  approved_by_user:
  residual_risk:
```

在实际执行时，建议 `removed_categories` 至少支持：direct identifiers、quasi-identifiers、confidential business context、private contact details、internal system names、security-sensitive paths、timeline markers、free-text narrative clues。`residual_risk` 不应用“安全/不安全”二元值，而应用简短叙述，例如：`low for public excerpt; residual linkage risk if combined with internal meeting notes`. 这更接近 HHS 的 anticipated recipient 风险思路，也更符合 ICO 对 identifiability as context-dependent 的理解。citeturn14view0turn8view14

### Git 历史暴露分析

Mnemosyne 的存储政策必须把 **Git history exposure** 当作一等约束，而不是附录风险。GitHub 官方文档给出的现实情况非常明确：历史改写会改变 commit hashes，破坏依赖哈希稳定性的工具链，导致 PR diff 与评论失效，移除签名；更重要的是，旧 clone、fork、PR references 和 cached views 会继续保留敏感数据，且合作者一个不当 merge/push 就可能把内容重新带回仓库。citeturn9view1turn9view2turn9view3turn9view5

这带来两个直接政策后果。第一，**“以后删掉就行”不能构成允许 originals 进 Git 的理由。** 第二，**secret prevention 比 post-hoc cleanup 更重要。** GitHub 的 push protection 明确是为了阻止 hardcoded secrets 在到达仓库前就被拦截；对 Mnemosyne 来说，原始敏感用户材料虽然不一定是 credential，但治理哲学相同：最好的泄漏修复是不要把它提交进去。citeturn8view2turn8view0

因此，Mnemosyne 的 v0.1 应把“原件外置、repo 只留 pointer 和 approved artifacts”视为 **history-safe default**。这条规则的价值不在于它完美，而在于它把最难补救的风险——Git 历史污染——提前规避掉。citeturn9view1turn9view3

## 用户审批工作流与候选 v0.1 政策

### 用户审批工作流

AI-generated restatement 与 user-approved decision 之间，必须通过一个显式审批关口，而不是通过文件名或目录位置暗示“已经被认可”。NIST AI RMF 与 GenAI Profile 都强调 documentation、human review、content provenance、audit against guidelines 以及 additional oversight；SEBoK 则强调 baselining、validation traceability 与 approved snapshot。将这几类证据合并起来，Mnemosyne 最合理的流程是：**采集原始输入 → 生成人工/AI 整理版 → 标出不确定项 → 用户确认或修订 → 生成 decision record → decision record 成为执行权威 → 后续变更通过 change note 追加。** citeturn12view4turn13view0turn8view6turn8view7turn16view0

这个流程里至少要有四个 ID：`source_item_id`、`restatement_id`、`decision_id`、`redaction_id`。其中 `restatement_id` 必须回指 `source_item_id`，`decision_id` 必须指明其基于哪个 `restatement_id` 与哪些 `source_item_id`，但**不得把 restatement 标记为 original**。如果用户拒绝某个 restatement，那么它应被保留为 rejected interpretive artifact，而不是静默删除；这对 accountability 与 future dispute resolution 都更好。citeturn8view4turn12view5turn13view0

### 候选 Mnemosyne v0.1 政策

下面给出一个可直接采用的 v0.1 policy 文本骨架。它是本报告的推荐，不是从外部文档直接摘录。citeturn8view6turn11view0turn9view1turn10view2

**Policy statement**：Mnemosyne 在 target-project workspace 中，默认不将用户原始构想、原始需求、原始上传材料或其他敏感 originals 存入 Git 仓库；仓库只保存经过批准的 decision artifacts、经验证的 redacted/synthetic artifacts，以及用于 provenance、retention、authority 和 location 管理的 pointer/manifests。

**Authority rule**：用户原始输入具有证据权威但不构成执行 baseline；AI 或人工整理版具有解释权威但不构成原文或 baseline；只有被用户批准的 decision record 具有执行权威；redacted/synthetic artifacts 只具有披露权威；source maps 与 authority notes 只具有谱系/治理权威。citeturn8view5turn8view6turn16view0turn12view5

**Visibility rule**：public repo 仅允许 disclosure-safe artifacts；private repo 也不默认允许 originals；visibility unverified 或可能变化时按 public-risk 处理；任何计划未来 public/open-source 的项目，从第一天开始就按“不在 Git 中存 originals”执行。citeturn10view2turn9view6

**Redaction rule**：所有 redacted artifact 必须附 redaction manifest；所有 synthetic substitute 必须标记为 synthetic，不得伪装成原文摘录；pseudonymised content 不自动视为 anonymous；必要时进行识别性复核。citeturn8view13turn8view14turn15view3turn14view0

**History rule**：如果敏感内容误入 Git 历史，应立即停止扩散、评估是否属于 sensitive exposure、按平台指导协调 history rewrite 与 clone cleanup，但该补救流程不改变“v0.1 禁止 originals 入 Git”的默认规则。citeturn8view0turn9view1turn9view5

**Execution-source rule**：本研究报告、AI restatement、讨论草稿与 redaction manifest 都不是 Mnemosyne execution source；execution source 只能是被明确标识为 approved 的 decision artifact。这个做法与 SEBoK 的 baseline/approval 思路一致，也降低“模型整理稿悄悄变标准文本”的风险。citeturn8view6turn16view0

### Candidate updates for Mnemosyne

下面把建议拆成题目要求的五类。citeturn8view6turn15view3turn9view1turn10view2

```yaml
execution_source_candidate:
  - 仅 user-approved decision record 可作为 target-project 执行依据
  - AI restatement、research report、chat transcript、raw originals 均不得自动成为执行依据

manifest_template_candidate:
  - source pointer manifest
  - redaction manifest
  - approval manifest
  - authority note
  - visibility status manifest

target_workspace_policy_candidate:
  - repo 内 originals 目录只存 pointer，不存原文
  - restatements 仅限 private verified repo，且强制标注 non-authoritative
  - decisions 目录保存 approved baseline
  - redactions 目录保存 disclosure-safe outputs
  - governance 目录保存 source maps / authority notes / visibility status

open_question:
  - 外部受控存储选型是什么
  - 是否需要 per-project retention schedule
  - 是否引入 cryptographic checksum 及其粒度
  - synthetic substitute 的可接受相似度阈值如何定义

defer_to_v0.2:
  - 自动分类与自动 pointer 生成
  - 自动 redaction suggestion
  - secure vault integration
  - signed approvals
  - policy-as-code checks in CI
```

### Future v0.2 improvements

v0.2 可以在不改变 v0.1 保守原则的前提下增强自动化。最值得做的不是“自动吞原文”，而是**自动生成 provenance stub、自动检测含敏感上下文的提交、自动验证 decision 是否回链到 source 和 approval、以及对 public-facing artifacts 做 release gate**。NIST SSDF 对 provenance integrity 与更新，NIST GenAI Profile 对 lineage、audit 和 human review 的强调，都支持这种“先把治理自动化，再讨论内容自动化”的路线。citeturn8view9turn13view0

此外，v0.2 还可以把 visibility policy 写成 machine-readable control。例如：若 `visibility-status.yaml != verified-private-stable`，CI 自动阻止 `restatements/` 与 `decisions/` 中未脱敏内容进入默认分支；若 `redaction_manifest.approved_by_user != true`，则禁止产出 public package。这样能把 policy 从“文档”提升到“执行约束”。citeturn15view3turn8view9

## 证据表与不确定性

### 证据表

下表把本报告中最关键的判断与主要依据对应起来。citeturn8view5turn8view6turn16view0turn11view0turn11view1turn9view1turn10view2

| 关键判断 | 主要证据 |
|---|---|
| stakeholder needs、derived requirements、approved baselines 应分离 | SEBoK 对 Stakeholder Needs Definition、System Requirements Definition、Requirements Management、Configuration Baselines 的区分与基线化说明。citeturn8view5turn8view4turn8view6turn16view0 |
| 只有批准后的 decision artifacts 应成为执行依据 | SEBoK 对 baselining、validation traceability、formally approved snapshot 的定义。citeturn8view6turn8view7turn16view0 |
| data inventory、owner/operator、processing environment、purposes 与 data elements 应被单独记录 | NIST Privacy Framework 的 ID.IM-P1–P8。citeturn12view2 |
| 数据最小化、删除与存续期管理应成为默认原则 | ICO 对 data minimisation、storage limitation 与 accountability 的说明。citeturn11view0turn11view1turn11view2 |
| pseudonymisation 不能等同 anonymisation | ICO 明确指出 pseudonymised data 仍可能是 personal data；identifiability 需用 motivated intruder test 评估。citeturn8view13turn8view14 |
| redaction 需要方法、责任、文档化与复核 | ICO 的 anonymisation governance 指南；HHS 的 Expert Determination 要求记录方法和分析结果。citeturn15view3turn15view0turn14view0 |
| AI restatement 不应自动成为 authoritative original | NIST AI RMF 与 GenAI Profile 强调 documentation、human review、content provenance、audit 和额外 oversight。citeturn12view5turn13view0 |
| Git 历史暴露使 originals 不适合进入 repo | GitHub 官方说明：cleanup 需要改写历史，且 clones、forks、cached views、PR references 可保留旧内容；commit hashes 会改变并产生 recontamination 风险。citeturn8view0turn9view1turn9view2turn9view3turn9view5 |
| `.gitignore` 不能修复已提交内容 | Git 官方文档：已被跟踪的文件不受 `.gitignore` 影响。citeturn8view3 |
| 仓库可见性变化会放大共享面，且 public forks 不会因为转 private 而自动变私有 | GitHub 官方 visibility 文档。citeturn9view6turn10view2 |

### 已知不确定性与限制

本报告在 Git 平台风险部分主要引用了 GitHub 官方文档，因为它公开、具体且工程上最具代表性；如果 Mnemosyne 使用的是 GitLab、自建 forge 或完全不同的 versioned content system，某些平台级细节会不同，但“Git history 难以彻底清除敏感内容”“public/private switch 会带来额外暴露面”“原件不宜进版本历史”这些核心结论仍然成立。相关平台差异应在 v0.2 的 implementation note 中单独补充。citeturn8view0turn10view2turn9view6

第二，本报告主要使用 requirements engineering、privacy governance、Git security、AI documentation/provenance 指南来构造 v0.1 policy；它不是法律意见，也没有针对特定司法辖区、特定合同框架、医疗/金融/政府等强监管行业做专门合规分析。如果 Mnemosyne 的目标项目进入受监管领域，应在本政策之上再叠加行业-specific controls。citeturn11view2turn14view0

第三，报告刻意采用了保守默认值：**不把 originals 放进 Git，即使当前 repo 是 private。** 这会牺牲一部分便利性，但考虑到 Mnemosyne 还处于第一次真实 dry-run 前，且用户明确要求不要忽视 Git 历史暴露与可见性切换风险，这个保守默认比“先方便、后治理”更符合 v0.1 的目标。citeturn9view1turn10view2