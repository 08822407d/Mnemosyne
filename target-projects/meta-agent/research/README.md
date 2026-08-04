---
target_project_id: meta-agent
artifact_id: META-AGENT-RESEARCH-EVIDENCE-README-004
artifact_role: research_evidence_navigation
status: independent_wave_reports_adjudicated_PR_247_pending_MA_DR_09_report_pending_intake
authority_level: navigation_and_evidence_support
target_runtime_truth_source: false
last_updated_by_task: META-AGENT-INDEPENDENT-WAVE-REPORT-RECORDING-001
canonical_Batch_A_recording_PR: 242
canonical_independent_wave_task_recording_PR: 246
current_report_recording_PR: 247
---

# Meta-Agent Research Evidence

## 1. Role and authority

This directory preserves research tasks, exact report exports, evidence identities, intake reviews, convergence decisions, candidate ledgers and prepared follow-up tasks.

Nothing under `research/` is Meta-Agent target truth. Research cannot override:

```text
target-projects/meta-agent/current/approved-spec.md
```

Research completion, report convergence and PR merge do not authorize operational activation, private material, a pilot, methodology promotion, tools or external writes.

## 2. Research collections

### DR-01–05 foundational round

```text
target-projects/meta-agent/research/
  archive/
  meta/manifest.yaml
  reviews/MA-DR-01-05-cross-report-synthesis-v0.1.md
  reviews/MA-DR-01-05-gap-analysis-v0.1.md
```

Five original prompts and five complete reports are preserved. Their product-native source-panel links were not independently preserved.

### Batch A — MA-DR-06 / MA-DR-07

```text
target-projects/meta-agent/research/batches/2026Q3-batch-a/
```

Batch A preserves exact reports, intake reviews, cross-report adjudication, a candidate ledger, the MA-DR-08 task package and the former deferred input contract for MA-DR-09.

```yaml
MA_DR_06: ACCEPT_EVIDENCE_ONLY_TARGET_MAPPING_BLOCKED
MA_DR_07: ACCEPT_WITH_CORRECTIONS_AS_NON_EXECUTION_SOURCE_EVIDENCE
cross_report: ACCEPT_BATCH_A_AS_NON_EXECUTION_SOURCE_EVIDENCE_WITH_CORRECTIONS
```

### Independent Wave — MA-DR-08 / MA-DR-10–15

```text
target-projects/meta-agent/research/waves/2026Q3-independent-wave-001/
```

PR #246 recorded the seven independent task specifications. PR #247 records:

- exact MA-DR-08 and MA-DR-10–15 report transports;
- original report identities and remote reconstruction verification;
- seven per-report reviews;
- the MA-DR-11 enhanced correctness review;
- cross-report convergence;
- a candidate-only convergence ledger;
- formal adjudication and downstream gates;
- a runnable MA-DR-09 task, operator guide and return contract;
- active-context and handoff synchronization.

```yaml
remote_report_transport_components: PASS_56_OF_56
remote_report_reconstruction_SHA256: PASS_7_OF_7
wave_disposition: ACCEPT_INDEPENDENT_WAVE_AS_NON_EXECUTION_SOURCE_EVIDENCE_WITH_REVIEWER_CORRECTIONS
clean_reruns_required: 0
```

## 3. MA-DR-09 execution and intake state

```yaml
prepared_task_status: READY_NOT_SELECTED
external_run_reported_completed_by_Owner: true
report_received_by_dedicated_conversation: true
formal_intake_and_evidence_adjudication: pending_separate_task
report_recorded_in_PR_247: false
duplicate_run_prohibited: true
```

The task artifact records the research contract. The returned report remains unaccepted external evidence until a separate review checks identity, inputs, completeness, sources, protocol quality and target-specific mapping.

## 4. Evidence and candidate lifecycle

```text
research task
-> canonical report/export
-> exact identity and input/completeness review
-> per-report and cross-report adjudication
-> candidate change ledger
-> specification or experiment
-> Owner decision
-> authorized target/method change
-> validation and rollback/revision record
```

No research report, review, model inference or candidate becomes target truth because of location, recency, length or multi-report agreement.

## 5. Preservation and portability

- Original bytes are preserved where the relevant manifest says exact preservation was performed.
- Missing images, opaque citations, current-document freshness, preprint maturity and legal/jurisdiction limits remain recorded in reviews.
- Reports must not be silently normalized, rewritten or replaced by summaries.
- Derived reviews may be superseded, while historical reports and source roles remain traceable.

## 6. Public-repository boundary

Only public/non-sensitive research, synthetic fixtures, explicitly redacted material or safe pointers may enter this public-risk bootstrap repository after task-local preflight. Secrets, private source, confidential/customer material and unredacted personal/chat/voice records remain prohibited without a separately approved storage route.

## 7. Current next action

```yaml
current_action: human_review_and_merge_PR_247
after_merge: separate_MA_DR_09_report_intake_and_adjudication
no_automatic_target_change: true
no_automatic_pilot_or_activation: true
```
