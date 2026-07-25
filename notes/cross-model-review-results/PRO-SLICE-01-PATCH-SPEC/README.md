# PRO-SLICE-01 Patch-Specification Lineage

> Exact non-execution-source preservation of `PRO-SLICE-01-PATCH-SPEC-001` and its bounded v2 revision. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
storage_task: MNEMOSYNE-155
lineage:
  v1: PRO-SLICE-01-PATCH-SPEC-001
  v2: PRO-SLICE-01-PATCH-SPEC-002
repository_baseline: master@1e1334ad4dce36c2c47ffcfef3e90c9fd843815c
v1_disposition: accepted_as_historical_input_superseded_for_implementation_by_v2
v2_disposition: accepted_for_user_patch_scope_and_phase_A_authorization_decision
implementation_authorized: false
execution_source_modified: false
```

## Contents

- `manifest.yaml` — exact identities, structural receipt, and disposition.
- `maintainer-receipt.md` — mechanical and bounded substantive review.
- `archive-parts/PRO-SLICE-01-PATCH-SPEC-v1-v2.tar.bz2.base64.part-0001.txt` through `part-0007.txt` — exact deterministic archive containing the two taskbooks, both complete-response files, and all v1/v2 named artifacts.

## Reconstruction

From this directory:

```bash
cat archive-parts/PRO-SLICE-01-PATCH-SPEC-v1-v2.tar.bz2.base64.part-* \
  | tr -d '\n' \
  | base64 --decode \
  | bzip2 --decompress \
  > PRO-SLICE-01-PATCH-SPEC-v1-v2.tar

sha256sum PRO-SLICE-01-PATCH-SPEC-v1-v2.tar
tar -xf PRO-SLICE-01-PATCH-SPEC-v1-v2.tar
```

Expected identities:

```yaml
tar:
  bytes: 440320
  sha256: e7fa17560ba5b4e5787d41edb0c8d9261d02df5e084a00c5f2bbae6f06498d4d
bzip2_before_Base64:
  bytes: 60046
  sha256: 0189d64d479f17264dda8d502f6068370941c9f741bd2fce71276b6a59fbb381
base64_characters: 80064
ordered_parts: 7
members: 13
```

Verify every extracted member against `manifest.yaml`.

## Lineage interpretation

V1 correctly identified the four authorized hard-contract propagation subjects but required repair before implementation. V2 preserves the same bounded scope and repairs R1–R10, including evidence-bearing safety preflight, one-of storage routes, surface-specific no-write claims, coherent approved-exception semantics, mechanical evidence binding, receiving-operation state, reference-first drift control, Chinese-primary prose, exact literal patch anchors, and two sequential nonparallel implementation phases.

V2 recommends:

```yaml
phase_A_foundation:
  files: 5
  patches: 11
phase_B_propagation:
  files: 4
  patches: 18
stop_gate_between_phases: required
parallel_branches_or_PRs: prohibited
```

This archive does not approve either phase. Phase A requires explicit user patch-scope/write authorization under a fresh task ID. Phase B remains blocked until Phase A is merged and mechanically verifies the stop gate.

## Complete-response file relation

Both v1 and v2 archives include an explicitly named `*-complete-response.md`. The user's experience obtaining these files motivated the MNEMOSYNE-155 amendment to `current/artifact-delivery-and-direct-generation-guard.md`: future taskbooks that require return of the complete reply must request this file in advance, in the same final response, rather than forcing a separate export request.

## Boundary

Nothing in this directory:

- updates the execution source;
- authorizes implementation;
- performs target-project work;
- runs external research;
- rewrites historical records;
- authorizes Phase B before the Phase A stop gate.
