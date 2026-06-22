# MNEMOSYNE-031 D-01–D-07 Execution-Source Coverage Map

## file_positioning

- This is a non-execution-source review/proposal artifact.
- It maps final MNEMOSYNE-031 D-01 through D-07 user-confirmed checkpoint decisions to the current execution source.
- It does not approve promotion into `current/human-approved-spec.md`.
- It does not modify, replace, or reinterpret the final D-01–D-07 checkpoint record.
- Current execution source remains `current/human-approved-spec.md`.
- Only content already reflected in `current/human-approved-spec.md` is currently executable.
- Any unreflected candidate wording below requires separate user approval before promotion.

## source_files_compared

- checkpoint source: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`
- execution source compared: `current/human-approved-spec.md`

## allowed_coverage_status_values

- `already_reflected`
- `partially_reflected`
- `not_reflected`
- `intentionally_non_executable`
- `checkpoint_only`
- `unclear_requires_user_review`

## coverage_map

### D-01

- decision_id: D-01
- decision_title: Confirm core definition
- user_confirmed_checkpoint_status: accepted; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-01`)
- current_spec_sections:
  - `current/human-approved-spec.md` section 1, `Mnemosyne 的定位`
  - `current/human-approved-spec.md` section 9, `交付包原则`
  - `current/human-approved-spec.md` section 10, `当前 v0.1 边界`
- coverage_status: partially_reflected
- coverage_explanation: The spec already says Mnemosyne is a memory-system meta-agent work repository for designing external durable memory systems for other projects and not an ordinary memory repository for one concrete project. It also says target-project repositories/directories are the runtime truth source and that current Codex Cloud use is mainly remote file-writing/version-saving assistance. The spec does not explicitly carry the checkpoint wording that Mnemosyne is not a direct project implementation Agent, not a coding Agent, and not a replacement for Codex / Claude Code / Cursor.
- operational_risk_if_left_ambiguous: Future tasks may incorrectly ask Mnemosyne itself to act as the implementation/coding executor for target projects, blurring the boundary between memory-system design/review and actual project coding tools.
- recommended_disposition: Promote the missing negative-boundary wording into section 1 or section 10 only after separate user approval.
- candidate_exact_spec_wording_if_promotion_is_recommended:
  - proposed_insertion_section: `current/human-approved-spec.md` section 1, after the existing positioning bullets.
  - wording: `- Mnemosyne 不是直接项目实施 Agent、不是 coding Agent，也不是 Codex / Claude Code / Cursor 等项目执行工具的替代品；它的职责是设计、维护、复核和演化外部持久记忆系统。`
- needs_new_user_approval: yes

### D-02

- decision_id: D-02
- decision_title: Confirm storage principle
- user_confirmed_checkpoint_status: accepted; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-02`)
- current_spec_sections:
  - `current/human-approved-spec.md` section 2, `外部记忆架构`
  - `current/human-approved-spec.md` section 8, `模型迁移原则`
  - `current/human-approved-spec.md` section 9, `交付包原则`
- coverage_status: already_reflected
- coverage_explanation: The spec directly states that models compute and files remember; models are replaceable computation units, not long-term truth sources; external files/Git repositories are the long-term memory and audit basis; model internal memory is cache or auxiliary context. Section 8 also reflects model migration and raw/source fallback. Section 9 reflects that target-project repositories/directories are the target-project runtime truth source. The checkpoint phrase that Markdown/GitHub is the current practical default but not a permanent storage limitation is not stated verbatim, but the spec already uses broad `external files / Git repositories` wording rather than making Markdown/GitHub a permanent limit.
- operational_risk_if_left_ambiguous: Low. The durable external-state principle is already executable. The only minor risk is over-reading current Markdown/GitHub practice as the only possible future storage substrate.
- recommended_disposition: No immediate promotion needed. If later storage-substrate evolution becomes important, add a separate candidate requirement.
- candidate_exact_spec_wording_if_promotion_is_recommended: none
- needs_new_user_approval: no

### D-03

- decision_id: D-03
- decision_title: Confirm execution-source boundary, with handoff revision
- user_confirmed_checkpoint_status: accepted_with_wording_revision; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-03`)
- current_spec_sections:
  - `current/human-approved-spec.md` section 4, `执行源原则`
  - `current/human-approved-spec.md` section 6, `需求进入原则`
  - `current/human-approved-spec.md` section 6.1, `self-improvement workflow 高层原则`
  - `current/human-approved-spec.md` section 7, `handoff / active-context 原则`
