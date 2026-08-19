# Canonical Receive-Report Schema 001 — F2 / V2-A A1 Handoff 003

```yaml
schema_id: MNE-F2-V2A-A1-HANDOFF-RECEIVE-REPORT-SCHEMA-001
schema_role: route_specific_machine_comparable_receive_contract
created_by_task: MNEMOSYNE-234
execution_source: false
A1_execution_authorized: false
```

This file is the single canonical field/schema definition for both Handoff Package 003 and Post-Merge Receive-Rehearsal Contract 002. Those artifacts must reference this exact path/blob and must not independently rename, flatten, alias or retype these fields.

YAML mapping order is not significant. Field paths, scalar/list/mapping types and comparison semantics are significant. A receiver may not substitute synonymous field names. The top-level key must be exactly `mnemosyne_handoff_receive`.

## Exact report shape

```yaml
mnemosyne_handoff_receive:
  report_schema:
    id:
      expected: string
      actual: string_or_null
      exact_match: boolean
    path:
      expected: string
      actual: string_or_null
      exact_match: boolean
    blob:
      expected: git_sha1_string
      actual: git_sha1_string_or_null
      exact_match: boolean

  handoff_receive_status: RECEIVED | BLOCKED_PACKAGE_ABSENT | BLOCKED_PACKAGE_ID_MISMATCH
  identity_verification_status: PASS | BLOCKED_LOAD_BEARING_IDENTITY_MISMATCH | INCOMPLETE
  substantive_continuation_status: BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE | BLOCKED_IDENTITY_OR_TASK_RECONSTRUCTION

  execution_time_master:
    repository:
      expected: string
      actual: string_or_null
      exact_match: boolean
    branch:
      expected: string
      actual: string_or_null
      exact_match: boolean
    observed_start_sha: git_sha1_string_or_null
    observed_end_sha: git_sha1_string_or_null
    unchanged_during_receive_check: boolean

  package:
    present:
      expected: boolean
      actual: boolean
      exact_match: boolean
    path:
      expected: string
      actual: string_or_null
      exact_match: boolean
    id:
      expected: string
      actual: string_or_null
      exact_match: boolean
    blob:
      expected: git_sha1_string
      actual: git_sha1_string_or_null
      exact_match: boolean
    status:
      expected: string
      actual: string_or_null
      exact_match: boolean

  execution_source:
    path:
      expected: string
      actual: string_or_null
      exact_match: boolean
    blob:
      expected: git_sha1_string
      actual: git_sha1_string_or_null
      exact_match: boolean

  supporting_commands:
    handoff_receive_command:
      path:
        expected: string
        actual: string_or_null
        exact_match: boolean
      blob:
        expected: git_sha1_string
        actual: git_sha1_string_or_null
        exact_match: boolean
    guidance_load_command:
      path:
        expected: string
        actual: string_or_null
        exact_match: boolean
      blob:
        expected: git_sha1_string
        actual: git_sha1_string_or_null
        exact_match: boolean

  identities:
    candidate_004:
      path:
        expected: string
        actual: string_or_null
        exact_match: boolean
      blob:
        expected: git_sha1_string
        actual: git_sha1_string_or_null
        exact_match: boolean
    package_004_manifest:
      path:
        expected: string
        actual: string_or_null
        exact_match: boolean
      blob:
        expected: git_sha1_string
        actual: git_sha1_string_or_null
        exact_match: boolean
    source_archive_manifest:
      path:
        expected: string
        actual: string_or_null
        exact_match: boolean
      blob:
        expected: git_sha1_string
        actual: git_sha1_string_or_null
        exact_match: boolean
    archive_reconstruction_receipt:
      path:
        expected: string
        actual: string_or_null
        exact_match: boolean
      blob:
        expected: git_sha1_string
        actual: git_sha1_string_or_null
        exact_match: boolean

  package_004_file_count:
    expected: integer
    actual: integer_or_null
    exact_match: boolean

  source_review:
    original_bytes:
      expected: integer
      actual: integer_or_null
      exact_match: boolean
    original_sha256:
      expected: sha256_hex_string
      actual: sha256_hex_string_or_null
      exact_match: boolean

  A1_status:
    execution_authorized:
      expected: boolean
      actual: boolean
      exact_match: boolean
    executed:
      expected: boolean
      actual: boolean
      exact_match: boolean
    G2A_issued:
      expected: boolean
      actual: boolean
      exact_match: boolean
    controller_or_worker_launched:
      expected: boolean
      actual: boolean
      exact_match: boolean
    validation_branches_created:
      expected: boolean
      actual: boolean
      exact_match: boolean
    validation_repository_written:
      expected: boolean
      actual: boolean
      exact_match: boolean

  receiver_guidance_load:
    project_guidance:
      expected: string
      actual: string_or_null
      exact_match: boolean
    mnemosyne_guidance:
      expected: string
      actual: string_or_null
      exact_match: boolean
    loaded_during_receive:
      expected: boolean
      actual: boolean
      exact_match: boolean

  repository_or_service_writes_during_receive:
    expected: []
    actual: list_of_strings
    exact_match: boolean

  current_task_from_package:
    task_id:
      expected: string
      actual: string_or_null
      exact_match: boolean

  forbidden_actions:
    expected: list_of_strings
    actual: list_of_strings
    exact_match: boolean

  evidence_paths_checked: list_of_strings
  evidence_paths_missing_or_unchecked: list_of_strings

  safe_next_action:
    expected: string
    actual: string_or_null
    exact_match: boolean

  limitations_or_unknowns: list_of_strings
```

