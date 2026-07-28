# Exact Prompt and Report Archive

> Byte-preserving non-execution-source archive for `RC-2026Q3-target-memory-governance-and-learning`.

```yaml
archive_format: tar.bz2
archive_bytes: 56573
archive_sha256: f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
tar_bytes: 235520
tar_sha256: b63b62b2a397c31bff6a57aeefec6b0cccdd1a477e93550435bb34b75f2a8168
base64_chars: 75432
base64_sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
part_count: 8
part_order: lexical_part_number
```

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

After extraction, verify every member against `manifest.json`. The originals are evidence artifacts, not execution source. Conversation-local citation tokens in some exported reports remain non-portable; use the maintainer `source-manifest.md` for sampled stable-source mappings and the review record for interpretation limits.