- coverage_status: partially_reflected
- coverage_explanation: The global execution-source hierarchy is already reflected: the spec is the execution source; raw records, research reports, candidate requirements, decision records, active context, and handoff are not execution source; user confirmation is required before spec updates. The task-local handoff exception lifecycle is not reflected: the spec does not state that handoff can provide strong task-local continuation guidance, nor does it define required fields for temporary exceptions such as reason, scope, continuation context, and expected recovery/expiration condition.
- operational_risk_if_left_ambiguous: Future agents may either ignore useful task-local handoff context during recovery or over-promote handoff text into permanent project law without explicit scope and expiry.
- recommended_disposition: Promote a narrowly scoped handoff-local exception rule into section 7 only after separate user approval.
- candidate_exact_spec_wording_if_promotion_is_recommended:
  - proposed_insertion_section: `current/human-approved-spec.md` section 7, after the existing handoff/active-context bullets.
  - wording: `- 在任务恢复 / 任务交接场景中，handoff 可以作为当前任务的局部 continuation context，为正确恢复当前任务提供强操作指导；但它仍不是全局 project law，不能替代已批准的 Agent 行为指导。若 handoff 必须临时覆盖、暂停或限定某条全局行为规则，必须显式写明 reason、scope、continuation context 和 expected recovery/expiration condition；该局部例外不得静默变成永久项目规则或全局执行源变更。`
- needs_new_user_approval: yes

### D-04

- decision_id: D-04
- decision_title: Confirm public/private permission boundary, with wording revision
- user_confirmed_checkpoint_status: accepted_with_wording_revision; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-04`)
- current_spec_sections:
  - `current/human-approved-spec.md` section 1, `Mnemosyne 的定位`
  - `current/human-approved-spec.md` section 4, `执行源原则`
  - `current/human-approved-spec.md` section 9, `交付包原则`
  - `current/human-approved-spec.md` section 10, `当前 v0.1 边界`
- coverage_status: not_reflected
- coverage_explanation: The spec distinguishes Mnemosyne as a design factory from target-project repositories/directories as runtime truth sources, and it protects execution-source promotion. It does not define the ordinary target-project Agent permission boundary from D-04: public guidance may be read; authorized memory content may be written/appended/updated according to approved rules; shared memory-system design layer, public rules, directory structure, collaboration protocols, workspace boundaries, and execution-source boundaries must not be redesigned or modified unless explicitly authorized.
- operational_risk_if_left_ambiguous: Target-project agents may confuse authorized memory maintenance with authority to redesign the memory framework itself, causing silent drift in public rules, directory responsibilities, and execution-source boundaries.
- recommended_disposition: Promote as a new target-project Agent permission-boundary principle, likely near section 9, only after separate user approval.
- candidate_exact_spec_wording_if_promotion_is_recommended:
  - proposed_insertion_section: `current/human-approved-spec.md` section 9, after the target-project repository/runtime-truth-source bullet.
  - wording: `- 普通目标项目 Agent 可以读取公开 memory-system guidance，并且只能在目标项目已授权文件中、按已批准 memory rules 写入、追加或更新项目 memory content。除非得到明确授权，普通目标项目 Agent 不得重新设计或修改 shared memory-system design layer，包括 public Agent behavior rules、memory directory structure、file responsibilities、collaboration protocols、public/private workspace boundaries、execution-source boundaries，或将 raw / summary / handoff / candidate material 静默提升为执行源。`
- needs_new_user_approval: yes

### D-05

- decision_id: D-05
- decision_title: Confirm original-source preservation principle
- user_confirmed_checkpoint_status: accepted_with_principle_revision; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-05`)
- current_spec_sections:
  - `current/human-approved-spec.md` section 5, `研究证据层原则`
  - `current/human-approved-spec.md` section 6, `需求进入原则`
  - `current/human-approved-spec.md` section 8, `模型迁移原则`
  - `current/human-approved-spec.md` section 14, `Manual import inbox / Codex Cloud non-image attachment boundary`
