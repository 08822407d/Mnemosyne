# V2-A A1 Package 004 — Independent Archive Reconstruction and Identity Receipt

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-ARCHIVE-RECONSTRUCTION-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
task_id: MNEMOSYNE-233
verification_actor: mechanical_local_reconstruction_under_Pro_maintenance_task
verification_date: 2026-08-18
```

## Input identity

```yaml
source_attachment_scope: exact_file_exposed_to_current_conversation
operator_filename: MNE-DR-005-A1-PACKAGE002-READINESS-REVIEW-complete-response(1).md
bytes: 37074
sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
source_device_identity_verified: unknown
```

## Deterministic reconstruction method

1. read the exact received 37,074-byte Markdown file;
2. gzip with empty filename and `mtime=0`;
3. set the gzip OS byte to `255`;
4. Base64-encode with no wrapping;
5. split Base64 text into `6000 + 6000 + 2000 + 2000 + 1648` characters;
6. append exactly one LF to every part;
7. calculate each part's Git blob SHA;
8. remove exactly one final LF from each part, concatenate, Base64-decode and gzip-decompress;
9. compare the output bytes and SHA-256 with the input.

```yaml
gzip_bytes: 13234
gzip_sha256: e138a3ab4f28f38b5c17935992d3db6c2e0688f5dc5a46ca37bb346b62e7032c
gzip_os_byte: 255
base64_characters_before_part_LFs: 17648
```

## Reconstructed part identities

| Part | Bytes including LF | Git blob SHA | Result |
|---|---:|---|---|
| `archive-part-001.b64` | 6001 | `89d4bbbae13745fd7ebea22fb16cb026b4e834e9` | PASS |
| `archive-part-002.b64` | 6001 | `ccd208ca144c59251533c310fd7bd0a27317721a` | PASS |
| `archive-part-003.b64` | 2001 | `cce7403d68c3ac9337620f2cf1b5a56aefaac968` | PASS |
| `archive-part-004.b64` | 2001 | `4b716ad17d9216bad885d4ec8da0bd2fb972e21e` | PASS |
| `archive-part-005.b64` | 1649 | `77a827e8532e0ffba920e80cda7a71ee1446d591` | PASS |

```yaml
all_part_identities_match_repository_archive_manifest: true
reconstructed_bytes: 37074
reconstructed_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
reconstruction_byte_identical_to_received_file: true
```

## Correct canonical path/blob

```yaml
path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
actual_blob_on_PR_300_merge_tree_and_master: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
incorrect_predecessor_recorded_blob: 7c2af723c395283aca23a5240847e46e6c97e93b
```

The actual manifest's five part identities, gzip identity, byte count and reconstructed source hash agree with this independent calculation.

## Claim limits

This receipt proves deterministic reconstruction of the file exposed to the current conversation and agreement with the five repository part identities. It does not independently prove identity with an unobserved user-device file, report correctness, producer identity or hidden model identity.
