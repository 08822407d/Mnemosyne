# MNE-DR-005 — MNEMOSYNE-235 / 236 Dual-Failure Forensic Report

```yaml
report_id: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002-forensic-report
task_id: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002
audit_role: independent_read_only_dual_failure_forensic_audit_and_recovery_architecture
repository_writes_performed: false
git_objects_or_refs_created: false
retry_of_235_or_236_performed: false
cleanup_performed: false
G2A_issued: false
A1_executed: false
verdict: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
```

## 0. Evidence transport model and its limits

The original `MNEMOSYNE-235-repository-payload.zip` (139,424 B, SHA-256 `b99fd32ac091dc497412901d1a4b3b583646162f907284a00ef2f607a8c17c86`) was **not** uploaded and was **not** inspected by this audit. ZIP-container evidence (member ordering, CRC32, round-trip byte identity) rests entirely on the mechanical extraction receipt `MNEMOSYNE-235-PAYLOAD-ZIP-TO-TEXT-EVIDENCE-RECEIPT-001`, which attests 32/32 members round-trip byte-identical into the text evidence bundle. This audit independently verified the **bundle**, not the container: every claim below about payload bytes is a claim about the bundle contents cross-checked against the independently uploaded payload manifest, joined to the ZIP only through the receipt's attestation.

One transport-naming variance is on record: the receipt names the bundle file `…-text-evidence-bundle.json` while the uploaded file is `…-text-evidence-bundle.txt`. Declared bytes (452,856) and SHA-256 (`89c8eebb…794ee7a`) are identical to the uploaded file's observed values, so content identity holds; the variance is a receipt-metadata cosmetic defect, non-blocking under the Section 3 gate criteria (byte counts + SHA-256), and disclosed here.

## 1. Input-integrity gate — result: PASS_32_OF_32

Executed mechanically (Python; scripts retained in the audit workspace):

1. All 8 evidence files listed in `MNEMOSYNE-235-236-DUAL-FAILURE-NOZIP-EVIDENCE-MANIFEST-001` match declared bytes and SHA-256 exactly. The manifest itself (9th evidence input) cannot attest its own hash; its observed identity is 1,517 B, SHA-256 `4a79af3e57451ae5928f5c79319bab10c8083185bc018ba84a8cc9b0cf7c7fa2`. Total uploaded files: exactly 10 (task file + 9 evidence inputs).
2. Bundle header verified: source-ZIP identity, source-manifest identity (`488e27d9…5cc4c6`), `ordered_member_count: 32`.
3. All 32 members: Base64 decoded (RFC 4648, strict); decoded byte count == bundle `bytes`; decoded SHA-256 == bundle `sha256`; path, bytes and SHA-256 equal the same-ordered entry of `MNEMOSYNE-235-repository-payload-manifest.yaml`. 32/32 PASS.
4. Ordered path equality bundle↔manifest: PASS. Duplicate exact paths: none. Case-insensitive collisions: none. All paths ASCII.
5. Extraction receipt: 32 round-trip entries, path list equal in order, all `bytes_match`/`sha256_match`/`zip_member_byte_identical` true, `all_roundtrip_members_byte_identical: true`. Treated as mechanical transport evidence only, per contract.
6. Publishable-root filter over the manifest yields exactly **31** paths; the single exclusion is `README.md` (local payload metadata), exactly as MNEMOSYNE-236 §5.1–5.2 requires.

Conclusion: the source payload is internally healthy and exactly reconstructible. Neither failure originated in payload content.

## 2. Repository dynamic gate — start and end, zero drift

Read-only access only. REST reads were partially rate-limited on the shared egress IP; the audit switched to `git ls-remote` smart-HTTP and `raw.githubusercontent.com` + local `git hash-object`, which are mechanical equivalents for ref and blob identity. Container clock read 2026-08-19T16:19Z at capture (≈1 day behind the product-stated current date 2026-08-20); values are internally consistent and the start→end delta is what matters.

