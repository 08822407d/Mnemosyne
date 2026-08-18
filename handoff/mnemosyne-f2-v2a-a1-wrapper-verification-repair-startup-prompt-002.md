# Startup Prompt 002 — Receive F2 / V2-A A1 Package 004 Handoff

```text
@GitHub

Receive Mnemosyne handoff.

Use this authorized handoff package:

handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-002.md

Package ID:

MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-002

Expected package blob on execution-time latest 08822407d/Mnemosyne@master:

30699edcf16228f931f89e9162b2f9bc08d4c4c7

This is a mandatory post-merge receive rehearsal. It is receive-only.

Required operation:

1. Read commands/receive-mnemosyne-handoff.md from execution-time latest 08822407d/Mnemosyne@master.
2. Fetch the exact authorized package path and verify its package ID and blob.
3. Read only the package's minimum receive evidence.
4. Verify every package-declared load-bearing path/blob, Package 004 file count, canonical archive-manifest identity, independent reconstruction receipt and A1 unauthorized state.
5. Output one mnemosyne_handoff_receive YAML object using the package's separate handoff_receive_status, identity_verification_status and substantive_continuation_status fields.
6. Stop and wait. Do not load guidance in this operation.

The complete receive report will be returned to the originating conversation for rehearsal adjudication.

Do not execute A1, issue G2A, create or move validation branches, modify packages or expected values, write any repository, import unrelated routes, read cold originals without a mismatch trigger, retry a blocked receive, or use Web, Deep Research, Fable, other Apps, private material or external quota.
```
