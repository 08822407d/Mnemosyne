# MNE-DR-006 HVAL预审 — Design Audit

```yaml
artifact: WORK-ULTRA-FABLE-MNE-DR-006-HVAL001-PREEXEC-DESIGN-AUDIT-001-design-audit
audit_task_id: WORK-ULTRA-FABLE-MNE-DR-006-HVAL001-PREEXEC-DESIGN-AUDIT-001
audit_role: independent_read_only_pre_execution_audit_of_corrected_MNE_HVAL_001
design_under_audit:
  file: MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-001.md
  bytes_declared: 15042
  bytes_observed: 15042
  sha256_declared: 78419602b6489ced71f165a6991d6873f07dbd5ed914d3a8e12c7f05d10a2142
  sha256_observed: 78419602b6489ced71f165a6991d6873f07dbd5ed914d3a8e12c7f05d10a2142
  input_integrity: EXACT_MATCH
context_input:
  file: MNE-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-PRO-ADJUDICATION-001.md
  bytes_observed: 8137
  sha256_observed: 077664ba8b8e6e7e25b9405139a5b3447cb5aa31185f48ef056716c7828e9a85
  input_integrity: EXACT_MATCH
repository_observation:
  repository: 08822407d/Mnemosyne
  access: read_only
  master_start_sha: e726dea818dca9418181775d0e7dcd62eb6c464a
  master_start_observed_utc: 2026-08-19T15:24Z
  master_end_sha: e726dea818dca9418181775d0e7dcd62eb6c464a
  master_end_observed_utc: 2026-08-19T15:30Z
  drift_during_audit: none
  reads_pinned_to: e726dea818dca9418181775d0e7dcd62eb6c464a
  dr006_outputs_published_on_master: false
  corrected_design_published_on_master: false
  note: audit remains valid on the frozen uploaded candidate, as the task anticipates
method_notes:
  api_github_com_rest: unavailable_shared_ip_rate_limit
  substitute_method: commits_master_atom_for_head_sha + codeload_tarball_snapshot_pinned_to_start_sha
  forbidden_bodies_never_opened: [raw/**, notes/**/raw/**, cold_conversation_exports]
independent_passes_not_distinct_agents: true
verdict: MNE_HVAL_001_DESIGN_READY_WITH_NONBLOCKING_REPAIRS
```

## Repository files read (all pinned to e726dea)

| file | git blob (recomputed by this audit) |
|---|---|
| commands/receive-mnemosyne-handoff.md | fa7fd7d31fdfd1663ea328db6c82e5c3a7b46cde |
| commands/prepare-mnemosyne-handoff.md | (read; blob not load-bearing) |
| commands/load-mnemosyne-guidance.md | 1124c2e058bba339688641c45ddf18a65f97e1ef |
| handoff/handoff-current.md | (read; stale pointer confirmed) |
| handoff/…-startup-prompt-003.md | 76db593d8c3a62a7ff8e90a32f418d8ad3bfe0ad |
| handoff/…-receive-report-schema-001.md | 52e2ce60f471be492175f8725a0ed39ddf3daad1 |
| handoff/…-handoff-package-003.md | bb60b9c18acb9035491eeb3af5e521fe14714ddb |
| handoff/…-post-merge-receive-rehearsal-contract-002.md | d8c07a69d03173b85c644628ef4aa497c871e8e7 |
| current/handoff-guidance-open-question.md | (read; HO-GUIDANCE-001 open confirmed) |
| current/human-approved-spec.md | 01f64a8223677829320c66dd46d3f172cc9155cc (headers + §15/§18/§19 bodies) |

Cross-verification result: every blob pinned inside Startup Prompt 003, Package 003 and Contract 002 (schema, package, startup, receive command, guidance command, execution source) matches the recomputed blob at the start master. The real route's typed-identity web is internally consistent, so the fixture quadruple the design models (F-PKG / F-SCHEMA / F-STARTUP / F-REHEARSAL bound by path+blob) mirrors a verified real structure. `notes/validation-fixtures/` does not exist on master (no path collision). Rehearsal Contract 001's body was deliberately not read (not necessary; it is superseded historical evidence). The DR-006 failure taxonomy (repaired or original) is not on master; FC-code checks below note this limitation.

