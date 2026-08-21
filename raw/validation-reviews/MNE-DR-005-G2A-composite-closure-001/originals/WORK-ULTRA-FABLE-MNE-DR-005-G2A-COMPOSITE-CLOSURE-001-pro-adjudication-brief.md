NON_AUTHORIZING_CANDIDATE — DO NOT SEND TO A CONTROLLER UNTIL A LATER PRO REVIEW AND SEPARATE OWNER G2A.

# Pro Adjudication Brief — Composite G2A Candidate

```yaml
brief_id: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-PRO-BRIEF-001
subject: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-COMPOSITE-G2A-CANDIDATE-001
subject_file_sha256: e51af7f7c175bf9ce43171a56921f77a51dfe5d05cff973ae4f05ceadf3a2516
composed_against_mnemosyne_master: e726dea818dca9418181775d0e7dcd62eb6c464a
this_brief_authorizes: nothing
```

## 1. What this candidate is, in one paragraph

One complete, non-authorizing controller G2A/startup text for the V2-A A1 positive independent pair, composed under the Package 004 line. It binds candidate/manifest 004 and the inherited 003/002/001 pairs by exact blob, imposes 004→003→002→001 reading and scoped precedence, embeds the two Package 003 canonical `BEGIN…END` wrapper blocks byte-exactly (cmp-verified against blob `20ca5ceb…`; canonical SHA-256 `8d82d785…` / `798f8ba6…`), retains Package 002 staged label timing and Package 001 ceilings, declares the Package 002 §4/§5 prose wrappers historical for wrapper transport, and leaves every dynamic value a placeholder with `G2A_authorized: false` fixed. It removes the message-composition ambiguity that motivated this task: exactly one wrapper transport (canonical blocks), exactly one fill schedule, exactly one precedence map.

## 2. Ordering reminder before this review can even start

Per the current F2 status gate and Package 004's publication closure, the Handoff 003 post-merge receive rehearsal must be accepted before the fresh Pro execution-time review of Packages 004/003/002/001. This candidate does not alter that sequence. Reviewing this candidate is part of, not a substitute for, that execution-time review.

## 3. Mechanical checks Pro should repeat independently

1. Re-derive both canonical blocks from `notes/…-package-003/02-canonical-runtime-wrapper-transport-and-comparison-contract.md` at its then-current (must still be `20ca5ceb…`) blob and `cmp` them against candidate §6.1/§6.2. Expect byte identity and canonical SHA-256 `8d82d785612bd1a42a284e23b80cc22b14b1b89ec2528d0382da1c7e1cd0b210` (Alpha) and `798f8ba658430559e479c5244806edf2d22894b49de9a70bfd92349de013b445` (Beta) over BEGIN…END plus exactly one trailing LF.
2. Re-verify all eight candidate/manifest path/blob pairs and the archive tuple (`6e90c8f1…` controlling; `7c2af723…` superseded for scope) against then-current master.
3. Re-run the 40-hex whitelist scan on the candidate (20 expected values; any new 40-hex string is a defect) and the hygiene scan (no CR, no BOM, no trailing spaces, banner on line 1, `G2A_authorized: false` present).
4. Confirm the placeholder inventory is exactly: eight issuance placeholders, two authorized-label wrapper placeholders (shared tokens with the issuance list), two `__MNE_*_AT_LAUNCH__` selected-label placeholders, and nothing else fillable; confirm the two superseded Package 002 tokens occur only inside the [C-13] supersession clause.
5. Confirm live validation pins still equal the candidate §3 values (master `e8e3296…`, fixture `81f18eb…`/`f1e221c…`, A0 head `d936cd2…`, 16 `tlr-v1-*` refs per pkg001 manifest §4, five A1 names absent, zero PRs).

## 4. The five flagged items requiring a Pro decision

- F1 language presentation. The composite body is English; the historical pkg002 §3 message was Chinese. All operative tokens, IDs, SHAs and stop words are byte-exact and language-independent. Options: accept as-is, or commission a Chinese parallel rendering whose tokens must be byte-identical; if both exist, name one canonical.
- F2 state-token spelling. `NOT_YET_OBSERVED_UNTIL_ALPHA_LAUNCH` / `…BETA_LAUNCH` (message layer, from pkg002/03 §3) versus `not_yet_observed` (yaml layer, from pkg002/02 §2). The candidate declares the rendering relation at [C-08]. Options: accept the declared equivalence, or normalize to one token in the issued message.
- F3 composite candidate ID. `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-COMPOSITE-G2A-CANDIDATE-001` is newly minted by this task and exists in no repository. Pro/Owner confirm or rename before any publication.
- F4 `<G2A_TIMESTAMP_UTC>`. Added to satisfy this task's "timestamps" dynamic class; no package lists it as a G2A field (packages list `execution_window_start`). Keep or drop at issuance-template time; it carries no authority either way.
- F5 V1 inventory by reference. Candidate §3 binds "exactly the 16 tlr-v1 refs and SHAs frozen in Package 001 manifest §4" instead of re-listing them. Live heads were verified equal during composition. Pro may require inline listing in the issued message.

## 5. What must happen between Pro acceptance and any execution

1. Pro completes the execution-time review of Packages 004/003/002/001 including this candidate, resolving F1–F5.
2. The Owner — separately, and only if the Owner so decides — issues the real G2A by sending a message that reproduces every static binding of this candidate exactly and fills only the eight issuance fields of [C-08] from then-current repository state and direct Owner/operator evidence. Alpha/Beta selected labels are not filled there; they remain `not_yet_observed` until each worker launch.
3. Nothing in this brief, in the candidate, in the adversarial review or in the composition task's `READY` verdict is, implies, or schedules that Owner decision.

## 6. Non-effects of this composition task (attested in the complete response)

No repository write, no branch or ref movement, no PR, no G2A, no A1 branch, no controller or worker launch, no package modification, no expected-value refresh, no Web/Research use, and no cold-source read occurred. GitHub was accessed read-only; both repositories' start and end states were captured and equal.
