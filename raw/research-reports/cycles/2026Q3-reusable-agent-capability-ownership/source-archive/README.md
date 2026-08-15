# FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001 Exact Source Archive

```yaml
archive_role: exact_reconstructable_source_archive
preservation_level: EXACT_RECONSTRUCTABLE_ARCHIVE
created_by_task: MNEMOSYNE-213
archive_bytes: 23782
archive_sha256: 29bee30189073df82b43741954aea3913ff34240c3e2f277d8c2540545adcb8d
base64_part_count: 7
provider_internal_representation_identity: unknown_or_not_attestable
```

## Reconstruction

Concatenate the ordered part files, remove line breaks, Base64-decode, and verify the ZIP SHA-256 before opening it.

```bash
cat FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-*.txt | tr -d '\n' | base64 -d > FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip
sha256sum FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip
# expected: 29bee30189073df82b43741954aea3913ff34240c3e2f277d8c2540545adcb8d
```

## Ordered parts

- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-001.txt`
- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-002.txt`
- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-003.txt`
- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-004.txt`
- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-005.txt`
- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-006.txt`
- `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-source-archive.zip.b64.part-007.txt`

## ZIP members

| Member | Bytes | SHA-256 |
|---|---:|---|
| `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-report.md` | 38468 | `80da22b0d4b35ecf1525b1e9a12a7357c8d32557af92cc7730e93fa780b6ae59` |
| `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-task.md` | 11314 | `9fed83fc00aeecd528709409cd2bb0718e325371938a257bc294b27d3fba9fda` |
| `FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-input-manifest.yaml` | 3138 | `ab6d1c06c36480cb2d653b21bc94f17f1b710725bce232e2d2465b91e5e5c1a5` |

## Claim limits

- The ordered Base64 parts reconstruct the exact ZIP bytes created and verified by MNEMOSYNE-213.
- The ZIP members reproduce the exact report, task and input-manifest bytes received by the current Pro intake task.
- This does not prove byte identity with an unobserved Claude internal representation or provider storage.
- The separate visible-process record is normalized user-pasted text and is not an exact provider log.