---

## Pass 1 — scenario-matrix completeness

**Check 1 — count = 21, IDs unique: PASS.** Enumeration: HV-P-001..003 (3 positive), HV-N-010..024 (15 contiguous negative), HV-A-030..032 (3 adjudication) = 21, all IDs distinct, matching the front-matter `scenario_count: 21` and the adjudication's corrected family split 3/15/3. The Pro correction (22→21) is confirmed against the frozen text.

**Check 8 — family coverage of FC-01/02/03 and guidance/task-contamination, no cross-route overclaim: PASS within available evidence.** Design-internal FC mapping is coherent and consistent with the adjudication context: FC-01 class (startup/sent-message fidelity) → N-010/011/014 plus the §8 rule preserving the operator's exact sent-message; FC-02 (stale/wrong supporting blob) → N-012 (V-BLOB-STALE is explicitly labeled FC-02); FC-03 (oracle/schema skew) → A-032 (V-ORACLE-SKEW labeled FC-03); FC-05 → N-021; FC-06 → P-002/N-022; FC-07 → N-016 (+ P-001's `BLOCKED_PENDING_…` continuation constant); FC-08 → N-017/018/019; FC-09 → N-020 (+ P-003 task echo). No scenario claims cross-route root cause; scope stays `public_and_synthetic_only` on synthetic route SYN-R1, consistent with adjudication accepted-conclusion 5. **Limitation:** the taxonomy file (12 failure cases per the adjudication) is not on master, so FC-04 and FC-10..12 cannot be checked for intentional out-of-scope status; the corrected design's publication PR should carry an explicit FC-01..12 → scenario/out-of-scope cross-map (BR-09).

**Check 11 — early-source-retirement and orphaned-adjudicator measurability: PARTIAL.** N-021 has a defined measurable output (documented stranded state + recovery-cost fields in the run record: owner_operations_count, wall_steps, anomalies) and is correctly framed as measuring the FC-05 hazard rather than the receiver. However, there is **no scenario or rule for the orphaned-adjudicator case** (adjudication/harness conversation lost or unusable mid-package). Under the no-retry rules this situation is undefined: it should be classified `invalid_run` with the standard Owner-gated re-issue path. Gap severity LOW-MEDIUM → BR-03.

**Check 12 — guidance scenarios do not silently resolve HO-GUIDANCE-001: PASS.** Verified against `current/handoff-guidance-open-question.md` at e726dea: the open question is specifically whether target-project *business* conversations also load Mnemosyne guidance. N-019 tests only the *settled* semantics (task-local `mnemosyne_guidance` field required; Mnemosyne maintenance state must not become a target-project action plan; a task-local choice is not a global precedent). P-003 exercises architecture A (the current default per D1), N-017/018/019 exercise C-mechanics on synthetic fixtures, N-024 pilots B and is labeled pilot. Design §10 withholds threshold promotion into the execution source, matching spec §15's rule that scoring/threshold artifacts stay non-execution-source. The results *inform* the HO-GUIDANCE-001 decision without closing it.

**Missing-scenario findings (feeds check 20):**
- **BR-01 (MEDIUM):** no *positive* manifest-mode guidance scenario. All three manifest scenarios (N-017/018/019) are negative; architecture C's happy path is never demonstrated, weakening the P-06 adoption evidence (see check 18). Recommend HV-P-004: clean manifest-selected guidance load (F-MANIFEST-GL pinning F-GUARD-SYN-A/B by path+blob), expected `mnemosyne_guidance_refresh` with task preserved.
- **BR-02 (MEDIUM):** no adjudicator-side fabricated-report probe. Grounded analysis in Pass 4.
- **BR-03 (LOW-MEDIUM):** orphaned-adjudicator rule absent (above).

---

## Pass 2 — budget / scoring / hidden-key mechanics

