# V2-A A1 Composite G2A Candidate — Fresh Pro Adjudication 001

```yaml
adjudication_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-COMPOSITE-G2A-PRO-ADJUDICATION-001
source_task: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001
source_candidate:
  filename: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-composite-g2a-candidate.md
  bytes: 26377
  sha256: e51af7f7c175bf9ce43171a56921f77a51dfe5d05cff973ae4f05ceadf3a2516
source_verdict: CANDIDATE_COMPOSITION_READY_FOR_PRO
formal_disposition: SOURCE_CANDIDATE_NOT_DIRECTLY_ISSUABLE_MATERIAL_TRANSFORMATION_DEFECT_REPAIRED_WITHOUT_PACKAGE_SEMANTIC_CHANGE
packages_004_003_002_001_readiness: PASS_PRESERVED
G2A_issued: false
A1_execution_authorized: false
repository_writes_performed_by_this_adjudication: false
```

## 1. Input and independent checks

The six Fable output files passed byte/hash verification against their output manifest. This Pro review independently checked:

- the candidate file is UTF-8 without BOM, LF-only, with no trailing spaces;
- both embedded Package 003 canonical runtime-wrapper blocks are byte-identical to blob `20ca5ceb51c8991d29acef81124ec9276f8c1b2c`;
- canonical block SHA-256 values are:
  - Alpha: `8d82d785612bd1a42a284e23b80cc22b14b1b89ec2528d0382da1c7e1cd0b210`;
  - Beta: `798f8ba658430559e479c5244806edf2d22894b49de9a70bfd92349de013b445`;
- current Mnemosyne has only `master`, the validation repository has the expected 18 branch names, the five A1 names remain absent, and both repositories have no open PR;
- Package 002's controlling worker selected-label state is exactly `not_yet_observed`.

No cold original was read.

## 2. Material defect missed by the Fable audit

The Fable candidate correctly follows its task's non-authorization rule, but it does not define a mechanically exact transformation into a future authority-bearing Owner message.

Its fixed outer content states, among other things:

- `G2A_authorized: false`;
- the artifact is not an Owner G2A or startup message;
- review, quotation and transmission cannot flip that state.

Its C-24 then says a later Owner G2A should fill only C-08 dynamic fields and reproduce every static binding of the candidate exactly.

Those requirements cannot all hold simultaneously. Filling only C-08 while preserving every static binding would yield a message that still declares itself permanently non-authorizing. Removing or rewriting those clauses would be a substantive, undefined transformation, defeating the exact-composition objective.

```yaml
finding_id: MNE-V2A-A1-G2A-CANDIDATE-NONAUTHORIZATION-TRANSFORMATION-DEFECT-001
classification: material_pre_G2A_message_composition_defect
package_semantics_affected: false
Fable_candidate_directly_issueable: false
G2A_blocked: true
A1_runtime_failure: false
Fable_rerun_required: false
```

## 3. F1–F5 dispositions

```yaml
F1_language_presentation:
  disposition: ACCEPT_ENGLISH_LOAD_BEARING_BODY
  reason: translation would add avoidable semantic-drift risk; Chinese operator guidance remains outside the payload
F2_state_token_spelling:
  disposition: NORMALIZE_TO_PACKAGE_002_CANONICAL_NOT_YET_OBSERVED
F3_new_candidate_ID:
  disposition: PRESERVE_SOURCE_ID_AS_FABLE_EVIDENCE_ONLY
  Pro_corrected_artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-ISSUANCE-TEMPLATE-CANDIDATE-001
F4_G2A_timestamp:
  disposition: DROP
  reason: not required by Packages 001–004; execution_window_start remains
F5_V1_inventory_by_reference:
  disposition: ACCEPT
  reason: exact Package 001 manifest blob is bound and controller must read/verify its sixteen-ref inventory; duplicating it creates a second drift surface
```

## 4. Pro repair

This adjudication creates a two-layer artifact:

1. a permanently non-authorizing outer evidence/template document;
2. one exact inner `OWNER_G2A_PAYLOAD_TEMPLATE` that contains no self-negating candidate language and becomes authority only when the Owner separately sends it after allowed dynamic filling.

The inner template:

- binds Packages 004→003→002→001;
- retains exact Package 003 canonical wrappers;
- adds a post-publication self-blob placeholder for the template's own merged Git blob;
- uses `not_yet_observed`;
- removes the unsupported timestamp field;
- keeps G2A and A1 false until the Owner sends the filled payload.

Artifacts:

```yaml
template:
  filename: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-ISSUANCE-TEMPLATE-CANDIDATE-001.md
  bytes: 27490
  sha256: ae3c2f7a4d56195eec9faa99c2041404718d1d557c20a3d13ea56a66fe252265
  inner_payload_bytes: 25109
  inner_payload_sha256: bda27d39dcfe0159523721e5c8831f86886031cb3d4ba4365979ea3a5245ddd4
manifest:
  filename: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-ISSUANCE-TEMPLATE-MANIFEST-001.yaml
  bytes: 2332
  sha256: aa94da575987a5bd479a0b1eec38562bfbc934def82747cba331716a8df09e00
validator:
  filename: validate_and_fill_mne_v2a_a1_controller_g2a.py
  bytes: 5676
  sha256: 43a58a58d9696e292bf66999dc6ffdcac78191fb4b1b1178d6bf518d5eb421bf
fill_values_template:
  filename: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-G2A-FILL-VALUES-TEMPLATE-001.yaml
  bytes: 408
  sha256: a05025a129bde252d5fb45955a7cf631e44958a310bdd6b9de5e2f0d7ab35921
```

The validator was exercised with synthetic fill values and returned byte-exact PASS. That test did not issue G2A.

## 5. Formal gate

```yaml
Packages_004_003_002_001:
  readiness: PASS
source_Fable_composite_candidate:
  readiness_for_direct_Owner_issue: FAIL
Pro_corrected_issuance_template:
  readiness_for_repository_publication: PASS
  readiness_for_actual_Owner_issue: BLOCKED_UNTIL:
    - merged_repository_path_blob_readback
    - current_dynamic_field_fill
    - mechanical_fill_validation
    - separate_explicit_Owner_G2A
G2A_issued: false
A1_execution_authorized: false
```

No Package 005 is created or required. The repair is a message-publication/issuance closure artifact and does not alter any Package 001–004 execution semantics, expected value, fixture, branch map, output contract, evidence ceiling or no-retry rule.
