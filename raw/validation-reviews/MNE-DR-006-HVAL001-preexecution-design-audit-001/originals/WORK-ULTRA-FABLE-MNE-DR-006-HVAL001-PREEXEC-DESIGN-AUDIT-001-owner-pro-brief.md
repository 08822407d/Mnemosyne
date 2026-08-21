# MNE-DR-006 HVAL预审 — Owner / Pro Brief

```yaml
artifact: WORK-ULTRA-FABLE-MNE-DR-006-HVAL001-PREEXEC-DESIGN-AUDIT-001-owner-pro-brief
audience: Owner_and_Pro_adjudication
verdict: MNE_HVAL_001_DESIGN_READY_WITH_NONBLOCKING_REPAIRS
design_audited: MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-001.md (sha256 78419602…a2142, exact match)
repository_window: master e726dea818dca9418181775d0e7dcd62eb6c464a at start and end, no drift
this_audit_performed_no_writes_no_fixture_publication_no_scenario_execution: true
independent_passes_not_distinct_agents: true
```

## One-paragraph summary

The Pro-corrected MNE-HVAL-001 design is architecturally sound, protocol-faithful, and safely gated. Independent re-derivation confirms all three Pro corrections: the scenario count is exactly 21 with unique IDs; the 24-receiver-conversation ceiling accommodates the mandatory set plus the stated re-issue policy (worst case 23); and the 6-Pro-turn ceiling is coherent under one clarification the design must state explicitly. Every status token, report field, and mechanical rule the scenarios assert was verified verbatim against the real route artifacts at `e726dea` (schema-001, contract-002, package-003, startup-003, both generic commands), and the route's pinned blob identity web re-verified clean. The audit found no material defect that invalidates the architecture, and seventeen bounded findings: seven Class-A repairs (AF-01..07) that gate fixture publication or execution authorization, and ten Class-B recommendations (BR-01..09 plus disclosures). Because the design already makes fixture publication and execution separately Owner-gated, the Class-A repairs can land in the publication PR without re-running any prior stage — hence "ready with nonblocking repairs" rather than "blocked".

## What was independently confirmed (highlights)

1. **Count and ceilings (Pro corrections 2):** 21 = 3 positive + 15 negative + 3 adjudication; worst-case conversation trace 23 ≤ 24; the ≤2-invalid / ≤1-reissue-per-scenario rules are mutually consistent.
2. **Protocol fidelity:** all asserted tokens exist verbatim (`BLOCKED_PACKAGE_ABSENT`, `BLOCKED_PACKAGE_ID_MISMATCH`, `BLOCKED_LOAD_BEARING_IDENTITY_MISMATCH`, `BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE`, `REHEARSAL_ACCEPTED_RECEIVER_MAY_LOAD_GUIDANCE`, `BLOCKED_REQUIRES_PRO`, `mnemosyne_guidance_refresh` fields, task-ID echo, `unchanged_during_receive_check`, four-way master equality). The fixture quadruple mirrors the real blob-verified structure; F-EVID-01..04 mirrors the real 4-tuple identities block; the self-blob-from-startup rule matches schema-001 exactly.
3. **Safety and isolation:** `notes/validation-fixtures/` has no collision on master; fixtures sit outside `handoff/`; a fixture startup pasted into a real receive fails closed on synthetic identities; the real guidance command can never reach fixture paths; `handoff-current.md` confirmed stale, supporting P-09b; HO-GUIDANCE-001 confirmed open and untouched by the scenario set (N-019 tests only settled semantics).
4. **No-retry alignment:** the design's no-retry + Owner-gated fresh re-issue is faithful to startup-003's verbatim `do_not_retry_blocked_receive`.
5. **Spec references resolve:** "spec §11/§15/§18/§19" resolve to real sections of `current/human-approved-spec.md` (blob `01f64a82…`), including §19's git-diff-class no-write proof the run record invokes.

## Class A — required before the marked gate (all bounded edits)

