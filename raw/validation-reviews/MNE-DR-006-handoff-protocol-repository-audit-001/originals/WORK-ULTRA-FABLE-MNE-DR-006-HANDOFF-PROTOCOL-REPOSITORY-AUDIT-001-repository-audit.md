# WORK-ULTRA-FABLE-MNE-DR-006 — Repository Audit

```yaml
artifact_id: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001-repository-audit
task_id: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
canonical_task_id: FABLE5-MNE-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
artifact_role: repository_only_audit_of_handoff_correctness_mechanisms
execution_source_of_audited_repository: current/human-approved-spec.md
this_artifact_is_execution_source: false
repository: 08822407d/Mnemosyne
audited_master_sha: e726dea818dca9418181775d0e7dcd62eb6c464a
claim_classes:
  - VERIFIED_REPOSITORY_FACT
  - REPOSITORY_SUPPORTED_INFERENCE
  - OWNER_REPORTED_BUT_NOT_ARCHIVALLY_VERIFIED
  - DESIGN_RECOMMENDATION
  - UNKNOWN_REQUIRES_GOD_VIEW_EVIDENCE
```

Unless a claim is explicitly tagged otherwise, statements in this document about file contents, paths, and blob identities are `VERIFIED_REPOSITORY_FACT` observed at `master@e726dea818dca9418181775d0e7dcd62eb6c464a`.

---

## 1. Execution gates (results)

### 1.1 Input-integrity gate — PASSED

| check | expected (manifest) | observed | result |
|---|---|---|---|
| task-file bytes | 9449 | 9449 | PASS |
| task-file SHA-256 | b259fb3ed9e24f05314bf13fe758a233ae7b48c0305b9da2d0f941328775b34b | identical | PASS |
| task_id / canonical_task_id / display_name | as in manifest | identical in task file | PASS |
| uploaded task inputs | exactly two | exactly two (task file + input manifest) | PASS |
| Research | OFF | OFF (not used) | PASS |
| GitHub use | read-only | only GET-class operations performed | PASS |

### 1.2 Execution-time repository gate — PASSED

```yaml
repository: 08822407d/Mnemosyne (public, not a fork)
default_branch: master
master_sha_at_start: e726dea818dca9418181775d0e7dcd62eb6c464a   # 2026-08-19T06:59:41Z (UTC)
master_sha_at_end:   e726dea818dca9418181775d0e7dcd62eb6c464a   # recorded in the output manifest; equality required and observed
visible_branches: [master]           # exactly one
open_pull_requests: []               # zero
last_push_before_audit: 2026-08-19T01:16:09Z
snapshot_method: all file contents fetched pinned to master_sha_at_start; every fetched
  blob re-hashed locally (git blob SHA-1) and compared to the recursive tree
```

No write, branch, PR, issue, or comment was created. No drift was observed during the run.

### 1.3 Static expected identities — 17/17 PASSED

All seventeen path/blob tuples in the input manifest matched the pinned tree exactly (including `current/human-approved-spec.md @ 01f64a82…`, the three commands, the five guards, the TODO, the two defect notes, the four Handoff‑003‑generation artifacts, and the F2 status file). No mismatch, no missing path.

### 1.4 Read log

Content reads beyond the seventeen manifest files (each blob-verified against the pinned tree before reading):

