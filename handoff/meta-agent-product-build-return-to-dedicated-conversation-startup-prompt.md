# Meta-Agent Product Build — Return to Existing Dedicated Conversation Startup Prompt

Use this prompt in the user's **existing dedicated Meta-Agent construction conversation** after the canonical MNEMOSYNE-172 handoff PR has merged.

Repository: `08822407d/Mnemosyne`

## Task

Receive the repository-backed Meta-Agent product-build handoff and re-anchor this existing conversation to the latest target state.

This first operation is **receive-only**. Do not perform owner acceptance, operational activation, repository writes, target revision, pilot planning or substantive continuation in the first response.

## Mandatory first read order

Read these files separately and preserve their roles:

```text
handoff/meta-agent-product-build-return-to-dedicated-conversation-handoff-package.md
target-projects/meta-agent/handoff/handoff-current.md
target-projects/meta-agent/current/approved-spec.md
target-projects/meta-agent/authority/source-and-owner-map.md
target-projects/meta-agent/current/active-context.md
current/meta-agent-product-build-status.md
current/first-target-minimum-upgrade-contract-status.md
```

Then read, if available:

```text
target-projects/meta-agent/methodology/core-methodology.md
target-projects/meta-agent/history/decision-version-and-migration-log.md
target-projects/meta-agent/cases/case-and-feedback-ledger.md
notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
notes/codex-task-results/MNEMOSYNE-171-result.md
notes/codex-task-results/MNEMOSYNE-171-pr-finalization.md
notes/codex-task-results/MNEMOSYNE-172-result.md
```

Do not bulk-load unrelated historical Meta-Agent or Mnemosyne records unless a conflict or missing-source question requires them.

## Baseline that must be verified, not assumed

```yaml
expected_baseline:
  M0:
    state: merged_via_PR_221
  M1:
    state: merged_via_PR_221
  M2:
    state: merged_via_PR_222
  target_files:
    count: 7
  designated_target_truth_source:
    path: target-projects/meta-agent/current/approved-spec.md
    effective_for_operational_use: false
  owner_acceptance: pending
  operational_use_authorized: false
  real_cases: 0
  real_feedback_records: 0
  real_evaluation_records: 0
  upgrade_profile: standard
  current_product_route_owner_after_handoff: this_dedicated_conversation
  Mnemosyne_maintenance_route_owner: separate_Mnemosyne_conversation
```

If repository evidence conflicts with this baseline, report the conflict and stop.

## Treatment of this conversation's earlier context

Earlier reasoning in this dedicated conversation may be useful, but it predates the current repository baseline.

```yaml
old_context_policy:
  role: historical_or_candidate_evidence
  authority: not_target_truth
  automatic_promotion: prohibited
  required_action:
    - compare_with_latest_repository_state
    - identify_stale_or_conflicting_assumptions
    - label_uncommitted_ideas_as_candidate_or_unknown
    - preserve_user_corrections
```

Do not reconstruct missing original conversations as fact.

## First-response output contract

Return only a receive report with this structure:

```yaml
handoff_receive_report:
  repository:
  verified_master_sha:
  handoff_package_read: yes | no
  target_handoff_read: yes | no
  designated_target_truth_path:
  target_truth_effective_for_operational_use: false | conflict
  owner_acceptance: pending | conflict
  M0_state:
  M1_state:
  M2_state:
  target_files_found: []
  target_files_missing: []
  loaded_sources: []
  missing_sources: []
  conflicts_or_stale_context: []
  old_conversation_context_role: historical_or_candidate_evidence
  repository_write_performed: false
  owner_disposition_performed: false
  operational_activation_performed: false
  route_ownership_accepted:
    Meta_Agent_product_build: this_dedicated_conversation
    Mnemosyne_self_development: separate_current_Mnemosyne_conversation
  status: RECEIVED_NOT_ACTIVATED | INPUT_OR_STATE_CONFLICT
```

After the YAML, add no more than a short paragraph stating what the user must do next.

Then stop.

## Required next operation after a successful receive

Do not automatically load or import the Mnemosyne maintenance route.

For the immediate bootstrap owner-review task, wait for the user to send a separate instruction equivalent to:

```text
加载 Mnemosyne 约束指导，但只作为 Meta-Agent bootstrap 审阅和仓库操作的流程／安全约束刷新；不要导入 Mnemosyne maintenance route，不要把 Mnemosyne 指导当作 Meta-Agent target truth。
```

This task-local refresh does not establish a universal guidance policy for future ordinary Meta-Agent work.

After that separate refresh, wait for another explicit user instruction before substantive owner review or any repository action.

## Hard prohibitions

- Do not claim Meta-Agent v0.1 is operational or production-ready.
- Do not treat PR #222 merge as owner acceptance.
- Do not repeat M0, M1 or M2 as unfinished tasks.
- Do not modify `current/human-approved-spec.md`.
- Do not activate or change `target-projects/meta-agent/current/approved-spec.md` without fresh target-scoped authorization.
- Do not ingest private or raw materials.
- Do not create extra target files, a pilot case, RAG, MCP, automation, shared memory, learner profile or GPT Live module.
- Do not take over the non-FABLE health-review route.
- Do not use old conversation memory as authority.
- Do not assume a global task number; check latest repository state and open PRs before any later write.
- Do not infer the served backend from UI labels, latency, style or self-report.
