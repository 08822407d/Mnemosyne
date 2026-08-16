# V2-A A0 Package 003 — Next-Tier Controller Amendment

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CONTROLLER-AMENDMENT-003
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-003
parent_controller_task: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CONTROLLER-TASK-002
status: frozen_not_authorized_not_executed
```

## 1. Mission and inherited task

Execute the parent package-002 A0 controller task only after exact package-003 G2A authorization. All repository, fixture, seven-file write-set, no-PR, no-retry and stop rules remain unchanged.

Package 003 changes only the controlling decision/package identity and model-selection evidence contract.

## 2. P0 model-selection receipt

Before any GitHub write, extract these exact strings from the Owner G2A/startup message and current operator/UI evidence:

```yaml
model_selection_receipt:
  Owner_authorized_visible_label:
  Owner_authorization_evidence:
    class: direct_user_instruction
    ref: exact_startup_message_or_stable_message_ref
  operator_selected_visible_label:
  operator_selection_evidence:
    class: operator_observed_or_operator_reported
    ref:
  exact_string_match:
  backend:
    status: unknown_or_not_attestable
    reason: consumer_chat_surface
```

A controller may not set `operator_selected_visible_label` from:

- a prior conversation;
- assistant memory;
- model self-identification;
- response style or speed;
- the recommended label written in a repository file;
- an unstated assumption about the current picker.

If reliable operator/UI evidence is unavailable, set `exact_string_match: unknown`, return `BLOCKED`, and stop before branch creation.

## 3. Package identity preflight

The Owner message must name:

```yaml
required_exact_blobs:
  run_decision_candidate_003:
  package_003_source_manifest:
```

The controller verifies both, then verifies every parent-package and package-003 blob listed in manifest 003. Candidate 002 and manifest 002 remain exact inherited inputs but are not the controlling G2A decision identities.

## 4. Execution-window protected refs

Use the exact Mnemosyne and Meta-Agent master SHAs in the same Owner message as the before/after no-write baseline.

Do not refresh them. A mismatch before the first validation write is `BLOCKED`. A mismatch after A0 is a failed/disputed no-write result requiring fresh Pro review.

## 5. Output additions

The existing seven-file output set is unchanged. The following fields must appear in the existing files:

### `00-controller-receive.yaml`

```yaml
Owner_authorized_visible_model_label:
operator_selected_visible_model_label:
model_label_exact_match:
model_selection_evidence_refs: []
```

### `01-product-and-permission-receipt.yaml`

```yaml
model_selection_authorization:
  Owner_authorized_label:
  Owner_authorization_evidence_class: direct_user_instruction
  operator_selected_label:
  operator_selection_evidence_class:
  exact_match:
  limitations: []
```

### `05-sentinel-result-bundle.yaml`

```yaml
model_selection_binding_result:
  authorized_label:
  selected_label:
  exact_match:
  evidence_refs: []
  backend_identity: unknown_or_not_attestable
```

No eighth output file is authorized.

## 6. Stop conditions added by package 003

Stop before branch creation when:

- candidate-003 or manifest-003 blob is absent/mismatched;
- the authorized model label is absent from the Owner startup message;
- actual selected label cannot be established;
- authorized and selected labels differ;
- a prior-turn label is being reused as if current;
- the controller is asked to treat a UI label as hidden-backend attestation;
- another active Mnemosyne write route is expected to move the protected master during the run window and has not been paused/completed.

Do not substitute another model, edit the authorization, or retry.

## 7. Fresh Pro return

Fresh Pro must separately adjudicate:

- package-003 and inherited package-002 identities;
- exact label binding and evidence class;
- branch/path/ref evidence;
- whether the operator-selection receipt is trustworthy enough for the bounded claim;
- whether any mismatch is a user setup, executor, product-surface or package defect.