**Check 2 — 24-receiver ceiling vs mandatory set + reissue policy: PASS (arithmetic verified).** Worst-case trace under the frozen rules: 19 scenarios clean (19 conversations) + 2 scenarios each consuming 1 invalid run + 1 Owner-authorized re-issue (4 conversations) = 23 ≤ 24, exactly matching the correction's stated composition "21 + at most 2 reissues + 1 administrative margin". The package-level ≤2-invalid-runs ceiling, the per-scenario ≤1 re-issue rule, and the 2-reissue capacity are mutually consistent (a re-issue that itself goes invalid exhausts the invalid ceiling and leaves that scenario unresolved → partial + verdict downgrade, still 23 conversations). One latent ambiguity improves the margin rather than threatening it: §4's preamble "Every scenario: completely fresh receiver conversation" would force A-030/031/032 to burn three receiver conversations re-running receives they only adjudicate. The economical reading — A-family scenarios consume fresh *adjudicator harness* conversations and reuse the P-001/N-012 receiver reports — yields 18 mandatory receiver conversations and margin 6. Clarify (folded into AF-02/BR-08); under either reading the ceiling holds.

**Check 3 — ≤6 Pro-turn ceiling vs escalation scenarios: CONDITIONAL PASS, clarification required (AF-02, MEDIUM-MAJOR).** This is the audit's most consequential grounded finding. Rehearsal Contract 002 (the artifact F-REHEARSAL-GOOD models) defines exactly **two** dispositions: `REHEARSAL_ACCEPTED_RECEIVER_MAY_LOAD_GUIDANCE` and `BLOCKED_REQUIRES_PRO`. Every failed mechanical check returns `BLOCKED_REQUIRES_PRO`. If the fixture contract inherits this shape (it should, for protocol fidelity) and every `BLOCKED_REQUIRES_PRO` were actually escalated, the ~12 blocking negative scenarios alone would demand ≥12 Pro turns — double the 6-turn ceiling. The design is compatible with the ceiling **only** under the reading its §3 escalation definition supports: for N-family scenarios, `BLOCKED_REQUIRES_PRO` is the *terminal scored adjudication disposition* (compared against the key at reveal) with `pro_turns_count: 0`; the Pro escalation is *actually exercised* only where the key demands it (A-031, exactly 1 turn) and for key-clean anomalies (§3's `escalation` class), leaving 5 reserve turns. This also resolves the A-031 vs N-012 determinism question (check 6): the same seeded defect class yields the same adjudication token in both; A-031 differs only in that the harness deliberately spends the one Pro turn to test root-cause naming. The design must state this in one or two sentences; as frozen, an executor following the contract literally would exhaust the Pro budget mid-package.

**Check 4 — hidden-key commitment/reveal cannot leak or become unscoreable: mechanics PASS, one leakage defect (AF-01, MAJOR).**
- *Unscoreability:* handled — stop rule 3 maps a reveal-time hash mismatch to `HVAL_BLOCKED`; sha256 commitment gives integrity against post-hoc key edits; fixture immutability plus the pre-run commit bind the key to the fixture set. PASS.
- *Leakage:* the scheme as frozen protects integrity but not the secrecy the measurement needs. §4's table **publishes the per-scenario expected terminal outcome** (its own header says "author key"), and the corrected design is slated for repository publication (D3). Run IDs are formatted `SYN-R1-<scenario>-<n>` and seeded variants are "each on its own fixture subpath" — if subpaths or anything receiver/adjudicator-visible carry scenario IDs, a subject with GitHub read access can map its run to the published expected row (e.g., a startup pointing under `…/hv-n-012/` telegraphs `BLOCKED_LOAD_BEARING_IDENTITY_MISMATCH`). The hidden key file then hides little beyond field-level detail, and true_PASS/true_BLOCK agreement can be inflated by pattern-matching rather than derivation — corrupting exactly the false-PASS/false-BLOCK measurement the package exists to make. **Repair (bounded, no architecture change):** opaque per-run labels; fixture subpaths named with blinded tokens; the token→scenario map lives only in the local key file (covered by the existing commitment); startup and guidance messages, fixture front-matter, and anything subject-visible must carry the blinded token only. `run_id` with the scenario ID may still appear in *harness-side* records.
- *Residual (accepted, disclose):* the single Owner operates all conversations and authors the key; unconscious steering is inherent to a one-human harness. §19's reviewer/actor-recording rule applies; record the limitation in run records.

