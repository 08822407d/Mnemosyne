# Recovery Architecture Comparison — MNEMOSYNE-237 Candidate Transports

```yaml
comparison_id: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002-recovery-architecture-comparison
status: ADVISORY_ONLY — nothing in this document authorizes execution, repository writes,
  G2A issuance, or A1 execution; the Owner decides
```

The three candidate architectures for publishing the frozen 32-member payload (31 publishable files) plus bounded updates and incident records as **one reachable commit** on the existing branch:

- **A — Deterministic local Git worktree.** Clone at base `e726dea8…`, materialize files from the verified payload into a worktree with a mechanical copier, `git add`, verify the index against the manifest, one local commit, one non-force push, post-push readback. Requires an execution surface with local git + filesystem (e.g., a Codex-style container or CI runner).
- **B — Connector object API, receipt-disciplined.** The GitHub Data API path 235/236 attempted, hardened: per-file `create_blob(base64)` with the per-call receipt schema, single flat-path `create_tree(base_tree)`, `create_commit`, non-force `update_ref`, readback. Requires only the GitHub connector.
- **C — Contents API sequential commits.** `PUT /contents/{path}` per file (~41 commits). Requires only the connector.

## Criterion-by-criterion

**1. Exact-byte and path-case guarantees.**
- A: Strongest. Bytes go through the local filesystem verbatim; `git hash-object`/index SHAs are computed by git itself; a `git ls-tree -r` diff against the manifest allowlist verifies every path string-exactly and every blob SHA before anything is pushed. One residual hazard is the case-insensitive local filesystem (see simulation S1).
- B: Strong *if* the §4.6 receipt discipline is followed: base64 removes encoding ambiguity (decisive against the 236 indeterminate class — 21/32 members carry CJK bytes); returned-SHA == locally-precomputed-SHA plus readback proves byte identity; recursive candidate-tree verification proves path exactness pre-commit. Without the discipline, this is exactly the architecture that failed twice.
- C: Weak. Content is base64 (fine), but path casing rides on ~41 separately hand-addressed URL paths with no single pre-commit set-equality check; per-call verification is possible but there is no "candidate tree" moment at which the whole change is checkable before it becomes reachable.

**2. Partial reachable-state risk (the decisive criterion).**
- A: None until the single push; a failure at any earlier step leaves the remote untouched. The push itself is atomic per ref.
- B: None until `update_ref`; failures before it leave only unreferenced objects (disclosed, no cleanup), exactly like 235/236 — the fail-closed geometry both blocked runs already demonstrated.
- C: **Structural violation.** Each PUT is an immediately reachable commit; a failure at file k of 41 leaves a *reachable half-published state* on the canonical branch, which the standing rules then forbid repairing (no cleanup, no force). C converts any mid-run failure into a contaminated branch. This alone rejects C, independent of its 41-commit history noise and its violation of the one-reachable-commit contract term.

**3. Auditability.**
- A: Excellent and cheap — the worktree state, the index listing, the commit object, and the push receipt are all locally capturable; a single `git ls-tree -r` output is a complete manifest-vs-tree proof.
- B: Excellent but expensive — ~35 object calls, each needing the full receipt schema; the upside is that the receipts double as the incident evidence 235/236 lacked.
- C: Poor — evidence is scattered across ~41 commit responses with no unified pre-commit artifact.

**4. Required product/tool capability.**
- A: Needs a shell/container surface with git and network push rights — the heaviest requirement, and the one variable the Owner must confirm (the 235/236 operator surface reportedly had repo write *actions*; whether it exposes a shell is an Owner-side fact this audit cannot attest).
- B: Needs only the GitHub connector already demonstrated live by the Pro receipt (blob and tree creation both succeeded from the current surface).
- C: Same connector; lowest capability bar, but see criterion 2.

**5. Model/executor freedom (drift surface).**
- A: Smallest. The copier and verifier are scripts; the executor's only free text is the commit message. Path strings never pass through model output.
- B: Medium. Every path string appears in constructed JSON; the §5.3 mechanical-derivation rule plus staging-plan assertion must be re-imposed verbatim, and the receipt schema removes silent improvisation.
- C: Largest. ~41 hand-addressed calls, each an independent opportunity for the 235 defect class.

**6. Stop/recovery semantics under the standing rules (stop on first failure, no retry, no cleanup).**
- A: A stop leaves zero remote effects (pre-push) — the cleanest possible blocked state; a fresh future task can start from scratch with no disclosure debt beyond the report itself.
- B: A stop leaves unreferenced objects — acceptable and precedented, but each blocked attempt accumulates disclosure obligations.
- C: A stop can leave a reachable partial publication that no successor task may silently repair — the worst possible blocked state.

## Adversarial simulations

**S1 — Case-insensitive local filesystem (A's specific hazard).** On a case-insensitive FS, two payload paths differing only by case would silently collide at materialization. Mitigations, both mandatory in the contract: (a) this audit already proved the payload has **zero** case-insensitive collisions, so faithful materialization cannot collide; (b) the verifier compares `git ls-tree -r` output (which reflects exact index strings, not FS display) against the manifest allowlist string-exactly, so any FS-induced rename is caught pre-commit. Residual risk: negligible with (b) enforced; the check is the same one that would have caught 235.

**S2 — Mid-run network failure.** A: worktree survives locally; run stops; remote untouched; blocked report only. B: stop mid-blob-phase; unreferenced objects disclosed with full receipts (the failing call's receipt is the required output). C: reachable partial state — contract breach by geometry.

**S3 — Connector truncation / content mangling.** A: not applicable (no connector on the content path). B: caught deterministically by returned-SHA ≠ locally-precomputed-SHA or by readback mismatch, before the tree references anything. C: caught only if per-PUT readback is added, and by then the bad commit is already reachable.

**S4 — Base moved (master ≠ `e726dea8…`) between gate and write.** All three must re-verify immediately before the mutating step and stop as `MNEMOSYNE_237_BLOCKED` on mismatch. A: recheck before push (compare-and-swap semantics of non-force push also protects). B: recheck before `update_ref`; non-force update fails safely on a moved ref. C: no equivalent guard exists per-PUT — another rejection ground.

**S5 — Recurrence of the 422 / dangling-reference class.** A: impossible by construction (git computes and uploads objects itself; the pack push is internally consistent). B: prevented by ordering discipline — a tree entry may reference only a SHA that has a recorded successful `create_blob` receipt *and* a passed readback; the b49f205a-style ambiguity is prevented by per-call sequence numbers. C: not applicable (no raw tree calls), but irrelevant given criterion 2.

## Recommendation (advisory)

**Primary: A**, because it is the only architecture whose failure mode is "nothing happened remotely," whose byte/path guarantees come from git itself, and whose verification artifact (`ls-tree` vs manifest) is a single mechanical comparison. **Fallback: B**, contract-hardened per §4.6/§5.4 of the forensic report, for the case where the Owner's execution surface lacks a shell — B is demonstrably live today (Pro receipt) and its residual failure geometry (unreferenced objects only) is precedented and acceptable. **Rejected: C** — it structurally violates the one-reachable-commit requirement and converts any mid-run failure into a reachable half-published branch that the no-cleanup rule then freezes in place.

The future-publication-contract output encodes A as the primary procedure with B as an Owner-selectable alternate, a single shared verification core, and identical fail-closed reporting for both.
