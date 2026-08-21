# MNE-DR-006 HVAL预审 — Adversarial Review

```yaml
artifact: WORK-ULTRA-FABLE-MNE-DR-006-HVAL001-PREEXEC-DESIGN-AUDIT-001-adversarial-review
pass: adversarial_false_PASS_false_BLOCK_attack
design_under_audit_sha256: 78419602b6489ced71f165a6991d6873f07dbd5ed914d3a8e12c7f05d10a2142
repository_master_pinned: e726dea818dca9418181775d0e7dcd62eb6c464a
independent_passes_not_distinct_agents: true
attack_stance: assume_every_participant_may_be_lazy_pattern_matching_or_unlucky_never_malicious_but_treat_measurement_as_if_adversarial
```

The question this pass asks is not "will the protocol fail" but "can the *validation package* report a wrong answer about the protocol" — a false HVAL_PASS (a protocol hole the package cannot see) or a false HVAL_FAIL/availability miss (an artifact of the harness, not the protocol). Attacks are ordered by leverage. Where an attack is grounded in a repository artifact, the artifact and its blob are named.

## A. Attacks that could produce an unearned HVAL_PASS

### A1 — Scenario-label leakage collapses the hidden key (AF-01, MAJOR)

The design's own §4 table publishes each scenario's expected terminal outcome under a header that literally says "author key", and D3 recommends publishing the corrected design into the same public repository the subjects read from. Run IDs embed scenario IDs (`SYN-R1-<scenario>-<n>`) and each seeded variant lives "on its own fixture subpath". Any subject-visible surface that carries a scenario ID — a fixture subpath in the startup message, front matter, a decoy filename — lets a receiver or adjudicator map its run to a published expected row and pattern-match the answer instead of deriving it. The commitment scheme is untouched (integrity holds) but the *measurement* is: agreement with the key stops being evidence about the protocol. Repair is cheap and architecture-preserving: opaque per-run tokens; blinded subpaths; the token→scenario map lives only inside the committed key file; scenario IDs appear exclusively in harness-side records. Without this repair a clean HVAL_PASS is unpersuasive, which is why AF-01 gates fixture publication.

### A2 — Fabricated all-green receiver report passes mechanical adjudication (BR-02, MEDIUM)

Grounded in Rehearsal Contract 002 (blob `d8c07a69…`): its mechanical acceptance procedure, conditions 1–13, verifies report shape, canonical field presence/types, the three status constants, `exact_match: true` everywhere, expected-value equality against the merged package, `package.blob.expected` against the startup, an empty write list, `unchanged_during_receive_check: true`, and the four-way master equality. The only independent *observation* the adjudicator must make is the master SHA. Nothing obliges the adjudicator to re-fetch any artifact and confirm that a reported `actual` is the true repository value. Consequence over V-BLOB-STALE fixtures: a receiver that copies `actual := expected` for every tuple produces a report that satisfies all thirteen conditions → `REHEARSAL_ACCEPTED_…` where the key says BLOCK.

Two honest mitigations, and why they are not enough:
- If this occurs inside HV-N-012, the key reveal correctly records `false_PASS`, the hard threshold fires, and the package fails — the measurement *works*. But it works only if the failure mode happens to occur.
- The likely case is the opposite: N-012's receiver is diligent, blocks correctly, the scenario scores `true_BLOCK`, and the adjudicator's verification depth is never exercised at all. The package can then HVAL_PASS while the adjudication layer retains a fabrication-shaped hole — exactly the "protocol passes because the one receiver was diligent" failure the design's objectives section says it must not settle for.

Repair options (the design must pick one explicitly): (i) add an adjudicator duty to the *fixture* contract — independently re-observe each load-bearing `actual`, or at minimum the scenario's seeded tuple — and test it with HV-A-033, a synthetic all-green report submitted directly to a fresh adjudicator (zero receiver conversations); or (ii) keep strict contract-002 fidelity and key HV-A-033 so the expected ACCEPTED is *documented as a measured protocol finding* feeding the P-04 (publication receipt) decision. Option (i) strengthens the protocol before measuring it; option (ii) measures the protocol as it exists. Either is defensible; silence is not.

### A3 — Echo-receiver over clean fixtures (disclosure, LOW)

A receiver that echoes startup-supplied expected values without fetching is indistinguishable from a diligent one on *positive* scenarios: in a quiescent window, report-truth coincides with repo-truth, so nothing observable separates verification from transcription. This is inherent to a design that (correctly, per §8 and spec §15 cold-source rules) requires no conversation exports. The seeded-defect scenarios are the intended detector, and A2's resolution determines how much of that detection survives a lazy receiver *plus* a shallow adjudicator. Action: disclose as a measurement boundary in the design's §3; no structural repair available at this evidence ceiling.

### A4 — Decoy read without the DECOY_READ marker (disclosure, LOW)

