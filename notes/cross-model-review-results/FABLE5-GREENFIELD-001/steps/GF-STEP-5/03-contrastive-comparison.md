# FABLE5-GREENFIELD-001 GF-STEP-5 Exact Comparison Report Index

The exact source bytes are preserved as deterministic gzip (`mtime=0`, compression level 9), Base64-encoded, and split into the ordered text parts below.

```yaml
source_filename: FABLE5-GREENFIELD-001-STEP5-contrastive-comparison.md
size_bytes: 76917
sha256: 82a5c8ee79a51f7bcfe0f5688e8bde71235cb6438cd87060c92035e009f48bfe
canonical_git_blob_sha_if_single_file: e6a429bb9a1a1a38e50b59e86abaed6a81b316e1
encoding: utf-8
line_endings: lf
final_lf_present: true
source_lines: 316
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 26941
archive_gzip_sha256: a81ffebb9f22ac60622cbc826fc7617e967bdf0096b1ab7cb6fe9b16b5807d3a
ordered_parts: 5
parts:
  - path: 03-contrastive-comparison-gzip-base64-part-01.txt
    base64_characters: 8500
    sha256: 957120e6cba35516fd705b951678d0b768b1a0fc9ca4205fe2101a77083a9d8a
  - path: 03-contrastive-comparison-gzip-base64-part-02.txt
    base64_characters: 8500
    sha256: a0e216b8b86a08f63d29c88d6ffa612ffe4d290298f6fc30f3c55505475f866c
  - path: 03-contrastive-comparison-gzip-base64-part-03.txt
    base64_characters: 8500
    sha256: e4ad7c0fcd209967d4a5457b7d30a0523af07c3f84ebd76704bbdebe26db89e5
  - path: 03-contrastive-comparison-gzip-base64-part-04.txt
    base64_characters: 8500
    sha256: 0e17d9fef7ff317e3e36f2c0c3da23eecd6e04e8e3fe2187048dedd58fd3baf7
  - path: 03-contrastive-comparison-gzip-base64-part-05.txt
    base64_characters: 1924
    sha256: 4a909d6a3c36bbcb708b322216c12bc436ab268d0c989756d8e01673e3216d30
reconstruction:
  - concatenate parts in listed order without inserting delimiters
  - Base64-decode the concatenated text
  - gunzip the decoded bytes
  - verify source size, SHA-256, Git blob SHA, LF endings and final LF
authority_level: non_execution_source_advisory_evidence
```

This index is not the source file itself and is not an execution source.
