# FABLE5-GOV-001 Exact Archive Reconstruction Index

> Non-execution-source storage record. The task and report are preserved as deterministic gzip (`mtime=0`, level 9) encoded as Base64 and split into ordered text parts.

## Task artifact

```yaml
filename: FABLE5-GOV-001-independent-evidence-governance-research-task-v2.md
size_bytes: 18554
sha256: 81368ae96a2e716268583a0f4a36d69c476fed7e50add3b25963f68c8c096e96
git_blob_sha_if_single_file: 0b9e1b63bea06f00a75e0f209fc08f65d7d0f207
encoding: utf-8
newline_characters: 506
final_lf_present: true
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 7104
archive_gzip_sha256: 122f4d6ba7d81aa6e5dd6d0747e5851a29421f93b0da1f04af1c531c201b7677
archive_base64_chars: 9472
ordered_parts: 2
```

| Ordered part | Base64 chars | SHA-256 | Git blob SHA |
|---|---:|---|---|
| `fable5-gov-001-task.tarless.gz.base64.part-0001` | 8192 | `f690e352dfbcf950e38cebe4c2dfbe4c376a616ec7432f8cd10a7d33b0c32800` | `f3d155bd47185c4be36309384ab6a08b46ba88aa` |
| `fable5-gov-001-task.tarless.gz.base64.part-0002` | 1280 | `1a34afc0b71df4c96062c4c58c701ad82943a1a7e877595bd2de2ec730adc712` | `c2aa325ffce2f5c9a340bd18159d6f0ffadeb8ee` |

## Report artifact

```yaml
filename: FABLE5-GOV-001-independent-governance-research-report.md
size_bytes: 59630
sha256: 6a815c6d3c506d630b226fe53e1141057c9d9c1b69bab62b9586e22e67798ffe
git_blob_sha_if_single_file: e8910988127a7b8383a1cb3e54bb2600ee02ea97
encoding: utf-8
newline_characters: 487
final_lf_present: true
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 22592
archive_gzip_sha256: 4cc96bacfb5d05fb3f299d3279ca2bd3f6f574dab7695979665c4f0812305d15
archive_base64_chars: 30124
ordered_parts: 4
```

| Ordered part | Base64 chars | SHA-256 | Git blob SHA |
|---|---:|---|---|
| `fable5-gov-001-report.tarless.gz.base64.part-0001` | 8192 | `847a251d40cb0e4ea17b6116948a2075d690b180e855d2515da4a9fa4639c1ae` | `9175684100db2c4909f3cfbb349fc8babca28b31` |
| `fable5-gov-001-report.tarless.gz.base64.part-0002` | 8192 | `65d15f41054811e1f00966e856b30befd498783c64e468da56ca2fe76f71f130` | `f60a5e68f4e00013f709eadc1e90e9ef29563284` |
| `fable5-gov-001-report.tarless.gz.base64.part-0003` | 8192 | `7c67fcf1197d579eb57b22ffd35780814e99c6f4b06f2b7b5d97509ac59e206e` | `1fd5937d08f9f808f9fb377f2fd1f531771789e6` |
| `fable5-gov-001-report.tarless.gz.base64.part-0004` | 5548 | `9cdc4556a8db5fb78f26f8345fa77357c562d0ee5e220973f0e13fa00f0d1b3f` | `cea475558eb5d5384bc88b9ba27c80a07eb1dd15` |

## Reconstruction

From this directory:

```bash
cat archive-parts/fable5-gov-001-task.tarless.gz.base64.part-* \
  | base64 --decode \
  | gzip --decompress \
  > FABLE5-GOV-001-independent-evidence-governance-research-task-v2.md

cat archive-parts/fable5-gov-001-report.tarless.gz.base64.part-* \
  | base64 --decode \
  | gzip --decompress \
  > FABLE5-GOV-001-independent-governance-research-report.md

sha256sum FABLE5-GOV-001-independent-evidence-governance-research-task-v2.md FABLE5-GOV-001-independent-governance-research-report.md
```

Expected SHA-256 values:

```text
81368ae96a2e716268583a0f4a36d69c476fed7e50add3b25963f68c8c096e96  FABLE5-GOV-001-independent-evidence-governance-research-task-v2.md
6a815c6d3c506d630b226fe53e1141057c9d9c1b69bab62b9586e22e67798ffe  FABLE5-GOV-001-independent-governance-research-report.md
```

## Verification status

All six remote archive-part Git blob SHAs were re-read after upload and matched the local precomputed values. The deterministic archives were reconstructed locally before upload and matched the original bytes exactly.
