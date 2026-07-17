# FABLE5-GREENFIELD-001 — GF-STEP-3A exact output archive index

This index is not the returned source text. The exact uploaded Markdown file is preserved as a deterministic gzip stream split into two ordered binary parts.

```yaml
uploaded_filename: FABLE5-GREENFIELD-001-STEP3A-information-authority-architecture.md
source:
  size_bytes: 47324
  sha256: 3d82a3728ee7ff628be8495469e3e7039a273e28ad9262af4dea88351d8896b1
  expected_git_blob_sha_if_stored_uncompressed: 840f1f79e84c5c704a8372d8b720595044289682
  encoding: utf-8
  line_endings: lf
  final_lf_present: true
archive:
  format: gzip
  deterministic_mtime: 0
  compression_level: 9
  size_bytes: 17301
  sha256: 80c384a3b782e8733766be8c877129acc019716ee8e3b4a136a6c77a7ef613a6
ordered_binary_parts:
  - path: 02-information-authority-architecture-gzip-part-01.bin
    size_bytes: 8651
    sha256: 076541b5e3e1a06c8456e8cb7e05eaa8503e7b285da81222869bbaa5348a3b17
    git_blob_sha: 7f3e28b6678bbf7b40baf61ebc9335d179ef0b31
  - path: 02-information-authority-architecture-gzip-part-02.bin
    size_bytes: 8650
    sha256: 1d65a149e5420e0b01d00083a5db7b7c1452cc5bc24de0c3bcedde80b0d94fa3
    git_blob_sha: 38bea6928f1556a1b78a7243f4ff0f3642dd7b7f
reconstruction:
  concatenate_parts_without_delimiter: true
  then_gunzip: true
  expected_reconstructed_size_bytes: 47324
  expected_reconstructed_sha256: 3d82a3728ee7ff628be8495469e3e7039a273e28ad9262af4dea88351d8896b1
verification:
  local_round_trip_verified: true
  stored_part_blob_shas_match_expected: true
```

Example reconstruction:

```bash
cat 02-information-authority-architecture-gzip-part-01.bin \
    02-information-authority-architecture-gzip-part-02.bin \
  > FABLE5-GREENFIELD-001-STEP3A-information-authority-architecture.md.gz

gzip -dc FABLE5-GREENFIELD-001-STEP3A-information-authority-architecture.md.gz \
  > FABLE5-GREENFIELD-001-STEP3A-information-authority-architecture.md
```

The archive form changes only repository transport/storage. It does not normalize or alter Fable's returned Markdown bytes.
