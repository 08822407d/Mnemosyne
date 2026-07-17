# FABLE5-GREENFIELD-001 — GF-STEP-3A exact task archive index

This index is not the task source text. The exact Markdown task is preserved as one deterministic gzip binary blob.

```yaml
source_filename: FABLE5-GREENFIELD-001-GF-STEP-3A-task.md
source:
  size_bytes: 23937
  sha256: 991bbf83234822e478cc003ceaec225844564b2094ade2df79352df039a4472a
  expected_git_blob_sha_if_uncompressed: 37c6e3fd0684118b38f9fab46e8d0e8b1b7e1c17
  encoding: utf-8
  line_endings: lf
  final_lf_present: true
archive:
  path: 00-task-as-sent-gzip.bin
  format: gzip
  deterministic_mtime: 0
  compression_level: 9
  size_bytes: 7492
  sha256: ea266b71f72a00d3ddcb61fbc92498bd60fd3441cfd58c91c0cf18697cf3f04d
  git_blob_sha: c7dd0cee22a287baf9312af545ced3705013a12a
reconstruction:
  gunzip: true
  expected_reconstructed_size_bytes: 23937
  expected_reconstructed_sha256: 991bbf83234822e478cc003ceaec225844564b2094ade2df79352df039a4472a
verification:
  local_round_trip_verified: true
  stored_blob_sha_matches_expected: true
```

Example reconstruction:

```bash
gzip -dc 00-task-as-sent-gzip.bin > FABLE5-GREENFIELD-001-GF-STEP-3A-task.md
```

The archive form changes only repository transport/storage and does not normalize the task text.
