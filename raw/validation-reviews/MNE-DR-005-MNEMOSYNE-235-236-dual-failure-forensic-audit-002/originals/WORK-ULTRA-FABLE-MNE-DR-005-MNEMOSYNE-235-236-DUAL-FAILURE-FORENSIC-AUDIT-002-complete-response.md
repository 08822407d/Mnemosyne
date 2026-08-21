# WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002 — Complete Response

```yaml
task_id: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002
model_and_mode: Claude Fable 5 / Work mode / Ultra effort / Research OFF
run_role: independent read-only dual-failure forensic audit + recovery architecture design
attestations:
  repository_writes_performed: false
  git_objects_created: false           # no create_blob / create_tree / create_commit
  refs_created_moved_or_deleted: false
  pull_requests_opened: false
  retry_of_MNEMOSYNE_235_or_236: false
  cleanup_of_unreferenced_objects: false
  G2A_issued: false
  A1_executed: false
  validation_repository_written: false
  missing_236_raw_error_invented: false
input_integrity_gate: PASS_32_OF_32
repository_drift_during_audit: none (full ref maps byte-identical start to end)
verdict: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
```

## 1. Inputs and integrity gate

Exactly 10 files were present (task file + 9 evidence inputs). All 8 evidence files listed in the no-ZIP evidence manifest match their declared bytes and SHA-256; the manifest itself (structurally unable to self-attest) was recorded at 1,517 B, SHA-256 `4a79af3e…c7fa2`. The text evidence bundle parsed as JSON with the declared source-ZIP identity (`b99fd32a…17c86`, 139,424 B), source-manifest identity (`488e27d9…5cc4c6`), and 32 ordered members; **all 32 members Base64-decoded to byte counts and SHA-256 values equal to both the bundle's declarations and the same-ordered payload-manifest entries**; no duplicate paths, no case-insensitive collisions, all paths ASCII; the extraction receipt's 32/32 round-trip attestations and path list check out against the decoded set. The publishable-root filter yields exactly 31 paths with root `README.md` the sole exclusion. One disclosed variance: the receipt names the bundle `….json` while the uploaded file is `….txt` — bytes and SHA-256 identical, hence non-blocking under the Section 3 criteria. Gate result: **PASS_32_OF_32**. The original ZIP was not uploaded and was not inspected; all container-level claims rest on the extraction receipt, treated strictly as mechanical transport evidence.

## 2. Repository dynamic gate — start and end

Read-only reads only. REST calls were partially rate-limited on the shared egress IP; the audit pivoted to `git ls-remote` (smart-HTTP) and `raw.githubusercontent.com` fetches hashed locally with `git hash-object` — mechanical equivalents for ref and blob identity — plus HTML pulls-page corroboration. Container clock read 2026-08-19T16:19Z at end-capture (~1 day behind the product-stated date 2026-08-20; noted, immaterial to deltas).

