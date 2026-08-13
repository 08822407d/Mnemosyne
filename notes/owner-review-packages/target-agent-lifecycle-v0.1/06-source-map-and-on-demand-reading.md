# Source Map and On-Demand Reading

```yaml
package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
```

## 1. Required sources

These are read during receive:

- `current/human-approved-spec.md` — current Mnemosyne execution source and authority boundaries;
- `notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md` — Owner-confirmed OR-02 through OR-09 decisions;
- `notes/first-three-system-capability-selection-v0.3.md` — consolidated target capability selection;
- `notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md` — architecture candidate under review;
- `notes/target-agent-container-evolution-and-dependency-frontier-adjudication-v0.1.md` — Pro/frontier findings and repair recommendations;
- `notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md` — prepared validation scenarios and evidence plan;
- all package files.

## 2. On-demand sources

Read only for the named need and disclose the additional path.

### `notes/target-local-repository-operating-model-candidate-v0.1.md`

Use when the Owner asks how the earlier dedicated-repository model handled primary writes, concurrency, bootstrap, or parent/meta records.

### `current/github-single-active-pr-lineage-guard.md`

Use when the Owner asks whether same-repository concurrency changes the one-task/one-canonical-PR rule. It does not; the question concerns distinct tasks.

### `current/source-artifact-preservation-and-design-rationale-guard.md`

Use when the Owner asks what must be preserved in parent-owned design records, how exact originals differ from summaries, or why same-conversation memory is not exact source.

### `current/run-context-and-pr-provenance-guard.md`

Use when the Owner asks how model/surface/write provenance is recorded or why visible model selection does not attest the backend.

### `notes/reusable-agent-capability-catalog-v0.2.md`

Use when a question depends on exact ACAP-011, 012, 013, 033, 034, 037, or 038 wording.

### `notes/first-three-systems-frontier-reentry-backlog-v0.1.md`

Use when the Owner asks how this review relates to Meta-Agent readiness, language-learning research, or backups.

## 3. Default cold/do-not-read material

Do not read by default:

- full current-conversation export;
- historical Mnemosyne construction conversations;
- full research prompts/reports;
- old handoffs and completed task archives;
- old OR-01 or OR-02 interview packages;
- Meta-Agent historical bootstrap tree;
- code-library/language-target repositories;
- paused FCV/Fable materials;
- unrelated current route files.

## 4. Context discrepancy route

If the Owner alleges that result 002 omitted or altered a specific earlier decision:

1. record the exact alleged discrepancy;
2. do not resolve it from model memory;
3. request or use the exact exported conversation if available;
4. perform a bounded transcript-to-result audit of the named scope;
5. preserve any correction as a new decision record rather than silently rewriting historical evidence.

A general worry that long chats may omit context is not by itself evidence that a specific saved decision is wrong.

## 5. Missing source behavior

If a required source is missing or materially inconsistent, stop with:

`MISSING_ARTIFACT_BLOCKS_DECISION — <path and affected TLR question>`

Do not fill the gap from old chat memory.
