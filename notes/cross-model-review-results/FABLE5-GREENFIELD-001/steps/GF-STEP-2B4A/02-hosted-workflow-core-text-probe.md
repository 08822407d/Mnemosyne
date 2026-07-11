# FABLE5-GREENFIELD-001 — GF-STEP-2B4A Hosted-Workflow Core Text Probe

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B4A
step_name: hosted_repository_workflow_report_core_text_probe
record_type: hosted_repository_workflow_core_text_probe
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B3
research_mode: false
date: 2026-07-11
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf
  expected_blob_sha: ee4bb0ab829cb59819263858c3c4a3a0178c22da
  observed_blob_sha: ee4bb0ab829cb59819263858c3c4a3a0178c22da
  sha_match: true
report_id: RPT-2026Q2-0005
execution_mode: core_text_probe_mode
report_stated_evidence_date: none_stated_in_inspected_text (cycle 2026Q2)
step_status: GF_STEP_2B4A_complete_probe_ready_for_STEP2B4B
```

## 2. Scope and hard limits

Preliminary probe only; not the RPT-2026Q2-0005 review, no final S-05 disposition. Limits: paths 1/1; batteries 1/1; PDFs 1/1; mode core_text_probe_mode (mandatory — full_text_mode not used although the file is short); provisional items 3/3 max; final dispositions 0; no STEP-1 linkage table; no contradiction register; no OCR or visual inspection; no other reads; no web search; Research mode off; no automatic continuation.

## 3. Allowed-source and anti-contamination policy

Inputs: the STEP2B3 deliverable (S-05 preliminary references, domain/need IDs, write-vs-review-vs-correctness distinctions, caveat discipline) and exactly the one pinned PDF, fetched by the single permitted battery and SHA-verified before extraction. Local reads of the extracted text are not repository batteries. No other repository file or prohibited tier opened; PDF-internal references are metadata only. No knowledge outside the report used. Prior-exposure disclosure carries forward: independence by derivation and disclosure.

## 4. Source integrity and text-access result

Expected SHA `ee4bb0ab829cb59819263858c3c4a3a0178c22da`; observed identical; match true (422,372 bytes). Pages: 3; extracted text ~10,908 characters, 149 lines; text layer usable, clean extraction, no OCR, no retries. Batteries: 1 of 1. Every conclusion here is text_only; visual objects were not inspected.

## 5. Core-text portions inspected

Inspected (line-anchored): title and 总体结论 (ll.1–11); 云端 Agent 能做什么 — environment, tests, PR generation with human-merge requirement, logs/artifacts (ll.12–24); opening of 适合云端 Agent 写回的记忆文件 (ll.26–35, partial); PR / CODEOWNERS / 分支保护 approval section (ll.56–66); 需要人工或难以自动化的环节 plus closing statement (ll.84–103); heading/keyword line map of the whole file. Deliberately not inspected in full: sensitive-file detail and same-repo-vs-separate-repo comparison (ll.36–55), GitHub Actions automation section (ll.67–83), reference list (ll.104–149). Full-report inspection is not claimed.

## 6. Provisional evidence register

Register-wide: text_only = true; visual_review_status = not_performed; provisional_status = requires_full_report_review; source period cycle 2026Q2 (no date in inspected text). 3 items.

| evidence_id | source_anchor | concise_statement | evidence_category | named_workflow_scope | confidence_as_report_evidence | write_audit_correctness_distinction | related_research_domain_ids | related_STEP1_need_ids | possible_relation_to_S05 | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|---|
| F2B4A-P01 | ll.1–11 | hosted Copilot coding agent + GitHub workflow can achieve memory write-back with audit to a degree, given careful permission/process design: Actions environment reads/modifies repo, runs tests, generates PRs, all operations logged; CODEOWNERS and protected branches force human review; secrets/personal data kept outside agent reach; merges via PR with forced human approval | report_author_synthesis | Copilot coding agent + GitHub | high | write capability and audit trail affirmed; correctness is gated by review, not proven by writes | RD-04 | GF1A-N07; GF1B-N15,N13 | present | "feasible with configuration" ≠ safe by default |
| F2B4A-P02 | ll.17–24 | agent creates PRs in the background (submitter shown as "GitHub Copilot"); a human must merge — the requester cannot self-approve; all Actions job logs are preserved and artifacts uploadable, so failed runs remain reconstructable | cited_external_claim_not_independently_checked | same | high | a PR/log proves a repository change and trail, not that the change is correct | RD-04 | GF1A-N07,N11; GF1B-N13 | present | log existence ≠ semantic verification |
| F2B4A-P03 | ll.56–66, 84–99 | enforcement mechanics: CODEOWNERS paths plus branch protection (code-owner review, PR reviews, status checks, no direct pushes) make human approval mandatory for memory-file changes; the agent cannot merge its own PR; unsigned commits can block the agent; highly sensitive updates should not be fully automated, and non-public content should not sit in Git at all | mixed_or_uncertain | GitHub branch protection / CODEOWNERS + agent | high | the authority layer is platform-enforced and separate from write capability | RD-04; RD-09 (adjacent) | GF1A-N07,N11; GF1C-N20 (adjacent) | present | protections are opt-in configuration, not defaults |

## 7. Provisional S-05 note

- signal_id: S-05. prior_signal_theme: hosted repository write-back claims may differ from observable diffs; reliable audit requires repository evidence plus review.
- provisional_support: **present** — the inspected portions affirm the repository-evidence-plus-mandatory-review half (PR trails, logs, artifacts, CODEOWNERS/branch-protection gating, no self-merge).
- supporting_provisional_evidence_ids: F2B4A-P01, P02, P03.
- what_full_review_must_still_check: whether the report addresses claimed-completion vs observed-diff divergence explicitly; same-repo vs separate-memory-repo tradeoffs and token scopes (read-only MCP token vs PAT, ll.46–55); the Actions automation section (ll.67–83); the partially inspected note that the agent can access and update even Copilot-excluded files (ll.29–30) and its governance implications.
- date_and_surface_caveat: cycle-level 2026Q2; Copilot-agent-plus-GitHub surface only; not generalized to other hosted services.
- prohibited_overclaim: do not conclude "hosted write-back is audited by default" — every protection named is opt-in configuration.

## 8. Unreviewed scope and STEP2B4B requirements

Uncovered text: ll.36–55 (sensitive-file classes; same-repo vs separate-repo comparison, token/permission mechanics), ll.67–83 (Actions-based automation and where human confirmation is retained), ll.104–149 (reference list — metadata only). Visual material entirely unreviewed. A later full text-layer review is justified: the uncovered sections carry load-bearing material for S-05's divergence dimension, repository-placement tradeoffs, permission scoping, and the exclusion-bypass nuance. GF-STEP-2B4B must: read the full remaining text under the same text-only rules; produce the final S-05 disposition; issue F2B4-E evidence items superseding these provisional P-items; keep RD-09-adjacent findings as corroboration only.

## 9. Status determination

Determination: **GF_STEP_2B4A_complete_probe_ready_for_STEP2B4B**. Integrity verified, text layer usable, core portions probed, provisional items recorded, uncovered scope preserved exactly. S-05, GF-STEP-2B4, and GF-STEP-2 are not complete; STEP2B4B is not executed here.

## 10. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no reading of any other report, summary, prompt, index, or PDF, no OCR or visual interpretation, no external research, no security testing, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2B4A is complete; GF-STEP-2B4 and GF-STEP-2 are not complete.
