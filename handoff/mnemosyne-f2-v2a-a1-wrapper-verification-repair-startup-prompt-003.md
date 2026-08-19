# Startup Prompt 003 — Receive F2 / V2-A A1 Handoff 003

```text
@GitHub

Receive Mnemosyne handoff.

Use this authorized handoff package:

handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-003.md

Package ID:

MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-003

Expected package blob on execution-time latest 08822407d/Mnemosyne@master:

bb60b9c18acb9035491eeb3af5e521fe14714ddb

Use this exact canonical receive-report schema:

handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-receive-report-schema-001.md

Schema ID:

MNE-F2-V2A-A1-HANDOFF-RECEIVE-REPORT-SCHEMA-001

Expected schema blob:

52e2ce60f471be492175f8725a0ed39ddf3daad1

This is a mandatory post-merge receive-only rehearsal.

Required operation:

1. Read commands/receive-mnemosyne-handoff.md from execution-time latest 08822407d/Mnemosyne@master.
2. Read the exact authorized Handoff Package 003 and canonical schema above.
3. Set mnemosyne_handoff_receive.package.blob.expected to the exact package blob stated in this Startup Prompt 003. All other static expected values come only from Handoff Package 003.
4. Read only the handoff package's minimum receive evidence.
5. Populate every field required by the canonical schema. Do not rename, flatten, alias or omit fields. Do not add an alternate report schema.
6. Apply the schema's dynamic execution-time-master rule, including start/end master observations.
7. Output exactly one top-level mnemosyne_handoff_receive YAML object and stop.
8. Do not load Mnemosyne guidance in this operation.

Return the complete receive report to the originating conversation for rehearsal adjudication.

Do not execute the Package 004 substantive readiness review, issue G2A, execute A1, create or move validation branches, modify packages or expected values, write any repository or connected service, import unrelated routes, read cold originals without a mismatch trigger, retry a blocked receive, or use Web, Deep Research, Fable, other Apps, private material or external quota.
```
