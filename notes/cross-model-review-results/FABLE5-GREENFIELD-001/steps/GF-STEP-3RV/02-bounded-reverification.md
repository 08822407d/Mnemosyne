# FABLE5-GREENFIELD-001 — GF-STEP-3RV exact output archive index

The exact source Markdown is preserved through a deterministic gzip/Base64 multipart archive.

Reconstruction:

1. concatenate the Base64 part files in list order with no inserted delimiter;
2. Base64-decode the concatenated ASCII text;
3. gzip-decompress the decoded bytes;
4. verify the reconstructed source identity below.

```yaml
source_filename: FABLE5-GREENFIELD-001-STEP3RV-bounded-reverification.md
source_size_bytes: 46623
source_sha256: e2bcf75d33da2c27639b45284e7e131105409225d8ca7d6577dcde875c7573ca
source_git_blob_sha: 1337f4cc18163fbd67db1559c10a5de0a5e84c96
source_encoding: utf-8
source_line_endings: lf
source_final_lf_present: true
archive_format: deterministic_gzip_mtime_0_level_9_then_base64
archive_gzip_size_bytes: 17297
archive_gzip_sha256: 7fcff8618cefc8b51b9634e338034d6c92e9ad179497be80a5c95b3b1e7df7fd
archive_base64_length: 23064
ordered_parts:
  - path: 02-bounded-reverification-gzip-base64-part-01.txt
    base64_characters: 7688
    base64_text_sha256: a3e018c68f7d23d420225bd0c655848804a9efaf8087bb805a9e3e5b168c16d7
    git_blob_sha: 99d600d9d85620aedd2b43a1870e72abdafd729c
  - path: 02-bounded-reverification-gzip-base64-part-02.txt
    base64_characters: 7688
    base64_text_sha256: 003a1dbf89ed1b8b60f570b1ed30a596afc46844405df23ba73805ac51813f0d
    git_blob_sha: 05f5b99556b9f23deff3b960732943ccc43079b3
  - path: 02-bounded-reverification-gzip-base64-part-03.txt
    base64_characters: 7688
    base64_text_sha256: c8efc47ac69abb32e7a8167a5382c175dc81bddf49bf9ee99eae0dc5763fba4d
    git_blob_sha: 0a5da6a5e69940ca8fb0916ddd6936f8be860d34
concatenation_rule: concatenate_in_list_order_with_no_inserted_delimiter
exact_local_reconstruction_verified: true
```

This index records storage integrity only. It does not make the task or report an execution source and does not substantively accept any Fable claim.
