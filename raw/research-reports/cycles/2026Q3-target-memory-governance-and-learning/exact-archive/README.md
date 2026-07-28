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
part_count: 8
part_order: lexical_part_number
storage_status: complete_on_this_revision
source_storage_PR: 216
post_merge_repair_task: MNEMOSYNE-166
```

## Post-merge repair note

PR #216 merged only parts 1 through 6 although the archive manifest declared eight parts. MNEMOSYNE-166 regenerated the deterministic archive from the exact eight local prompt/report inputs and obtained the exact manifest identities above. Parts 7 and 8 were then restored without changing `manifest.json` or any accepted report byte.

Repair details:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`

## Reconstruction

From the cycle root:

```bash
cat exact-archive/parts/part-*.txt | tr -d '\n\r' > /tmp/mnemosyne165.b64
printf '%s' "$(cat /tmp/mnemosyne165.b64)" | base64 --decode > /tmp/mnemosyne165.tar.bz2
sha256sum /tmp/mnemosyne165.tar.bz2
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

Expected Base64 identity after removing all CR/LF from the ordered parts:

```text
characters: 75432
sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
```

After extraction, verify every member against `manifest.json`.

## Evidence and interpretation boundary

The originals are evidence artifacts, not execution source. Conversation-local citation tokens in some exported reports remain non-portable. Use the canonical derived records for interpretation and correction boundaries:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`

No independent cycle-local `source-manifest.md` is claimed by this archive.
