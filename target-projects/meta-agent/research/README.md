---
target_project_id: meta-agent
artifact_id: META-AGENT-RESEARCH-EVIDENCE-README-003
artifact_role: research_evidence_navigation
status: DR_01_05_and_Batch_A_recorded_MA_DR_08_ready_not_selected
authority_level: navigation_and_evidence_support
target_runtime_truth_source: false
last_updated_by_task: META-AGENT-SUPPORT-METADATA-SYNC-001
canonical_Batch_A_recording_PR: 242
canonical_Batch_A_merge_commit: 531aab228836915162ec5f5c45cbbcfc97f1e572
---

# Meta-Agent Research Evidence

## 1. Role and authority

This directory preserves Meta-Agent research tasks, report originals/exports, evidence identities, intake reviews, cross-report adjudications, candidate ledgers and staged follow-up tasks.

Nothing under `research/` is Meta-Agent target truth. Research evidence cannot override:

```text
target-projects/meta-agent/current/approved-spec.md
```

Research conclusions, task readiness and PR merge state do not authorize operational activation, private material, a pilot, methodology promotion, tool use or external writes.

## 2. Research collections

### DR-01–05 foundational round

```text
target-projects/meta-agent/research/
  archive/
  meta/manifest.yaml
  reviews/MA-DR-01-05-cross-report-synthesis-v0.1.md
  reviews/MA-DR-01-05-gap-analysis-v0.1.md
```

The deterministic archive preserves five original prompts and five complete operator-exported reports. Its product-native source-panel links were not independently preserved.

### Batch A — MA-DR-06 / MA-DR-07

```text
target-projects/meta-agent/research/batches/2026Q3-batch-a/
```

Batch A was recorded on `master` through PR #242. This collection preserves:

- exact `MA-DR-06` and `MA-DR-07` report exports;
- individual intake reviews;
- cross-report adjudication;
- a candidate-change ledger;
- the Batch-B gate;
- a prepared `MA-DR-08` task package;
- a deferred input contract for `MA-DR-09`.

Current evidence disposition:

```yaml
MA_DR_06: ACCEPT_EVIDENCE_ONLY_TARGET_MAPPING_BLOCKED
MA_DR_07: ACCEPT_WITH_CORRECTIONS_AS_NON_EXECUTION_SOURCE_EVIDENCE
cross_report: ACCEPT_BATCH_A_AS_NON_EXECUTION_SOURCE_EVIDENCE_WITH_CORRECTIONS
```

## 3. Current external-task execution intent

```yaml
MA_DR_08:
  execution_disposition: READY_NOT_SELECTED
  current_execution_requested: false
  current_execution_required: false
  quota_authorized: false

MA_DR_09:
  execution_disposition: DEFERRED
  runnable_task_present: false
```

Readiness is not selection. A later response must explicitly use a `RUN_*` disposition and provide a dedicated operator flow before the user is asked to spend quota or launch another conversation.

## 4. Evidence and candidate lifecycle

```text
research task
-> canonical report/export
-> identity/input/completeness review
-> cross-report adjudication
-> candidate change ledger
-> Owner decision
-> authorized target/method change
-> validation and rollback/revision record
```

No research report, review, model inference or candidate becomes target truth by location, recency or length.

## 5. Preservation and portability

- Original report bytes are preserved where the package manifest says exact preservation was performed.
- Missing images, inaccessible repository inputs, opaque citations, current-document freshness and preprint version limits are recorded in the relevant manifest/review.
- Research reports must not be silently normalized, rewritten or replaced by summaries.
- Derived reviews may be superseded, but their historical role and source reports remain traceable.

## 6. Public-repository boundary

Only public/non-sensitive research material, synthetic fixtures, explicitly redacted material or safe pointers may enter this public-risk bootstrap repository after task-local preflight. Secrets, private source, confidential/customer material and unredacted personal/chat/voice records remain prohibited without a separately approved storage route.

## 7. Update rule

A future task may add a report, correct a review, supersede a gate or prepare a later task. It may not silently:

- change the target truth source;
- expand accepted methodology;
- activate Meta-Agent;
- authorize a pilot;
- select external research execution;
- import the Mnemosyne maintenance route.