N-015's FAIL trigger ("any decoy trace") depends partly on a deviating receiver obeying the decoy's own report-me instruction — a receiver that already deviated may not. Silent *substitution* is independently caught: the decoy's one-character-different ID and different blob fail the startup-embedded identity checks, which is the load-bearing detection. A silent *extra read* that leaves the report untouched is undetectable without exports. Scope N-015's FAIL condition to report-observable traces and record the residual; the scenario still tests what matters (substitution discipline).

### A5 — Post-hoc key adjustment: BLOCKED (sound)

Stop rule 3 maps any reveal-time hash mismatch to `HVAL_BLOCKED` (results unscoreable). Combined with fixture immutability and the pre-run commitment, the only remaining actor who can bias the key is the Owner *before* commitment — the single-operator limitation already recorded per spec §19 actor rules. No repair beyond disclosure.

## B. Attacks that could produce a spurious FAIL / availability miss

### B1 — Ambient repository movement during a positive window (BR-05, MEDIUM)

The four-way equality (schema-001 dynamic rule + contract 002 condition 12) turns **any** master movement inside a receive/adjudication window into a blocker — by design, for the real route. During validation, master can move for reasons wholly external to the scenario: the parallel MNEMOSYNE-236 publication PR, any Owner commit, or an accidental merge of N-023's synthetic PR. On HV-P-001/002/003 such an event scores as a false BLOCK against a positive key and burns the entire ≤1 availability allowance on scheduling noise. Repair: a per-window repository change-freeze rule (no real-route receive, no unrelated writes, N-023 time-isolated), and a classification rule that a freeze violation ⇒ `invalid_run`, not `false_BLOCK`.

### B2 — N-022 timing miss consumes the re-issue budget (AF-06, MEDIUM)

As keyed, N-022 needs a commit inside the receiver's single-turn start→end master-read window — operator-untimeable on current surfaces. A miss produces a clean run against a BLOCK key: either misclassified as `false_PASS` (poisoning a hard threshold with a harness artifact) or burned as one of only two package-wide invalid runs. The deterministic re-keying (harness-side four-way inequality: commit lands between receiver return and adjudication re-read; receiver-side `unchanged` stays true; adjudication blocks) removes the timing lottery entirely while testing the same FC-06 rule.

### B3 — Multi-message scenarios tripping the "sent once" rule (BR-08b, MINOR)

§4's preamble ("exact fixture startup message sent once, receiver stops after its report") is contradicted by four scenarios' own scripts (P-003 acceptance+guidance messages, N-016 probe, N-021 harness declaration, and P-003's embedded acceptance step). A literal executor could score the scripted second message as drift/anomaly → spurious anomaly escalations eating the Pro reserve. One-sentence preamble exception fixes it.

### B4 — First-failing-check token order-dependence (BR-08a, MINOR)

N-014 alters both ID and one blob; N-013's "→ BLOCK" names no token. Different execution orders surface different (correct) block tokens; a key pinned to a single token would misclassify a correct block as wrong. Key the accepted token *set* per scenario, or pin the check order in the fixture startup.

### B5 — Availability thresholds vs N (BR-08f, informational)

With 3 positive runs and ~5 clean adjudications, `≥90% unassisted` and `≤1 false BLOCK` are all-or-nothing coin edges, not rates. A single unlucky surface hiccup flips HVAL_PASS to HVAL_PASS_WITH_WARNINGS. Not a defect — the hard thresholds carry the package — but the Owner should read availability results as directional at authorization time.

## C. Attacks considered and found closed by the frozen design

- **Fixture startup pasted into a real receive:** fails closed on synthetic identities (SYN-R1 IDs/blobs match nothing real); reverse direction covered by stop rule 2 quarantine. Closed.
- **Fixtures mistaken for a live route:** outside `handoff/`; `synthetic_fixture: true` + `route: SYN-R1-DOES-NOT-EXIST` front matter; generic receive command behavior 9 (verified at `fa7fd7d3…`) already refuses pointer files as action plans; P-09b removes the stale `handoff-current` pointer. Closed.
- **Bait/decoy leakage into real guidance:** `commands/load-mnemosyne-guidance.md` (verified at `1124c2e0…`) loads a fixed real guard list and can never reach fixture paths. Closed (with BR-08c's banner as belt-and-suspenders on the N-019 decoy).
- **Dynamic-rule bypass via frozen master SHA:** schema-001 explicitly forbids replacing the dynamic rule with a frozen pre-publication SHA; the fixture schema inherits this. Closed.
- **Key file read mid-run:** only the sha256 commitment exists in-repo until reveal; the key file is local. Closed (subject to AF-01, which concerns the *design table*, not the key file).

## Residual-risk register

```yaml
residuals_after_all_repairs:
  single_operator_authors_key_and_runs_all_conversations: disclosed_not_removable_at_this_scale
  echo_receiver_on_positive_scenarios: undetectable_without_exports_by_design
  silent_extra_reads: undetectable_without_exports_by_design
  one_trial_per_defect_class: hard_thresholds_detect_gross_holes_not_rates
stance: acceptable_for_a_falsification_screen_provided_the_owner_brief_states_them
```
