# Owner Brief — MNEMOSYNE-235/236 Dual Failure, Audit 002

```yaml
brief_id: WORK-ULTRA-FABLE-MNE-DR-005-MNEMOSYNE-235-236-DUAL-FAILURE-FORENSIC-AUDIT-002-pro-owner-brief
verdict: DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
audit_mode: read_only — zero writes, zero retries, zero cleanup, no G2A, no A1
```

**Situation.** Two consecutive publication attempts of the frozen F2 closeout payload blocked before creating any reachable commit: 235 on a self-detected path case-drift during tree staging; 236, after all four preflight gates passed, on a single failed blob write it did not evidence. A separate Pro-side object-API investigation reproduced a related tool-contract failure class (`tree.sha … is not a valid blob`, HTTP 422) with full receipts. This audit verified the evidence chain and both repositories read-only.

**Proven (mechanically, this audit).**
- Evidence gate PASS_32_OF_32: all 8 manifest-listed evidence files hash-exact; all 32 payload members Base64-decode to byte/SHA-exact matches of the manifest; the publishable filter yields exactly 31 files with only `README.md` excluded. The payload is healthy and exactly reconstructible without the original ZIP.
- Repository state ideal for recovery and **unchanged across the audit window** (full ref maps byte-identical start→end): master = branch = `e726dea8…`, 0 open PRs (triple-corroborated), all six anchor blobs exact, `G2A_issued/A1_* = false`, the five A1 branches absent in the validation repo, and the payload's frozen validation-repo anchors still match live heads.
- 235's cause is **sufficiently determined**: executor casing bleed during manual path assembly, inside a payload where 7 of 31 paths carry the same token in two casings; the audit's drift simulation proves 236's §5.3 checks would each have caught it. Task design was contributory (no mechanical-path-derivation mandate); detection and fail-closed stop were correct.
- 236's recorded gate values are all externally corroborated — its self-report is credible.

**Unknown (and provably unknowable from preserved evidence).** The specific cause of 236's failed blob write: no path, encoding, request, status, or error body was preserved. The audit rules **out** ordering, size, and inherent content invalidity; leaves **indeterminate** encoding/multibyte handling (elevated prior — 21/32 files carry CJK bytes; base64 transport eliminates the class), request shape, and connector semantics; and finds **no established link** to the Pro 422s (different call class). The Pro receipt's own b49f205a anomaly (one SHA in both the success and failure lists) is unresolvable because the receipt lacks per-call sequencing — which is exactly why the proposed contract mandates a per-call receipt schema.

**Risk.** Low and bounded. No reachable contamination exists anywhere; the only repository side effects are the empty branch ref plus unreferenced objects from three sources (235, 236 — SHAs unpreserved; Pro — SHAs fully listed), none reused, none cleaned, all disclosed. The main forward risks are a third evidence-poor failure (mitigated by the receipt schema) and a reachable-partial-state architecture (mitigated by rejecting the Contents-API path).

**Recommendation.** Approve **MNEMOSYNE-237** per the drafted contract: one reachable commit of 41 paths (31 payload + 4 bounded updates + 6 incident/result records) on the existing branch, one Ready PR, `RECOMMEND_MERGE`, no merge by the task. Transport **Architecture A** (local git worktree, single push — failure leaves the remote untouched) if a shell surface is available; otherwise **Architecture B** (object API with base64 blobs, per-call receipts, single flat-path tree) — proven live by the Pro receipt. Architecture C (per-file Contents-API commits) is rejected: it creates reachable half-published states that the no-cleanup rule would then freeze.

**Decisions requested.**
1. Approve/amend the MNEMOSYNE-237 contract (a fresh Owner instruction is required; nothing is authorized by the audit).
2. Select surface: A (shell+git) or B (connector-only).
3. Confirm the standing no-cleanup posture for all previously created unreferenced objects.

```text
DUAL_FAILURE_PARTIAL_CAUSE_RECOVERY_ARCHITECTURE_READY_WITH_UNKNOWNS
```
