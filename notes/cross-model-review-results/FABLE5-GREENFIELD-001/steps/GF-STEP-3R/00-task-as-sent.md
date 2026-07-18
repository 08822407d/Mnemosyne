# FABLE5-GREENFIELD-001 — GF-STEP-3R task as sent

The exact task is preserved as a deterministic gzip archive encoded as three ordered Base64 text parts. Reconstruct by concatenating the Base64 parts without a delimiter, decoding Base64, and gunzipping.

```yaml
source_filename: FABLE5-GREENFIELD-001-GF-STEP-3R-task.md
source_size_bytes: 19101
source_sha256: 4a786d24d2004f92eb25cc8c6361eb62333d3c3f8ebbffc60950d3f6fed60d2d
source_git_blob_sha: e117dc0d1b5afd76c070907be15c68b50e975430
source_encoding: utf-8
source_line_endings: lf
source_final_lf_present: true
source_lines: 561
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 7199
archive_gzip_sha256: 6a32023b1fd0798a93e3f0f8e3feefaa26b3d9f4a7f6a7370cc01a742bcff1fe
archive_base64_characters: 9600
ordered_parts:
  - path: 00-task-as-sent-gzip-base64-part-01.txt
    base64_characters: 3500
    content_sha256: 8c031774e0b0cc86e9be700009a0224efdbc23d7dbf5140db329db000331cc68
    git_blob_sha: bb096cf7997a4b75fb6ae9176309fc42bcc1f623
  - path: 00-task-as-sent-gzip-base64-part-02.txt
    base64_characters: 3500
    content_sha256: 4f25a2ff9168af10b0b166d6477048ddcf76578bba7571a9ab6dd68c9da7463e
    git_blob_sha: d1df4c9ff34bc22f2d94506bc73c48f173a37604
  - path: 00-task-as-sent-gzip-base64-part-03.txt
    base64_characters: 2600
    content_sha256: 0dba6caa5c0c3e87d3ab23e9eeaf335c693bca183c76576b217aad568f4b0a3c
    git_blob_sha: 0c0eb964a4728924c222eb8fcf14156ef61eef8c
concatenation_rule: concatenate_base64_parts_in_order_with_no_inserted_delimiter
reconstruction_rule: base64_decode_then_gunzip
exact_local_reconstruction_verified: true
```

This is the GF-STEP-3R governing task used for the failed attempt. It is not design evidence or an execution source.
