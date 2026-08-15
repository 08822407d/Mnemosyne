# MNE-DR-004 Capability Ownership — Pro/Frontier Adjudication 001

```yaml
adjudication_id: MNE-DR-004-CAPABILITY-OWNERSHIP-PRO-ADJUDICATION-001
canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
run_display_name: MNE-DR-003 能力归属
canonical_display_name_after_storage: MNE-DR-004 能力归属
reviewer_surface: ChatGPT Pro
backend_identity: unknown_or_not_attestable
report_disposition: ACCEPT_WITH_MATERIAL_CORRECTIONS
implementation_readiness: REJECT
execution_source_modified: false
Meta_Agent_modified: false
target_adoption_authorized: false
```

## 1. Bottom line

The report is accepted as useful independent advisory evidence. Its central direction—role-based federation, target-local authority, no automatic downstream propagation, stable capability identities, explicit lifecycle relationships, and no new shared repository at the current maturity level—is directionally sound.

The report is not accepted as an implementation specification. It contains material repository-topology and authority overstatements, has no portable source table despite reporting 218 sources, and applies package-versioning analogies more strongly than the present natural-language capability objects justify.

Recommended disposition for the Owner is `ACCEPT_MODIFIED_PROVISIONAL_BASELINE`.

## 2. Run and input integrity

Accepted:

- the task and manifest identities match;
- the report includes the required 24 sections and exactly one allowed advisory disposition;
- the visible process and report consistently state that Project knowledge coverage preceded external research;
- no repository write or validation execution is reported;
- the report preserves the distinction between operator-visible selection and hidden backend identity.

Limitations:

- Project RAG retrieval cannot establish byte-complete reading;
- absence of prohibited material was checked by retrieval, not exhaustively proved;
- the report's 218-source claim is not portable because the received Markdown contains no URLs, footnotes, citation markers or source table;
- the visible process output is user-pasted and not an exact provider trace.

These limitations do not invalidate the core architecture analysis, but they prevent treating every external example or statistic as independently verified evidence.

## 3. Accepted findings

1. Do not create a fourth shared capability repository now.
2. Physical repository location and semantic authority are different decisions.
3. Each target owns its selected capabilities, local adaptations, implementation and current truth.
4. Upstream changes create review candidates; they do not automatically modify downstream targets.
5. Published capability IDs must not be reused. Split, merge, supersession and retirement need explicit relationships.
6. A consuming target should declare the capability identity/revision it uses; any upstream impact view is derived and non-authoritative.
7. Portable semantics, provider-neutral packaging patterns, dated provider facts and target-specific configuration must remain distinguishable.
8. Any future ownership cutover requires destination-only recovery, one active writer and explicit retirement of the previous authority.

## 4. Material corrections

### 4.1 Current catalogue location and ownership

The report repeatedly describes the reusable capability catalogue as though it already resides in Meta-Agent. It currently resides in `08822407d/Mnemosyne:notes/reusable-agent-capability-catalog-v0.2.md`, and the catalogue itself states `Meta_Agent_modified: false`.

Therefore transferring catalogue authority to Meta-Agent would be a real cross-repository cutover, not a near-zero-cost clarification. No such cutover is authorized by the report, this adjudication or MNEMOSYNE-213.

### 4.2 Meta-Agent authority

Meta-Agent's `current/approved-spec.md` is an inactive target-truth baseline. `methodology/core-methodology.md` has `authority_level: method_support`. Neither currently grants Meta-Agent canonical ownership of the Mnemosyne capability catalogue.

A future Owner decision may assign a general capability family to Meta-Agent, but that is a candidate architecture change requiring explicit scope, migration, validation and no-dual-writer closure.

### 4.3 Evidence ownership

The statement that raw evidence and rationale should generally belong to Mnemosyne is too broad. The corrected rule is source-local ownership:

- the repository/store that legitimately owns or receives a material source preserves the canonical original according to its authority and privacy rules;
- other repositories retain safe identities, pointers or reviewed derivatives;
- Mnemosyne preserves research and evidence generated for Mnemosyne, but does not automatically own all target business evidence or all Meta-Agent method evidence.

### 4.4 Version model

Full Semantic Versioning is not yet a universal requirement for every natural-language capability. SemVer presupposes a declared public API and meaningful compatibility classes. Many catalogue entries remain provisional behavior descriptions without that maturity.

The present minimum should be:

- stable capability ID;
- catalogue version;
- object revision;
- status;
- supersedes/split-from/merged-into/retired relationships;
- compatibility or affected-selection note;
- target-side review when a selected revision changes.

Full MAJOR/MINOR/PATCH semantics may later be adopted for capability families with stable, testable contracts and repeated consumers.

### 4.5 New repository semantics

A fourth physical repository is not inherently a competing truth source. It becomes one only if authority/writer boundaries overlap or cutover is incomplete. A future dedicated repository could be valid if it becomes the sole canonical owner for an explicitly scoped object family.

The current reason not to create it is empirical and proportional: insufficient multi-target demand, no demonstrated publication burden, and no evidence that the lighter relation/selection mechanism is inadequate.

### 4.6 Provider adapter ownership

Dated provider facts should not automatically be placed in Meta-Agent. The owner depends on scope:

- a provider-neutral packaging method may belong to Meta-Agent methodology;
- a product fact/evidence record belongs to the project or evidence cycle that verifies and uses it;
- a target-specific adapter/configuration belongs to the target;
- portable semantics must not silently absorb a product workaround.

## 5. Corrected provisional model

### Current phase

- Mnemosyne remains the current owner of the reusable capability catalogue and Mnemosyne research evidence.
- Meta-Agent owns only its accepted general methodology and its own target truth; it may consume or reference capability candidates without becoming their owner.
- Targets own capability selections, adaptations, implementations and current truth.
- No new shared repository and no cross-repository ownership migration occurs now.
- Stable IDs, object revisions and explicit lifecycle relationships are prepared as candidate mechanisms, not active universal schema.

### Future phase

The Owner may later assign one or more portable capability families to Meta-Agent or a dedicated shared package. That requires:

1. exact object-family scope;
2. destination truth and writer declaration;
3. source-to-destination migration map;
4. reference and compatibility plan;
5. destination-only recovery;
6. retirement of the old writer;
7. target impact review;
8. explicit Owner acceptance.

## 6. Evidence value and limits

The report's external analogies—package registries, dependency graphs, ADR supersession, provenance models and supply-chain incidents—are useful for generating failure modes and candidate mechanisms. They do not decide repository authority for Mnemosyne.

Because the received report lacks portable citations, no quoted statistic, named incident, provider policy or vendor claim should be promoted into durable project fact solely from this report. Load-bearing external facts must be independently verified when they become decision-critical.

## 7. Decision and next gate

This adjudication does not ask the Owner to accept the uncorrected report. It prepares:

- `notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md`;
- `notes/owner-decision-candidates/MNE-REUSABLE-CAPABILITY-OWNERSHIP-DISPOSITION-CANDIDATE-001.md`.

No implementation, migration, target adoption or validation begins until the Owner separately accepts, modifies, defers or rejects the corrected candidate.
