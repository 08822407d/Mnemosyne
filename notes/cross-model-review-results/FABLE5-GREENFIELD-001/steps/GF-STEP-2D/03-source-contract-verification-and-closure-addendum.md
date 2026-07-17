# FABLE5-GREENFIELD-001 — GF-STEP-2D exact output archive index

This index is not the returned source text. The exact uploaded Markdown file is preserved as a deterministic gzip stream split into two ordered binary parts.

```yaml
uploaded_filename: FABLE5-GREENFIELD-001-STEP2D-source-contract-verification-and-closure-addendum.md
source:
  size_bytes: 68834
  sha256: ebb994bd3d8f4998cbdc7aead17dcc609958a53798f6c8e9d6dd03d8de5893ac
  expected_git_blob_sha_if_stored_uncompressed: 118ceb82f46b2f4299ff8126cbe06fd2e3261480
  encoding: utf-8
  line_endings: lf
  final_lf_present: true
archive:
  format: gzip
  deterministic_mtime: 0
  compression_level: 9
  size_bytes: 22882
  sha256: b5694be22019e7e39facd1d344b4fa9c355002d27b68013ef376f06f22be61cd
ordered_binary_parts:
  - path: 03-source-contract-verification-and-closure-addendum-gzip-part-01.bin
    size_bytes: 11441
    sha256: 6d0528e0bc332894c556c79ccfc4890ff256cc8bbf57718113ffb89175d1bd66
    git_blob_sha: d570fcf3d76a9c3e7f5ae68e2626483858003cde
  - path: 03-source-contract-verification-and-closure-addendum-gzip-part-02.bin
    size_bytes: 11441
    sha256: 7a7d99df34ae97d4897983d839622ff1407fa6b1b85760b0ad55ce23c43b7442
    git_blob_sha: 25c3496f51bff434d47817de6c8ba9285fc6c5f8
reconstruction:
  concatenate_parts_without_delimiter: true
  then_gunzip: true
  expected_reconstructed_size_bytes: 68834
  expected_reconstructed_sha256: ebb994bd3d8f4998cbdc7aead17dcc609958a53798f6c8e9d6dd03d8de5893ac
verification:
  local_round_trip_verified: true
  stored_part_blob_shas_refetched: true
```

Example reconstruction:

```bash
cat 03-source-contract-verification-and-closure-addendum-gzip-part-01.bin \
    03-source-contract-verification-and-closure-addendum-gzip-part-02.bin \
  > FABLE5-GREENFIELD-001-STEP2D-source-contract-verification-and-closure-addendum.md.gz

gzip -dc FABLE5-GREENFIELD-001-STEP2D-source-contract-verification-and-closure-addendum.md.gz \
  > FABLE5-GREENFIELD-001-STEP2D-source-contract-verification-and-closure-addendum.md
```

The archive form changes only repository transport/storage. It does not normalize or alter Fable's returned Markdown bytes.
