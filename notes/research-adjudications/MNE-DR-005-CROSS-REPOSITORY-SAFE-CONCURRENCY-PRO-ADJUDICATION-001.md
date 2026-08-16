# MNE-DR-005 Cross-Repository Safe Concurrency — Pro/Frontier Adjudication 001

```yaml
adjudication_id: MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
reviewer_surface: ChatGPT_Pro
backend_identity: unknown_or_not_attestable
review_task_id: MNEMOSYNE-221
return_identity: PASS_EXACT
run_validity: ACCEPT_WITH_LIMITATIONS
input_verification: PASS_WITH_BOUNDED_IDENTITY_DEFECT
task_contract_compliance: PASS_WITH_LIMITATIONS
citation_portability: FAIL
architecture_direction: ACCEPT_AS_CORROBORATED_MODIFIED_PROVISIONAL_DIRECTION
technical_detail_disposition: ACCEPT_WITH_MATERIAL_CORRECTIONS
implementation_readiness: REJECT
candidate_v0_2_modified_by_this_adjudication: false
validation_execution_authorized: false
real_target_adoption_authorized: false
execution_source_modified: false
Meta_Agent_modified: false
```

## 1. Bottom line

The Fable report is accepted as substantial independent advisory evidence, but not as a directly adoptable specification.

Its central direction is sound:

- keep target-local task contracts and exact scope evidence as the normal baseline;
- permit concurrency only for demonstrably independent work;
- fail closed or explicitly reconcile shared, repository-global, authority-changing or unknown work;
- do not make a permanent central orchestrator the mandatory route for all repository writes;
- treat cross-repository work as ordered, identity-bearing steps with explicit failure handling;
- require stronger synthetic failure evidence before claiming production readiness.

That direction largely corroborates the already Owner-accepted Target Lifecycle candidate v0.2 rather than replacing it. Candidate v0.2 already contains task-local write contracts, read/dependency sets, shared/global classification, merge-order dependency handling, no-dual-writer boundaries and the rule that Git mergeability is insufficient evidence of semantic non-interference.

The report nevertheless adds useful pressure in four areas:

1. stale read/ref handling;
2. partial failure in ordered cross-repository work;
3. generated/derived-object and hidden semantic interference;
4. explicit fault-injection cases before any stronger acceptance claim.

Recommended Owner disposition:

```text
ACCEPT_MODIFIED_F2_PROVISIONAL_AMENDMENT_AND_PREPARE_BOUNDED_V2_DESIGN
```

This recommendation authorizes neither V2 execution nor any real-target write.

## 2. Exact return-integrity gate

The receive-only handoff required reconstruction of the Fable return from eight ordered base64 parts.

Fresh Pro verification produced:

```yaml
archive:
  byte_size: 27293
  sha256: d141fb3962c61617e2051c9b318516d63437e287f7b88b2f3e41df9d130c0559
  ZIP_CRC_check: PASS
  deterministic_member_timestamps: true

formal_report:
  archive_name: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001-report.md
  byte_size: 42407
  sha256: 83468668e64a7bf9b82292b0b672d6cb8b249e4cd069395df3a0888b9eda2ccd
  Git_blob_sha1: 9b877ba8dae3b77fec777cfbc02ca089a7150bd5

visible_process_output:
  archive_name: MNE-DR-005-visible-process-output.md
  byte_size: 20298
  sha256: 4575975fa7af3dd2de3d8fbf4d06dd662257efc94f046d335c48a0731d964304
  Git_blob_sha1: d2583901f217506ac968be993d18dda31f0ef492
  exact_hidden_provider_trace_claimed: false
```

The eight staged Git blob identities, their order and sizes all match the source manifest. The uploaded Markdown byte streams match the corresponding reconstructed ZIP members.

Disposition:

```text
RETURN_IDENTITY_PASS_EXACT
```

## 3. Run and task-contract compliance

### Accepted

- the report has all 28 required substantive sections;
- it compares all six required mechanisms A–F;
- it analyzes all fourteen required failure classes;
- it selects exactly one allowed final disposition:
  `RECOMMEND_HYBRID_LOCK_AND_TASK_CONTRACT_MODEL`;
- Project Search/RAG semantic coverage occurred before reported external web research;
- the report preserves historical V1 `pending_fresh_Pro` fields as historical evidence while recognizing the later fresh-Pro and Owner decisions as current state;
- it does not claim production readiness or real-target adoption;
- no repository write, validation execution, automatic retry or private-target access is reported;
- the final report distinguishes repository evidence, external claims and inference.

### Limitations

