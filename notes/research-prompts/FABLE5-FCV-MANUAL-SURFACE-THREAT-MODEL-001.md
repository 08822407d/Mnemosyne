# FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001

```yaml
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
execute_in: fresh_Fable_5_high_or_xhigh_research_conversation
exact_topic: Independent threat model and evidence audit of a manual multi-conversation surface for Mnemosyne frontier-clarification V0
role: independent_surface_isolation_provenance_no_write_and_operator_burden_review
repository: 08822407d/Mnemosyne
pinned_baseline_commit: use_latest_master_containing_MNEMOSYNE_182_after_merge_or_explicit_user_supplied_commit
repository_access: read_only
repository_write: prohibited
connected_service_write: prohibited
validation_execution: prohibited
context_creation_or_live_surface_test: prohibited
real_or_private_data: prohibited
prior_Pro_or_Fable_reports_supplied: false
canonical_report_required_in_final_response: true
complete_response_copy_filename: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-complete-response.md
```

## 1. Input-integrity and repository-read gate

This is an independent static threat-model task. Do not assume the manual surface is acceptable merely because it is convenient or described as a low-cost diagnostic.

Before substantive analysis, verify:

- the exact task ID and topic are visible;
- the complete task text is available;
- the repository and exact commit under audit are recorded;
- all mandatory files are separately readable at that commit;
- no prior Pro or foundational Fable report is supplied;
- the task does not authorize creating fresh conversations, transferring packets, connecting GitHub, using credentials, spending quota or executing V0;
- current product/platform claims are verified from authoritative current sources or explicitly marked unknown.

Mandatory files:

```text
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
notes/frontier-clarification-validation-package/README.md
notes/frontier-clarification-validation-package/01-protocol-spec-v0.1.md
notes/frontier-clarification-validation-package/02-condition-contracts-q0-q4-v0.1.md
notes/frontier-clarification-validation-package/04-hidden-author-keys-v0.1.md
notes/frontier-clarification-validation-package/07-reviewer-and-adjudication-taskbook-v0.1.md
notes/frontier-clarification-validation-package/08-v0-sentinel-context-isolation-taskbook-v0.1.md
notes/frontier-clarification-validation-package/10-run-manifest-template-v0.1.md
notes/frontier-clarification-validation-package/11-result-return-and-maintainer-review-package-v0.1.md
notes/frontier-clarification-validation-package/12-execution-surface-and-user-decision-package-v0.1.md
current/human-approved-spec.md
```

If any mandatory file is missing, truncated, from a different version or not accessible, return only:

```yaml
status: INPUT_OR_REPOSITORY_INTEGRITY_FAILURE
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
analysis_started: false
repository_commit:
missing_or_conflicting_paths: []
reason:
```

If the gate passes, complete the report in one run. Do not stop at a plan.

## 2. Decision this report can change

The report must support exactly one primary disposition:

```yaml
allowed_surface_dispositions:
  - MANUAL_PREFLIGHT_WORTH_PREPARING
  - MANUAL_PREFLIGHT_WORTH_PREPARING_ONLY_WITH_REQUIRED_AMENDMENTS
  - MANUAL_ROUTE_BLOCKED_PREFER_API_OR_RUNTIME_PREPARATION
  - DEFER_ALL_SURFACE_SELECTION
  - STOP_VALIDATION_ROUTE
```

The report may compare surface classes but does not select a provider, authorize credentials, create a harness or approve V0.

## 3. Independent surface reconstruction

Reconstruct the proposed manual surface as an execution system rather than a set of chats.

Identify:

- actors and contexts;
- what each context knows;
- what is transferred manually;
- what state may be shared by the product outside the visible transcript;
- what tools, files, connectors, project memory or account memory may be available;
- how packet and output identity are preserved;
- how scripted owner turns are released;
- how reviewer separation is established;
- how repository no-write claims are supported;
- what the human operator must do and can accidentally change.

Produce a data-flow/context graph and a trust-boundary table.

## 4. Threat model

At minimum analyze these threat classes:

### 4.1 Context and memory contamination

- prior chats in a Project or workspace;
- account/global memory;
- project-only/default memory ambiguity;
- reused conversation contexts;
- hidden system or workspace instructions;
- old uploaded files or connected repository context;
- model/provider cache or session behavior that is not user-observable;
- worker exposure to another condition or reviewer material.

Distinguish what can be prevented, observed, operator-declared, mechanically attested or only assumed.

