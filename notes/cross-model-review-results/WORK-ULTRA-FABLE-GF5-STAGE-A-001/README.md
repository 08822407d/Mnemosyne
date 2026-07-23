# WORK-ULTRA-FABLE-GF5-STAGE-A-001

> Exact non-execution-source preservation of the completed Stage A independent architecture assessment. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
task_id: WORK-ULTRA-FABLE-GF5-STAGE-A-001
storage_task: MNEMOSYNE-152
stage: A
status_claim: WORK_ULTRA_GF5_STAGE_A_COMPLETE
maintainer_receipt: RECEIVED_COMPLETE_HIGH_SIGNAL
comparison_firewall: passed
GF_STEP_5_read_or_adjudicated: false
implementation_performed: false
repository_architecture_ref: 898b20e16f9b4694bb45110a0be036761b511740
precondition_PR: 202
precondition_merge_commit: ea40aaefe6a486e710012e10521a73a81890be43
```

## Contents

- `manifest.yaml` — exact identities for eight source artifacts and the archive representation.
- `maintainer-receipt.md` — mechanical receipt and bounded substantive interpretation.
- `storage-anomaly-record.md` — the two recoverable multipart storage-boundary anomalies.
- `archive-parts/WORK-ULTRA-FABLE-GF5-STAGE-A-001.tar.bz2.base64.part-0001.txt` through `part-0015.txt` — deterministic exact archive of:
  1. Stage A task contract;
  2. complete Work response;
  3. N0;
  4. N1;
  5. current assessment;
  6. Greenfield assessment;
  7. Stage A synthesis;
  8. source/exposure ledger.

## Reconstruction

From this directory:

```bash
cat archive-parts/WORK-ULTRA-FABLE-GF5-STAGE-A-001.tar.bz2.base64.part-* \
  | tr -d '\n' \
  | base64 --decode \
  | bzip2 --decompress \
  > WORK-ULTRA-FABLE-GF5-STAGE-A-001.tar

sha256sum WORK-ULTRA-FABLE-GF5-STAGE-A-001.tar
tar -xf WORK-ULTRA-FABLE-GF5-STAGE-A-001.tar
```

Expected archive identities:

```yaml
tar:
  bytes: 358400
  sha256: 6f214d2df97511ff94e719a85f0e992d293c0f34fbc6e3f292cc8cf3e3ffb630
bzip2_before_Base64:
  bytes: 64386
  sha256: 9231cc8b3f5a42205cf84d7089e6633f9f1781f49ddc94950f6e9d1684732f71
base64_characters: 85848
ordered_parts: 15
```

Verify each reconstructed member against `manifest.yaml`.

## Important identity relation

The complete Work response and `stage-a-synthesis.md` are byte-for-byte identical:

```yaml
same_bytes: true
sha256: 2f0b6f471117da64e592bac7abd2530ad7c7309afd31d5a078641a04db99a0fc
git_blob_sha_if_single_file: 1d79d754685eaff56e04eadda17376596860b4af
```

Both filenames remain in the archive because they have different provenance roles.

## Authority boundary

These artifacts are advisory review evidence. They do not:

- adopt the current or Greenfield architecture;
- update the execution source;
- reveal or adjudicate GF-STEP-5;
- answer open user parameters;
- authorize Stage B execution;
- authorize research refresh, repair, target-project work, repository writes, merges, or auto-merge.