| Item | Start | End |
|---|---|---|
| `Mnemosyne` HEAD→ | `refs/heads/master` | identical |
| `master` | `e726dea818dca9418181775d0e7dcd62eb6c464a` | identical |
| `mnemosyne-235-f2-g2a-and-handoff-audit-closeout` | `e726dea818dca9418181775d0e7dcd62eb6c464a` | identical |
| compare expected-base…branch | same commit → identical, ahead 0, behind 0 | identical |
| Mnemosyne branches | exactly 2 (the two above) | identical |
| Open PRs (Mnemosyne) | 0 — triple-corroborated: zero `refs/pull/*/merge` refs; pulls page "0 Open / 297 Closed"; 297 `refs/pull/*/head` (max #302; gaps 170,171,244,250,265 are issue numbers in the shared sequence) | 0 |
| Open PRs from the 235 branch | 0 | 0 |
| validation-002 `master` | `e8e3296922185b4b70997c2351d6f39423f2cd4f` | identical |
| validation-002 branches | 18 (`master`, `tlr-v1-*` ×16, `v2a-sentinel-001-controller` @`d936cd2d…`) | identical |
| validation-002 PR refs | 0 ever | 0 |
| Five A1 branches (`v2a-a1-001-controller`, `-alpha`, `-beta`, `-order-alpha-beta`, `-order-beta-alpha`) | all five ABSENT (template requires `all_five_absent` at preflight) | all five absent |
| G2A/A1 state (live `current/fable5-…status.md`) | `G2A_issued: false`, `A1_branches_created: false`, `A1_execution: false`, `A1_runtime_failure: false` | blob unchanged |

Six-blob verification at master (raw fetch + `git hash-object`), start and end, all MATCH:
`current/fable5-cross-repository-safe-concurrency-research-status.md` = `0e02aab3e777000a159401ba9cf168b530ee7ac4`; registry = `aad3ed795fd426fceb581bc65ca2ce061be42742`; handoff-hardening TODO = `fd231986dab84d77f265264f599c98d64a91dbfd`; `handoff/handoff-current.md` = `d44a951a80153d2ad560b22b5c428e3f59447fd1`; root `README.md` = `b6d99d254a01a30c930bc44e3f99c448589734da`; `current/human-approved-spec.md` = `01f64a8223677829320c66dd46d3f172cc9155cc`.

Full sorted ref maps of both repositories are **byte-identical** start→end. Additional live↔payload cross-check: the frozen anchors inside the payload's G2A composite candidate (`validation master@e8e32969…`, fixture base `81f18eb5…`, sentinel controller head `d936cd2d…`) match today's live heads exactly. Recovery preconditions of MNEMOSYNE-236 §3 are all still satisfiable at audit end.

## 3. MNEMOSYNE-235 — forensic reconstruction

**3.1 Source-path correctness.** Verified: the correct member path
`raw/validation-reviews/MNE-DR-005-G2A-composite-closure-001/originals/WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-clause-source-matrix.yaml`
exists exactly once in manifest and bundle (29,844 B, SHA-256 `096ccce…`), with no case-sensitive duplicate and no case-insensitive colliding sibling. The payload gave the executor a single, unambiguous correct string.

**3.2 The structural hazard.** The token `MNE-DR-005-G2A-…-001` appears in **two casings inside one path**: lowercase `composite-closure` in the directory (display-name convention) and uppercase `COMPOSITE-CLOSURE` in the filename (task-ID convention). Census over the 31 publishable paths: **7 paths** carry both casings simultaneously — all seven DR-005 files whose filenames embed the task token (the eighth DR-005 file, `source-artifact-receipt.yaml`, does not). The reported drifted member is one of these seven. Any hand-assembly or string-derivation of these paths invites casing bleed from the directory segment into the filename segment; the payload is healthy but hazard-dense.

**3.3 Where the drift was introduced.** Per the blocked-run output (Chinese, executor-authored): the drift arose from 手工传输 ("manual transport") — one **transient staging tree entry** carried `…G2A-composite-closure-001…` in the filename component where the manifest requires `…G2A-COMPOSITE-CLOSURE-001…`. Content handling was byte-exact (hashes were checkable); the corrupted element was the **path string at `create_tree`-entry assembly**, i.e., after content extraction, before commit creation. Drift simulation performed by this audit confirms the geometry: the drifted string is (a) absent from the manifest under case-sensitive comparison, and (b) casefold-identical to the correct path — so either an exact-string allowlist assertion or a case-insensitive collision check against staged entries catches it deterministically.

**3.4 Task-design vs executor responsibility — shared, with a specific design gap.** MNEMOSYNE-235's contract verified content identity rigorously (§7.1 per-file SHA-256; §7.2 originals byte-identical) but **did not mandate mechanical path derivation**: no "path string comes ONLY from parsed `manifest.files[].path`", no "do not hand-type any tree path", no pre-write staging-plan equality assertion, no case-insensitive collision check. §7.11 ("changed-path set equals the authorized scope") catches wrong casing only if implemented as exact string comparison against manifest-derived strings — which the task did not require. The executor introduced the drift (proximate cause); the task design permitted the introduction path (contributory cause); the executor's verification then detected it pre-commit and failed closed without repair/retry — fully compliant with §9. MNEMOSYNE-236 §5.3 (parse-manifest-only paths, staging-plan string-exact assertion, CS-duplicate and CI-collision checks, "Do not hand-type any tree path") is the direct and, per the drift simulation, sufficient repair for this defect class.

**3.5 Reachable vs unreferenced effects.**
- Reachable: exactly one — the canonical branch ref was created, pointing at the pre-existing base commit `e726dea8…`. Zero content delta; no commit, no PR; both facts confirmed live at audit start and end.
- Unreferenced: prior `create_tree` calls produced tree/blob objects not referenced by any ref, including the miscased staging tree entry. The blocked run **disclosed their existence but preserved no object SHAs**, so they are not enumerable (GitHub exposes no unreachable-object listing; server-side GC lifetime is not observable or controllable). `ref_not_moved ≠ zero_repository_side_effect` is confirmed as the correct framing. No cleanup performed or authorized.

**3.6 Missing incident evidence** (what a compliant receipt would have preserved): the exact wrong path string as staged; each `create_blob`/`create_tree` request and verbatim response; returned object SHAs; which check first detected the drift; call timestamps/sequence; per-call tool identity beyond the operator-reported surface.

## 4. MNEMOSYNE-236 — forensic reconstruction

**4.1 Gates.** All four recorded gates report PASS with specific values: payload ZIP/manifest SHA-256 and 32-count; staging plan of 31 mechanically derived paths, root `README.md` excluded, no CS duplicates, no CI collisions; recoverability (master `e726dea8…`, master tree `de6474d8…`, branch identical/0/0, 0 open PRs, no competing PR, no new branch, no 235 retry); bounded target blobs `0e02aab3`/`aad3ed79`/`fd231986` matched with `handoff-current` at `d44a951a`, root README at `b6d99d25`, spec at `01f64a82`; G2A/A1 all false. Every one of those values is **externally corroborated by this audit's live reads** — the recorded gate output is internally consistent and matches reality, which gives it high credibility as far as it goes.

**4.2 Exact recorded stop point.** After all four gates; **during blob-object creation** ("这个失败的 blob 写入" — "this failed blob write"); explicitly **before final-tree construction**; therefore before any commit, ref movement, or PR. Disposition `MNEMOSYNE_236_BLOCKED`; no retry, no cleanup — compliant with §11.

**4.3 Preserved vs not preserved about the failed blob write.** Preserved: the phase, the fact of a single failed `create_blob`-class call, and no-retry compliance. **Not preserved:** the target file path; the requested encoding; the request payload/shape; the HTTP status; the error body; any returned or partial object SHA; how many blobs succeeded before the failure; timestamps. Per contract, this audit does not invent a filename or a raw error; none exists in evidence.

**4.4 Was a complete mechanically executable content-to-`create_blob` transport procedure supplied?** **No — and the gap maps exactly onto the failure.** The task's *path* mechanics are exemplary (§5.3, §7). Its *content transport* mechanics are underspecified: no encoding directive for `create_blob` (`base64` vs `utf-8`); no per-blob receipt (returned SHA + readback) requirement; no gate between blob phase and tree phase; and no failure-capture schema ("preserve the exact failing request/response") — §11 requires stopping but not evidencing. The run stopped correctly inside the one mechanical zone the contract left open, and the absence of a mandated receipt is precisely why the cause is now under-determined.

**4.5 Rule-in / rule-out for the recorded failure** (conditional on the "blob write" characterization being accurate):

| Candidate cause | Status | Basis |
|---|---|---|
| Object-ordering | **Ruled out** | `create_blob` takes no object references; ordering can only fail `create_tree`/`create_commit`. |
| File size (API limit) | **Effectively ruled out** | Largest member 29,844 B, orders of magnitude under Git-data API blob limits; connector-side truncation is a separate connector-semantics question. |
| Content invalidity | **Ruled out as inherent** | All 32 members byte-verified; all are valid UTF-8, no BOM, LF-only. |
| Encoding declaration / multibyte handling | **Cannot rule in or out** | No request preserved. Elevated prior: 21/32 members contain non-ASCII (CJK) bytes; raw-`utf-8` transport paths and JSON escaping of multibyte content are classic failure surfaces that `base64` transport eliminates. |
| Request shape (missing/invalid fields, malformed JSON) | Cannot rule in or out | No request preserved. |
| Connector semantics (schema, truncation, timeout, auth scope, rate/abuse limits, transient 5xx) | Cannot rule in or out | No response preserved. |
| Common cause with the Pro-receipt 422s | **Not established** | Different call class (`create_tree` contract failures vs a `create_blob` failure); no shared preserved identifier; the receipt itself disclaims the link. Hypothesis only. |

**4.6 Fields a future receipt must preserve, per object call (success and failure):** ISO-8601 timestamp and monotonic sequence number; endpoint + method + repository; the exact path string as sent (verbatim, plus its SHA-256); full request JSON with `content` replaced by `{bytes, sha256, declared_encoding}`; locally precomputed expected Git blob SHA-1; HTTP status; complete verbatim response body; returned object SHA; independent readback result (fetched bytes' SHA-256 vs manifest); retry count (must be 0). On any failure: emit the complete receipt for the failing call and stop — never a summary in place of the record.

## 5. Current Pro object-API investigation — evaluation

**5.1 What the receipt establishes.** From the current surface against `08822407d/Mnemosyne`: 2 `create_blob` successes and 10 `create_tree` successes (all SHAs preserved — the receipt discipline 235/236 lacked); repeated HTTP 422 failures of the exact form `tree.sha <id> is not a valid blob` across 13 listed object IDs; one `fetch_blob` 404 for an object an attempted tree construction expected, one `fetch_blob` success for a present object; and unchanged protective invariants (no reachable commit, no ref movement, no PR, no cleanup, no G2A/A1), which this audit confirmed live.

**5.2 422 semantics.** The error means: a tree entry declared as a blob (mode `100644`, type `blob`) referenced SHA X, and X **is not a blob object present in this repository's object database** at call time. Three mechanisms fit the observations: (i) X was computed locally (Git IDs are pure content-address functions computable offline) but never uploaded — **directly evidenced** by the 404 `fetch_blob`; (ii) X exists but is a tree — blob-vs-subtree typing confusion, e.g., a subtree SHA placed in a blob-typed entry; (iii) create-order violation — the tree call preceded completion of the blob's creation. The anomaly that `b49f205a4b07e5ae9d242f67e664b494cdc2a4c0` appears **both** in the successful-`create_blob` list **and** among the 422-failing IDs is cleanly explained by (iii) or by the receipt's lists being unordered; because the receipt preserves **no timestamps or sequence numbers**, (ii)/(iii)/list-artifact cannot be separated. That irresolvability is itself the finding: even an otherwise good receipt cannot answer ordering questions without per-call sequencing — hence §4.6's schema.

**5.3 Why locally known/computed object IDs are not proof of remote blob existence.** Content-addressing guarantees the conditional "if the object is present, it has this ID" — never the existential "it is present." GitHub's Data API validates every referenced SHA against the target repository's actual object store at call time; offline computation, presence in another repository or fork network, or an in-flight create all leave the reference dangling. The observed 404 is the in-hand empirical proof; the 422s are its `create_tree`-side symptom.

**5.4 Correct ordering (normative).** Per file: `create_blob(content: base64)` → record returned SHA → assert returned SHA == locally precomputed Git blob SHA-1 → readback fetch, decode, SHA-256-compare to manifest → only then reference in `create_tree` (single call, `base_tree` = base commit's tree, **flat slash-containing manifest path strings**, mode `100644`, type `blob`) → fetch the candidate tree recursively and verify the changed-path set equals the allowlist exactly (string-exact, casing-exact) and every entry SHA equals its recorded blob SHA → `create_commit(tree, parents=[base])` → non-force fast-forward `update_ref` → post-ref readback of every changed path. Flat-path + `base_tree` lets the server synthesize subtrees, removing the client-side blob-vs-tree typing surface entirely; if bottom-up assembly is ever used instead, directories must be `040000/tree` and only leaf files `100644/blob`.

**5.5 What the receipt does and does not prove about the external 236 failure.** Proves: the object API is reachable and writable from the current surface; unreferenced-object side effects are real, and enumerable when receipts are kept; the protective invariants held. Does **not** prove: any causal identity with 236's failed blob write — different call class, no shared preserved identifiers, and the receipt's own evidence-limit section says so. The relationship remains an investigation hypothesis.

## 6. Cross-cutting conclusions

1. Both external failures were **fail-closed successes and evidence failures**: correct stopping behavior, near-zero machine-readable incident evidence. The scarce resource is receipts, not caution.
2. The two defects live in different layers — 235 in path-string assembly (fixed by 236's §5.3, proven sufficient by drift simulation), 236 in content transport (still unspecified anywhere). A future contract must close the second gap with the §4.6 receipt schema and an explicit `base64` transport rule.
3. The repository is in the **best possible state for recovery**: base unmoved, branch empty at base, zero open PRs, all six anchor blobs intact, G2A/A1 false, five A1 branches absent, validation repo untouched, and the payload exactly reconstructible from attested transport. Nothing observed forecloses a clean single-commit recovery under a new task ID.
4. Verdict basis: 235 cause **sufficient**; 236 cause **partial** (stop point and rule-outs established; specific cause indeterminable because the raw request/response was never preserved — the contract's explicitly valid partial-cause condition); recovery architecture **ready** (see comparison + contract outputs).

```text
DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
```
