NON_AUTHORIZING_CANDIDATE — DO NOT SEND TO A CONTROLLER UNTIL A LATER PRO REVIEW AND SEPARATE OWNER G2A.

# V2-A A1 Composite Controller G2A/Startup Candidate (Package 004 line)

```yaml
composite_candidate_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-COMPOSITE-G2A-CANDIDATE-001
produced_by_task: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
stage: V2_A
selected_cells: [A1]
cell_name: positive_independent_pair
artifact_class: non_authorizing_message_candidate_for_later_Pro_review
source_master_at_composition: e726dea818dca9418181775d0e7dcd62eb6c464a
G2A_authorized: false
A1_execution_authorized: false
validation_repository_written_by_composition: false
```

[C-01] This artifact is a candidate text only. It is not an Owner G2A, not a startup message, and not authorization for any branch creation, repository write, worker launch or validation cell. `G2A_authorized: false` is a fixed property of this artifact and cannot be flipped by review, quotation, transmission or lapse of time. Only a separate, later message actually sent by the Owner — after the Handoff 003 receive rehearsal is accepted and after a fresh Pro execution-time review of Packages 004/003/002/001 passes — can constitute the Owner G2A. When the Owner later issues that message, the issued message, not this candidate, is the sole official controller G2A/startup message for run MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001.

[C-02] Scope granted by the future issued message is exactly: the V2-A A1 positive independent pair. It does not authorize A2–A7, V2-B, V2-C, any real target, Meta-Agent writes, or Mnemosyne writes during A1.

## 1. Controlling identities (static; bound by this candidate)

[C-03] Top control layer — Package 004:

```yaml
run_decision_candidate_004:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-004.md
  blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
package_004_source_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/01-package-and-source-manifest.md
  blob: 8a978e1a075674e9f6d3909a1530c483abaf428d
package_004_required_file_count: 6
```

[C-04] Inherited layers — bound with exact identities:

```yaml
run_decision_candidate_003:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-003.md
  blob: 28da6ab6a3f3638292e83a7df511100d8d23b4b0
package_003_source_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-003/01-package-and-source-manifest.md
  blob: 7611773d861e065f539118853ec93026515f4065
run_decision_candidate_002:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002.md
  blob: a8b627b8aa74b5a1a5af19d3af485a17aa2cd0b7
package_002_source_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/01-package-and-source-manifest.md
  blob: 1f54f4711a44129c3dfee066aa2ab297f94718b7
run_decision_candidate_001:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md
  blob: bb140196a38d8b14f6eba9e2175cd45744efb23b
package_001_source_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/01-package-and-source-manifest.md
  blob: 12a480449b1dac45cd265864a812f399d19ec15c
```

## 2. Reading order and precedence

[C-05] The controller must read, in this order and in full, before any write: Package 004, then Package 003, then Package 002, then Package 001 — each via its run-decision candidate and source manifest above, and each package's exact files at the blobs listed in its own manifest. If any of the four candidate/manifest pairs is missing, unreadable, or does not match its bound blob, the controller returns `CONTROLLER_BLOCKED` and stops. Reading fewer than all four packages (for example, only Package 002) is itself a blocking condition.

[C-06] Precedence on conflict is 004 → 003 → 002 → 001, applied only within each package's declared supersession scope:

```yaml
package_004_controls_only:
  - source_review_archive_manifest_tuple:
      path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
      controlling_actual_blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
      superseded_incorrect_blob_for_scope: 7c2af723c395283aca23a5240847e46e6c97e93b
  - route_specific_handoff_publication_and_receive_rehearsal_closure
package_003_controls:
  - canonical_runtime_wrapper_transport
  - exact_Owner_sent_and_worker_received_wrapper_preservation
  - controller_three_way_wrapper_comparison
  - phase_appropriate_stops_after_wrapper_or_identity_mismatch
  - object_side_effect_disclosure
package_002_controls:
  - staged_model_label_binding_and_timing
package_001_controls:
  - fixture_branch_task_effect_blob_tree_order_output_retention_and_evidence_ceilings
```

Outside these scopes every lower-layer term remains mandatory and unmodified. Where Package 004 states an identity for the source archive manifest, the controlling blob is `6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a`; the Package 003 manifest's value `7c2af723c395283aca23a5240847e46e6c97e93b` is superseded for that tuple only, and Package 003 remains controlling for everything else it declares.

## 3. Validation repository static pins

[C-07] The following pins are static preconditions inherited through Packages 001–004. The controller verifies them read-only at preflight; it never refreshes them.

