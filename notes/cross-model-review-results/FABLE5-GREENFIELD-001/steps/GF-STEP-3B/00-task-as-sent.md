# FABLE5-GREENFIELD-001 — GF-STEP-3B task as sent

The exact task is preserved as three ordered UTF-8/LF text parts. Reconstruct by concatenating them in order without inserting a delimiter.

```yaml
source_filename: FABLE5-GREENFIELD-001-GF-STEP-3B-task.md
size_bytes: 29026
sha256: 3f803aa6cab84056460b7ffd84eb7cc619fcc00d1e400ad9ef58c64332c0b89a
encoding: utf-8
line_endings: lf
final_lf_present: true
ordered_parts:
  - path: 00-task-part-01.txt
    git_blob_sha: f5bc7dc02869676b8565d5e1e15a081ed435a90d
  - path: 00-task-part-02.txt
    git_blob_sha: 416d8d082935d3ecfb2f1d50db6292e397ea832a
  - path: 00-task-part-03.txt
    git_blob_sha: c09167bd9b58cbea7427d42c584066baae367017
concatenation_rule: concatenate_in_list_order_with_no_inserted_delimiter
```

Known task-text defect preserved verbatim: the STEP1E SHA-256 in the task omitted its final hexadecimal `0`. The same task also supplied the correct byte count and canonical Git blob SHA; Fable disclosed and handled the defect rather than silently normalizing the prompt.
