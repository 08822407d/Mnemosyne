# FABLE5-GREENFIELD-001 GF-STEP-5 Exact Task Index

The exact source bytes are preserved as deterministic gzip (`mtime=0`, compression level 9), Base64-encoded, and split into the ordered text parts below.

```yaml
source_filename: FABLE5-GREENFIELD-001-GF-STEP-5-task.md
size_bytes: 24403
sha256: 96349148e8b4b6b1292b521fef08c037debb7d03f3d6565e6b0e1eac6c497845
canonical_git_blob_sha_if_single_file: b6f723c842ea797b79700a349c9b20f39fee8f85
encoding: utf-8
line_endings: lf
final_lf_present: true
source_lines: 634
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 9193
archive_gzip_sha256: 1652dddcf4fdd88b8f69825b1dec32ddce0e9ac19ac107bcb57d2963e0cc4bc1
ordered_parts: 2
parts:
  - path: 00-task-as-sent-gzip-base64-part-01.txt
    base64_characters: 8500
    sha256: 06eba911f2c6e39b12da7e597ba72bdd7830e6747226dc80986a251676644f1c
  - path: 00-task-as-sent-gzip-base64-part-02.txt
    base64_characters: 3760
    sha256: fce5aaa5892e5652ec87a65ebcafdb285b91147945af63d1b8b2ff2d9ef919c0
reconstruction:
  - concatenate parts in listed order without inserting delimiters
  - Base64-decode the concatenated text
  - gunzip the decoded bytes
  - verify source size, SHA-256, Git blob SHA, LF endings and final LF
authority_level: non_execution_source_advisory_evidence
```

This index is not the source file itself and is not an execution source.
