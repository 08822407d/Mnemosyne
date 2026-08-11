# Proposed Active-Guidance Amendments from OR-01 v0.1

> Exact bounded amendment contract for three active guards. This file is a non-execution-source proposal; the guards are unchanged until a separately verified implementation commit updates their current paths.

```yaml
proposal_id: MNEMOSYNE-OR01-ACTIVE-GUIDANCE-AMENDMENTS-001
task_id: MNEMOSYNE-202
status: implementation_ready_candidate_not_active
owner_review_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
execution_source_modified: false
```

## 1. Why these three items should become active repairs

Most OR-01 feedback changes the non-execution-source capability catalogue or needs real-use evidence. Three items correct recurring behavior already governed by active guards and are sufficiently bounded to implement without new architecture:

1. honest distinction between byte change and substantive-content change;
2. repair handling for a short “排版不对” response after transfer content;
3. periodic auditing of explicit branch-retention obligations.

They do not change Owner authority, target truth, privacy permission, external execution, or research quota.

## 2. Source-preservation guard amendment — ACAP-004

Target:

```text
current/source-artifact-preservation-and-design-rationale-guard.md
```

### Required semantic additions

Add a two-dimension transformation record:

```yaml
source_transformation_assessment:
  byte_identity:
    status: unchanged | changed | unknown
    evidence_refs: []
  transformation_class:
    exact_move_or_rename |
    line_ending_normalization |
    encoding_normalization |
    wrapping_or_container_normalization |
    substantive_content_edit |
    mixed |
    unknown
  substantive_content:
    status: unchanged_as_reviewed | changed | not_fully_reviewed | unknown
    review_scope:
  preservation_level_before:
  preservation_level_after:
  exact_received_source_retained_separately: true | false | not_applicable
  limitations: []
```

Required wording rule:

- do not use an unqualified “content was modified” when only byte-level normalization was established;
- prefer: “bytes changed because line endings/encoding were normalized; no substantive-content change was found within the stated review scope”;
- `substantive_content_unchanged` does not restore exact byte identity;
- preserve the exact received file separately when material and feasible;
- if substantive equivalence was not reviewed, state `not_fully_reviewed` rather than assuming it.

No new preservation level is required. `NORMALIZED_READABLE_COPY` remains accurate for a normalized derivative.

## 3. Artifact-delivery guard amendment — ACAP-027

Target:

```text
current/artifact-delivery-and-direct-generation-guard.md
```

### Context-sensitive repair shortcut

When all of the following are true:

- the immediately preceding Agent response contained content intended for copying/transfer, especially Markdown, YAML, code blocks, task prompts, or a long structured package;
- the user responds with a short phrase equivalent to `排版不对`, `内容排版不对`, `格式坏了`, or `复制过去格式不对`;
- no stronger context indicates a different request;

interpret the leading hypothesis as **transfer-structure damage**, not ordinary aesthetic editing.

Required response:

1. identify the likely affected artifact/content;
2. preserve semantics and ordering;
3. repair using a verified downloadable file when file-first applies, otherwise a complete fenced block;
4. avoid re-explaining the whole design unless needed;
5. state briefly what structural failure was repaired;
6. ask one clarification only when several materially different prior artifacts could be meant;
7. do not claim a file exists without verification.

This is a context-sensitive shortcut, not a global keyword command. If the prior message did not contain transfer content, interpret the user's ordinary formatting request from context.

## 4. Branch-retention guard amendment — ACAP-031

Target:

```text
current/pr-merge-branch-disposition-guard.md
```

### Periodic obligation audit

Add a bounded audit section:

```yaml
branch_retention_obligation_audit:
  audit_id:
  repository:
  observed_at:
  active_obligations_checked: []
  obligation_results:
    - obligation_id:
      branch:
      branch_exists:
      stated_reason:
      retain_until:
      responsible_route_or_task:
      gate_status: not_reached | reached | unclear | dependency_missing
      unique_unpreserved_work_status:
      disposition: keep | release_notice_required | clarify | incident
  repository_writes_or_deletions_authorized: false
```

Rules:

- periodic manual or automated maintenance may enumerate and assess only obligations that were explicitly created;
- the audit may identify zombie/stale obligations, satisfied gates, missing dependencies, or absent branches;
- the audit must not delete a branch automatically;
- a satisfied gate still requires verification of unique unpreserved work and an explicit user-facing release notice;
- an unclear gate is routed to the responsible task/Owner, not silently extended forever;
- a branch missing while an obligation remains active is an incident candidate, not a reason to mark the obligation cleanly released;
- audit cadence remains repository/Owner-specific and should be informed by actual branch volume.

## 5. Implementation contract

A bounded next-tier implementation task may:

- update only the three named guards;
- update their version/amendment metadata;
- add a result and PR-finalization record;
- leave `current/human-approved-spec.md`, the loader, and unrelated guards unchanged;
- use exact changed-path allowlists and mechanical wording checks.

It must stop if:

- another active PR changes any target guard;
- the required current guard content differs materially from the versions reviewed by MNEMOSYNE-202;
- implementation would create a new authority/privacy rule rather than the bounded clarifications above;
- the user has not authorized the implementation task's exact branch/PR actions.

## 6. Verification

Mechanical checks:

- each guard names the new amendment task/version;
- the source guard contains byte identity and substantive-content dimensions;
- the artifact guard recognizes the contextual formatting-repair trigger without a global keyword-only rule;
- the branch guard contains periodic audit and explicit no-auto-delete language;
- no execution source or loader diff;
- no duplicate active PR lineage.

Semantic review:

- normalization is not mislabeled exact;
- “排版不对” does not silently change substantive content;
- audit does not create deletion authority or routine branch retention.

## 7. Model routing

```yaml
frontier_work_completed:
  - semantics_and_scope_frozen_in_this_proposal
next_tier_suitable_candidate:
  - exact_guard_edits
  - metadata_update
  - result_and_PR_records
mechanical:
  - changed_path_allowlist
  - exact_phrase_and_section_checks
  - diff_verification
human:
  - merge_and_final_acceptance
```
