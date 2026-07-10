# FABLE5-GREENFIELD-001 — Maintainer High-Model Intake Review

```yaml
review_id: FABLE5-GREENFIELD-001-INTAKE-001
created_by_task: MNEMOSYNE-101
review_model_context: GPT-5.6-high-reasoning-maintenance-context
authority_level: non_execution_source_maintainer_review
scope:
  - review Fable greenfield charter
  - audit MNEMOSYNE-095..100 work performed during reduced-model period
  - identify preservation and planning gaps
```

## Overall conclusion

The reduced-model period did **not** cause execution-source drift, paused-route resumption, target-project action, regression formalization, or unauthorized operational work. The mainline safety boundaries were preserved.

There were, however, two workflow deviations and two planning-quality issues:

1. MNEMOSYNE-096 and MNEMOSYNE-097 accidentally wrote small non-execution-source files directly to the default branch because branch parameters were omitted. Both deviations were disclosed; MNEMOSYNE-098 added a branch/write preflight checklist and later tasks followed it.
2. MNEMOSYNE-096 preserved only metadata/hash for the uploaded full Fable response even though the attachment remained available. The full response should be added verbatim; this is a real preservation gap, not merely optional bookkeeping.
3. MNEMOSYNE-098..100 became somewhat over-fragmented. The preflight checklist was justified, but the separate decision-package and transfer-prompt tasks added repository churn before the actual higher-model decision work. They remain useful and need not be removed.
4. MNEMOSYNE-097's Q2-2/R3 audit was appropriately conservative, but it is an evidence table rather than a completed high-judgment decision. Its `likely`/`partial` classifications should not be treated as settled repair authority.

## Per-task review

### MNEMOSYNE-095

Appropriate low-scope action. It stored a faithful summary and correctly kept the Fable response advisory/non-execution-source. Its known weakness was summary loss, which later Fable review identified explicitly.

### MNEMOSYNE-096

Directionally correct but incomplete. It preserved available context, user instructions, provenance, and integrity metadata. The principal omission is the missing full uploaded Fable response. The earlier seven Chinese answers and the complete conservative interpretation package remain genuinely unavailable as exact originals and must not be reconstructed from summaries.

### MNEMOSYNE-097

The read-only evidence audit was a reasonable response to lower model strength. Its direct-default-branch write was a workflow error, not an authority/content error. The Q2-2 table is useful. R3-F-001 was correctly reclassified as not currently reproduced in the live manifests; R3-F-003 remains a user-preference/retention question; R3-F-004 remains an absence-based wayfinding question rather than a demonstrated safety defect.

### MNEMOSYNE-098

Useful corrective support instrument. Because ordinary ChatGPT conversation state is not durable, recording the branch/write preflight in the repository is justified despite being process overhead.

### MNEMOSYNE-099 and MNEMOSYNE-100

Safe but more elaborate than necessary. The decision package and transfer prompt preserve the deferred Q2-2/R3 review and are still usable. No further packaging layer should be added before the actual review is run.

## Greenfield charter assessment

The uploaded charter is strong and should be accepted as the working plan for the independent reference-design track.

Strengths:

- It correctly defines the output as a contrastive reference, not a replacement or execution source.
- It honestly states that Fable cannot be clean-room by amnesia because the same conversation lineage saw the current design; independence is therefore enforced by derivation, source restriction, and exposure disclosure.
- Its source firewall, incidental-exposure ledger, derivation citations, atomicity assumptions, and verbatim-storage rules are appropriate.
- It separates independent design from the later comparison phase.
- It distinguishes genuinely new Deep Research topics from already-covered or merely stale topics.

Refinements to apply when running steps, without editing the original charter:

1. **Use the normal order `1 -> 2 -> 3 -> 4 -> 5`.** The shrinking-window fallback `1 -> 3 -> 2 -> 5 -> 4` conflicts with the charter's own comparison gate unless the user explicitly waives Step 4. Step 5 must not precede Step 4 by default.
2. **Add hard usage caps to each execution prompt.** Qualitative labels such as `medium` and `large` are not enough for a five-hour usage window. Each prompt should set maximum retrieval batches/files, a target output size, a checkpoint/stop condition, and a continuation ledger.
3. **Split large steps when needed.** GF-STEP-3 and GF-STEP-5 are explicitly large and should normally be split. GF-STEP-1 may also be split into bounded source extraction and synthesis passes if Fable reports quota pressure.
4. **Keep user-origin evidence separate from concept-time assistant proposals.** The charter already says to extract the underlying user need rather than copy mechanisms; step outputs should label `user_origin_evidence`, `assistant_origin_era_proposal`, and `independent_design_choice` distinctly.
5. **Use short source anchors rather than repeated long quotations.** This preserves derivability while controlling context and output cost.
6. **Recognize existing storage authorization.** The user has already authorized PR-based storage of later Fable responses/files without re-asking. This satisfies the charter's storage-approval boundary for this track, while still not authorizing execution-source changes or auto-merge.

## Additional work identified

```yaml
immediate:
  - store the uploaded charter verbatim under FABLE5-GREENFIELD-001
  - add the previously uploaded full Fable triage response verbatim and update its raw manifest
next_fable_work:
  - run a bounded GF-STEP-1 pilot or Step-1 substep with explicit usage caps
  - preserve the exact prompt and downloadable output after completion
separate_pending_track:
  - execute MNEMOSYNE-100 Q2-2/R3 advisory review when useful
  - do not create another package before executing that review
not_needed:
  - no new execution-source update
  - no current-state/handoff update for the greenfield charter
  - no Codex task for simple artifact storage
  - no paused-route resumption
```

## Preliminary higher-model view on Q2-2/R3

This is advisory and not a final task decision:

- Q2-2 is better modeled as **layered canonicalization** than as choosing one global six-item list. The dry-run result is canonical for original run warnings; the maintainer review is canonical for ingestion/acceptance interpretation; the freeze/package list is canonical for handoff-carry semantics. Frozen artifacts should not be rewritten to force artificial list identity.
- R3-F-001 currently needs no repair because the live manifests no longer contain the stale line.
- R3-F-003 should remain a user-preference decision; a processed/superseded marker is lower-risk than deletion if later cleanup is desired.
- R3-F-004 should not automatically add a live-route pointer: the Fable work is inserted advisory work, and forcing it into live current-state files could contaminate the paused route. Existing review indexes may be sufficient unless the user wants review-track discoverability in live state.

## Boundary

This review is not execution source and does not itself authorize repair, execution-source changes, target workspace/material/write/build/regression actions, Codex tasks, auto-merge, or resumption/closure of the paused post-handoff route.
