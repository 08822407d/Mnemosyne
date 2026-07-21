# FABLE5-GREENFIELD-001 — GF-STEP-5 Input Integrity Failure Report

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-5
step_name: contrastive_comparison_against_existing_design
record_type: input_integrity_failure_report
status: GF_STEP_5_INCOMPLETE_INPUT_INTEGRITY_FAILURE
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
research_mode: false
date: 2026-07-21
fresh_conversation: true
frozen_current_design_commit: 644bb7d7f864bb23d942520ebb7f206b8805475e
frozen_commit_read: false
```

## 2. Verification performed

Identity checks only, before any substantive reading, per §3 and workflow step 1 of §6:

- Enumerated `/mnt/user-data/uploads` (7 files present).
- Computed byte counts and SHA-256 for all 7 presented files.
- Computed Git blob SHA-1 for the presented files pinned as A, E, F.
- No attachment content was read substantively (hashing only).
- No repository path was fetched. The §0 read-only firewall over CUR-01…CUR-07 was never exercised; no current-design content entered this conversation.

## 3. Attachment identity results

| id | required filename (§1/§3) | expected bytes / SHA-256 (prefix) | observed | result |
|---|---|---|---|---|
| A | STEP1E-second-tier-prompts-and-final-closure.md | 32577 / `60fd4ca8…` | 32577 / `60fd4ca8…`; blob `af62ffb5…` match | PASS |
| B | STEP2D-source-contract-verification-and-closure-addendum.md | 68834 / `ebb994bd…` | 68834 / `ebb994bd…` | PASS |
| C | STEP3A-information-authority-architecture.md | 47324 / `3d82a372…` | 47324 / `3d82a372…` | PASS |
| D | STEP3B-lifecycle-operations-architecture.md | 68033 / `af4dd4c2…` | **not present in upload set** | **FAIL — missing** |
| E | STEP4-self-critique.md | 64639 / `6ae4f2a6…` | 64639 / `6ae4f2a6…`; blob `1270f3e8…` match | PASS |
| F | STEP3R-bounded-architecture-repairs.md | 58339 / `961a8c30…` | 58339 / `961a8c30…`; blob `5d6b5312…` match | PASS |
| G | STEP3RV-bounded-reverification.md | 46623 / `e2bcf75d…` | 46623 / `e2bcf75d…` | PASS |

Out-of-list file present (not on the §1 required list, identity recorded only):

```text
FABLE5-GREENFIELD-001-GF-STEP-3RV-task.md
22375 bytes
sha256 = 9209de4e35dbda892ac57bf1a43a0c04513775763fc0f9a562c98c9f83fc826a
```

Summary: 6/7 required attachments pass full identity checks (3/3 pinned Git blobs match); required attachment D is absent; one file outside the required set was attached in its place. The task prompt itself was received pasted in the chat body, not as an eighth attachment, as §1 requires.

## 4. Failure determination

- §1 requires exactly the seven listed files; §3 states any mismatch requires `GF_STEP_5_INCOMPLETE_INPUT_INTEGRITY_FAILURE`.
- The mismatch is load-bearing, not incidental: §4 defines the effective greenfield design base as `STEP3A_plus_STEP3B`. Without STEP3B, the effective greenfield design cannot be assembled and no need row or architecture topic can be compared honestly.
- Substitution of STEP3B from memory, Project knowledge, past-chat retrieval, or the repository is prohibited by §1 and was not attempted.
- Execution therefore stops at workflow step 1 of §6. Workflow steps 2–11, the firewall opening over CUR-01…CUR-07, and all comparison registers were not performed.

## 5. Access and action counters

```yaml
attachments_presented: 7
required_attachments_matched: 6_of_7
required_attachment_missing: D_STEP3B
out_of_list_attachments: 1
attachments_read_substantively: 0
repository_paths_read: 0
retrieval_batteries_used: 0
repository_searches: 0
repository_tree_browsing: 0
web_or_external_research_used: false
Project_knowledge_used: false
past_chat_retrieval_used: false
current_design_firewall_exercised: false
premature_GF_STEP_3_candidate_read: false
target_project_paths_read: 0
repository_actions: 0
execution_source_changes: 0
greenfield_parameters_answered: 0
follow_on_tasks_generated: 0
```

## 6. Remediation note (diagnosis only, not a task)

The defect is confined to the attachment set: attachment D (`FABLE5-GREENFIELD-001-STEP3B-lifecycle-operations-architecture.md`, 68033 bytes, SHA-256 `af4dd4c2d9658319462a28cc13c469f24823be06cc003f33858b348a68fb6685`) is missing, with the GF-STEP-3RV task file attached in its place. Re-issuing GF-STEP-5 in a genuinely fresh conversation with the exact seven §1 attachments would satisfy §3. Because no CUR path was read and no attachment was substantively read here, this failed run contaminates nothing. This note authorizes nothing and generates no task.

## 7. Filename note

§21 names the deliverable for the completed comparison. The §2/§3 failure branch names no file, so this report uses a distinct failure filename to avoid a file labeled `contrastive-comparison` that contains no comparison. Disclosed as a judgment call under ambiguity.

## 8. Boundary statement

This record is non-execution-source advisory evidence only. No comparison was performed. No greenfield or current-design content was substantively read in this conversation. No repository read, write, search, branch, commit, PR, issue, or comment occurred; no target-project action; no web or external research; no Project knowledge or past-chat retrieval; no `GF3A-DP01…DP15` answered; no `GF4-F03…F19` repaired; no Codex, GPT Pro, Deep Research, repair, or follow-on Fable task generated. The existing-design comparison firewall was never opened in practice and is closed. Execution stops here; any re-run requires separate user authorization via a fresh trigger.