```yaml
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
material_class: public_synthetic_only
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture:
  ref: tlr-v1-fixture-base
  commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller:
  ref: v2a-sentinel-001-controller
  final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
protected_V1_ref_inventory: exactly_the_16_tlr_v1_refs_and_SHAs_frozen_in_package_001_manifest_section_4
five_A1_branch_names:
  - v2a-a1-001-controller
  - v2a-a1-001-alpha
  - v2a-a1-001-beta
  - v2a-a1-001-order-alpha-beta
  - v2a-a1-001-order-beta-alpha
required_A1_branch_state_at_preflight: all_five_absent
pull_requests: prohibited
```

## 4. Dynamic fields and placeholder discipline

[C-08] G2A-issuance fields. The following values do not exist in this candidate and must not be filled in it. They are supplied only by the Owner (with fresh Pro support) inside the actually issued G2A message, from then-current repository state and direct Owner/operator evidence. No assistant may infer them.

```yaml
G2A_issuance_fields_placeholders_only:
  protected_Mnemosyne_master: <PROTECTED_MNEMOSYNE_MASTER_AT_G2A>
  protected_Meta_Agent_master: <PROTECTED_META_AGENT_MASTER_AT_G2A>
  controller_Owner_authorized_visible_label: <CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL>
  controller_operator_selected_visible_label: <CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL>
  Alpha_Owner_authorized_visible_label: <ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>
  Beta_Owner_authorized_visible_label: <BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>
  execution_window_start: <EXECUTION_WINDOW_START_UTC>
  G2A_message_timestamp: <G2A_TIMESTAMP_UTC>
controller_selected_evidence_class: operator_observed_or_operator_reported
controller_exact_raw_string_equality_required: true
Alpha_operator_selected_visible_label: NOT_YET_OBSERVED_UNTIL_ALPHA_LAUNCH   # state token, not a fillable field
Beta_operator_selected_visible_label: NOT_YET_OBSERVED_UNTIL_BETA_LAUNCH    # state token, not a fillable field
backend_identity: unknown_or_not_attestable
```

`NOT_YET_OBSERVED_UNTIL_*_LAUNCH` renders the Package 002 state `not_yet_observed`: an explicit state, not an error and not a blank to fill, because the worker conversations do not exist at G2A time. The issued G2A must not contain asserted Alpha/Beta selected-label values, and must not claim that either worker has already selected a model.

[C-09] Wrapper-template fill schedule. Inside the two canonical wrapper templates of section 6, exactly two placeholder classes exist, with this exclusive schedule:

```yaml
fill_schedule:
  before_template_freeze:
    only: [ "<ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>", "<BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>" ]
    filled_by: controller
    value_source: the issued G2A's Owner-authorized labels, copied exactly
  at_exact_worker_launch:
    only: [ "__MNE_ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__", "__MNE_BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__" ]
    filled_by: operator
    value_source: current operator-observed or operator-reported UI raw string for that exact worker conversation
  per_sent_wrapper_substitutions_relative_to_frozen_template: exactly_one
```

Template freeze is blocked if an authorized-label placeholder is still unresolved; a selected-label placeholder resolved before its worker's actual launch is a mismatch and blocks. No other placeholder may ever be introduced into, or resolved inside, a canonical wrapper block.

## 5. Read-only preflight before any write

[C-10] On receiving the issued G2A, the controller first performs a completely read-only preflight and must verify, with nothing missing, unknown or mismatched:

- candidate/manifest identities of section 1 (all eight path/blob pairs) and each package's file set and count against its own manifest, including Package 004's six files and the controlling archive-manifest blob `6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a`;
- A0 accepted state; validation master, fixture commit/tree and A0 controller head equal to section 3; the complete 16-ref `tlr-v1-*` inventory exactly as frozen in Package 001 manifest section 4;
- the complete current branch and PR inventory of the validation repository, observed fresh at preflight (never pre-asserted in the G2A), with all five A1 branch names absent and no open PR;
- protected Mnemosyne and Meta-Agent masters equal to the issued G2A's frozen values, and no known competing route expected to move protected refs during the bounded execution window;
- material boundary (public synthetic only) and tool capability (GitHub only; exact branch/path scope enforceable);
- the controller Owner-authorized and operator-selected labels byte-identical as raw strings, both worker Owner-authorized labels present, and both worker selected labels in state `not_yet_observed`.

Any failed, missing or unknown condition returns `CONTROLLER_BLOCKED` and stops before any branch creation. The controller must not create branches, refresh expected values, repair a package, substitute a model, reinterpret a near match, or retry.

## 6. Branch creation, pre-worker outputs and canonical wrapper transport

[C-11] Only after preflight PASS may the controller create exactly:

```text
v2a-a1-001-controller  from validation master@e8e3296922185b4b70997c2351d6f39423f2cd4f
v2a-a1-001-alpha       from fixture@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
v2a-a1-001-beta        from fixture@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
```

It then writes only the Package 001 frozen pre-worker outputs `00-controller-receive.yaml`, `01-product-model-and-permission-receipt.yaml` and `02-branch-task-effect-map.yaml` on the controller branch, recording per Package 002: the controller authorized/selected exact match; both worker authorized labels; both worker selected labels as `runtime_pending`; and both immutable worker task payloads:

```yaml
Alpha_immutable_task_payload:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md
  blob: 9cb67f6e8b007941779326509db0b2d07fd035dd
Beta_immutable_task_payload:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md
  blob: 9544963bc40face1eb3caca190de6fe5f96802f5
```

Before Alpha is launched, the controller must also freeze both canonical wrapper templates of [C-12], with only the authorized-label placeholders filled per [C-09], into `02-branch-task-effect-map.yaml`. Both immutable task payloads and both frozen wrapper templates must exist before any worker result is returned, and must never be rewritten after a worker result appears. The controller then stops active work, returns the two frozen worker launch payloads to the Owner, and does not open, execute or monitor workers itself.

[C-12] Canonical runtime-wrapper transport (Package 003). The load-bearing runtime wrapper is the complete text block from `BEGIN` through `END`. Prose outside it is navigation only and cannot change the immutable package task. Canonical serialization is UTF-8 without BOM, LF line endings, no trailing spaces, and exactly one LF after the `END` line. Preserve exact line order and text; do not trim, reorder, case-fold, rewrap or otherwise normalize after canonicalization. Authorized and selected labels must each be one line and must not contain CR/LF. Exactly one role-specific selected-label placeholder may be replaced. `MNE-A1-WORKER-PROHIBITIONS-001` means the union of the exact Package 001 role task prohibitions plus: exact two-path write only; no branch/PR/evidence file; no peer runtime output; no other App/private material/quota; no model substitution, expected-value refresh, repair, retry, reset, force-push, rollback or cleanup; immediate stop on missing/unknown/mismatch. The profile ID alone is insufficient; controller and final reviewer verify the exact package path/blob.

The following two blocks are byte-exact mechanical copies from Package 003 `02-canonical-runtime-wrapper-transport-and-comparison-contract.md`, blob `20ca5ceb51c8991d29acef81124ec9276f8c1b2c`. They are the only valid A1 runtime-wrapper templates.

### 6.1 Alpha canonical wrapper template (verbatim)

```text
MNE_A1_RUNTIME_WRAPPER_V1_BEGIN
schema=MNE-A1-WORKER-RUNTIME-WRAPPER-001
run_id=MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
role=Alpha
task_id=MNE-V2A-A1-ALPHA-001
task_contract_path=notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md
task_contract_blob=9cb67f6e8b007941779326509db0b2d07fd035dd
repository=08822407d/mnemosyne-target-lifecycle-validation-002
branch=v2a-a1-001-alpha
required_current_branch_head=81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
owner_authorized_visible_label=<ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>
operator_selected_visible_label=__MNE_ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__
selected_evidence_class=operator_reported
backend_identity=unknown_or_not_attestable
prohibition_profile=MNE-A1-WORKER-PROHIBITIONS-001
MNE_A1_RUNTIME_WRAPPER_V1_END
```

### 6.2 Beta canonical wrapper template (verbatim)

```text
MNE_A1_RUNTIME_WRAPPER_V1_BEGIN
schema=MNE-A1-WORKER-RUNTIME-WRAPPER-001
run_id=MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
role=Beta
task_id=MNE-V2A-A1-BETA-001
task_contract_path=notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md
task_contract_blob=9544963bc40face1eb3caca190de6fe5f96802f5
repository=08822407d/mnemosyne-target-lifecycle-validation-002
branch=v2a-a1-001-beta
required_current_branch_head=81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
owner_authorized_visible_label=<BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>
operator_selected_visible_label=__MNE_BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__
selected_evidence_class=operator_reported
backend_identity=unknown_or_not_attestable
prohibition_profile=MNE-A1-WORKER-PROHIBITIONS-001
MNE_A1_RUNTIME_WRAPPER_V1_END
```