## Comparison semantics

For every `{expected, actual, exact_match}` mapping:

- `expected` is copied exactly from Handoff Package 003 into the receiver report;
- `actual` is independently observed by the receiver from execution-time GitHub evidence or its own receive state;
- `exact_match` is `true` iff the typed `actual` value exactly equals the typed `expected` value;
- strings use raw Unicode string equality; no case-folding, trimming, alias substitution or semantic paraphrase is allowed;
- SHA values are lowercase hexadecimal strings of the specified algorithm;
- list equality is exact ordered-list equality unless the field definition explicitly says otherwise; this schema defines no unordered-list exceptions;
- a missing observation is represented by `null` where the type permits it, and its `exact_match` must be `false`;
- a successful rehearsal report must not omit any field in this schema.

## Successful receive constants

Handoff Package 003 supplies all route-specific expected values. A mechanically acceptable receive additionally requires:

```yaml
handoff_receive_status: RECEIVED
identity_verification_status: PASS
substantive_continuation_status: BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE
```

Every `exact_match` field must be `true`; `repository_or_service_writes_during_receive.actual` must be exactly `[]`; and no guidance may be loaded during receive.

## Dynamic execution-time master rule

`execution_time_master` intentionally does not encode a pre-publication expected SHA.

Receiver requirements:

1. read `08822407d/Mnemosyne@master` immediately before load-bearing receive verification and place that SHA in `observed_start_sha`;
2. repeat the `master` read after receive verification and place that SHA in `observed_end_sha`;
3. set `unchanged_during_receive_check: true` only when the two SHAs are identical.

Originating-conversation rehearsal acceptance requires all of:

```text
receiver.observed_start_sha
== receiver.observed_end_sha
== originating conversation's master SHA observed immediately before launching the fresh receiver
== originating conversation's master SHA observed when adjudicating the returned receive report
```

Any inequality is a dynamic-state blocker. Neither Handoff Package 003 nor Rehearsal Contract 002 may replace this rule with a frozen pre-publication master SHA.

## Schema authority boundary

This schema defines route-specific transfer/report mechanics only. It is not an execution source and does not authorize guidance loading, repository writes, G2A, A1, later validation cells, package edits, retries or cleanup.