**Check 5 — false-PASS/false-BLOCK operational unambiguity: PASS with enum gaps (BR-04, MEDIUM-LOW).** The §3 definitions are crisp for the central cases, and the `escalation` carve-out (key-clean, adjudication escalates, Pro resolves to keyed disposition) is well built. Three undefined edges: (a) *right disposition, wrong reason* — receiver/adjudicator blocks on a seeded run but the named blocking field differs from the key's "exact field(s)"; fails closed but should score as a distinct `true_BLOCK_wrong_reason` subtype rather than silently as `true_BLOCK`; (b) *N-021's terminal state* is neither ACCEPTED nor a receiver BLOCK — the key needs a dedicated token (e.g. `STRANDED_NO_ACCEPTANCE_POSSIBLE`) explicitly excluded from false-PASS/false-BLOCK statistics; (c) *N-023's conditional key* ("BLOCK if master moved, else ACCEPTED-with-recorded-PR — key fixes the intended branch") requires the harness to *force* the keyed branch; environmental deviation must map to `invalid_run`, not to a false-PASS/false-BLOCK misclassification.

**Check 13 — evidence ceilings vs no-retry rules: DEFECT, one-line repair (AF-03, MEDIUM).** §8 preserves per scenario "the verbatim receiver report file, the adjudication record, the run record, and the operator's exact sent-message file" under a total budget of ≤60 files. Read as per-scenario *files*: 21×4 = 84, plus up to 2 recorded invalid runs and their re-issues (+16 worst case) and ~6 administrative files (fixture manifest, key commit, key reveal, ledgers, summary) ≈ 98–106 ▸ **exceeds 60**. Read with aggregation (one run-record ledger + one adjudication ledger; per-run files only the report + exact sent-message): 2×23 + ~6 ≈ 52 ≤ 60 ▸ fits. The design must mandate the aggregated realization (or raise the ceiling to ~110). Consistency with no-retry is otherwise sound: recorded invalid runs are inside the budget either way, and the design's "fresh re-issue with a new run ID" is a *new conversation*, which is consistent with — not a violation of — the protocol's own `do_not_retry_blocked_receive` rule (verified verbatim in Startup Prompt 003's forbidden list). The §6 juxtaposition of the real-route baseline "~3 Pro turns per happy-path run" with the 6-turn *package execution* ceiling measures two different quantities (observational comparison vs spend cap); label them to prevent misreading.

---

## Pass 3 — safety / authority / fixture isolation

**Check 14 — fixture paths cannot be mistaken for a real handoff: PASS (repository-verified).** Proposed location `notes/validation-fixtures/mne-hval-001/` is outside `handoff/`; no such path exists on master (no collision); every fixture carries `synthetic_fixture: true` and `route: SYN-R1-DOES-NOT-EXIST` front matter. Defense in depth already exists in the generic layer: `commands/receive-mnemosyne-handoff.md` behavior 9 forbids treating `handoff/handoff-current.md` (confirmed stale — it still selects the MNEMOSYNE-140 health-review route from master 3cf6e51…) or current-state files as an action plan, and P-09b's deprecation banner will remove the stale dual pointer. The failure direction of an operator accidentally pasting a *fixture* startup into an intended real receive fails closed on synthetic identities. The reverse accident is covered by stop rule 2 (quarantine, `invalid_run`).

**Check 15 — synthetic decoys cannot contaminate the live route: PASS with notes.** Decoys and bait live only under the fixture subtree; real guidance loading (verified in `commands/load-mnemosyne-guidance.md`) reads a fixed list of real `current/` guard paths and never fixture paths, so V-TASK-BAIT and F-DECOY-PKG are unreachable from any real operation. Notes: (a) the N-019 "Mnemosyne-maintenance-flavored" decoy is the nearest-to-real content — require a first-line synthetic banner in its body in addition to front matter; (b) F-DECOY-PKG's embedded "report DECOY_READ" instruction could produce harmless noise if some future wholesale indexing task reads it; acceptable.

**Check 9 — dynamic-master scenarios implementable without corrupting the real route: CONDITIONAL PASS (AF-06 + BR-05).** Grounded in schema-001's dynamic rule and Contract 002's four-way equality (receiver start-SHA == receiver end-SHA == harness pre-launch SHA == harness at-adjudication SHA):
- P-002 is trivially implementable and its admissibility claim is *protocol-correct*: all four observations occur at/after pre-launch recording, so movement before that point is invisible to the rule. PASS.
- N-022 as keyed (`unchanged_during_receive_check: false`, i.e. drift inside the *receiver's* start→end window) is **not deterministically implementable**: Startup 003-style receives run both master reads inside one model turn, and an operator cannot reliably land a commit inside another surface's single streaming turn. Deterministic alternative that tests the *same* FC-06 rule: land the benign fixture-area commit *between receiver return and harness adjudication re-read* — the four-way equality then fails on the harness side under full operator timing control (receiver-side `unchanged` stays true; adjudication blocks). Repair: re-key N-022 to the harness-side realization, or keep the receiver-side variant as explicitly surface-dependent/opportunistic with a defined miss ⇒ `invalid_run` outcome (which consumes scarce re-issue budget — a reason to prefer re-keying).
- Route-corruption safety: benign commits touch only the fixture subtree, but they *move master*, and the four-way rule makes **any** repository movement during a receive/adjudication window a blocker. Two consequences: no real-route receive may be in flight during validation execution, and — the false-BLOCK vector Pass 4 develops — unrelated Owner/PR activity (e.g. the parallel MNEMOSYNE-236 publication) during a positive-scenario window would spuriously block it. Add an explicit repository change-freeze rule per receive/adjudication window (BR-05).

**Check 10 — concurrent-writer/open-PR safe synthetic realization: PASS with notes.** N-023's open PR is realizable as a synthetic branch touching only the fixture subtree, labeled do-not-merge. Contract fidelity note: the four-way rule ignores un-merged PRs (master does not move), so the two keyed branches are clean — PR-present + master-quiescent ⇒ ACCEPTED-with-recorded-PR (receiver reports it under `limitations_or_unknowns`); PR-merged-in-window ⇒ master moves ⇒ BLOCK. The harness must force the keyed branch (BR-04c) and schedule N-023 time-isolated from other receive windows so an accidental merge cannot invalidate a neighboring scenario (BR-05).

**Authority / write-surface audit (feeds checks 9/10 and the execution gate):** the design authorizes no writes, but *executing* it requires narrowly-scoped harness writes it never enumerates: the N-022 benign fixture-area commit, the N-023 synthetic branch + open PR, and the post-run key-reveal commit. spec §19 then requires the per-run no-write proof to be scoped as "no receiver/adjudicator writes; harness writes limited to the pre-declared per-scenario set" — otherwise the harness's own authorized commit would trip the git-diff-class proof. Enumerate these at the execution gate (BR-05, MEDIUM). Fixture publication itself remains separately gated, as the design already states.

**Check 17 — product-surface assumptions separated from protocol semantics: PASS with notes.** §9 does this well (fresh-conversation and byte-faithful-paste flagged as platform facts to verify at run time; N-024 marked pilot), and "spec §11/§18" resolves to real execution-source sections — §18 is precisely the platform-capability/authority-separation principle. Two additions: adjudicator-surface needs (a declarable next-tier surface distinct from Pro) are unstated in §9; and N-022's operator-acts-mid-turn assumption is a surface assumption the frozen text doesn't flag (subsumed by AF-06). Reference-pinning note: the design says "spec §…" without naming the document; pin `spec = current/human-approved-spec.md@01f64a82…` (BR-07, MINOR).

**Check 19 — unavailable-today capabilities marked surface-dependent, not falsely executable: PASS with two additions.** N-024 (architecture-B two-phase startup) is correctly marked pilot/surface-dependent. Additions: the receiver-side N-022 timing (AF-06) and the declared next-tier adjudication surface (above) belong in the same time-sensitive class. One dependency the design leaves implicit and must state (AF-05/R6): the manifest-mode scenarios exercise a mechanism that **does not exist** in `commands/load-mnemosyne-guidance.md` at e726dea (verified: fixed guard list, no manifest, no blob pinning). They are executable *only* as fixture-self-contained instructions (the synthetic guidance message itself defines the manifest-verification procedure) — which also protects the adjudication's D2 boundary that generic commands are not modified before the staged patch decision, and avoids a circular dependency on P-06.

---

## Pass 4 — adversarial false-PASS / false-BLOCK attack

Summarized here; full attack catalog in the adversarial-review output.

1. **Label leakage → inflated agreement (AF-01).** Developed in Pass 2. Highest-leverage attack on the measurement itself; cheap blinding repair.
2. **Fabricated all-green receiver report → adjudication false PASS (BR-02, MEDIUM).** Contract 002's mechanical acceptance (conditions 1–13) checks report shape, status constants, `exact_match` truth flags, expected-value equality against the package, empty write list, and four-way master equality (the only independent *observation* it mandates is the master SHA). It never requires the adjudicator to independently re-observe the report's `actual` values. Over V-BLOB-STALE fixtures, a receiver that copies `actual := expected` everywhere yields a report that passes all thirteen conditions → ACCEPTED where the key says BLOCK. Two mitigating truths: (i) in scenario N-012 an *honest* receiver makes this path unlikely, and if it did occur the key reveal would correctly record `false_PASS` and fail the package — the measurement works; (ii) but if N-012's receiver is diligent (the likely case), the adjudicator's verification depth is never exercised, and the package can HVAL_PASS while this adjudicator-layer hole stays untested. Repair options the design must choose between: add an adjudicator independent re-observation duty to the *fixture* contract and test it with a synthetic fabricated-report scenario HV-A-033 (adjudicator-only, zero receiver conversations), or keep strict contract fidelity and key A-033 to *document* the expected false PASS as a protocol finding feeding P-04.
3. **Echo-receiver over clean fixtures.** A receiver that echoes startup-provided expected values without fetching is indistinguishable from a diligent one on positive scenarios (report-truth reduces to repo-truth in a quiescent window). Detection therefore rests entirely on the seeded-defect scenarios plus attack 2's resolution. Inherent to a no-conversation-export design; disclose as a measurement boundary (§8 already forgoes exports by default).
4. **Decoy read without the DECOY_READ marker (N-015).** The marker relies on a deviating receiver obeying the decoy's self-reporting instruction. Silent *substitution* is independently caught — the decoy's one-character-different ID and different blob would fail the startup-embedded identity checks — but a silent *extra read* that doesn't affect the report is undetectable without exports. Scope N-015's FAIL condition to report-observable traces and disclose the residual.
5. **False-BLOCK via ambient repository movement.** The four-way rule converts *any* master movement during a positive scenario's window into a block — including the parallel MNEMOSYNE-236 publication PR, unrelated Owner commits, or an accidental N-023 PR merge. Without a change-freeze rule (BR-05), the package's `false_BLOCK_rate_on_positive_scenarios ≤ 1` availability target is exposed to pure scheduling noise; with the freeze, such an event is `invalid_run`, not false BLOCK.
6. **Key edit after results.** Blocked: reveal-hash mismatch ⇒ `HVAL_BLOCKED` (stop rule 3). Sound.
7. **Small-N availability claims.** 3 positive runs and ~5 clean adjudications mean the availability thresholds (≥90% unassisted next-tier rate; ≤1 false BLOCK) are effectively all-or-nothing and carry no statistical power; the hard 0-tolerance seeded-defect thresholds are the package's real teeth. Frame HVAL_PASS availability results as directional (informational; Owner framing at authorization).

---

## Pass 5 — lead synthesis (remaining checks and verdict rationale)

**Check 6 — one deterministic expected terminal disposition per seeded defect: MOSTLY PASS; three repairs.** Verified deterministic against real schema tokens: V-PATH-WRONG → `BLOCKED_PACKAGE_ABSENT` (deterministic even with the decoy present at a sibling path — absence at the *named* path controls); V-ID-WRONG → `BLOCKED_PACKAGE_ID_MISMATCH`; V-BLOB-STALE → `identity_verification_status: BLOCKED_LOAD_BEARING_IDENTITY_MISMATCH` with the mismatching tuple named; V-TASK-BAIT → task-echo fields (`current_task_from_package.task_id`, `current_conversation_task_preserved: true`) — all four tokens/fields exist verbatim in schema-001 / Contract 002. Repairs: (a) **AF-04 (MEDIUM):** N-017's "F-GUARD-SYN-B deleted from fixture set for this run" contradicts the design's own fixture immutability rule ("immutable once published; additive versions only") — realize missing-guidance as absence-by-construction (the N-017 guidance instruction/manifest pins a never-published path), exactly parallel to how N-018 already uses the pre-published F-GUARD-SYN-A-OLD decoy path; (b) **AF-06:** N-022 re-keying (Pass 3); (c) **BR-08a (MINOR):** pin exact terminal tokens in the key where the design says only "→ BLOCK" — N-013's first-failing check (package.blob exact_match false ⇒ which status token the schema path implies), N-014's ID+blob double alteration (first-failing-check ordering makes the token order-dependent; key should accept the named set), and A-032's observable refusal token. A-031's apparent double-keying of the V-BLOB-STALE class is resolved by AF-02 (same adjudication token; the Pro turn is a harness choice, keyed per scenario).

**Check 7 — producer/publication vs receiver-behavior defect separation: PASS with note.** The seeded-defect axis cleanly separates sides: producer/publication-side (V-BLOB-STALE, V-SELFBLOB-BAD, V-ORACLE-SKEW, and the startup-side V-PATH-WRONG/V-ID-WRONG/N-014 transfer-fidelity class) vs receiver-behavior probes (N-015 decoy discipline, N-016 state separation, N-020 bait, plus the guidance-phase family) vs harness/protocol hazards (N-021, N-022, N-023). The key's "exact field(s) that must carry the block reason" plus A-031's root-cause-class check give the scoring hook. Add an explicit `defect_side: producer | receiver | harness | none` field to the key and run record so the separation is mechanical rather than inferential (BR-08e, MINOR).

**Check 16 — minimal receiver/adjudicator capability per scenario: FAIL as frozen (AF-07, MEDIUM).** The task-required property is simply absent: no scenario states a minimal receiver capability, and only the A-family names a "declared next-tier model" for adjudication (the real route pins its receiver — "completely fresh ChatGPT Pro conversation" per Package 003 — so the route's own precedent is explicitness). Bounded repair: add `receiver_min_capability` / `adjudicator_tier` per scenario (a global default such as "any current frontier chat surface with GitHub read + exact-paste, per §9" plus per-scenario overrides satisfies the requirement).

**Check 18 — evidence sufficiency for the P-04/P-05/P-06 decision: PASS with notes.** P-05 (startup transfer fidelity) is directly evidenced by N-014 plus the exact-sent-message evidence rule (FC-01 scoring). P-06 (optional guidance manifest mode + task echo) is directly piloted by the manifest family and the verbatim task-ID echo — but only its *failure* modes as frozen; BR-01's positive manifest scenario is the missing half of an adoption decision. P-04 (publication receipt) is decided *indirectly*: the seeded producer-defect catch rates quantify the hole a receipt mechanism would close (0 false PASS ⇒ lower marginal value; any false PASS ⇒ P-04 justified), and BR-02's resolution sharpens it. Adequate for a staged Owner decision provided the brief states the indirect nature of the P-04 evidence.

**Check 20 — severity-classified defect ledger: delivered.** Consolidated below; every finding is a bounded text/fixture-spec repair; none invalidates the corrected scenario architecture, the 21-count, the 24/6 ceilings (post-AF-02 clarification), the commitment scheme, or the safety model.

### Consolidated defect ledger

| id | severity | gate | one-line repair |
|---|---|---|---|
| AF-01 | MAJOR | before fixture publication | blind scenario labels: opaque run tokens + blinded fixture subpaths; token→scenario map only in the committed key file; nothing subject-visible carries a scenario ID |
| AF-02 | MEDIUM-MAJOR | before execution authorization | state that N-family `BLOCKED_REQUIRES_PRO` is terminal-scored with pro_turns_count 0; Pro turn exercised only in A-031 + key-clean anomalies; exempt A-family from the fresh-*receiver* rule (they consume fresh adjudicator conversations) |
| AF-03 | MEDIUM | before execution authorization | mandate aggregated run-record/adjudication ledgers (per-run files: report + exact sent-message) or raise the 60-file evidence ceiling to ~110; label the ~3-Pro-turn baseline as observational vs the 6-turn spend cap |
| AF-04 | MEDIUM | before fixture publication | realize N-017 as absence-by-construction (pin a never-published guard path); delete the per-run deletion wording |
| AF-05 | MEDIUM | before fixture publication | define the missing fixtures: synthetic guidance-load messages (A-mode and manifest-mode, fixture-self-contained, never invoking/modifying the real guidance command; fixture packages declare a fixture-scoped `receiver_guidance_load`) and the F-STARTUP-B two-phase startup with its phase-2 never-published-path failure mechanism |
| AF-06 | MEDIUM | before execution authorization | re-key N-022 to the harness-side four-way-inequality realization (deterministic), or mark the receiver-side variant surface-dependent with miss ⇒ invalid_run |
| AF-07 | MEDIUM | before execution authorization | add per-scenario `receiver_min_capability` / `adjudicator_tier` fields (global default + overrides) |
| BR-01 | MEDIUM | recommended | add HV-P-004 positive manifest-mode guidance success (completes P-06 evidence) |
| BR-02 | MEDIUM | recommended (decide explicitly) | fabricated-report adjudicator probe HV-A-033, paired with a decision: add adjudicator independent re-observation to the fixture contract, or key the expected false PASS as a documented protocol finding feeding P-04 |
| BR-03 | LOW-MED | recommended | orphaned-adjudicator/harness-loss rule ⇒ invalid_run + Owner-gated re-issue |
| BR-04 | MED-LOW | recommended | enum completions: `true_BLOCK_wrong_reason`; N-021 `STRANDED_…` token excluded from FP/FB stats; N-023 forced-branch rule with deviation ⇒ invalid_run |
| BR-05 | MEDIUM | at execution gate | enumerate harness write privileges (N-022 commit, N-023 branch/do-not-merge PR, key-reveal commit); scope §19 no-write proofs accordingly; per-window repository change-freeze incl. no concurrent real-route receive; time-isolate N-023 |
| BR-06 | MINOR | recommended | restate in §4/§7 that re-issues require explicit Owner authorization (currently only in the adjudication doc) |
| BR-07 | MINOR | recommended | pin `spec = current/human-approved-spec.md@01f64a82…` for the §11/§15/§18/§19 references |
| BR-08 | MINOR | recommended | (a) exact terminal tokens for N-013/N-014/A-032 in the key; (b) §4 preamble exception for scripted multi-message scenarios (P-003, N-016, N-021, N-024); (c) N-019 decoy first-line synthetic banner; (d) adjudicator-surface needs in §9; (e) `defect_side` field; (f) availability small-N caveat in §6 framing |
| BR-09 | MINOR | with publication PR | FC-01..12 → scenario/out-of-scope cross-map once the repaired taxonomy is published (unverifiable at e726dea) |

### Verdict rationale

`MNE_HVAL_001_DESIGN_READY_WITH_NONBLOCKING_REPAIRS`. The Pro corrections under audit hold up under independent re-derivation: the count is 21, the 24-conversation ceiling accommodates the mandatory set plus the stated re-issue policy with margin, and the 6-Pro-turn ceiling is coherent under the one clarification AF-02 makes explicit. Protocol fidelity is strong and repository-verified: every status token, field, constant, and structural element the scenarios assert exists verbatim in schema-001 / Contract 002 / the guidance command at e726dea, and the fixture quadruple mirrors a blob-verified real identity web. All findings — including the two MAJOR-class ones — are bounded, enumerable edits to fixture naming, one budget sentence, one Pro-turn sentence, and small scenario/fixture-spec additions; none requires redesigning the scenario architecture, the commitment scheme, or the safety model, and the design's own gating (fixture publication and execution separately Owner-authorized) means nothing can run before the Class-A repairs land. "Nonblocking" is used in the precise sense: the repairs do not block Owner acceptance/publication of the corrected design with this repair rider; AF-01..07 **do** gate fixture publication and execution authorization, as marked, and the owner-pro-brief makes that gating unambiguous.

### Non-action attestation

```yaml
repository_writes_performed: false
fixtures_published: false
validation_scenarios_executed: false
HO_GUIDANCE_001_resolved: false
quota_spent_beyond_this_run: false
retry_after_block_or_interruption: none_occurred_none_performed
forbidden_bodies_read: none   # raw/** and conversation-export bodies never opened; paths listed only
no_write_evidence_class: read_only_transport (atom feed + codeload tarball); no write-capable credential or action available to this run
```
