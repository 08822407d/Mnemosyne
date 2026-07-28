# Exact Prompt and Report Archive

> Byte-preserving non-execution-source archive for `RC-2026Q3-target-memory-governance-and-learning`.

```yaml
archive_format: tar.bz2
archive_bytes: 56573
archive_sha256: f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
tar_bytes: 235520
tar_sha256: b63b62b2a397c31bff6a57aeefec6b0cccdd1a477e93550435bb34b75f2a8168
base64_chars_after_removing_CR_LF: 75432
base64_sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
logical_part_count: 8
physical_part_file_count: 18
physical_part_order: lexical_path_order
storage_status: complete_on_this_revision
source_storage_PR: 216
post_merge_repair_task: MNEMOSYNE-166
```

## Post-merge repair note

PR #216 merged a mismatched logical part 5 and only logical parts 1 through 6; logical parts 7 and 8 were absent although the archive manifest declared eight parts. MNEMOSYNE-166 regenerated the deterministic archive from the exact eight local prompt/report inputs and obtained the exact manifest identities above.

The repair:

- replaces logical part 5 with 11 small, individually Git-blob-verified physical segments;
- restores logical parts 7 and 8;
- preserves the eight logical-part boundaries and the exact Base64 byte stream;
- records the physical storage layout in `manifest.json`.

Repair details:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`

## Physical layout

```text
logical parts 1–4: one file each
logical part 5:   part-005-of-008-segment-001-of-010.txt
                  ...
                  part-005-of-008-segment-006-of-010.txt
                  part-005-of-008-segment-007a-of-010.txt
                  part-005-of-008-segment-007b-of-010.txt
                  part-005-of-008-segment-008-of-010.txt
                  part-005-of-008-segment-009-of-010.txt
                  part-005-of-008-segment-010-of-010.txt
logical parts 6–8: one file each
```

The segment names preserve lexical order. CR/LF is transport-only and must be removed before Base64 decoding.

## Reconstruction

From the cycle root:

```bash
cat exact-archive/parts/part-*.txt | tr -d '\n\r' > /tmp/mnemosyne165.b64
printf '%s' "$(cat /tmp/mnemosyne165.b64)" | base64 --decode > /tmp/mnemosyne165.tar.bz2
sha256sum /tmp/mnemosyne165.tar.bz2
bzip2 -dc /tmp/mnemosyne165.tar.bz2 > /tmp/mnemosyne165.tar
sha256sum /tmp/mnemosyne165.tar
tar -tjf /tmp/mnemosyne165.tar.bz2
mkdir -p /tmp/mnemosyne165-extracted
tar -xjf /tmp/mnemosyne165.tar.bz2 -C /tmp/mnemosyne165-extracted
```

Expected archive SHA-256:

```text
f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
```

Expected tar SHA-256 after decompression:

```text
b63b62b2a397c31bff6a57aeefec6b0cccdd1a477e93550435bb34b75f2a8168
```

Expected Base64 identity after removing all CR/LF from the ordered physical files:

```text
characters: 75432
sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
```

Logical-part repair checks:

```text
logical part 5 SHA-256: 6ae53fdae639053fa5893b885da4c76f8cf11e3c66074478fb8ef59043297468
logical part 7 SHA-256: cf9f696f14cd8fea48f19c8a74e5baa55f7f14b80657187ab33c6baf04cda295
logical part 8 SHA-256: b5ec7860ddf620b1d91ec47c5924dad1475713cd7ce27761d9e8027709b30b24
```

After extraction, verify every member against `manifest.json`.

## Evidence and interpretation boundary

The originals are evidence artifacts, not execution source. Conversation-local citation tokens in some exported reports remain non-portable. Use the canonical derived records for interpretation and correction boundaries:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`

No independent cycle-local `source-manifest.md` is claimed by this archive.
