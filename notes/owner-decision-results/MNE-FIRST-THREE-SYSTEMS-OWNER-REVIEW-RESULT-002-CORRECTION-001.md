# Correction 001 — First Three Systems Owner Review Result 002

> Explicit correction to one provenance/classification statement in `MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md`. This correction does not change any target's selected capability outcome.

```yaml
correction_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002-CORRECTION-001
source_result: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md
source_audit: notes/audits/first-three-systems-owner-review-transcript-audit-v0.1.md
task_id: MNEMOSYNE-207
status: active_correction_pending_merge
execution_source: false
target_selection_changed: false
```

## Corrected statement

In result 002 §3.1, the OR-02 shared default-active floor must **not** include `ACAP-037`.

Correct OR-02 shared floor:

```text
ACAP-001–009
ACAP-011–012
ACAP-014–015
ACAP-017–019
ACAP-021
ACAP-023–034
ACAP-038–042
```

`ACAP-037` was selected separately for all three targets:

- Meta-Agent: OR-03;
- code-library Agent: OR-04;
- natural-language learning Agent: OR-05.

## Effect

- Meta-Agent still requires `ACAP-037`.
- Code-library Agent still requires `ACAP-037`.
- Natural-language learning Agent still requires `ACAP-037`.
- Only the decision-route attribution changes.

Readers must apply this correction when interpreting result 002 and selection v0.3 provenance.