- Project RAG retrieval does not prove byte-complete reading;
- the visible process transcript is Owner-supplied provider-visible output, not an exact hidden execution trace;
- the process output states both “10 Project Search/RAG calls” and contains eighteen visible `Searched project for` entries;
- the formal report says exact visible model/effort are unknown, while the visible process says the selected model was `Claude Fable 5`; no exact effort label was returned;
- the received report contains no portable links, footnotes, citation markers or source table despite the UI/process claim of 244 sources.

These limitations do not invalidate the independent architecture analysis. They do prevent treating every detailed external claim or quotation as verified evidence.

## 4. Input-verification adjudication

The 30-file semantic-coverage result is accepted with one bounded identity defect.

### Accepted

The report correctly recovered:

- the 2 + 14 + 14 input topology;
- the task and snapshot manifest identities;
- Mnemosyne execution-source and active-guard roles;
- the historical V1 execution package and controller evidence;
- the current fresh-Pro adjudication and Owner architecture decision;
- V1 selected scenarios, M0–M11, no-write proof, S8 isolation, S11 restore and incident ledger;
- the historical/current two-layer interpretation of `pending_fresh_Pro`;
- the bounded nature of `V1-PROTOCOL-DISCREPANCY-001`.

### Bounded identity defect

The correct Owner architecture-decision blob is:

```text
bc4cd7950831c6382c200b64c7e6be74ad6a8459
```

The formal report truncates it to:

```text
bc4cd7950831c6382c200b64c7e6be74a8459
```

The visible process output notices a length problem but repeatedly reproduces the same malformed value rather than resolving it.

This is a real failure of the “complete repository/ref/path/blob mapping recovered” claim. It is bounded because:

- the correct source path, document role and current decision semantics were recovered;
- the exact 40-character blob remains present in the snapshot manifest, task and source file;
- no substantive recommendation depends on the missing three characters.

Disposition:

```text
INPUT_VERIFICATION_PASS_WITH_BOUNDED_IDENTITY_DEFECT
```

Future Fable coverage gates should validate all claimed SHA-like identities mechanically for length and equality before issuing `PASS`.

### Post-run F1 state

The Fable run consumed the exact launch-time F1 candidate blob:

```text
accb13ccb57677d316f5f94ef58f7939ad69521b
```

At launch that file said `pending_Owner_disposition`. A separate later Owner-decision route is being published through PR #288. That later decision must be treated as post-run state: it does not retroactively change the Fable input or invalidate this F2 report, and this F2 route must not edit or pre-empt the F1 PR.

## 5. Accepted architecture findings

### 5.1 Authority and task-writer separation

Authority ownership, one-task write permission and physical tool access are separate layers. A task writer does not become a second authority owner, and a connector capable of writing does not create task authorization.

### 5.2 Default task-local mechanism

The default should remain:

- one task identity;
- one canonical branch/PR lineage;
- pinned base and material read/dependency identities;
- exact write scope;
- final diff/path verification;
- no automatic cross-target propagation.

### 5.3 Conservative scope escalation

Shared, repository-global, authority-changing or unknown work must not be treated as ordinary independent concurrency. It must serialize, reconcile explicitly or stop for a human/Owner gate.

### 5.4 No universal central orchestrator

Current evidence does not justify a permanent global coordinator or transaction service through which every repository write must pass. Such a system would add a high-authority dependency before repeated contention or strong-atomicity demand has been demonstrated.

### 5.5 Ordered cross-repository work

Cross-repository work needs:

- explicit step order;
- committed/immutable identity handoff between steps;
- revalidation of the preceding result;
- explicit stop and recovery behavior when a later step fails;
- no claim of distributed atomicity.

### 5.6 Evidence scope

No-write and no-dual-writer evidence applies only to the named repositories, refs, time window and observed action surface. It must not be generalized to unnamed real targets.

### 5.7 More failure evidence before stronger acceptance

The existing V1 run is useful bounded evidence but does not establish production-grade concurrency. Synthetic failure injection is justified before any stronger global acceptance or real-target adoption claim.

## 6. Material technical corrections

### 6.1 Disjoint write sets are not a sufficient concurrency proof

The report sometimes states that disjoint exact write sets plus absence of shared/global paths are sufficient—or effectively “if and only if”—for safe concurrency.

That is too strong. Safe concurrency also depends on:

- read/write and version dependencies;
- generated or derived outputs;
- semantic contract changes;
- authority and destination changes;
- base-ref freshness;
- merge-order dependence;
- dependencies on uncommitted results;
- side effects outside the named repository/path surface.

