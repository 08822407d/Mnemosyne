
@GitHub

Receive the Mnemosyne post-PR303 AI-onboarding handoff.

Use:

handoff/mnemosyne-post-pr303-ai-onboarding-handoff-package-001.md

Expected package blob on execution-time latest 08822407d/Mnemosyne@master:

<PACKAGE_BLOB_FROM_MERGED_MNEMOSYNE_242>

Read `commands/receive-mnemosyne-handoff.md`, then the exact handoff package and only its minimum receive evidence.

As the receive report, output exactly one top-level `mnemosyne_handoff_receive:` YAML
object and no other top-level object. It must preserve every field required by the
"Required first response after receiving" section of
`commands/receive-mnemosyne-handoff.md`.

Inside that object, add one nested `receive_evidence` block:

```yaml
receive_evidence:
  package_path:
  package_id:
  observed_package_blob:
  execution_time_master_start:
  execution_time_master_end:
  branch_retention_obligations:
```

Then stop.

Do not load Mnemosyne guidance in this receive operation. Do not continue MNEMOSYNE-243, modify repositories, issue G2A, execute A1/HVAL, delete branches, import another route, or infer a task from `handoff/handoff-current.md`.

Stop after the receive report.