### 4.2 Connected tools and repository access

- GitHub selected globally, per chat, through a plus menu or inherited workspace configuration;
- read versus write capability;
- persistent permission versus task authorization;
- broad file, web, app or connector access;
- a worker searching for hidden keys or other condition files;
- inability to prove that a connector was unavailable;
- actions outside default-branch commits, including branches, PRs, comments, labels or issues.

Do not infer current product behavior from old reports. Verify current facts where material.

### 4.3 Packet and artifact identity

- copy/paste truncation or formatting conversion;
- attachment transformation;
- line-ending or encoding changes;
- packet labels leaking condition identity;
- mismatch between recorded hash and rendered worker input;
- operator edits;
- incomplete output capture;
- hidden reasoning or product summaries being mistaken for canonical output;
- duplicate or reordered scripted turns.

Determine the minimum reconstructable identity standard appropriate to V0.

### 4.4 Hidden-key and scripted-turn handling

- human controller sees keys and later contaminates a worker;
- reviewer context created from a worker context;
- key file accidentally attached to a Project;
- future scripted turns released early;
- operator paraphrases or repairs a scripted response;
- condition-specific differences in timing or formatting;
- reviewer key defects.

### 4.5 No-write evidence

- unchanged `master` but a new branch/PR/comment exists;
- model self-report of no tool use;
- incomplete open-PR enumeration;
- connector logs unavailable;
- operator uses another chat or tab during the run;
- repository activity from an unrelated actor;
- before/after comparisons that are too narrow;
- historical run-scoped exceptions being treated as precedent.

Specify which evidence classes can support which claim scopes.

### 4.6 Surface fallback and model-condition drift

- visible mode changes;
- product fallback or quota notice;
- user-selected label not attesting backend;
- reviewer/worker conditions silently differing;
- mid-run context length or feature changes;
- one condition receiving tool access or a stronger visible mode.

Define when a run is blocked, invalid or still interpretable with limitations.

### 4.7 Human operator burden and error

- number of contexts, transfers and receipts;
- repetitive manual hashing/logging;
- wrong packet to wrong worker;
- accidental leakage through clipboard or Project files;
- reviewer/result file mix-up;
- inability to preserve exact outputs;
- fatigue during 40-cell V1;
- manual route changing the measured burden more than the clarification architecture.

Estimate V0 and V1 orchestration burden ranges with transparent assumptions. Do not claim precise product timings without evidence.

## 5. Evidence ladder

Create an evidence ladder for each required property:

```yaml
evidence_ladder_entry:
  property:
  strongest_practical_evidence:
  weaker_but_possible_evidence:
  operator_declaration_only:
  unacceptable_evidence:
  claim_scope_supported:
  residual_risk:
  recommended_result_if_unavailable: PASS_WITH_LIMITATIONS | BLOCKED | INVALID | FAIL
```

Required properties:

- fresh worker context;
- no prior task material;
- no hidden-key exposure;
- no other-condition exposure;
- no connected tool/repository access;
- exact packet identity;
- exact output identity;
- reviewer separation;
- no repository write;
- stable visible model/mode condition;
- complete transfer log.

## 6. Manual-route preflight audit

Review every step and field in:

```text
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
```

For each requirement, classify:

```yaml
preflight_requirement_review:
  requirement:
  necessary: true | false | conditional
  sufficient: true | false | unknown
  observable_on_manual_surface: yes | partial | no | current_fact_unverified
  defect_or_gap:
  minimum_amendment:
  required_before: preparation | owner_decision | V0 | V1
```

Identify bureaucracy that adds little evidence and missing controls that materially affect trust.

## 7. V0 adequacy

Determine whether a zero-substantive-cell V0 can meaningfully qualify a manual surface.

Required questions:

- Can sentinel workers detect Project/memory/tool contamination without seeing hidden keys?
- What deliberate leakage or negative-control probes are needed?
- Can context isolation be demonstrated without relying on the worker's own promise?
- What exact artifact should the worker echo or return to prove packet identity?
- Can a manual reviewer be separated strongly enough for V0?
- Which V0 pass claims remain invalid for V1?
- Should V0 test all five visible condition configurations or only surface mechanics?
- What result should follow when context state is unknown but no direct contamination is observed?

Propose the minimum credible manual V0 preflight and the minimum credible V0 run, clearly separating them.

## 8. V1 feasibility and route switching

Even though V1 is not authorized, analyze whether a manual V0 route creates a dead end.