Candidate v0.2 already contains several of these exclusions. The corrected test is a conservative non-interference proof, not path-disjointness alone.

### 6.2 Final diff checking is not optimistic concurrency control

A final diff/path check proves that actual writes stayed inside the declared write scope. It does not prove that the task read a still-current dependency or that another task did not invalidate its assumptions.

An optimistic-concurrency analogue needs at least:

1. record read/version identities;
2. re-read or validate them before publication/merge;
3. abort or reconcile if they changed;
4. verify the final write scope.

The report's “mechanical diff as OCC validation phase” is therefore incomplete.

### 6.3 Lease expiration is not enough; fencing is required

A timed lease can bound how long a failed holder blocks progress. It does not by itself prevent an expired or partitioned former holder from issuing a delayed write.

Any future distributed lease/lock mechanism would need a monotonically increasing fencing token, epoch or sequencer that the protected write destination validates and rejects when stale.

No lock/lease service is justified for Mnemosyne now. The present default should remain task/PR serialization and explicit reconciliation. Reconsider a lease only after repeated shared-object contention is observed and the destination can enforce fencing.

### 6.4 “Saga” is a useful model, not an automatic rollback authorization

The saga analogy correctly highlights ordered local steps and partial failure. It does not make arbitrary GitHub changes safely compensatable.

For current Mnemosyne work:

- the normal recovery is stop, preserve the committed identities, and choose forward repair or an explicit revert;
- automatic compensation is permitted only when the inverse operation is predeclared, separately authorized, idempotent and tested;
- destructive reset/force-push is not a default rollback for canonical or shared branches;
- an evidence publication should normally be corrected/superseded rather than erased.

### 6.5 GitHub stale-ref mechanisms are surface-specific

The report correctly observes that the REST `Update a reference` endpoint accepts `sha` and `force`, not an expected-old SHA. For that endpoint—and for the current connector action—an application-layer read/pin/re-read check is needed.

The platform-wide statement is incomplete:

- the PR `update-branch` REST endpoint has `expected_head_sha`;
- GitHub GraphQL `updateRefs` supports `beforeOid` and atomic multi-ref updates.

The durable rule should therefore require the strongest available precondition on the selected tool surface and record the remaining limitation. It should not claim GitHub lacks conditional ref updates universally.

### 6.6 GitHub Actions concurrency semantics were misstated

The report's broad statement that a new run with the same concurrency key cancels an already running workflow is not generally correct.

Current GitHub semantics distinguish:

- pending-run replacement/cancellation;
- in-progress cancellation only when `cancel-in-progress` is enabled;
- queuing options on current surfaces;
- no general ordering guarantee in the documented concurrency mechanism.

Actions concurrency is also repository/workflow-local and is not a cross-repository authority lock. It may be a bounded implementation option for a future automated workflow, not a current architecture default.

### 6.7 Merge queue is optional, not a baseline requirement

A merge queue rechecks required status checks against the latest target branch and queued predecessors. That is useful for busy branches with reliable CI.

It does not prove semantic non-interference and is not universally available or proportionate for Mnemosyne's current low-volume, Owner-merged documentation PR flow. Current single-lineage, current-base and human merge gates remain sufficient unless traffic and CI evidence justify a queue.

### 6.8 SLSA level labels must not be applied to the current attestations

SLSA Build L1 requires provenance automatically generated by a conforming build platform. The V1 Owner/worker self-attestations are not thereby “approximately SLSA L1.”

SLSA is useful as an analogy for increasing provenance strength. Mnemosyne should use its own evidence-level vocabulary unless a real SLSA-conforming build/provenance pipeline exists.

### 6.9 Candidate novelty was overstated

The report lists as needed corrections several rules already present in candidate v0.2:

- task-local write contracts;
- `read_or_dependency_set`;
- shared/repository-global/unknown scope classes;
- explicit serialization or reconciliation;
- merge-order semantic dependence;
- provider/capability common-object conflicts;
- “Git text mergeability is not sufficient.”

The report should be treated as corroboration plus a narrower delta, not evidence that candidate v0.2 lacked these concepts.

## 7. External-claim verification disposition

The report's portable citation package fails: the Markdown has zero URLs, zero Markdown links, zero footnotes and no source list.

Fresh Pro independently checked the load-bearing claims against primary/official sources:

