# WORK-ULTRA-FABLE-MNE-DR-006 — Command / Guard Patch Specification

```yaml
artifact_id: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001-command-guard-patch-spec
status: SPECIFICATION_ONLY_NO_REPOSITORY_EDITS_PERFORMED
baseline_master: e726dea818dca9418181775d0e7dcd62eb6c464a
baseline_blobs:
  commands/prepare-mnemosyne-handoff.md: 23f7658073527037331d65fd8d4d7a495b982315
  commands/receive-mnemosyne-handoff.md: fa7fd7d31fdfd1663ea328db6c82e5c3a7b46cde
  commands/load-mnemosyne-guidance.md: 1124c2e058bba339688641c45ddf18a65f97e1ef
global_rules:
  - every proposal is additive_or_versioned; no existing handoff artifact is edited (immutable history)
  - all proposals are non-execution-source; none modifies current/human-approved-spec.md text except P-00 (explicitly flagged)
  - Owner approval: REQUIRED for every proposal (commands and guards are user-approved artifacts; prior
    owner decisions explicitly prohibited unauthorized command/spec edits)
  - each proposal names its MNE-HVAL-001 validation dependency; adoption before that validation is an
    explicit Owner risk acceptance
```

Failure-chain references (FC‑xx) point to the taxonomy artifact.

---

## P-00 — Execution-source touchpoint (optional, smallest possible)