[C-13] Supersession of Package 002 prose wrappers. The in-message prose wrapper templates in Package 002 `03-revised-operator-flow-and-startup-messages.md` sections 4 and 5, and that file's section 3 instruction to preserve "the two worker runtime-wrapper templates verbatim below this message" (本消息下方两份 worker runtime-wrapper template 原文), are historical and superseded for runtime-wrapper transport. They must not be frozen into `02-branch-task-effect-map.yaml` and must not be sent to any worker. The Package 002 placeholder tokens `<ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>` and `<BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH>` are superseded by the canonical tokens `__MNE_ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__` and `__MNE_BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__` inside the section 6 blocks. Package 002's staged model-label timing, evidence-class definitions, block conditions and sequential-launch rules remain fully controlling; only its wrapper bodies, wrapper pointer sentence, wrapper placeholder token names and worker-return message formats are superseded by Package 003.

## 7. Worker launch, staged label timing and return

[C-14] At each role launch, the operator opens one fresh worker conversation, observes or selects the current visible label, and replaces only that role's selected-label placeholder in the already frozen canonical template, yielding exactly one substitution relative to the frozen template. The Owner sends the complete wrapper block once, together with this exact instruction (byte-exact from Package 003 `03-revised-worker-launch-return-and-controller-resume-flow.md`, blob `a8447a57d4be9f8880ce758b87f38a1edb10cf1a`):

```text
@GitHub
The canonical wrapper block and immutable task path/blob inside it are the only authority-bearing inputs. Before write, perform package-003 full-wrapper and package-task checks. Mismatch means WORKER_BLOCKED_BEFORE_WRITE. On PASS, execute the immutable package-001 worker task, echo the complete received canonical wrapper block verbatim plus its SHA-256 in the raw result, return exact Git/model/incident evidence, and stop. No branch/PR/evidence file, peer output, other App/quota, substitution, repair or retry.
```

[C-15] Staged timing (Package 002): authorized labels for Alpha and Beta are bound at controller G2A; each selected label is bound only at that worker's actual launch, from current operator-observed or operator-reported evidence for that exact conversation. A recommendation, planned selection or model self-report is not an operator-selected receipt. Before any repository mutation each worker performs the Package 002 pre-write gate and the Package 003 full-wrapper reconstruction and exact comparison of the block, labels, task path/blob, repository, branch/base and profile. Any required field missing, unknown or mismatched returns `WORKER_BLOCKED_BEFORE_WRITE` with no write, no branch movement, no model substitution and no retry. Launch order is Alpha, then only after Alpha completes exactly, Beta. Explicit Alpha blocked/fail/disputed means Beta is not launched. Neither worker may receive or read the peer's final branch head or output before completing its own branch.

[C-16] Owner return after each worker must include two separately delimited objects in exactly this format (byte-exact from Package 003 `03-revised-worker-launch-return-and-controller-resume-flow.md`):

```text
--- <ROLE> OWNER-SENT WRAPPER BEGIN ---
<exact complete block sent>
--- <ROLE> OWNER-SENT WRAPPER END ---
<ROLE> OWNER-SENT WRAPPER SHA256: <sha256 of exact canonical block>

--- <ROLE> WORKER RAW OUTPUT BEGIN ---
<complete unedited worker output>
--- <ROLE> WORKER RAW OUTPUT END ---
```

The worker raw output must itself echo the complete received canonical block verbatim and report `received_wrapper_sha256` plus its self-check fields. Worker outputs are returned unedited; worker self-reported conclusions are never treated as authoritative.

## 8. Controller resume: three-way comparison, orders and outputs

[C-17] Controller resume performs the Package 001 Git checks plus, for each role, the Package 003 three-way wrapper comparison. The controller computes SHA-256 over all three canonical UTF-8/LF representations and independently compares: the expected frozen template with one selected-label substitution; the exact Owner-sent block; and the exact worker-received echo. A positive result for a role requires all three byte-identical, all three SHA-256 values equal, exactly one permitted selected-label substitution relative to the frozen template, and every fixed field exact — recorded in the Package 003 `runtime_wrapper_comparison` schema (expected/Owner-sent/worker-received verbatim blocks and SHA-256 values, the three pairwise equality fields, `only_role_selected_label_placeholder_changed`, `G2A_authorized_label_match`, `task_path_blob_repository_branch_base_profile_match`, and `comparison_result: PASS | FAIL | DISPUTED_REQUIRES_FRESH_PRO`). Wrapper equality proves only equality of preserved text representations, not hidden backend identity or provider-signed telemetry. A worker self-PASS never substitutes for the controller comparison; if the controller comparison fails or is disputed, the role is not accepted regardless of self-report.

[C-18] Only if both worker Git contracts and both wrapper comparisons are exact PASS may the controller create, per Package 001:

```text
v2a-a1-001-order-alpha-beta  from the verified Alpha worker final head
v2a-a1-001-order-beta-alpha  from the verified Beta worker final head
```

