# Owner Decision — F2 V2-A A1 Handoff 003 Schema/Oracle Repair

```yaml
decision_id: MNE-F2-V2A-A1-HANDOFF003-SCHEMA-ORACLE-REPAIR-OWNER-DECISION-001
task_id: MNEMOSYNE-234
date: 2026-08-19
source_master: cc06e929515e6bcae8f4997cc6bb6e165bcdd151
authorized_defect: MNE-F2-V2A-A1-HANDOFF002-RECEIVE-SCHEMA-ORACLE-MISMATCH-001
authorization: route_specific_follow_up_repair
repository: 08822407d/Mnemosyne
A1_execution_authorized: false
validation_repository_write_authorized: false
```

The Owner accepts the prior Pro adjudication that Handoff Package 002's required receive report and Post-Merge Receive-Rehearsal Contract 001's mechanical acceptance oracle are not structurally isomorphic enough for a reliable mechanical acceptance gate.

Authorized scope is limited to:

- recording the protocol defect;
- creating one canonical receive-report schema with exact YAML paths, field types and `expected` / `actual` / `exact_match` comparison structure;
- creating corrected route-specific Handoff Package 003, Startup Prompt 003 and Post-Merge Receive-Rehearsal Contract 002 that all use the same canonical schema;
- preserving candidate/packages 001–004 and handoff/startup/rehearsal predecessors unchanged;
- updating the current F2 route state and MNEMOSYNE-234 task records;
- publishing one Ready PR;
- requiring post-merge exact readback and a completely fresh Pro receive-only rehearsal before route release.

Explicit prohibitions:

- no candidate/package 005;
- no edits to `commands/prepare-mnemosyne-handoff.md`, `commands/receive-mnemosyne-handoff.md` or `current/human-approved-spec.md`;
- no receive rehearsal or receiver guidance load during this repair;
- no A1/G2A authorization or execution;
- no validation branch/ref/PR/repository writes;
- no Meta-Agent or real-target writes;
- no A2–A7, V2-B or V2-C;
- no auto-merge, retry, cleanup or branch deletion.

If the repair cannot be completed solely at the route-specific handoff layer without modifying Package 004 semantics, the task must stop and return to Pro adjudication.