- **Target path**: `current/human-approved-spec.md` §15 (one added sentence).
- **Old problem**: §15 requires evidence-path mapping but never requires *publication closure* — no rule says frozen identities must be re-verified against the final merged head before a package is offered for receive (FC‑02's failed gate).
- **New contract (proposed sentence)**: 「交接材料在发布合并后、提供给接收方之前，必须按最终 merged head 完成关键 path/blob 的机械回读核验，并保留可查的 publication receipt；未完成回读核验的交接材料不得作为有效交接提供。」
- **Compatibility**: none retroactive; historical packages stay historical evidence.
- **Validation requirement**: HV‑N‑012/013 demonstrate the failure the sentence prevents; the receipt mechanism itself is P‑04.
- **Owner approval**: REQUIRED (execution-source change; user-confirmation workflow of spec §6 applies). May be deferred: P‑01/P‑04 deliver the behavior at command level without touching the spec.

## P-01 — Prepare command vNext

- **Target path**: `commands/prepare-mnemosyne-handoff.md` (versioned in place via reviewed PR).
- **Old problems**: (a) no identity block is required, so packages can omit or mis-freeze blobs (FC‑02); (b) nothing addresses the package self-blob impossibility (FC‑03 repair insight); (c) no publication-closure step (FC‑02); (d) no schema binding, so package-required report and any oracle can diverge (FC‑03); (e) no startup-transfer fidelity rule (FC‑01); (f) no source-conversation release rule (FC‑05); (g) no guidance manifest (FC‑08).
- **New contract** — add a "Publication correctness requirements" section:
  1. every load-bearing claim carries an exact `{path, blob}` tuple; the package states which tuples are load-bearing;
  2. the package binds one canonical receive-report schema by `{schema_id, path, blob}` and must not define report fields the schema lacks (single-source rule);
  3. self-reference rule: the package never states its own blob; the paired startup prompt supplies exactly `package.blob.expected` and the same schema identity, and is created only after the package blob exists;
  4. post-merge, before the package is offered to any receiver, complete the P‑04 publication receipt (final-head readback of every load-bearing tuple); a package without a completed receipt is `NOT_YET_RECEIVABLE`;
  5. the startup prompt is delivered to the Owner file-first (spec §13 / artifact-delivery §3) with the instruction "copy the exact merged artifact; do not retype or restate" (generalizes rehearsal‑contract rule);
  6. the package records the source-conversation release rule: origination retires only after receive acceptance (+ guidance confirmation when required) per P‑08;
  7. when guidance is required, the package embeds a P‑06 guidance manifest (or explicitly states `guidance_manifest: none_current_list_applies`);
  8. dynamic-state rule: never freeze a pre-publication master SHA as a receive condition (schema handles master dynamically).
- **Compatibility**: new handoffs only; existing packages remain valid historical artifacts; `receiver_guidance_load` block retained unchanged for continuity.
- **Validation requirement**: HV‑P‑001, HV‑N‑012/013/014; receipt path via P‑04.
- **Owner approval**: REQUIRED.

## P-02 — Receive command vNext

- **Target path**: `commands/receive-mnemosyne-handoff.md`.
- **Old problems**: the required first-response report is untyped, has no expected/actual split, no identity verification status, no continuation gate, no dynamic-master rule, and no anti-alias rule — so generic receives cannot be mechanically adjudicated (FC‑03/06/07), and nothing forbids substituting a nearby artifact (FC‑08/HV‑N‑015 class).
- **New contract**:
  1. when the package binds a canonical schema (P‑01 rule 2), the receiver emits exactly that schema's report; aliasing/flattening/renaming prohibited; missing observation ⇒ `null` ⇒ `exact_match: false`;
  2. when no schema is bound (legacy package), emit the generic P‑03 schema in degraded mode, filling `expected` fields only where the package states them and marking the rest `expected: not_stated_by_package`;
  3. tri-status is mandatory in both modes: `handoff_receive_status` / `identity_verification_status` / `substantive_continuation_status`, with success forced to a blocked continuation until explicit acceptance (+ guidance where required);
  4. dynamic execution-time-master rule (start/end SHA + `unchanged_during_receive_check`) is mandatory in both modes;
  5. exact-artifact rule: the receiver reads exactly the authorized package path; a similarly named sibling is never an acceptable substitute; any near-match situation is a BLOCK with the near-match named;
  6. fail-closed and no-retry restated: a blocked receive is returned, not retried, not repaired receiver-side;
  7. the existing rules (non-execution-source, evidence verification, rule‑9 exclusions, guidance separation) are retained verbatim.
- **Compatibility**: legacy packages still receivable (degraded mode) — no flag day.
- **Validation requirement**: HV‑P‑001/002, HV‑N‑010…016, HV‑N‑022/023.
- **Owner approval**: REQUIRED.

## P-03 — NEW generic canonical receive-report schema

- **Target path (new file)**: `handoff/mnemosyne-generic-receive-report-schema-v0.1.md`.
- **Old problem**: schema‑001 is structurally excellent but hard-codes route nouns (`candidate_004`, `A1_status.*`); it cannot be reused, so every future route would re-invent a schema — re-creating FC‑03 conditions.
- **New contract**: parameterized generalization of schema‑001: fixed skeleton (`report_schema`, tri-status enums, `execution_time_master` dynamic block, `package`, `execution_source`, `supporting_commands`, `receiver_guidance_load` incl. `loaded_during_receive`, `repository_or_service_writes_during_receive`, `current_task_from_package.task_id`, ordered `forbidden_actions`, `evidence_paths_*`, `safe_next_action`, `limitations_or_unknowns`) plus a route-defined `identities.<name>.{path,blob}` map and optional route-defined typed extras declared **inside the package's schema-binding block**, never invented by the receiver or the oracle. Comparison semantics copied verbatim from schema‑001 (raw string equality, ordered lists, null⇒false, no omission on success). Self-blob exception codified as a schema feature.
- **Compatibility**: additive; schema‑001 remains the F2 route's binding schema; new routes bind v0.1‑generic with their identity map.
- **Validation requirement**: the entire MNE‑HVAL‑001 fixture set instantiates this schema (SYN‑R1 is its first consumer).
- **Owner approval**: REQUIRED.

## P-04 — NEW publication receipt template + workflow hook

- **Target path (new file)**: `notes/templates/handoff-publication-receipt-v0.1.md`; referenced by P‑01 rule 4.
- **Old problem**: FC‑02's inferred root cause is identity propagation "without final-head path/blob readback"; the readback exists today only as prose steps in the route rehearsal contracts, leaving no artifact proving it happened.
- **New contract** (receipt fields): `receipt_id`, `handoff_package {path, blob}`, `startup_prompt {path, blob}`, `schema {id, path, blob}`, `rehearsal_contract {path, blob}` (when used), `merge_commit`, `master_sha_at_readback`, `load_bearing_tuples: [{path, expected_blob, observed_blob, match}]` (all must match), `startup_self_blob_check: {embedded_expected, package_actual, match}`, `schema_closure_check: {schema_expected_field_count, package_supplied_count, uncovered_fields (must be exactly [package.blob] or [])}`, `performed_by`, `timestamp`, `disposition: RECEIVABLE | NOT_YET_RECEIVABLE`. The closure-check line mechanizes the exact test this audit ran manually.
- **Compatibility**: additive artifact per handoff generation.
- **Validation requirement**: HV‑N‑012/013 must be catchable by a correctly filled receipt *before* any receiver runs (receipt-level true-BLOCK).
- **Owner approval**: REQUIRED.

## P-05 — Guard amendment: startup-message transfer fidelity

- **Target paths**: `current/cross-conversation-execution-intent-and-operator-flow-guard.md` (new subsection) and `current/artifact-delivery-and-direct-generation-guard.md` §3B (one added rule).
- **Old problem**: FC‑01 — the only generic control ("operator flow and repository artifact must agree", §3B rule 9) is a source-side self-check with no transfer-channel protection; the drift happened in the Owner-relayed chat text.
- **New contract**: for any startup/launch message destined for another conversation: (a) file-first delivery of the exact message is mandatory (not optional) when the message contains identities; (b) the canonical message must embed at least the target package's expected blob and schema identity so a drifted paste fails closed receiver-side (generalizing Startup 002/003); (c) the source response must instruct copy-not-retype; (d) when a rehearsal/adjudication loop exists, the operator's exact sent message is preserved as evidence (echo pattern generalized from FC‑12's three-way comparison).
- **Compatibility**: behavioral only; no artifact format breaks.
- **Validation requirement**: HV‑N‑014 (drifted paste must fail closed with canonical artifacts untouched).
- **Owner approval**: REQUIRED (guards are user-approved).

## P-06 — Load-guidance command: manifest mode + task echo

- **Target path**: `commands/load-mnemosyne-guidance.md`.
- **Old problems**: FC‑08 (receiver-side unpinned guidance selection); FC‑09 (task-preservation asserted but not anchored to an identifier).
- **New contract**: (a) accept an optional source-supplied guidance manifest `[{path, pin: exact_blob|current_at_path, blob?}]`; in manifest mode load exactly those files, verify pinned blobs, fail closed per entry with the mismatch named; absent a manifest, current behavior applies unchanged; (b) `mnemosyne_guidance_refresh` gains `preserved_task_id:` which must echo the received package's `current_task_from_package.task_id` verbatim when one exists (mechanical anchor for `current_conversation_task_preserved`); (c) restate that manifest mode never authorizes reading files outside the manifest plus the command's own required files.
- **Compatibility**: fully backward compatible (manifest optional).
- **Validation requirement**: HV‑P‑003, HV‑N‑017/018/019/020.
- **Owner approval**: REQUIRED. Note: this implements architecture option C only; options B2/E are separate later decisions per the comparison artifact.

## P-07 — NEW generic rehearsal-oracle template

- **Target path (new file)**: `notes/templates/handoff-rehearsal-oracle-v0.1.md`.
- **Old problem**: rehearsal‑contract‑002's 13-point mechanical procedure exists only route-locally; future routes would re-write it (FC‑03 recurrence risk), and "mechanical" currently means a model executing comparison prose.
- **New contract**: parameterized version of the 13-point procedure bound to the P‑03 schema (single-key check, schema-field presence/type check, no-alias rule, tri-status constants, all `exact_match:true`, expected-value source checks incl. self-blob, empty writes list, quiescence + four-way master equality, no-extra-actions clause, `BLOCKED_REQUIRES_PRO` on any anomaly, exact acceptance token). Plus an explicitly optional "tool-assisted comparison" annex: where a code-execution surface is available, the adjudicator runs a deterministic field-by-field comparison script over the verbatim report and attaches its output — reducing residual model-interpretation risk (this audit's adversarial-pass concern). The annex is optional because surface availability is a time-sensitive product fact.
- **Compatibility**: additive; rehearsal‑contract‑002 remains the F2 binding text.
- **Validation requirement**: HV‑A‑030/031/032; the tool-annex, when available, is exercised on HV‑P‑001.
- **Owner approval**: REQUIRED.

## P-08 — Source-conversation release rule (generic)

- **Target paths**: P‑01 and P‑02 command texts (shared clause).
- **Old problem**: FC‑05 — the generic/legacy pattern (visible in `handoff/handoff-current.md`) permits source retirement at merge, before any receive validation; the route contracts fixed this only locally.
- **New contract**: "The originating conversation remains the adjudication owner and may retire only after (a) receive acceptance under the bound oracle, and (b) where guidance is required, the guidance-refresh report with preserved task echo. If the originating conversation becomes unavailable first, the handoff is `ORPHANED_REQUIRES_OWNER_DESIGNATED_ADJUDICATOR` — a fresh Pro conversation the Owner explicitly appoints with the receipt + oracle; no receiver self-acceptance."
- **Compatibility**: behavioral; matches what the route already does.
- **Validation requirement**: HV‑N‑021 (measures the orphaned-state recovery cost).
- **Owner approval**: REQUIRED.

## P-09 — `handoff/handoff-current.md` staleness policy

- **Target path**: `handoff/handoff-current.md` (policy decision, then either refresh-per-handoff or deprecation banner).
- **Old problem**: the card currently points at a superseded route (MNEMOSYNE‑140 era) while the live route is MNEMOSYNE‑234 — a standing FC‑08-class stale-pointer hazard sitting exactly where a naive receiver might look, held in check only by exclusion rules.
- **New contract** (Owner chooses one): (a) the prepare command's closure checklist requires updating `handoff-current.md` to point at the newly receivable package, or (b) the file is reduced to a permanent banner: "no per-route state here; the authorized package path comes only from the Owner's startup message" — removing the maintenance burden and the hazard together. This audit recommends (b) (`DESIGN_RECOMMENDATION`): per-handoff freshness of a global pointer file re-creates a dual source of truth.
- **Compatibility**: (b) is one small edit; (a) adds a per-handoff step.
- **Validation requirement**: HV‑N‑015 indirectly (no substitution from stale pointers).
- **Owner approval**: REQUIRED.

## P-10 — Strategy v0.2 + scorecard taxonomy extension

- **Target paths**: `notes/handoff-package-strategy-v0.1.md` → v0.2; `notes/handoff-replay-scorecard-v0.1.md` → v0.2.
- **Old problem**: strategy v0.1's `receiving_operation_statuses` ladder lacks `identity_verified` and `task_reconstructed`; scorecard v0.1's failure taxonomy has no producer/publication-side classes, so a maintainer scoring a replay today has no rubric row for the very defects that actually occurred (FC‑01/02/03/11/12).
- **New contract**: strategy v0.2 aligns the ladder to five+2 states (receive → **identity_verified** → report → **task_reconstructed** → guidance → continuation) and folds in the P‑01 identity/schema-binding fields; scorecard v0.2 adds a producer-side section importing the taxonomy artifact's five producer classes with detection signals (receipt mismatch, closure-count gap, oracle-skew, retype drift, temporal unsatisfiability) and routes them to publication-time (not replay-time) checks.
- **Compatibility**: versioned; v0.1 files remain historical.
- **Validation requirement**: none beyond consistency review (documentation alignment), plus MNE‑HVAL‑001 uses the v0.2 vocabulary.
- **Owner approval**: REQUIRED.

## P-11 — Migration notes for existing handoffs

- **Target path (new file)**: `notes/migration-designs/handoff-protocol-vnext-migration-notes-v0.1.md`.
- **Content contract**: (a) all existing packages/startup prompts/rehearsal contracts (F2 001–003 and the ~15 other-route artifacts under `handoff/`) remain immutable historical evidence; none is edited or re-issued retroactively; (b) any *future receive* of a legacy package runs under P‑02 degraded mode and its limitations are recorded; (c) the paused/parked routes with prepared packages (e.g., frontier-clarification resumption pair) are received legacy-mode unless their owners re-issue under vNext; (d) the F2 Handoff 003 rehearsal proceeds under its own already-approved route contracts, unaffected by this migration; (e) vNext applies to packages prepared after the Owner adopts P‑01/P‑02.
- **Owner approval**: REQUIRED.

## P-12 — Validation package publication

- **Target**: publish MNE‑HVAL‑001 fixtures per the validation-design artifact (its own write authorization, fixture paths, and key-commitment step).
- **Owner approval**: REQUIRED (separate write + execution authorizations; execution additionally consumes quota).

---

## Suggested adoption order and dependency graph

```text
P-04 (receipt) ── independent, highest single-defect coverage (FC-02), zero receiver impact
P-03 (generic schema) → P-02 (receive vNext) → P-01 (prepare vNext) → P-08 (release rule, inside P-01/02)
P-05 (transfer fidelity guard) ── independent, covers FC-01
P-06 (manifest mode) ── independent, covers FC-08/09; = architecture option C
P-07 (oracle template) ── after P-03
P-09, P-10, P-11 ── documentation/consistency layer, any time after the above are decided
P-00 (spec sentence) ── optional capstone after behavior is proven
P-12 ── gates behavioral claims for everything above
```

Minimal high-value subset if the Owner wants the smallest change: **P‑04 + P‑05 + P‑06** (covers FC‑01/02/08/09 with zero schema migration), leaving P‑01/02/03/07 for after the Handoff 003 rehearsal and MNE‑HVAL‑001 report back real behavior.