- estimated number of contexts and transfers for 40 primary cells;
- error accumulation and operator burden;
- whether packet/output identity remains feasible;
- whether reviewers can remain independent;
- whether the surface should be allowed to switch after V0;
- what evidence from manual V0 transfers to API/runtime V1;
- whether architecture comparisons become confounded by surface changes.

Do not design or execute V1. Recommend only route-selection implications.

## 9. Compare manual, API and runtime architecture classes

Compare the architecture classes from the decision package using:

- context isolation;
- hidden-state observability;
- tool/file permission control;
- packet and output identity;
- no-write evidence;
- repeatability;
- reviewer separation;
- credential and secret risk;
- external cost;
- implementation burden;
- operator burden;
- V0 diagnostic value;
- V1 scalability;
- platform dependence and staleness.

Do not assume API or runtime is automatically safer. Identify their own failure modes, including shared caches, harness bugs, credential leakage, incorrect logging and correlated reviewer configuration.

## 10. Run-scoped exception analysis

The manual candidate allows no implicit exception. Analyze whether any narrow exception framework would ever be defensible when default no-write or isolation proof is unavailable.

Required fields for a defensible exception proposal:

```yaml
exception_candidate:
  exact_run:
  default_evidence_missing:
  reason_missing:
  substitute_evidence:
  claim_scope_narrowed_to:
  confidence:
  approved_by:
  independent_human_verification:
  expires_with_run: true
  not_future_precedent: true
  unacceptable_residual_risks: []
```

State when the correct result is simply `BLOCKED` rather than inventing an exception.

## 11. Minimum amendment ledger

Return:

```yaml
surface_amendment_ledger:
  - finding_id:
    severity: BLOCKING | HIGH | MEDIUM | LOW
    affected_file_or_step:
    threat:
    evidence:
    consequence:
    minimum_fix:
    verification_method:
    required_before: owner_selection | preparation | V0 | V1
    current_product_fact_needs_reverification: true | false
```

## 12. Evidence and current-fact requirements

Use official, current platform documentation where a product claim materially affects the decision. Use primary technical sources for API/runtime isolation, logging, permissions or model metadata. For empirical or human-factors claims, use relevant research with calibrated transfer.

Clearly separate:

- verified current product fact;
- observed/operator-declared UI state;
- general architecture property;
- adjacent empirical evidence;
- original threat-model reasoning;
- unknown or non-attestable property.

Include a portable source table with literal URLs, stable identifiers, dates, access status, claim mapping and limitations.

## 13. Required final report sections

1. Input-integrity receipt
2. Executive surface disposition
3. Independent manual-surface reconstruction
4. Context/data-flow and trust-boundary graph
5. Threat inventory
6. Context and memory isolation
7. Connected tools and repository access
8. Packet/output identity
9. Hidden-key and reviewer separation
10. No-write evidence
11. Surface fallback/model-condition drift
12. Human operator burden
13. Evidence ladder
14. Manual preflight audit
15. V0 adequacy
16. V1 feasibility and route-switch implications
17. Manual/API/runtime comparison
18. Run-scoped exception analysis
19. Required amendment ledger
20. Unknowns and evidence gaps
21. Portable source table
22. Final disposition, confidence and boundaries

Begin with:

```yaml
input_integrity_receipt:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  exact_topic: Independent threat model and evidence audit of a manual multi-conversation surface for Mnemosyne frontier-clarification V0
  full_task_text_available: true
  repository: 08822407d/Mnemosyne
  repository_commit:
  mandatory_paths_read: []
  prior_Pro_or_Fable_reports_used: false
  live_surface_or_validation_executed: false
  current_product_claims_verified_or_marked_unknown: true
  substantive_analysis_completed: true
```

End with exactly one allowed surface disposition and a confidence statement.

## 14. Delivery and authority boundary

The complete report body must appear in the final response. If the current Fable surface supports file creation, also create:

```text
FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-complete-response.md
```

The file is a transfer copy of the same report, not separate authority.

State that exact served backend identity is unknown or not attestable unless provider metadata for the exact run exists.

Do not:

- modify GitHub or any connected service;
- create or inspect live worker conversations for this task;
- execute V0/V1/V2/V3;
- use private/real user material;
- authorize credentials, cost, surface selection or an exception;
- approve an execution-source or target-truth change;
- infer backend identity from visible labels, latency, style or self-report;
- assess or profile the current user;
- claim the report itself is authority.