| id | gate | repair |
|---|---|---|
| AF-01 | fixture publication | **Blind the scenario labels.** The design table publishes each expected outcome; run IDs and per-scenario fixture subpaths would let subjects with repo read-access pattern-match answers. Use opaque run tokens and blinded subpaths; keep the token→scenario map only inside the committed key file. |
| AF-02 | execution authorization | **State Pro-turn terminality.** Contract-002 has only two dispositions; declare that N-family `BLOCKED_REQUIRES_PRO` is terminal-scored (pro_turns_count 0), the Pro turn is exercised only in A-031 and for key-clean anomalies, and A-family scenarios consume adjudicator (not receiver) conversations. Without this sentence the 6-turn ceiling is breached by construction. |
| AF-03 | execution authorization | **Fix the evidence arithmetic.** Per-scenario-file reading yields ~90–106 files vs the 60 ceiling; mandate aggregated run-record/adjudication ledgers (≈52 files) or raise the ceiling; label the ~3-Pro-turn figure as an observational baseline distinct from the 6-turn cap. |
| AF-04 | fixture publication | **Re-realize N-017.** Per-run deletion of F-GUARD-SYN-B contradicts fixture immutability; use absence-by-construction (pin a never-published guard path). |
| AF-05 | fixture publication | **Define the missing fixtures.** Synthetic guidance-load messages (A-mode and manifest-mode, fixture-self-contained — the real guidance command has no manifest mode at `e726dea` and must not be invoked or modified) and the F-STARTUP-B two-phase startup for N-024; raise the 25-file fixture ceiling to ~30 to absorb them. |
| AF-06 | execution authorization | **Re-key N-022.** The receiver-side mid-turn commit is not operator-timeable; use the deterministic harness-side four-way-inequality realization (commit between receiver return and adjudication re-read), or mark the receiver-side variant surface-dependent with miss ⇒ invalid_run. |
| AF-07 | execution authorization | **Add capability fields.** Task check 16 is unmet as frozen: add per-scenario `receiver_min_capability` / `adjudicator_tier` (global default + overrides). |

## Class B — recommended (decide at publication PR)

**BR-01** add HV-P-004 (positive manifest-mode guidance success — completes the P-06 evidence, +1 receiver conversation). **BR-02** decide the fabricated-report question explicitly: contract-002's mechanical conditions never require the adjudicator to re-observe reported `actual` values, so an all-green fabricated report over seeded-defect fixtures would be ACCEPTED; either add an adjudicator independent re-observation duty to the fixture contract and test it (HV-A-033, zero receiver conversations), or key A-033 to document the expected false PASS as a protocol finding feeding P-04. **BR-03** orphaned-adjudicator rule (⇒ invalid_run + Owner-gated re-issue). **BR-04** classification-enum completions (wrong-reason BLOCK subtype; N-021 STRANDED token excluded from stats; N-023 forced-branch rule). **BR-05** at the execution gate: enumerate the three harness write privileges (N-022 commit, N-023 branch/do-not-merge PR, key-reveal commit), scope §19 no-write proofs accordingly, and adopt a per-window repository change-freeze — this is also the false-BLOCK shield if MNEMOSYNE-236 publication or other Owner activity lands mid-window. **BR-06..09** minor text pins (re-issue authorization restated in-design; `spec = current/human-approved-spec.md@01f64a82…`; exact terminal tokens for N-013/N-014/A-032; multi-message preamble exception; N-019 decoy banner; `defect_side` field; small-N availability framing; FC-01..12 cross-map once the repaired taxonomy publishes).

## Decision points for the Owner

1. **Accept the verdict and adopt the repair rider?** Recommended path: fold AF-01..07 (and any accepted BR items) into the corrected design at the MNEMOSYNE-236 publication PR — no re-audit needed for text-level repairs; a delta check suffices.
2. **BR-02 choice** (strengthen the fixture contract vs measure the contract as-is). This materially shapes what an HVAL_PASS will mean for the P-04 decision.
3. **BR-01 adoption** (and with it, whether the receiver ceiling stays 24 or moves to 26 under the strict fresh-receiver reading).
4. **Evidence realization** (aggregated ledgers at 60 files vs raised ceiling) — AF-03.
5. Fixture publication and scenario execution remain **separately gated** Owner decisions after the repairs land; nothing in this audit or the repaired design authorizes them.

## What this audit did not do

No repository writes, no fixture publication, no scenario execution, no HO-GUIDANCE-001 resolution, no quota beyond this run, no retries. `raw/` bodies and conversation exports were never opened. The DR-006 output set (including the repaired taxonomy) is not yet on master, so FC-04/FC-10..12 mappings remain unverifiable until publication (BR-09).
