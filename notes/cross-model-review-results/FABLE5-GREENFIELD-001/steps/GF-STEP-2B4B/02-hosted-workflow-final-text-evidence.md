# FABLE5-GREENFIELD-001 — GF-STEP-2B4B Hosted-Workflow Final Text Evidence

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B4B
step_name: hosted_repository_workflow_full_text_completion_and_S05_disposition
record_type: hosted_repository_workflow_full_text_completion
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B4A
research_mode: false
date: 2026-07-11
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf
  expected_blob_sha: ee4bb0ab829cb59819263858c3c4a3a0178c22da
  observed_blob_sha: ee4bb0ab829cb59819263858c3c4a3a0178c22da
  sha_match: true
report_id: RPT-2026Q2-0005
execution_mode: full_text_completion_of_B4A_probe
report_stated_evidence_date: none_stated_in_text (cycle 2026Q2)
step_status: GF_STEP_2B4_complete_full_text_layer_reviewed_S05_disposed
```

## 2. Scope and hard limits

Completion of the RPT-2026Q2-0005 text-layer review begun in B4A. Limits: paths 1/1; batteries 0/1 (B4A's verified local copy re-hashed; no new retrieval); PDFs 1/1; final evidence records 5/5 max; claimed-vs-observed rows 3/4 max plus stated limitation; placement rows 4/4 max; final disposition exactly S-05; linkage entries 4/4 max; limitations 4/4 max; no OCR or visual inspection; no other reads; no web research; Research mode off; no automatic continuation.

## 3. Allowed-source and anti-contamination policy

Inputs: the B4A deliverable (source identity, inspected/uninspected ranges, P01–P03, provisional S-05 note, ID and caveat discipline) and exactly the one pinned PDF. No other repository file or prohibited tier opened; PDF-internal links, docs, and the cited changelog/community items are metadata only, never followed. No knowledge outside the report used. Prior-exposure disclosure carries forward: independence by derivation and disclosure.

## 4. Source integrity and text-access result

Expected SHA `ee4bb0ab829cb59819263858c3c4a3a0178c22da`; observed (local re-hash of the B4A-fetched bytes) identical; match true (422,372 bytes). Text layer remains usable; extraction complete and untruncated: 3 pages, ~10,908 characters, 149 lines. All conclusions text_only; visual objects not inspected.

## 5. B4A linkage and supersession rule

F2B4A-P01…P03 are **superseded** by the final register below (P01→E01, P02→E02; the exclusion-bypass nuance B4A flagged for follow-up is carried by E04). Provisional and final records are not parallel evidence; only F2B4-E01…E05 count.

## 6. Completed text-layer coverage record

Previously inspected (B4A): ll.1–11, 12–24, 26–35 (partial), 56–66, 84–103, heading/keyword map. Newly inspected here: ll.25–55 in full (suitable and unsuitable memory files; exclusion-bypass statement; same-repo vs separate-repo; token scopes), ll.67–83 (Actions automation and human-confirmation boundaries), ll.104–149 as reference-metadata layer only (GitHub official docs on cloud agent, CODEOWNERS, branch protection, secret scanning, workflow logs, artifacts, MCP; one community discussion; one GitHub changelog dated 2025-11-13 on the agent as a ruleset bypass actor — none opened). Minimal re-check anchors: ll.29–30 for P01 reconciliation. Complete substantive text coverage: **yes**; no text step remains for this report.

## 7. Final evidence register

Register-wide: text_only = true; visual_review_status = not_performed; source period cycle 2026Q2. 5 records.

| evidence_id | supersedes_provisional_ids | source_anchor | concise_statement | evidence_category | named_workflow_scope | confidence_as_report_evidence | date_sensitivity | write_permission_audit_review_correctness_distinction | related_research_domain_ids | related_STEP1_need_ids | supports_or_challenges_S05 | prohibited_overclaim | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2B4-E01 | F2B4A-P01 | ll.1–11 | hosted Copilot agent + GitHub can achieve memory write-back with audit to a degree, given careful permission/process design: Actions environment reads/modifies/tests and creates PRs, all operations logged; CODEOWNERS and protected branches force human review; merges via PR with forced approval | report_author_synthesis | Copilot cloud agent + GitHub | high | high | write feasible; audit via configured gates; correctness never implied by writes | RD-04 | GF1A-N07; GF1B-N15,N13 | supports | "feasible with configuration" ≠ safe by default | — |
| F2B4-E02 | F2B4A-P02 | ll.17–24, 71–75 | observable evidence chain: background PR creation (submitter "GitHub Copilot"), requester cannot self-approve; status checks; Actions logs preserved; artifacts uploadable and recoverable after failure | cited_external_claim_not_independently_checked | same | high | high | events (branch, commit, diff, PR, review, checks, logs, artifacts, merge) are provable; semantics are not | RD-04 | GF1B-N13; GF1A-N07,N11 | supports | trail existence ≠ semantic verification | — |
| F2B4-E03 | — | ll.46–55 | same-repo memory: default GITHUB_TOKEN read/write, protections apply directly, simpler flow — but repo bloat, memory–code coupling, wider exposure; separate memory repo: permission isolation, per-repo audit, cross-team sharing — but default MCP token is read-only for the current repository, so cross-repo writes need org-scope PAT or dedicated credentials and explicit configuration | mixed_or_uncertain | same | high | high | permission scope is a distinct axis from write capability and from audit policy | RD-04; RD-09 (adjacent) | GF1B-N15; GF1C-N20 (adjacent) | supports (permission dimension) | neither option is report-endorsed as universally correct | unresolved tradeoff |
| F2B4-E04 | — (carries B4A follow-up flag) | ll.29–30, 34–39 | sensitive credentials, PII, private algorithms, financial or legal material must not be agent-reachable; secret scanning warns committed credentials leak; **Copilot content-exclusion configuration does not bind the cloud agent — excluded files remain visible and modifiable**; sensitive memory needs storage outside the agent's reach entirely | cited_external_claim_not_independently_checked | same | high | high | exclusion settings are not a permission boundary; protection requires placement, not configuration hints | RD-04; RD-09 (adjacent) | GF1A-N03; GF1C-N20 (adjacent); GF1A-N07 | supports | one product's documented 2026Q2 behavior, not universal | stated twice in the report |
| F2B4-E05 | — | ll.67–83 | Actions can automate PR-time validation (linters/tests, logged), artifact archiving (snapshots, diff reports, checkpoint recovery), and scripted write-back commits (GITHUB_TOKEN `contents: write`; separate-repo pushes need dedicated credentials) — but the PR human-confirmation step is generally retained | mixed_or_uncertain | GitHub Actions within the same workflow | medium | high | automation covers mechanics; approval remains a human gate by practice | RD-04 | GF1A-N07,N11; GF1B-N13 | supports | automatable ≠ recommended unattended; one cited source is a community discussion | changelog [12] (bypass actor) cited as metadata |

## 8. Claimed-versus-observed evidence check

| check_id | claimed_or_requested_event | observable_repository_evidence | what_the_evidence_can_establish | what_it_cannot_establish | human_or_platform_gate | related_F2B4_evidence_ids |
|---|---|---|---|---|---|---|
| C-1 | agent asked to change a memory file | branch, commit, diff, PR with "GitHub Copilot" submitter | that a change exists, its content, its labeled authorship | that the change is semantically correct or intended | branch protection + reviewer; no self-merge | E01,E02 |
| C-2 | change claimed validated | status checks + Actions run logs | format/test pass and a reproducible trail | quality beyond what the checks encode | required-status-checks configuration | E02,E05 |
| C-3 | run produced intermediate results | uploaded artifacts (snapshots, diff reports) | recoverable state even after failed jobs | that archived content is correct | platform artifact retention | E02,E05 |

Limitation: the report does not explicitly discuss divergence between model-claimed completion and the observed diff; that premise is not contradicted here, but its direct evidence lives at the foundational layer, not in this report.

## 9. Repository-placement and permission map

| option_or_boundary | report_supported_advantage | report_supported_risk | permission_or_token_scope | audit_implication | sensitive_information_implication | status |
|---|---|---|---|---|---|---|
| same-repository memory | default-token access; protections apply directly; simple flow | repo bloat; memory–code coupling; wider exposure if permissions broad | default GITHUB_TOKEN (current repo) | CODEOWNERS/branch protection directly usable | unsuitable for sensitive content | unresolved_tradeoff |
| separate memory repository | permission isolation; per-repo audit policies; cross-team sharing | configuration complexity; explicit credential management | default MCP token read-only; org-scope PAT/dedicated creds for writes | independent protection and audit rules | better isolation; still Git-exposed | unresolved_tradeoff |
| Copilot content exclusion | none for agent containment | excluded files remain agent-visible and modifiable | n/a | not an audit or permission control | not a protection boundary for the cloud agent | report_finding |
| outside-Git storage for sensitive memory | removes agent/tool exposure | leaves the Git audit chain | n/a | not Git-audited | recommended destination for secrets/PII/restricted material | report_recommendation |

No architecture option is selected for Mnemosyne.

## 10. Final S-05 disposition

- signal_id: S-05. previous_or_provisional_wording: hosted write-back claims may differ from observable repository changes; reliable audit requires repository evidence, configured review gates, and a traceability-vs-correctness distinction. B4A provisional support: present.
- Disposition: **dedicated_report_refines**.
- replacement_wording_if_refined: on the Copilot-cloud-agent + GitHub surface (2026Q2), write-back is PR-mediated with platform-enforceable, opt-in review gates (no self-merge, CODEOWNERS, protected branches, status checks) and full log/artifact trails, so verification rests on observable repository evidence — branch, commit, diff, PR, review decision, checks, logs, artifacts, merge — rather than agent claims; trails establish traceability, never semantic correctness; default tokens are current-repo-scoped (MCP read-only) and cross-repo writes need elevated credentials; Copilot content-exclusion does not bind the agent, so sensitive material requires placement outside the agent's reach.
- supporting_F2B4_evidence_ids: E01–E05. named_surface_scope: Copilot cloud agent + GitHub only; not generalized.
- write_vs_observed_change_distinction: the report supplies the observable-evidence chain; explicit claim-vs-diff divergence is not examined (stated limitation, §8).
- audit_vs_correctness_distinction: trails prove events; correctness only via review and checks, to their encoded depth.
- configuration_and_permission_caveat: every gate is opt-in; token scopes differ by placement; a changelog (metadata) shows the agent can even be configured as a ruleset bypass actor.
- report_date_caveat: cycle-level 2026Q2; no self-stated date. remaining_visual_dependency: none identified for these claims; visuals unreviewed. remaining_current_fact_refresh_dependency: yes (STEP2A D-03). remaining_original_report_dependency: none for S-05; foundational corroboration stands.
- prohibited_overclaim: never "hosted write-back is audited by default," and a gated write-back success never confers target-write authority.
- S-01…S-04 not reassessed.

## 11. Minimal STEP-1 linkage delta

| need_id | coverage_change | supporting_evidence_ids | remaining_report_dependency | user_decision_not_resolved |
|---|---|---|---|---|
| GF1A-N07 | strengthened: platform-enforceable mandatory review, no self-merge, per-action gates | E01,E02,E05 | batch-3 reports | Q-02 approval granularity |
| GF1B-N13 | strengthened: logs, artifacts, diffs, and PR history as durable evidence trails | E02,E05 | 0006 | — |
| GF1B-N15 | strengthened: placement options, token scopes, and protection mechanics for the substrate | E03,E05 | 0006 | Q-04 storage product |
| GF1C-N20 | corroborated (adjacent): exclusion-bypass, secrets-never-reachable, outside-Git recommendation | E03,E04 | UIG-0001 (dedicated) | Q-07-updated preservation balance |

## 12. Visual, date, scope, and evidence limitations

1. Visual content unreviewed: 422 KB file vs ~10.9 K characters of text; all conclusions text_only; figure/layout meaning pending the repository's manual review process (index not opened).
2. Dating and sourcing: cycle-level 2026Q2 only; claims rest on cited GitHub official docs plus one community discussion and one changelog, none verified here; product drift covered by STEP2A D-03.
3. Configuration semantics: every protective gate is opt-in, and the cited changelog shows gates can be relaxed (bypass actor) — defaults must never be assumed protective.
4. Scope: findings bind the Copilot-agent + GitHub surface only; the claim-vs-diff divergence premise of S-05 was not directly examined by this report.

## 13. Status determination and bounded continuation

Determination: **GF_STEP_2B4_complete_full_text_layer_reviewed_S05_disposed**. B4A provisional records are superseded; complete substantive text coverage achieved; no further RPT-2026Q2-0005 text step is required. Proposed next bounded step (not executed), per STEP2A's deferred batches: GF-STEP-2B5 on RPT-2026Q2-0006 only (`raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf`), expected blob SHA pinned in its instruction; same text-only rules and mode gate; focus on the theory/engineering grounding behind S-01 and GF1A-N09/GF1B-N15. GF-STEP-2 is not complete.

## 14. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no reading of any other report, summary, prompt, index, or PDF, no OCR or visual interpretation, no external research or security testing, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2B4 is complete; GF-STEP-2 is not complete.
