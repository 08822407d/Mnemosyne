# MNEMOSYNE-224 Package 002 — Fresh Pro Review 001

```yaml
review_id: MNEMOSYNE-224-PACKAGE-002-FRESH-PRO-REVIEW-001
review_task: MNEMOSYNE-226
reviewed_task: MNEMOSYNE-224
reviewed_PR: 292
reviewed_merge_commit: d0cae2f1d145c8c3e63f4912c9685148face1dc7
review_surface: ChatGPT_conversation_with_GitHub_connector
operator_selection_verbatim: Pro
operator_selection_evidence: direct_user_instruction
backend_identity: unknown_or_not_attestable
provenance_disposition: FAIL_REQUIRES_ADDITIVE_CORRECTION
protocol_repair_core: ACCEPT
package_002_content: ACCEPT_WITH_ONE_MATERIAL_OPERATIONAL_CORRECTION
package_002_ready_for_G2A_without_correction: false
A0_execution_authorized: false
execution_source_modified: false
```

## 1. Overall verdict

PR #292 correctly identified and repaired the package-001 publication/freshness loop. The central two-layer model is technically sound:

1. immutable source integrity is established through exact path/blob identities;
2. mutable execution-window no-write baselines are frozen only after publication and checked before/after A0.

Package 002 also correctly preserves validation-master, fixture-tree and historical V1-ref identities as hard run dependencies, keeps A0-only scope, and prohibits retry/repair/hidden continuation.

However, PR #292 cannot be treated as already Pro-reviewed because its execution context was misreported. This review supplies the missing fresh Pro judgment.

The review also finds one material operational defect in package 002: the operator startup template omits the exact authorized visible model label from the message delivered to the fresh controller.

Disposition:

```text
ACCEPT_CORE_REPAIR_BUT_REQUIRE_PACKAGE_003_MODEL_AUTHORIZATION_BINDING_BEFORE_G2A
```

## 2. Correct findings in PR #292

### 2.1 Self-invalidation diagnosis

Package 001 required current Mnemosyne `master` to equal a pre-publication SHA. Publishing the package necessarily moved `master`, so the package invalidated itself. Repeating a PR merely to update the SHA would recurse.

This diagnosis is correct and is not a runtime A0 failure because A0 never started.

### 2.2 Source integrity versus no-write baseline

The repair correctly separates:

```yaml
source_integrity:
  proof: exact_load_bearing_path_blob_pairs

execution_window_no_write:
  proof: Owner_frozen_current_refs_checked_before_and_after_A0
```

A normal publication may move `master` while preserving exact load-bearing blobs. That should not invalidate the design. After Owner G2A freezes a no-write baseline, later movement must block the run.

### 2.3 Natural-language G2A without another Mnemosyne PR

Using the exact Owner startup/authorization message as the G2A authority avoids changing Mnemosyne `master` after freezing it. Preserving that message verbatim in validation evidence is a valid design candidate.

This does not weaken source integrity because candidate/manifest/package blobs remain exact inputs.

### 2.4 Additive historical treatment

Package 001 and MNEMOSYNE-223 remain preserved. Package 002 supersedes only the defective source-binding/baseline-timing scope. This is preferable to rewriting the historical failed design.

### 2.5 Hard-pinned validation dependencies

The following remain genuine execution dependencies and are correctly hard-pinned:

- validation repository `master`;
- read-only fixture commit/tree;
- complete historical `tlr-v1-*` ref inventory;
- controller-branch absence;
- exact seven-file write set.

## 3. Provenance failure

The Owner reports that MNEMOSYNE-224 ran under a next-tier selection, while PR #292 claimed `operator_selection_verbatim: Pro` and `PASS_Pro_protocol_repair`.

Therefore:

```yaml
MNEMOSYNE_224_same_turn_Pro_review_claim: invalid
PR_292_exact_repository_artifacts: preserved
current_fresh_Pro_review: this_file
```

The technical result can be recovered by fresh review; the historical attribution cannot be silently corrected.

See:

```text
notes/run-context-incidents/
MNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001.md
```

## 4. Material operational defect in package 002

Candidate 002 and current status correctly list five future G2A dynamic fields:

```yaml
required:
  - decision_candidate_blob
  - source_manifest_blob
  - protected_Mnemosyne_master
  - protected_Meta_Agent_master
  - authorized_visible_model_label
```

But package 002's `04-startup-message.md` states that the Owner authorization supplies **four** exact values and gives placeholders only for the two blobs and two protected refs. It tells the operator to select the authorized model, but the exact label is not included in the message delivered to the fresh controller.

This is material because:

- consumer-chat UI selection is not a reliable hidden input to the assistant;
- the immediately preceding incident demonstrates that the assistant may misstate the current selection;
- the fresh controller cannot compare the observed/reported selection to an authorization value that is absent from its input;
- `operator selected something` and `Owner authorized this exact label` are distinct claims.

The controller must receive the exact authorized visible label in the same Owner G2A/startup message that binds the run.

## 5. Required correction

Package 003 must:

1. inherit package 002 except for the model-selection authorization/startup scope;
2. bind its own candidate and manifest blobs;
3. include `authorized_visible_model_label` verbatim in the exact message sent to the controller;
4. require the controller to record both:
   - Owner-authorized label from direct instruction;
   - operator-observed/reported actual selected label;
5. block if they differ or either is unavailable;
6. keep backend identity `unknown_or_not_attestable`;
7. preserve all package-002 repository, fixture, path, no-retry and no-hidden-continuation boundaries.

## 6. Additional scheduling condition

At review time, another independent Mnemosyne write route exists on:

```text
mnemosyne-225-f1-bounded-validation-design-and-next-step-write-visibility
```

Its paths do not overlap with MNEMOSYNE-226, but it is expected to publish later and move Mnemosyne `master`. Therefore A0 G2A should not be issued until that route is merged, abandoned, or explicitly paused for the A0 execution window.

This is not a package-002 technical defect. It is a live scheduling condition for the dynamic no-write baseline.

## 7. Quality disposition

```yaml
problem_reconstruction: PASS
self_invalidation_root_cause: PASS
repair_architecture: PASS
historical_preservation: PASS
non_execution_boundary: PASS
source_manifest_strategy: PASS
G2A_no_PR_strategy: PASS
run_context_provenance: FAIL
model_label_authorization_binding: FAIL_MATERIAL
technical_quality_after_package_003: expected_PASS_pending_merge_and_freshness_gate
```

No A0 execution or G2A should occur from package 002 alone.
