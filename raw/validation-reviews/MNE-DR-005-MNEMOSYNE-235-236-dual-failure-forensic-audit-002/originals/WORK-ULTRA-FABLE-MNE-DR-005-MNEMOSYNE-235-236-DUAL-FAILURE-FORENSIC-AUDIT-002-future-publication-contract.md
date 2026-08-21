# MNEMOSYNE-237 — Recovery Publication Contract (DRAFT, not authorized)

```yaml
contract_id: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002-future-publication-contract
proposed_task_id: MNEMOSYNE-237
status: DRAFT_FOR_OWNER_DECISION — this document authorizes nothing; MNEMOSYNE-235 and
  MNEMOSYNE-236 are never rerun; a fresh Owner instruction is required to execute
supersedes_execution_of: [MNEMOSYNE-235 (blocked, closed), MNEMOSYNE-236 (blocked, closed)]
```

## 1. Objective and hard invariants

Publish the frozen MNEMOSYNE-235 payload (31 publishable files), four bounded current-state updates, and six incident/result records to `08822407d/Mnemosyne` as **exactly one reachable commit** on the existing branch, then open **exactly one Ready pull request**, and stop. Invariants: read-only outside the enumerated write set; no force; no ref deletion; no cleanup of any prior unreferenced objects; no retry of any failed call; no G2A issuance; no A1 execution; no write of any kind to `mnemosyne-target-lifecycle-validation-002`; fail closed on any mismatch with disposition `MNEMOSYNE_237_BLOCKED`.

## 2. Frozen source identities

- Payload ZIP: 139,424 B, SHA-256 `b99fd32ac091dc497412901d1a4b3b583646162f907284a00ef2f607a8c17c86` (32 members).
- Payload manifest: `MNEMOSYNE-235-repository-payload-manifest.yaml`, SHA-256 `488e27d95ec21ab726195fb2bf33711fc1fcbe0785051702ee269407175cc4c6`.
- Sanctioned alternate transport when the ZIP is unavailable: text evidence bundle (452,856 B, SHA-256 `89c8eebb2ac95bbd0a1cbbd11a3d8ff45e26a80a30619e58b25c6a91e794ee7a`) together with extraction receipt `MNEMOSYNE-235-PAYLOAD-ZIP-TO-TEXT-EVIDENCE-RECEIPT-001` (10,021 B, SHA-256 `78c6f025dfd82ba454e6b722e854582d68124f4b56b73a12e975c47f8ff991ac`); the run must re-verify 32/32 members (Base64 decode, bytes, SHA-256, ordered path equality against the manifest) before any write. AUDIT-002 verified this gate as PASS_32_OF_32; MNEMOSYNE-237 must reproduce it independently.
- Base commit: `e726dea818dca9418181775d0e7dcd62eb6c464a`; base root tree: `de6474d84b5b4ada6b73b0f2545372f4bd50d975`.

## 3. Preconditions gate (all must PASS immediately before any object write; any failure → `MNEMOSYNE_237_BLOCKED`)

1. `Mnemosyne` master == base commit above; branch `mnemosyne-235-f2-g2a-and-handoff-audit-closeout` exists and == base (identical, ahead 0, behind 0). **Branch reuse is mandatory; creating any new branch is prohibited.** If the branch has moved or been deleted → BLOCKED.
2. Open PRs on `Mnemosyne`: 0; specifically none from the branch.
3. Bounded-update target blobs at master exactly: status `0e02aab3e777000a159401ba9cf168b530ee7ac4`; registry `aad3ed795fd426fceb581bc65ca2ce061be42742`; TODO `fd231986dab84d77f265264f599c98d64a91dbfd`; `handoff/handoff-current.md` `d44a951a80153d2ad560b22b5c428e3f59447fd1`; root `README.md` `b6d99d254a01a30c930bc44e3f99c448589734da`; `current/human-approved-spec.md` `01f64a8223677829320c66dd46d3f172cc9155cc`.
4. Live status file still records `G2A_issued: false`, `A1_branches_created: false`, `A1_execution: false`.
5. Validation repository untouched: master `e8e3296922185b4b70997c2351d6f39423f2cd4f`; the five A1 branches `v2a-a1-001-controller`, `v2a-a1-001-alpha`, `v2a-a1-001-beta`, `v2a-a1-001-order-alpha-beta`, `v2a-a1-001-order-beta-alpha` all absent; zero open PRs. (Read-only observation; a mismatch blocks 237 because the frozen G2A expected values would be stale.)
6. Full precondition observations are captured into the receipts ledger before the first write.