| Claim area | Pro disposition |
|---|---|
| GitHub REST ref update has `sha`/`force` but no expected-old SHA | accepted for that endpoint |
| PR branch update has `expected_head_sha` | accepted |
| GitHub GraphQL has no relevant CAS/atomic multi-ref mechanism | rejected; `updateRefs.beforeOid` exists |
| merge queue validates latest base plus queued predecessors | accepted, with scope/proportionality limits |
| Actions concurrency always cancels the running job | rejected as a general statement |
| Chubby supports coarse-grained locking | accepted |
| lease TTL alone safely excludes stale writers | rejected; fencing/epoch validation is needed |
| saga uses ordered local transactions and compensating transactions | accepted as an analogy |
| in-toto artifact rules default to allow unless explicitly disallowed | accepted |
| current self-attestations are approximately SLSA Build L1 | rejected as a level claim |
| least privilege applies to the toolchain | accepted as a general security direction |
| 2021 Meta outage illustrates control-plane/tool coupling | accepted as an analogy; financial-loss estimate not retained |

No external quotation, incident statistic or vendor behavior from the Fable report becomes durable project fact unless independently verified and cited in the implementing design.

### Primary sources used for the Pro spot-check

The following current official/primary sources were used for the bounded claim check:

```text
GitHub REST API endpoints for Git references
https://docs.github.com/en/rest/git/refs

GitHub REST API endpoints for pull requests — Update a pull request branch
https://docs.github.com/en/rest/pulls/pulls#update-a-pull-request-branch

GitHub GraphQL reference — updateRefs / RefUpdate.beforeOid
https://docs.github.com/en/graphql/reference/git#updaterefs

GitHub Actions — Concurrency
https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency

GitHub Docs — Managing a merge queue
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue

Mike Burrows, The Chubby Lock Service for Loosely-Coupled Distributed Systems, OSDI 2006
https://www.usenix.org/legacy/event/osdi06/tech/full_papers/burrows/burrows_html/

Hector Garcia-Molina and Kenneth Salem, Sagas, SIGMOD 1987
https://doi.org/10.1145/38713.38742

SLSA v1.2 — Build Track Basics
https://slsa.dev/spec/v1.2/build-track-basics

in-toto — Getting Started / Artifact Rules
https://in-toto.io/docs/getting-started/

NIST SP 800-218 — Secure Software Development Framework v1.1
https://csrc.nist.gov/pubs/sp/800/218/final

Meta Engineering — More details about the October 4 outage
https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/
```

These sources support or correct only the bounded points listed above. They do not independently validate the whole Fable report or select a Mnemosyne architecture.

## 8. Corrected provisional F2 amendment

The associated amendment candidate narrows the accepted delta to:

1. expand non-interference evidence beyond write-set intersection;
2. add read/version freshness and tool-specific publication preconditions;
3. define generated/derived and semantic effects explicitly;
4. define ordered cross-repository checkpoints without claiming ACID;
5. prefer stop + forward repair/revert over automatic compensation;
6. require fencing before any lease can protect external writes;
7. use project-native provenance/evidence levels;
8. stage future synthetic validation instead of one universal IJ1–IJ11 gate.

Candidate v0.2 itself is not modified by this adjudication.

## 9. Corrected validation direction

The Fable IJ1–IJ11 list is valuable as a failure inventory, but it mixes three different validation surfaces and should not be one mandatory universal gate.

Recommended staged design:

### V2-A — Core repository concurrency and stale-state failures

- generated/derived-object collision;
- stale read/base ref;
- merge-order dependence;
- duplicate canonical PR lineage;
- shared/global/unknown scope blocking;
- mechanical-green/semantic-failure case.

### V2-B — Ordered cross-repository failure and recovery

- second repository step fails after first step commits;
- predeclared recovery succeeds;
- recovery fails and escalates to human;
- cutover rejects the stale former writer;
- backup cannot become live authority.

### V2-C — Connector and permission boundary

- cross-repository read/write denial;
- least-privilege credential scope;
- provider-visible denial evidence;
- privacy/material isolation.

V2-C requires a separate product/security authorization because it may exercise connector permissions. A lease-service failure case is relevant only after a lease mechanism actually exists.

Passing one stage does not imply production readiness or per-target adoption.

## 10. Owner-only decisions and next gate

Only the Owner may decide:

1. whether to accept the corrected F2 amendment candidate;
2. whether to authorize preparation of a bounded V2 design package;
3. whether to authorize any V2 execution;
4. whether to elevate the global architecture above provisional status;
5. whether any real target may adopt or test the model.

The recommended immediate option is:

```text
A — accept the modified provisional amendment and authorize V2 design only
```

No validation execution, target adoption, lock service, automatic compensation, merge queue, connector policy or candidate-v0.2 modification occurs from this adjudication alone.