```yaml
additional_content_reads:
  - README.md                                                            # 7259 B
  - commands/README.md                                                   # 3075 B
  - commands/list-mnemosyne-commands.md                                  # 1079 B
  - current/handoff-guidance-open-question.md                            # 3920 B
  - current/active-context.md                                            # 40682 B, PARTIAL read (headers + opening compact view only)
  - handoff/handoff-current.md                                           # 4019 B
  - handoff/startup-instructions.md                                      # 7435 B
  - handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package.md        # 1955 B (Handoff 001)
  - handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-002.md    # 5981 B
  - handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt.md         # 1178 B
  - handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt-002.md     # 1559 B
  - handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-post-merge-receive-rehearsal-contract-001.md  # 4395 B
  - notes/validation-protocol-defects/MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001.md    # 4919 B
  - notes/validation-protocol-defects/MNE-V2A-A1-PACKAGE002-RUNTIME-WRAPPER-INDEPENDENT-VERIFICATION-GAP-001.md  # 1611 B
  - notes/owner-decision-results/MNE-F2-V2A-A1-HANDOFF003-SCHEMA-ORACLE-REPAIR-OWNER-DECISION-001.md  # 2053 B
  - notes/startup-rehearsal-report.md                                    # 4756 B
  - notes/handoff-package-strategy-v0.1.md                               # 11121 B
  - notes/handoff-replay-scorecard-v0.1.md                               # 8066 B
  - notes/handoff-active-context-review.md                               # 4181 B
metadata_only_access:
  - recursive git tree at pinned SHA (paths + blob SHAs + sizes, all 1696 blobs)
  - one raw/ path checked by TREE METADATA ONLY (path→blob lookup, no content):
    raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
cold_sources_content_read: NONE
cold_source_classification: everything under raw/ (chatgpt-discussion exports,
  research-reports, validation-reviews exact-source archives, user-design-restatements)
  treated as preserved cold originals per the source-preservation guard §7 profile
  (default DO_NOT_READ / ON_DEMAND) and the input manifest; no mismatch trigger arose.
historical_conversation_exports_used: NONE (none supplied; prohibited)
```

---

## 2. Inventory of existing handoff-correctness mechanisms (§5.1)

### 2.1 Generic layer (applies to every Mnemosyne handoff)

| mechanism | path | authority class | mechanical? |
|---|---|---|---|
| Execution-source handoff principles | `current/human-approved-spec.md` §15 (plus §4, §7, §8, §12, §13, §17, §18, §19) | only execution source | no — normative prose |
| Prepare command | `commands/prepare-mnemosyne-handoff.md` | user-facing shortcut, non-execution-source | no — checklist prose; required package content list; mandatory `receiver_guidance_load` block in package **and** paired startup prompt |
| Receive command | `commands/receive-mnemosyne-handoff.md` | user-facing shortcut, non-execution-source | partially — defines a required first-response `mnemosyne_handoff_receive` YAML report, but fields are untyped, no expected/actual split, no identity pinning |
| Load-guidance command | `commands/load-mnemosyne-guidance.md` | user-facing shortcut, non-execution-source | partially — fixed guard list (~12 files + 3 conditional), 39 required behaviors, required `mnemosyne_guidance_refresh` report incl. `current_conversation_task_preserved` and `handoff_started: false` |
| Startup instructions | `handoff/startup-instructions.md` | non-execution-source | no — separates guidance refresh from handoff; forbids cross-context handoff detection; three-operation ordered receive sequence |
| Handoff package strategy v0.1 | `notes/handoff-package-strategy-v0.1.md` | non-execution-source strategy | no — three tiers (minimum/standard/extended), common mandatory fields, **five-state `receiving_operation_statuses` ladder** (receive → report → project guidance → mnemosyne refresh → substantive continuation), package-staleness rules |
| Handoff replay scorecard v0.1 | `notes/handoff-replay-scorecard-v0.1.md` | non-execution-source instrument | semi — two-stage review (executor claim vs maintainer review), 9 critical checks, 14-dimension weighted rubric, PASS/FAIL/BLOCKED semantics, provenance schema, and a 14-entry failure taxonomy (P0/P1) |
| Guidance-loading open question | `current/handoff-guidance-open-question.md` (HO-GUIDANCE-001) | live open-question record | no — settles the Mnemosyne-owned 3-step sequence and project-guidance-first rule; leaves target-project `mnemosyne_guidance: yes/no/unknown` open, task-local only |
| Handoff-current card | `handoff/handoff-current.md` | non-execution-source view | no — cross-conversation card; **currently stale** (last updated by MNEMOSYNE-140, points at the non-FABLE health-review route, not the live F2 route) |
| Guards | the five manifest guards plus `deep-research-report-delivery-correction`, `external-research-display-name`, `next-step-repository-write-visibility`, `agent-product-ready-pr-and-frontier-efficiency`, `pr-merge-branch-disposition`, and conditional `run-context-and-pr-provenance`, `github-single-active-pr-lineage`, `owner-review-branch-ledger` | user-approved behavior guards | no — behavioral requirements incl. execution-intent declaration schema, operator-flow mirroring (§3B), and §3B rule 9: "operator flow in the response and the repository/download artifact must agree; a material discrepancy blocks execution" |
| Early startup rehearsal | `notes/startup-rehearsal-report.md` (REH-2026Q2-0001, MNEMOSYNE-021, pass) | historical evidence | no — repository-startup rehearsal, not a handoff-receive rehearsal |