## 4. Machine-generated changed-path plan — exactly 41 paths, no hand-typing

The plan is produced by a script, never typed: (a) 31 payload paths = manifest `files[].path` filtered by the nine publishable roots (root `README.md` excluded — it is payload metadata, not repository content); the audit reproduced this filter mechanically and it yields exactly 31 with `README.md` the sole exclusion; (b) 4 bounded-update paths; (c) 6 record paths. Assertions before any write: plan length == 41; every payload path byte-equal to its manifest string; no case-sensitive duplicates; no case-insensitive collisions (this pair of checks is the proven kill-switch for the 235 defect class — the audit's drift simulation shows a re-drift is caught by either check); every record path absent from the base tree; every bounded-update path present.

Bounded updates (edit scope unchanged from MNEMOSYNE-236 §6, with references extended to name 235-BLOCKED, 236-BLOCKED, the Pro receipt, and AUDIT-002):
- `current/fable5-cross-repository-safe-concurrency-research-status.md` — additive lineage entries only; all authorization booleans remain false.
- `notes/registries/project-research-display-name-registry-v0.1.md` — additive row(s) only.
- `notes/todos/MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001.md` — additive annotation only.
- `handoff/handoff-current.md` — replaced to point at the 237 publication as current handoff surface.

Records (all under `notes/codex-task-results/`):
- `MNEMOSYNE-235-blocked-incident.md` — verbatim-preserving incident record: disposition, stop phase, the drifted-member identification, executor attribution, the explicit statement that per-call receipts/SHAs were not preserved, and the unreferenced-effects disclosure.
- `MNEMOSYNE-236-blocked-incident.md` — same discipline: four gate PASS values, stop phase (failed blob write before final tree), the enumerated not-preserved list, no-retry compliance.
- `MNE-235-236-PRO-RECOVERY-OBJECT-SIDE-EFFECT-RECEIPT-001.md` — the Pro receipt published verbatim as the durable object-side-effect disclosure (all tree/blob/422 SHAs).
- `MNEMOSYNE-237-result.md`, `MNEMOSYNE-237-verification.md`, `MNEMOSYNE-237-pr-finalization.md` — the run's own result, verification evidence (including the complete receipts ledger), and PR record.

## 5. Transport — Architecture A primary; Architecture B Owner-selectable fallback; C prohibited

**A (primary; requires shell+git surface).** Clone at base; verify HEAD == base; materialize the 41 files by script from verified sources (payload bytes from the re-verified bundle/ZIP; updates/records generated then frozen and hashed); `git add -A`; **verification core** (§6); one commit with message `MNEMOSYNE-237: recover F2 G2A and handoff-audit closeout publication (payload frozen from MNEMOSYNE-235; prior runs 235/236 BLOCKED; see notes/codex-task-results/)`; one non-force push to the existing branch; post-push readback. A failure anywhere pre-push leaves the remote untouched.

**B (fallback; connector-only).** For each of the 41 files in plan order: `create_blob(content=base64)`; record receipt (§7); assert returned SHA == locally precomputed Git blob SHA-1; readback-fetch the blob, decode, assert SHA-256 == source hash. Only after all 41 receipts pass: one `create_tree` with `base_tree` = base root tree and 41 flat slash-path entries (`mode 100644`, `type blob`, recorded SHAs) — never client-assembled subtrees; then the **verification core** (§6) on the returned tree; `create_commit(tree, parents=[base])`; non-force `update_ref`; post-ref readback. A tree entry may reference only a SHA with a passed blob receipt — this ordering rule plus per-call sequencing is the designed prevention for the Pro-receipt 422/dangling-reference class.

**C (Contents-API sequential commits) is prohibited**: it creates reachable partial states on failure, violating the one-reachable-commit invariant (see the architecture-comparison output).

## 6. Verification core (identical for A and B; all string comparisons byte-exact, casing-exact)

Pre-commit: the candidate tree's changed-path set (A: `git diff --name-status` base..index / `git ls-tree -r`; B: recursive fetch of the candidate tree diffed against the base tree) equals the 41-path plan exactly — no extras, no omissions, no casing variance; every payload entry's blob SHA equals the precomputed Git SHA-1 of the manifest-verified bytes; every record/update entry's blob SHA equals the hash of its frozen generated content. Post-ref: re-read all 41 paths from the branch head; byte/SHA-256 verify each; verify branch head's parent == base and master unchanged. Any mismatch at any point → stop, `MNEMOSYNE_237_BLOCKED`.

## 7. Per-object receipts ledger (mandatory in B for every call; in A for the push and readbacks)

Each entry: `seq` (monotonic), `timestamp_utc` (ISO-8601), `endpoint`, `method`, `repository`, `path_verbatim` + `path_sha256` (where applicable), `request_json` with `content` replaced by `{bytes, sha256, declared_encoding}`, `expected_git_sha1_local`, `http_status`, `response_body_verbatim`, `returned_sha`, `readback` `{fetched_sha256, match}`, `retry_count: 0`. **Fail-closed rule:** on the first failing call, emit that call's complete receipt (exact request as transformed above + exact verbatim response) inside the blocked report — a summary never substitutes for the record. This is the schema whose absence made the 236 cause indeterminable.

## 8. Pull request — exactly one, Ready, never merged by the task

Title: `MNEMOSYNE-237 — recover F2 G2A and handoff-audit closeout publication`. Base `master`, head the existing branch, Ready (not draft). Body must include: frozen payload identities; the 41-path plan; the statement that 235 and 236 were BLOCKED and are published as incident records in this PR; the Pro object-API receipt disclosure (unreferenced objects exist from 235/236/Pro attempts; none reused; no cleanup performed); AUDIT-002 reference and verdict line; the standing next-gate line (merge is an Owner decision; G2A/A1 remain unauthorized; `RECOMMEND_MERGE` is a recommendation only). The task records the PR URL/number in `MNEMOSYNE-237-pr-finalization.md` content prepared pre-commit with a placeholder? — **No placeholders:** the PR-finalization record is instead delivered in the run's chat/report output, not as a committed file, OR the PR body carries the finalization content. Resolution for this contract: `MNEMOSYNE-237-pr-finalization.md` is committed containing the *intended* PR title/body verbatim and the rule that the URL is reported in the run output; the live URL appears in the run report and the PR itself, avoiding any post-commit amendment. One reachable commit, untouched after the PR opens.

## 9. Stop rules

First failed gate, failed call, or failed verification → stop immediately; no retry; no cleanup; no second attempt at any step; emit the blocked report with the failing receipt (§7) and the disposition `MNEMOSYNE_237_BLOCKED`. Never delete or move any ref; never touch the validation repository; never issue G2A; never create any `v2a-a1-*` branch. A blocked 237 closes this ID permanently; any future attempt is MNEMOSYNE-238+ under a fresh Owner decision.

## 10. Owner decision points (before execution)

1. Approve this contract as MNEMOSYNE-237 (or amend).
2. Select surface: A (shell+git available) or B (connector-only).
3. Confirm the standing no-cleanup posture for all previously created unreferenced objects.
4. Confirm the six record paths and the bounded-update reference extensions.
