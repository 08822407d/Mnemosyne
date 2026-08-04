---
artifact_role: exact_research_report_navigation
status: seven_reports_recorded_and_remote_blob_verified
 target_project_id: meta-agent
target_truth_source: false
task_id: META-AGENT-INDEPENDENT-WAVE-REPORT-RECORDING-001
---

# Independent Research Wave Reports

This directory preserves the exact operator-exported UTF-8 bytes for:

- `MA-DR-08`;
- `MA-DR-10`;
- `MA-DR-11`;
- `MA-DR-12`;
- `MA-DR-13`;
- `MA-DR-14`;
- `MA-DR-15`.

## Reconstruction

For `MA-DR-08`, `10`, `11`, `12`, `13` and `15`, concatenate the numbered
Markdown parts in lexical/numeric order without inserting, deleting or
normalizing bytes.

`MA-DR-14` uses a mixed exact transport because one source section contains
product-native private-use citation characters that were unsafe to reproduce
through a single large text write:

```text
part-001.md ... part-005.md
+ Base64-decode(concatenate part-006-base64/segment-001.txt ... segment-010.txt)
+ part-007.md
```

Do not insert separators between pieces. The Base64 segments are ASCII and
contain no trailing newline.

The original byte counts and SHA-256 values, each transport component's expected
Git blob SHA-1, and the completed remote verification snapshot are recorded in
`report-parts-manifest.yaml`.

```yaml
remote_blob_identity_verification: PASS_56_OF_56
remote_report_reconstruction_identity: PASS_7_OF_7
```

The reports remain external research evidence. They are not Meta-Agent target
truth, accepted methodology, runtime configuration, pilot authorization,
private-material authorization or operational activation.