`REPOSITORY_SUPPORTED_INFERENCE`: the generic layer is **advisory prose plus untyped report shapes**. It contains no per-handoff identity pinning, no typed acceptance oracle, no publication receipt, and no mechanical closure check between what a package requires and what any adjudication instrument checks.

### 2.2 Route-specific F2 / V2‑A A1 layer (the repaired lineage)

```yaml
route: FABLE5_MNE_CROSS_REPOSITORY_SAFE_CONCURRENCY_F2_V2A_A1   # display MNE-DR-005
status_file: current/fable5-cross-repository-safe-concurrency-research-status.md
current_route_status: A1_PACKAGE_004_DURABLE_EXECUTION_NOT_AUTHORIZED_HANDOFF_003_REHEARSAL_REQUIRED
handoff_generations:
  handoff_001:            # prepared by MNEMOSYNE-232
    package: handoff/…-handoff-package.md            (blob d2dc7f9d…)
    startup: handoff/…-startup-prompt.md             (blob d5926454…)
    outcome: two failed receiver attempts (see failure chains FC-01, FC-02)
  handoff_002:            # prepared by MNEMOSYNE-233
    package: …-handoff-package-002.md                (blob 30699edc…)
    startup: …-startup-prompt-002.md                 (blob 868974db…)
    rehearsal_contract_001: …-post-merge-receive-rehearsal-contract-001.md (blob 1cb2f56c…)
    outcome: blocked pre-rehearsal by defect MNE-F2-V2A-A1-HANDOFF002-RECEIVE-SCHEMA-ORACLE-MISMATCH-001 (FC-03)
  handoff_003:            # prepared by MNEMOSYNE-234; current generation
    package: …-handoff-package-003.md                (blob bb60b9c1…)
    startup: …-startup-prompt-003.md                 (blob 76db593d…)
    canonical_schema: …-receive-report-schema-001.md (blob 52e2ce60…, schema_id MNE-F2-V2A-A1-HANDOFF-RECEIVE-REPORT-SCHEMA-001)
    rehearsal_contract_002: …-post-merge-receive-rehearsal-contract-002.md (blob d8c07a69…)
    receive_rehearsal_run: false
    guidance_loaded_in_receiver: false
owner_authorization: notes/owner-decision-results/MNE-F2-V2A-A1-HANDOFF003-SCHEMA-ORACLE-REPAIR-OWNER-DECISION-001.md (2026-08-19; blob 07b612bf…)
```

Handoff 003 design properties (all `VERIFIED_REPOSITORY_FACT`):

- **Single schema source**: schema‑001 is declared the sole source of field paths, types, and `{expected, actual, exact_match}` comparison semantics; package 003 and rehearsal contract 002 both bind to its exact path/blob and explicitly refuse to define a second field list.
- **Self-reference handling**: `package.blob.expected` is the one field a package cannot contain for itself; Startup Prompt 003 (created after the package blob exists) supplies exactly that one value, and the schema forbids any other alternate expected-value source.
- **Dynamic master rule**: no frozen pre-publication master SHA; receiver records `observed_start_sha`/`observed_end_sha` and `unchanged_during_receive_check`; acceptance additionally requires four-way equality with the originating conversation's pre-launch and adjudication-time master reads.
- **Tri-status separation**: `handoff_receive_status` / `identity_verification_status` / `substantive_continuation_status`, with a successful receive-only report forced to `BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE`.
- **Fail-closed comparison semantics**: raw Unicode string equality, no aliasing/case-folding/trimming, ordered-list equality, `null` ⇒ `exact_match:false`, no field omission on success.
- **Canonical ordered forbidden-action list** (11 items) compared as an exact ordered list.
- **Next-tier adjudication with one-Pro escalation**: rehearsal contract 002's 13-point mechanical procedure may be applied by a next-tier originating conversation; any missing/aliased/stale condition returns `BLOCKED_REQUIRES_PRO`.
- **Retirement gating**: the originating conversation may retire only after rehearsal acceptance, the receiver's separate guidance refresh, and task-preservation confirmation (steps 9–11).

