# MNE First Three Systems Owner Review — OR-01 Result

> Owner-review evidence for the first full human pass over the reusable Agent capability catalogue. This record is not an execution source, does not update Meta-Agent or any target truth, and does not authorize target creation, private-material ingestion, external research, or operational activation.

```yaml
result_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
task_id: MNEMOSYNE-202
source_package_task: MNEMOSYNE-201
source_catalogue: notes/reusable-agent-capability-catalog-v0.1.md
source_catalogue_version: 0.1.0
source_master_at_interview_start: bd15d62b3111a9f2e55aa64151943f7b4d7f8713
question: OR-01
status: COMPLETE_WITH_CATALOGUE_AMENDMENTS_AND_OPEN_VALIDATION_ITEMS
owner_disposition: ACCEPT_WORKING_CATALOGUE_WITH_REVISIONS_AND_REAL_USE_REFINEMENT
execution_source_modified: false
Meta_Agent_modified: false
target_repository_modified: false
external_research_or_quota_used: false
```

## 1. Review method selected by the Owner

The Owner did not accept or reject the 42-entry catalogue as a single block. The Owner required:

1. six batches of seven capabilities;
2. a plain-language explanation for every capability;
3. an item-by-item response of no problem, amendment, uncertainty, or need for later explanation;
4. deferred resolution of disputed items until all 42 had been reviewed once;
5. later target-specific selection from the reviewed capabilities rather than wholesale copying of the catalogue.

This method completed all 42 entries. It demonstrated that a human-readable catalogue can support deliberate selection, but also exposed duplicate scope, provider-specific facts, speculative boundaries, and terminology needing refinement.

## 2. OR-01 conclusion

The capability-catalogue approach is accepted as a **working inventory and selection aid**, not as a final ontology or an approved universal runtime package.

The catalogue may be used for the next target-selection stage after the v0.2 candidate incorporates the amendments below. Catalogue completeness is not a launch gate. Real target use must continue to reveal omissions, excessive controls, ambiguous names, and evidence gaps.

The catalogue remains:

- non-execution-source;
- non-authoritative for Meta-Agent or target systems;
- subject to target-specific selection and adaptation;
- separate from provider/model/product facts;
- revisable through evidence and Owner review.

## 3. Capability dispositions

### 3.1 Accepted without a material catalogue change

```text
ACAP-001, ACAP-002, ACAP-007, ACAP-008,
ACAP-014, ACAP-015, ACAP-016, ACAP-018, ACAP-019, ACAP-021,
ACAP-023, ACAP-024, ACAP-025, ACAP-026,
ACAP-029, ACAP-032, ACAP-037
```

Notes:

- `ACAP-002` is understood as one unambiguous **currently adopted authority boundary**, not one physical file and not simply the newest artifact by timestamp.
- `ACAP-006` was accepted after explanation, but receives a preservation-scope amendment in §3.2.
- `ACAP-034` was accepted in purpose but remains empirically immature, so it appears in §3.3 rather than this list.
- `ACAP-035` is handled under the material duplicate-resolution amendment in §3.4 rather than the unchanged list.

### 3.2 Accepted with a concrete semantic amendment

| Capability | Owner-reviewed amendment |
|---|---|
| `ACAP-003` | Artifact roles should normally be reflected in human-navigable repository/store organization, not only metadata. Target layouts may differ and need not copy Mnemosyne directory names. |
| `ACAP-004` | Separate byte identity, format normalization, and substantive-content change. A line-ending-only transformation changes bytes but may preserve substantive content; user-facing wording should not imply a semantic rewrite. |
| `ACAP-005` | Mechanical duplicate checks may be delegated, but material semantic conflict detection across old/new needs and ideas should use frontier/open-ended reasoning because neither the human nor a bounded executor can reliably retain all long-range implications. |
| `ACAP-006` | Preserve all material external engineering rationale and its source paths; do not delete or over-compress it merely because it may be large. Review can proceed newest-to-oldest along a small number of relevant paths. Private hidden chain-of-thought remains out of scope. |
| `ACAP-009` | The primary reason cold source is not execution source is role: raw conversations, research, and design inputs exist to be analyzed, compared, selected, and synthesized into approved control logic. Context saving and reduced interference are additional runtime benefits. |
| `ACAP-010` | Add explicit handling for a contemplated behavior with no matching specific rule: use general authority/safety rules for low-risk reversible work, stop for high-impact gaps, disclose the gap, and create a candidate coverage item rather than silently inventing a new active rule. |
| `ACAP-011` | A target may have a compact disaster-recovery snapshot or backup elsewhere if it is explicitly non-authoritative, immutable or read-only, identity-pinned, and prohibited from becoming an independent writer. |
| `ACAP-017` | Add a staged intent-clarification pattern: next-tier preliminary framing/questions; frontier analysis of answers and true need; frontier-prepared follow-up package; next-tier explanation and answer capture. |
| `ACAP-020` | Broaden beyond learning Agents. Long-lived systems must not infer stable user traits from sparse, context-dependent, mood-dependent, or changing requirements. Scoped recurring-pattern models may be useful only when the target purpose, evidence, correction rights, and uncertainty justify them. |
| `ACAP-027` | Treat a short contextual correction such as “排版不对” or “内容排版不对”, immediately after transfer content, as a likely Markdown/YAML/code-block transfer-format failure and offer a structure-preserving repair rather than mere aesthetic reformatting. |
| `ACAP-028` | Do not encode ChatGPT Deep Research's current one-report behavior as a universal Agent capability. Generalize the portable part to canonical-output and representation-role separation; keep provider-specific output topology as dated product evidence. |
| `ACAP-030` | One canonical active PR is a current safety default, not a claim that safe parallel contribution is impossible. Future validated coordination may permit parallel variants or multi-writer development with explicit reconciliation. |
| `ACAP-031` | Retained branches need durable obligations, release gates, responsible routes, and periodic stale/zombie audits. Periodic or automated maintenance may inspect obligations but must not delete without verification and authority. |
| `ACAP-038` | Replace rollback-centered wording with early bounded use plus controlled evolution. Upgrade, migration, recomputation, retirement, or re-evaluation are normal paths; rollback is only one possible response. |

