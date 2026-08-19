# F2 / V2-A A1 Handoff 003 — Post-Merge Receive-Rehearsal Contract 002

```yaml
rehearsal_contract_id: MNE-F2-V2A-A1-HANDOFF-003-POST-MERGE-RECEIVE-REHEARSAL-002
prepared_by_task: MNEMOSYNE-234
status: required_before_originating_conversation_release
execution_source: false
repository_write_authorized: false
A1_execution_authorized: false
```

## Canonical artifacts

```yaml
receive_report_schema:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-receive-report-schema-001.md
  blob: 52e2ce60f471be492175f8725a0ed39ddf3daad1
  id: MNE-F2-V2A-A1-HANDOFF-RECEIVE-REPORT-SCHEMA-001
handoff_package_003:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package-003.md
  blob: bb60b9c18acb9035491eeb3af5e521fe14714ddb
  id: MNE-F2-V2A-A1-WRAPPER-REPAIR-HANDOFF-003
startup_prompt_003:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt-003.md
  blob: 76db593d8c3a62a7ff8e90a32f418d8ad3bfe0ad
receive_report_key: mnemosyne_handoff_receive
```

This contract does not define a second receive-report field list. The canonical schema above is the sole source for field paths, types and `expected` / `actual` / `exact_match` semantics. Handoff Package 003 supplies all static expected values except its own self-blob; exact merged Startup Prompt 003 supplies only `mnemosyne_handoff_receive.package.blob.expected`.

## Required timing

1. merge the Handoff 003 repair Ready PR;
2. read back schema, handoff, startup, this rehearsal contract and all route load-bearing identities from the merge commit/current master;
3. originating conversation records `08822407d/Mnemosyne@master` immediately before launch;
4. open a completely fresh ChatGPT Pro conversation with GitHub read access;
5. copy and send the exact merged Startup Prompt 003 once; do not manually rewrite it;
6. receiver emits exactly one canonical-schema `mnemosyne_handoff_receive` object and stops;
7. return that complete report verbatim to the originating conversation;
8. originating conversation re-reads current master and applies the mechanical acceptance procedure below;
9. only after explicit `REHEARSAL_ACCEPTED_RECEIVER_MAY_LOAD_GUIDANCE` may the same receiver separately execute `加载 Mnemosyne 指导约束`;
10. receiver must emit `mnemosyne_guidance_refresh`, preserve the transferred Package 004 readiness-review task and keep A1 unauthorized;
11. only then may the originating conversation retire.

Do not reuse either failed pre-repair receiver conversation.

## Mechanical acceptance procedure

Acceptance is schema-driven, not alias-driven.

All must hold:

1. the report has exactly one top-level key `mnemosyne_handoff_receive`;
2. every field required by canonical schema blob `52e2ce60f471be492175f8725a0ed39ddf3daad1` is present with the required type;
3. no synonymous replacement path is accepted for a missing canonical path;
4. `handoff_receive_status` is exactly `RECEIVED`;
5. `identity_verification_status` is exactly `PASS`;
6. `substantive_continuation_status` is exactly `BLOCKED_PENDING_REHEARSAL_ACCEPTANCE_AND_GUIDANCE`;
7. every `{expected, actual, exact_match}` mapping in the canonical schema has `exact_match: true`;
8. every static `expected` value other than `package.blob.expected` exactly equals the corresponding expected-value source in merged Handoff Package 003;
9. `package.blob.expected` exactly equals `bb60b9c18acb9035491eeb3af5e521fe14714ddb`, the value supplied by exact merged Startup Prompt 003;
10. `repository_or_service_writes_during_receive.actual` is exactly `[]`;
11. `execution_time_master.unchanged_during_receive_check` is `true`;
12. dynamic master equality from the canonical schema holds:

```text
receiver.execution_time_master.observed_start_sha
== receiver.execution_time_master.observed_end_sha
== originating master SHA recorded immediately before launch
== originating master SHA re-read when adjudicating the returned report
```

13. no extra route, silent expected-value refresh, artifact substitution, package repair, guidance load, G2A, A1 execution, validation branch creation, repository/service write or retry appears in the receive report or observed execution state.

If any required field is missing, mistyped, unknown, aliased, contradictory or dynamically stale, return:

```yaml
rehearsal_disposition: BLOCKED_REQUIRES_PRO
```

A next-tier originating conversation may apply this mechanical procedure. The procedure must not invent a semantic mapping for non-canonical receiver fields.

If all checks pass, return exactly:

```yaml
rehearsal_disposition: REHEARSAL_ACCEPTED_RECEIVER_MAY_LOAD_GUIDANCE
```

## Guidance completion check

After accepted rehearsal, the separate guidance-load response must confirm at least:

```yaml
mnemosyne_guidance_refresh:
  operation: behavior_constraint_refresh
  current_conversation_task_preserved: true
  handoff_started: false
  maintenance_live_route_imported: false
  execution_source: current/human-approved-spec.md
```

It must also state that the local task remains the fresh Pro execution-time readiness review of Package 004 and inherited Packages 003/002/001, and that A1 remains unauthorized.

The broader design request for startup-time self-loading of exactly selected project/Agent guidance remains in `MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001`; this route-specific repair does not implement that global change.

## Boundaries

This rehearsal contract does not authorize repository writes, guidance load before rehearsal acceptance, Package 004 modification, candidate/package 005, substantive readiness review during receive, G2A, A1, later validation cells, cleanup or route import.
