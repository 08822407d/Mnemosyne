# FABLE5-GREENFIELD-001 — GF-STEP-3RV exact task archive index

The exact source Markdown is preserved through a deterministic gzip/Base64 multipart archive.

Reconstruction:

1. concatenate the Base64 part files in list order with no inserted delimiter;
2. Base64-decode the concatenated ASCII text;
3. gzip-decompress the decoded bytes;
4. verify the reconstructed source identity below.

```yaml
source_filename: FABLE5-GREENFIELD-001-GF-STEP-3RV-task.md
source_size_bytes: 22375
source_sha256: 9209de4e35dbda892ac57bf1a43a0c04513775763fc0f9a562c98c9f83fc826a
source_git_blob_sha: 664e7e32679c9aac01ec1f6fe15a0ad2bdf3651a
source_encoding: utf-8
source_line_endings: lf
source_final_lf_present: true
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 8513
archive_gzip_sha256: 96a68ce583f8cc55630a9108314452d398b77e5b24133ba8c09b5c02da2de214
archive_base64_length: 11352
ordered_parts:
  - path: 00-task-as-sent-gzip-base64-part-01.txt
    base64_characters: 5676
    base64_text_sha256: a3f98a68487c6e8e3210730eac73761c5d567153a182b7c5f7cc6ea2972c8384
    git_blob_sha: cdde9189f034f2f91199257989f956b7290ae2ee
  - path: 00-task-as-sent-gzip-base64-part-02.txt
    base64_characters: 5676
    base64_text_sha256: 4eaecfbff4ee9e37f570d832f7e90d4c0dd5b2ea20a886fb295a68e91d2fc30e
    git_blob_sha: 3be43fc7083d87aff992e626aca611664043ec1c
concatenation_rule: concatenate_in_list_order_with_no_inserted_delimiter
exact_local_reconstruction_verified: true
```

This index records storage integrity only. It does not make the task or report an execution source and does not substantively accept any Fable claim.