### 3.3 Accepted in direction but explicitly provisional pending real use

| Capability | Current limitation and required evidence |
|---|---|
| `ACAP-012` | Version/migration/evolution direction accepted; detailed boundaries remain under-informed by real target migrations. |
| `ACAP-013` | Upstream-impact assessment accepted; no multi-target deployment evidence yet establishes the minimum useful registry or impact workflow. |
| `ACAP-022` | Stop/escalation purpose accepted; reliable model self-recognition of capability limits is unresolved. Validation must balance bounded persistence against premature frontier escalation. |
| `ACAP-033` | Cross-repository ordering and authority accepted; general concurrency, partial failure, and recovery behavior need real target evidence beyond the Meta-Agent migration. |
| `ACAP-034` | Evaluation/feedback/postmortem purpose accepted; practical thresholds, evidence burden, and promotion paths remain speculative before repeated real use. |
| `ACAP-039` | Conditional retrieval automation accepted; no measured deterministic-retrieval failure threshold exists yet. |
| `ACAP-040` | Packaging portable capabilities into executable prompts/instructions/configuration is important but insufficiently analyzed; it requires focused design and target/provider experience. |
| `ACAP-041` | Skill/module packaging is accepted only as a provider-adapter question. It must be learned from current product documentation and actual Claude/other provider use. |
| `ACAP-042` | A dated provider/model/product capability catalogue is valuable, but reliable population requires repeated current-fact verification and bounded task testing. |

### 3.4 Duplicate resolution

`ACAP-035` and `ACAP-036` were judged by the Owner to appear fully duplicative.

The v0.2 disposition is:

- retain `ACAP-035` as **controlled case-to-general-method promotion and portability filtering**;
- merge the substantive portability-filter steps from `ACAP-036` into `ACAP-035`;
- retire `ACAP-036` as a separate active catalogue entry while preserving a v0.1-to-v0.2 mapping;
- do not reuse `ACAP-036` for an unrelated future capability.

## 4. Execution-source terminology alignment

The Owner's accepted working analogy is:

> model ≈ CPU; execution source ≈ the currently approved program that controls the model's formal behavior.

Operational clarification:

- an execution source is the approved programmatic/behavioral control layer;
- raw inputs, research, candidates, rationale, history, current state, and handoff may inform or support that program but do not control behavior automatically;
- a target truth source may be broader than an execution source because it can also include authoritative data, configuration, or current business state;
- “current” means currently adopted and authoritative, not merely most recently written.

This terminology record does not modify `current/human-approved-spec.md`.

## 5. Target-selection implication

After v0.2 is available, target-specific selection should:

1. choose capabilities separately for Meta-Agent, the work/business-function code-library system, and the long-term language-teacher/practice Agent;
2. use accepted/refined capabilities as ordinary candidates;
3. mark empirically immature capabilities as triggered experiments or deferred evidence needs rather than silently treating them as proven hard requirements;
4. keep provider adapters and dated product facts separate;
5. reference catalogue IDs/versions instead of loading the entire catalogue into target runtime context.

No target selection is approved merely by this OR-01 result.

## 6. Model-segment and evidence limits

```yaml
interview_segments:
  - segment: next_tier_interviewer
    operator_selection_verbatim: 次一档模型
    role:
      - explain_batches
      - capture_owner_feedback
      - maintain_chat_ledger
    exact_backend: unknown_or_not_attestable
  - segment: frontier_review_and_recording
    operator_selection_verbatim: Pro
    role:
      - adjudicate_feedback
      - create_v0_2_candidate
      - record_repository_result
    exact_backend: unknown_or_not_attestable
```

The Owner's answers in the current conversation are direct decision evidence for this candidate review. They do not attest model backend identity or prove that a capability is empirically effective.

## 7. Remaining owner-review scope

`OR-02` through `OR-09` were not completed by this record. They remain available for later capability selection, target storage, launch ordering, and provider-fact decisions after the revised catalogue is reviewed.