### 2.3 Generic protocol vs route-specific repair — the distinction

`VERIFIED_REPOSITORY_FACT`: the defect notes and the F2 status file state explicitly that the route repairs did **not** modify the generic layer (`generic_prepare_command_modified_by_MNEMOSYNE_234: false`, `generic_receive_command_modified_by_MNEMOSYNE_234: false`, `human_approved_spec_modified_by_MNEMOSYNE_234: false`), and defect 233 states "A separate general handoff-protocol hardening audit remains a TODO. It is not implemented by this repair."

`REPOSITORY_SUPPORTED_INFERENCE`: consequently, today every property in §2.2 exists **only** for one route. A new handoff prepared tomorrow under the generic commands would again have: no pinned identities, no typed oracle, no publication receipt, no drift-resistant startup transfer, and no schema/oracle isomorphism guarantee.

---

## 3. Status and authority boundaries (exact)

- `current/human-approved-spec.md` is the only execution source (spec §4; restated in every command, guard, package, and status file read).
- Commands, guards, packages, startup prompts, schemas, rehearsal contracts, status files, `handoff-current`, `active-context`, TODOs, defect notes, owner-decision records, scorecards, and this audit are **non-execution-source**.
- Handoff receive establishes task-local state; guidance refresh applies behavior constraints and must not replace the received task or import maintenance live routes (spec §15; both commands; HO‑GUIDANCE‑001 settled part).
- Receive must not treat `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, `current/open-questions.md` as the action plan (receive command rule 9; load command; startup instructions).
- No current record authorizes: A1/G2A execution, A2–A7, V2‑B/V2‑C, validation-repository writes, Meta-Agent/real-target writes, generic handoff-guidance modification, conversation-export ingestion, automatic retry/repair/cleanup/branch deletion, or a receive rehearsal before repair merge + final readback (F2 status "No current record authorizes" block; Handoff‑003 owner decision prohibitions).
- Repository writes require separate task-local Owner authorization on top of platform permission (spec §18: `platform_permission` ≠ `mnemosyne_task_authority`); this audit had `writes_authorized: []` and performed none.

---

## 4. Repository-proven failure chains (§5.2 — summary)

Full structured records are in `…-failure-taxonomy.yaml` (FC‑01 … FC‑12). Narrative digest of the F2 lineage:

1. **FC‑01 — chat-visible startup drift (Handoff 001, first attempt).** `VERIFIED_REPOSITORY_FACT` (as a committed defect-note statement): "the old conversation's visible startup text used a wrong package path, package ID and receive key even though the repository's canonical startup artifact used the correct values" (defect MNE‑V2A‑A1‑PACKAGE003‑SOURCE‑ARCHIVE‑MANIFEST‑IDENTITY‑DEFECT‑001). What the source conversation actually rendered, and what the receiver actually did with the drifted text, are `UNKNOWN_REQUIRES_GOD_VIEW_EVIDENCE` (exports not archived). Failed gate: publication closure / operator-flow-vs-canonical-artifact equality; the generic guard rule closest to this (artifact-delivery §3B rule 9) is a source-side self-check with no mechanical enforcement. Route correction: rehearsal contracts require the startup text to be "copied from the final merged startup artifact. Do not manually retype or restate it", and Startup 002/003 embed the expected package blob so a drifted message now fails closed at identity verification. Correction validation: **not yet exercised** (`receive_rehearsal_run: false`).

2. **FC‑02 — source-archive path/blob closure failure (Handoff 001, second attempt).** Package 003 and three publication/transfer artifacts froze `source_archive_manifest` blob `7c2af723…` while the actual blob at that path on the merged tree was `6e90c8f1…`; the recorded blob resolved to no repository blob. The receiver **correctly blocked** (TODO‑001: "a merged handoff/package source-identity mismatch that the receiving conversation correctly blocked") — the fail-closed receiver behavior worked; the producer-side identity was wrong. Root cause limit is stated in the note itself: strongest evidence-bound explanation is a provisional/stale/incorrectly calculated identity propagated **without final-head path/blob readback**; not mechanically proven producer state (`REPOSITORY_SUPPORTED_INFERENCE`, and the exact producer action is `UNKNOWN_REQUIRES_GOD_VIEW_EVIDENCE`). Correction: Package 004 (canonical identity `6e90c8f1…` + independent five-part reconstruction receipt reproducing bytes 37074 / SHA‑256 `6e639f7b…`) + Handoff 002. Underlying archive integrity was independently verified; no content corruption.

3. **FC‑03 — receive-schema / rehearsal-oracle mechanical incompatibility (Handoff 002).** This audit independently re-derived the mismatch from the two artifacts: package‑002 required report fields (`package_id`, `package_blob_match`, `candidate_004`, `package_004_manifest`, `source_archive_manifest`, `archive_reconstruction_receipt`, `A1_status`, `execution_time_master`, …) vs rehearsal‑contract‑001 oracle fields (`package_id_exact`, `package_blob`, `candidate_004_blob`, `…_manifest_blob`, four separate `A1_*` booleans, `guidance_loaded_during_receive`, `repository_or_service_writes_during_receive`, `source_original_sha256`, and **no** `execution_time_master`). Name mismatches, boolean-vs-value mismatches, object-vs-scalar (`current_task_from_package` as structured object vs exact scalar), and asymmetric field sets in both directions — with no frozen mapping. A compliant receiver could be mechanically rejected; alias resolution by model interpretation would defeat the mechanical-oracle objective. Detection: caught **pre-rehearsal** by Pro adjudication (owner decision accepts "the prior Pro adjudication"); no receiver ran against the broken pair. Correction: schema‑001 single source + Handoff 003 triple.

4. **FC‑03 correction — mechanically re-verified by this audit.** On the pinned tree: schema‑001 defines exactly 40 `{expected,…}` fields; Package 003 supplies expected values for exactly 39 of them; the single uncovered field is exactly `package.blob` — the designed self-reference exception — and Startup Prompt 003 supplies `bb60b9c1…`, which equals Package 003's actual blob in the tree. Zero extra expected paths. All cross-referenced blobs among package/startup/schema/rehearsal/status/owner-decision (25+ tuples checked) match the pinned tree. `VERIFIED_REPOSITORY_FACT`: Handoff 003 is **structurally and identity-closed on today's master**; the only unvalidated element is **behavioral** — no fresh-receiver rehearsal has run.

5. **FC‑04 … FC‑09** (separate-message guidance fragility; retirement timing; frozen-vs-dynamic master; received-vs-ready; stale/wrong guidance; task contamination during refresh) and **FC‑10 … FC‑12** (Owner-reported other-route incomplete handoff; the two adjacent V2‑A A1 contract defects 231/232): see the taxonomy file. The cross-cutting pattern (`REPOSITORY_SUPPORTED_INFERENCE`): every committed protocol failure so far is a **producer/publication-side contract defect** — an identity, mapping, or temporal requirement frozen incorrectly or unverifiably before publication — while receiver-side fail-closed behavior worked whenever the receiver reached identity verification. The v0.1 replay-scorecard failure taxonomy covers receiver-behavior failures (14 entries, P0/P1) and contains **none** of these producer-side classes.

---

## 5. Evaluation of the current protocol (§5.3)

Verdict first (`REPOSITORY_SUPPORTED_INFERENCE`): **the generic prepare/receive/load commands plus guards are an advisory protocol, not an enforceable one.** They reliably establish authority boundaries, non-execution-source semantics, and fail-closed receiver *attitude*, and the receiver blocked correctly in the one archived identity-mismatch case. But every mechanically enforceable property (identity pinning, typed oracle, expected-value closure, self-blob handling, dynamic-master rule, drift-resistant startup transfer, publication readback) exists only in the route-specific Handoff 003 set — which has itself never been behaviorally validated. The two committed F2 protocol failures both passed through the generic layer without triggering any generic control.

Per criterion:

| criterion | current state | class |
|---|---|---|
| Single source of truth for package/startup/report schema | Generic: **three uncoordinated shapes** (receive command's report, strategy‑v0.1 common fields, scorecard schemas) with no isomorphism requirement — the exact precondition of FC‑03. Route: solved by schema‑001, route-locally. | VERIFIED (contents) + INFERENCE (risk) |
| Exact post-merge readback | Generic: absent. Route: required by rehearsal contracts (read back canonical artifacts and load-bearing identities from merge commit/current master) but is Owner-procedural prose, no receipt artifact schema exists. FC‑02's inferred cause is exactly a missing final-head readback. | INFERENCE |
| Self-reference handling | Generic: unaddressed (a package listing its own blob is impossible; nothing says so). Route: solved cleanly (startup supplies the one self-blob expected value). | VERIFIED |
| Typed machine-comparable acceptance oracle | Generic: none (report is untyped; scorecard is judgment-weighted). Route: schema‑001 + 13-point procedure — the strongest artifact in the repository, but "mechanical" still means *a model executing exact-comparison prose*; no executable validator or tool-run comparison exists, so residual model-interpretation risk remains nonzero. | VERIFIED + INFERENCE |
| Dynamic start/end state | Generic: absent. Route: dynamic-master rule with four-way equality; well designed; cost is manual SHA copying across two conversations by the Owner. | VERIFIED |
| Source-conversation responsibility | Generic: legacy pattern permits retirement at merge (`handoff-current.md`: "After the … handoff PR merges, the source conversation may retire"). Route: origination remains responsible until rehearsal acceptance + guidance + task-preservation (steps 9–11). The generic layer therefore still allows the FC‑05 hazard. | VERIFIED |
| Receiver fail-closed behavior | Working in the archived case (FC‑02 blocked correctly); required by spec §15 and both commands; Handoff 003 formalizes `null ⇒ exact_match:false`, no-retry, stop-and-wait. | VERIFIED |
| Guidance selection and loading | Receiver-side, execution-time-latest list inside the load command; not source-pinned, no completeness check, no per-handoff manifest; HO‑GUIDANCE‑001 unresolved for target-project routes. | VERIFIED + INFERENCE |
| Task preservation across guidance refresh | Designed-in everywhere (`current_conversation_task_preserved`, `handoff_started: false`, maintenance-route import prohibitions, rehearsal guidance-completion check naming the exact transferred task); no committed violation instance; heavily defended, unvalidated. | VERIFIED (design) |
| Owner operation count | Handoff 003 happy path: ≈8 manual Owner operations across ≥2 conversations (merge PR; trigger readback; record master SHA; open fresh Pro conversation; paste exact startup; copy full report back to origin; relay acceptance; send separate guidance message) plus confirmations. Every operation is a manual copy/paste channel — the same channel class that produced FC‑01. | INFERENCE (counted from rehearsal‑002 timing steps) |
| Pro-turn count | Happy path ≈3 receiver+origin substantive turns if origin runs next-tier (receive turn, guidance turn, adjudication turn), ≤1 additional Pro escalation on anomaly; origin at Pro adds more. Each failed generation historically consumed a full repair task + Ready PR + Owner decision (001→002→003), i.e., failure cost ≫ rehearsal cost. | INFERENCE |
| Next-tier mechanical adjudication | Formalized in rehearsal contracts (next-tier may apply the exact oracle; anomalies escalate `BLOCKED_REQUIRES_PRO`, ≤1 Pro turn to identify blocker + root-cause class); consistent with the frontier guard's capability split; never yet exercised. | VERIFIED (design) |
| Recovery cost | High and deliberate: no-retry + immutable predecessors + additive versions means every publication defect costs a new package/handoff generation, PR, and Owner decision. Three handoff generations and four execution-package versions exist for one route. | VERIFIED |
| Cold-source burden | Low by design: minimum receive evidence lists; cold reads only on mismatch trigger; compact manifests. Working as intended. | VERIFIED |
| Compatibility / migration | schema‑001 hard-codes route nouns (`candidate_004`, `package_004_manifest`, `A1_status.*`) — it is a **template by example**, not a reusable generic schema; ~15 other handoff packages/startup prompts in `handoff/` predate all of this and conform to none of it; `handoff/handoff-current.md` points at a superseded route. | VERIFIED + INFERENCE |

---

## 6. Mechanical cross-checks performed by this audit

All executed against the pinned tree `e726dea8…` (no repository modification):

1. 17/17 manifest static identities — match.
2. 8/8 blob identities asserted inside the two manifest defect notes (incl. the corrected archive-manifest blob `6e90c8f1…` at the disputed `raw/` path, checked by tree metadata only) — match.
3. 7/7 blob identities asserted in the F2 status file's handoff‑003 and TODO blocks — match.
4. Rehearsal‑contract‑002's three canonical-artifact blobs (schema/package/startup) — match, and Startup 003's embedded `package.blob.expected` equals Package 003's actual tree blob.
5. Schema↔package expected-value closure: 40 schema `expected` fields; 39 supplied by Package 003; the single gap is exactly the designed `package.blob` self-reference; zero extraneous paths.
6. FC‑03 mismatch re-derivation from primary artifacts (independent of the defect note's own field lists) — confirms the recorded defect.

`VERIFIED_REPOSITORY_FACT`: the repository is internally identity-consistent for every load-bearing handoff claim checked, at the audited SHA.

---

## 7. What remains unvalidated or unknown

```yaml
unvalidated:
  - Handoff 003 behavioral rehearsal (receive_rehearsal_run: false); the schema/oracle pair
    is structurally closed but has never been exercised by a fresh receiver
  - next-tier mechanical adjudication in practice (false PASS / false BLOCK rates unmeasured)
  - guidance refresh task-preservation under the new rehearsal flow
  - every generic-layer control (no generic handoff has ever run under a mechanical oracle)