- coverage_status: partially_reflected
- coverage_explanation: The spec reflects raw/evidence importance: new input first becomes Raw Record; raw is the highest evidence source for migration; research evidence is a high-weight evidence layer; staged files require safety checks and must not contain secrets. The spec does not yet state the broader original-source preservation principle for Mnemosyne and target-project memory systems: raw user text, original ideas, oral restatements, uploaded source material, original prompts where available, and other first-hand records should be durably preserved and not silently discarded, overwritten, or replaced by summaries, indexes, cleaned restatements, candidate requirements, research syntheses, or other interpretations. It also does not state the deletion/redaction/access restriction boundary from D-05.
- operational_risk_if_left_ambiguous: Future cleanup or compression work may replace first-hand source material with model summaries, reducing auditability and causing cumulative reinterpretation drift across model/tool migrations.
- recommended_disposition: Promote an original-source preservation principle into the spec only after separate user approval, while preserving the explicit boundary that original sources are evidence/reference, not execution source.
- candidate_exact_spec_wording_if_promotion_is_recommended:
  - proposed_insertion_section: `current/human-approved-spec.md` section 6, after `新输入先保存为 Raw Record。`, or as a new subsection after section 6.
  - wording: `- Mnemosyne 和目标项目 memory system 应将 original-source materials 作为 durable source layer 保存，包括 raw user text、original requirements、original user ideas、oral restatements、uploaded source materials、available original prompts 和其他 first-hand input records。它们不应被 summaries、indexes、cleaned restatements、candidate requirements、research syntheses 或 Agent-generated interpretations 静默丢弃、覆盖或替代。Original-source preservation 不使 raw/original materials 成为执行源；任何转换为 confirmed requirements、candidate designs 或 Agent-readable execution guidance 仍需 synthesis、capability checking、conflict checking 和适当 user confirmation。删除、redaction 或 access restriction 不应作为普通 memory-compression 策略自动发生；如敏感材料必须移除、脱敏或限制访问，应由 explicit user-directed action 或 separate retention/privacy rule 管理。`
- needs_new_user_approval: yes

### D-06

- decision_id: D-06
- decision_title: Confirm memory-system testing / feedback / debugging as research-gated candidate requirement
- user_confirmed_checkpoint_status: accepted_with_research_gated_testing_revision; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-06`)
- current_spec_sections:
  - no current spec section promotes memory-system testing / feedback / debugging into an executable workflow.
  - related non-promotion boundaries: `current/human-approved-spec.md` section 5, `研究证据层原则`; section 6, `需求进入原则`; section 10, `当前 v0.1 边界`.
- coverage_status: intentionally_non_executable
- coverage_explanation: D-06 explicitly says the testing/debugging capability is a first-class candidate requirement, not final design, not currently verified capability, and research-gated. The current spec correctly does not promote a concrete testing/debugging workflow into execution source. DR1 or later research evidence may partially inform feasibility, but evidence ingestion alone does not authorize promotion into spec.
- operational_risk_if_left_ambiguous: If treated as executable too early, agents may overclaim testing/debugging reliability, design unsupported automated checks, or confuse research evidence with approved workflow.
- recommended_disposition: Keep non-executable until a separate research/capability review and user approval promote a concrete workflow. No spec wording should be promoted from D-06 by this map.
- candidate_exact_spec_wording_if_promotion_is_recommended: none; no promotion recommended now.
- needs_new_user_approval: yes, if any future concrete testing/debugging workflow is proposed for execution-source promotion.

### D-07

- decision_id: D-07
- decision_title: Confirm repository checkpoint / Codex writeback scope
- user_confirmed_checkpoint_status: accepted_with_checkpoint_scope_revision; user_confirmed: yes
- checkpoint_source_path: `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` (`final_R5_user_decisions` / `D-07`)
- current_spec_sections:
  - no current spec section needs to encode this one-time MNEMOSYNE-031 checkpoint/writeback authorization.
  - related non-promotion boundary: `current/human-approved-spec.md` section 4, `执行源原则`.
- coverage_status: checkpoint_only
- coverage_explanation: D-07 authorized the MNEMOSYNE-031 repository checkpoint/writeback scope and clarified that the original R5 draft is superseded where it conflicts with final D-01–D-07 decisions. It is a task-specific checkpoint/writeback authorization, not a standing behavior rule. The spec already states that Decision Records, handoffs, candidates, raw, and reports are not execution source and that spec updates require approved process.
- operational_risk_if_left_ambiguous: Low if kept as checkpoint-only. The risk would increase if future agents generalize this one-time writeback authorization into a standing rule that Codex may promote checkpoint records into the spec.
- recommended_disposition: Do not promote. Preserve as checkpoint record only.
- candidate_exact_spec_wording_if_promotion_is_recommended: none
- needs_new_user_approval: no for preserving checkpoint-only status; yes if someone proposes turning it into a standing execution rule.