**Mnemosyne, start and end (identical):** default branch `master` = `e726dea818dca9418181775d0e7dcd62eb6c464a` (the expected base); branch `mnemosyne-235-f2-g2a-and-handoff-audit-closeout` = same SHA (identical, ahead 0, behind 0); exactly 2 branches; **0 open PRs**, triple-corroborated (zero `refs/pull/*/merge` refs; pulls page "0 Open / 297 Closed"; 297 pull-head refs, max #302, gaps 170/171/244/250/265 being issue numbers); all six anchor blobs at master exact: status `0e02aab3…`, registry `aad3ed79…`, TODO `fd231986…`, `handoff-current` `d44a951a…`, root README `b6d99d25…`, human-approved-spec `01f64a82…`; live status lines `G2A_issued: false`, `A1_branches_created: false`, `A1_execution: false`, `A1_runtime_failure: false`.

**Validation repo, start and end (identical):** `master` = `e8e3296922185b4b70997c2351d6f39423f2cd4f`; 18 branches (`tlr-v1-*` set + `v2a-sentinel-001-controller` @ `d936cd2d…`, matching the status-recorded final head); zero PR refs ever; the **five A1 branch names** — `v2a-a1-001-controller`, `v2a-a1-001-alpha`, `v2a-a1-001-beta`, `v2a-a1-001-order-alpha-beta`, `v2a-a1-001-order-beta-alpha` (fixed verbatim in the G2A template, which requires `all_five_absent` at preflight) — **all five absent**. Live heads also still match the payload's frozen G2A anchors (validation master, fixture base `81f18eb5…`, sentinel head). Full sorted ref maps of both repositories are byte-identical start→end: **zero drift during the audit window**, and every MNEMOSYNE-236 §3 recovery precondition remains satisfiable.

## 3. Findings

**MNEMOSYNE-235 — cause SUFFICIENT.** The payload is healthy (correct target path present exactly once; no collisions), but 7 of 31 publishable paths embed the token `…G2A-composite-closure-001…`/`…G2A-COMPOSITE-CLOSURE-001…` in **two casings within one path** (lowercase directory convention vs uppercase task-ID filename convention) — a dense structural hazard. The drift was introduced at `create_tree` entry assembly during executor-attributed manual transport (casing bleed from directory into filename segment), detected pre-commit, and correctly failed closed. Responsibility is shared: executor proximate; task design contributory (content hashes were mandated, mechanical path derivation was not). The audit's drift simulation proves 236's §5.3 repair (string-exact staging-plan assertion; case-insensitive collision check) deterministically catches this exact defect. Effects: one reachable ref at the pre-existing base (zero delta) plus unreferenced staging objects whose SHAs were never preserved.

**MNEMOSYNE-236 — cause PARTIAL, by evidence gap.** All four recorded gates PASS with values this audit corroborated live, so the self-report is credible. The run stopped during blob creation, explicitly before final-tree construction — but preserved no failing path, encoding, request, HTTP status, error body, or SHA. The task's transport contract was complete on path mechanics and **incomplete on content transport** (no encoding directive, no per-blob receipt, no blob→tree gate, no failure-capture schema); the failure fell precisely in that unspecified zone. Ruled out: object ordering (`create_blob` takes no object refs), size (max member 29,844 B), inherent content invalidity (all 32 valid UTF-8, no BOM, LF-only). Indeterminate: encoding/multibyte handling (elevated prior — 21/32 members carry CJK bytes; base64 eliminates the class), request shape, connector semantics. No established common cause with the Pro 422s (different call class; receipt disclaims it). Per contract, the missing raw error is **not** invented; the partial-cause verdict is the designed outcome for this evidence state.

**Pro object-API receipt — evaluated.** It proves the object API is writable from the current surface (2 blobs, 10 trees, SHAs preserved) and that unreferenced side effects are enumerable *when receipts are kept*; the 13 `tree.sha … is not a valid blob` 422s are `create_tree` contract failures consistent with (i) locally computed SHAs never uploaded — directly evidenced by the one `fetch_blob` 404 — (ii) blob-vs-subtree typing confusion, or (iii) create-order violations; the `b49f205a…` both-lists anomaly is unresolvable absent per-call sequencing, which itself motivates the mandated receipt schema. Content-addressing gives "if present, then this ID," never existence — the normative order is blob→verify→readback→single flat-path `create_tree(base_tree)`→recursive verify→commit→non-force ref→readback. The receipt does **not** prove causal identity with 236's failure.

## 4. Recovery architecture and forward contract

Recommendation (advisory): **Architecture A** primary — deterministic local git worktree, single non-force push; failure leaves the remote untouched; byte/path guarantees come from git itself. **Architecture B** fallback where only the connector exists — base64 blobs with the per-call receipt schema, single flat-path tree, proven live by the Pro receipt; failure leaves only disclosed unreferenced objects. **Architecture C** (Contents-API sequential commits) rejected: reachable partial states on failure violate the one-reachable-commit invariant. Full analysis, including five adversarial simulations (case-insensitive FS, mid-run network failure, connector truncation, moved-base race, 422 recurrence), is in the architecture-comparison output. The drafted **MNEMOSYNE-237** contract (separate output; authorizes nothing) specifies: the 41-path machine-generated plan (31 payload + 4 bounded updates + 6 incident/result records including both blocked-incident records and the Pro receipt published verbatim), mandatory reuse of the existing branch iff still at base (else `MNEMOSYNE_237_BLOCKED`), the full preconditions gate including validation-repo/A1-absence checks, the per-object receipts ledger with fail-closed verbatim capture of any failing request/response, the shared verification core, one Ready PR (`MNEMOSYNE-237 — recover F2 G2A and handoff-audit closeout publication`, `RECOMMEND_MERGE`, never merged by the task), and permanent no-retry/no-cleanup rules.

## 5. Method record

Six sequential analysis passes were performed — (1) evidence-chain/mechanical gate, (2) payload forensics (hazard census, drift simulation, UTF-8 profile, taxonomy/HVAL/template probes), (3) live repository capture and corroboration, (4) 235 reconstruction, (5) 236 reconstruction + Pro-receipt evaluation, (6) architecture/contract synthesis — all by **one** Fable instance in one conversation: `independent_passes_not_distinct_agents`. Verification scripts and raw captures were retained in the audit workspace; every load-bearing number above was produced mechanically (Python/`git`), not transcribed by hand.

## 6. Limitations

The original ZIP was never inspected (attested transport only, as contracted). REST rate limiting forced the ls-remote/raw+`hash-object` pivot — mechanically equivalent for every value used, but the compare/pulls REST records for Mnemosyne exist as derivations plus HTML/ls-remote corroboration rather than raw REST bodies. The payload's validator script was statically checked (`py_compile` OK; emits `G2A_issued`) but deliberately not executed. Absolute timestamps for the 235/236/Pro events are unknown and left unknown (the only external anchor: Mnemosyne `pushed_at` 2026-08-19T12:36:25Z at audit start, unattributed to a specific ref). The 236 failing request/response does not exist in evidence and is reported as absent, not reconstructed. Container clock skew (~1 day) is disclosed above.

## 7. Deliverables

Eight files, this one included, all prefixed `WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002-`: `complete-response.md`, `forensic-report.md`, `timeline-and-object-effect-ledger.yaml`, `failure-classification-matrix.yaml`, `recovery-architecture-comparison.md`, `future-publication-contract.md`, `pro-owner-brief.md`, `output-manifest.yaml` (bytes + SHA-256 of the other seven).

```text
DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
```