Each order branch applies the peer's exact frozen blobs in one controller-owned integration commit; order commits may not be hand-edited to force equality. Both final root trees must equal `2b919544aecfbd1634e5f136af22571f2e8d9fd0`. The controller writes only the ten frozen result paths under `runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/` (00, 01, 02, 03, 04, 05, 06, 07, incidents/incident-ledger.yaml, 08 — exactly as listed in Package 001 manifest section 7), and must not create an eleventh output. `01-product-model-and-permission-receipt.yaml` may later be updated in place with the independently preserved worker receipts; `03`/`04` each store the expected, Owner-sent and worker-received wrapper blocks plus exact comparison fields; `08` summarizes both comparisons and any partial-state disposition. After the final bundle and after-checks, the controller stops and returns all branch heads, commits, trees, blobs, the three role model receipts, both wrapper comparisons, protected refs, the incident ledger and all limits to a fresh Pro adjudication. No PR is created and no branch is cleaned.

## 9. Phase dispositions and object-side-effect honesty

[C-19] Phase-specific stop rules (exact tokens):

```yaml
pre_write_mismatch: WORKER_BLOCKED_BEFORE_WRITE
known_Alpha_mismatch_before_Beta: STOP_NO_BETA
any_mismatch_before_orders: CELL_FAIL_NO_ORDER_CONSTRUCTION
mismatch_after_partial_writes: PRESERVE_PARTIAL_STATE_STOP_NO_RETRY
```

If Alpha blocks or fails: do not launch Beta; preserve the three initial branches and controller pre-worker outputs; return to fresh Pro. If Beta blocks or fails after Alpha writes: preserve Alpha's exact branch evidence; construct no order branch; record the partial state and stop.

[C-20] Object calls may succeed before `update_ref`. Incident evidence must record returned object SHAs when available, unknown unenumerable object risk when ambiguous, and ref state separately. `ref_not_moved` cannot support a `zero_repository_side_effect` claim. Partial object or ref state is preserved exactly; no retry, rollback, reset, force-push or cleanup is authorized.

## 10. Prohibitions in force throughout A1

[C-21] For every A1 execution conversation (controller and both workers), all of the following are prohibited: Web; Deep Research; Fable; any other App; private material; external quota; model substitution; expected-value refresh; package or fixture repair; retry after failure or block; reset or force-push; rollback; cleanup or branch deletion; auto-merge; creating any PR; creating any branch outside the frozen five-branch map; writing Mnemosyne or Meta-Agent or any real target during A1; modifying validation master, fixture, any `tlr-v1-*` ref or `v2a-sentinel-001-controller`; changing a worker message after the first worker result; exposing a peer final head or output to the other worker before completion; adding any generated, shared or global effect; running A2–A7, V2-B or V2-C; and any eleventh controller output.

## 11. Owner-visible stop conditions

[C-22] Return to fresh Pro without retry when any conversation reports: source/manifest/ref/branch mismatch; controller label mismatch; missing worker authorized label; worker selected-label mismatch or uncertainty; any wrapper three-way comparison FAIL or DISPUTED; controller branch creation ambiguity; worker branch not at fixture base; unexpected path/tree/blob/commit count; peer runtime-output dependency; order tree mismatch; protected ref movement; a request to create a PR, repair a package or fixture, or run another cell; or inability to enforce the exact tool and branch scope.

## 12. Evidence ceiling and retention

[C-23] Exact raw-string label equality supports only the claim that the authorized and operator-reported/observed visible labels match for the named conversation. It does not prove hidden/backend identity, provider routing or weights identity, that another conversation used the same backend, correctness of the worker output, or wall-clock concurrency. A1 tests branch/effect/order independence under the exact static semantic oracle of Package 001 only; sequential operator launch creates no simultaneity claim. The A0 controller branch remains immutable. All five A1 branches remain retained until the full raw bundle is complete or the run is explicitly abandoned, fresh Pro adjudication is complete, the Owner decides the result and any correction, durable result identities no longer depend on branch retention, and cleanup receives a separate explicit authorization.

## 13. Non-authorization closure

[C-24] Required sequence before this candidate's content may be issued as a real message: Handoff 003 post-merge receive rehearsal accepted → fresh Pro execution-time review of Packages 004/003/002/001 (including this candidate) → separate Owner G2A that fills only the [C-08] issuance fields and reproduces every static binding of this candidate exactly. No review, rehearsal, publication, quotation or transmission of this candidate authorizes A1, creates any branch, moves any ref, or constitutes G2A. This artifact's own authority state is, and remains, `G2A_authorized: false`.