unknown_requires_god_view_evidence:
  - exact producer action that generated the wrong blob 7c2af723… (committed history bounds
    but does not prove it)
  - exact content/behavior of the two failed Handoff-001 receiver attempts
  - the Owner-reported additional incomplete handoff on another route: identity, artifacts,
    failure mode, and receiver behavior (OWNER_REPORTED_BUT_NOT_ARCHIVALLY_VERIFIED per
    TODO-001; its exact source/receiver outputs were never ingested)
cross_route_root_cause: BLOCKED pending exact conversation exports; this audit asserts none.
```

---

## 8. Multi-pass review record (§6)

```yaml
passes_used:
  - protocol_inventory_and_evidence_pass
  - adversarial_failure_and_false_PASS_pass        # includes independent FC-03 re-derivation and the closure check in §6.5
  - architecture_and_options_pass                   # output: guidance-architecture-comparison artifact
  - implementation_and_validation_completeness_pass # outputs: validation-design + patch-spec artifacts
  - lead_disagreement_synthesis                     # reconciled: "Handoff 003 solves it" vs "only one route, unvalidated" → both recorded
independence_disclosure: independent_passes_not_distinct_agents
heterogeneous_review_claim: none_made
```

Principal disagreement resolved in synthesis: the adversarial pass argued Handoff 003's oracle is still model-interpreted prose and therefore not strictly "mechanical"; the inventory pass argued it is the intended mechanical design. Both are recorded: structurally closed (verified) but executor-dependent until a rehearsal and, ideally, a tool-side comparison exist (recommendation carried into the patch spec and validation design).
