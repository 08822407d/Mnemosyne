# Current Pro recovery-attempt object-side-effect receipt

```yaml
receipt_id: MNE-235-236-PRO-RECOVERY-OBJECT-SIDE-EFFECT-RECEIPT-001
repository: 08822407d/Mnemosyne
reachable_commit_created: false
branch_ref_moved: false
pull_request_created: false
cleanup_performed: false
G2A_issued: false
A1_executed: false
```

This receipt records a bounded current-conversation investigation performed after the two blocked external runs. It is evidence for forensic analysis, not a successful recovery result.

## Confirmed repository state before the object calls

- `master` was `e726dea818dca9418181775d0e7dcd62eb6c464a`.
- `mnemosyne-235-f2-g2a-and-handoff-audit-closeout` pointed to the same commit.
- compare status was identical, with zero commits.
- no open PR existed from the branch.

## Unreferenced tree objects returned by successful create_tree calls

```text
b247dc48a00bbe0baa98864050cd2b05f6e18491
ae807302bfc23c6ef3acc199ed8cfdffcec85889
4b3cfe96c225d7fb58d6401125af761d951ba804
2b40b48a8723e5aea87743beb2982062a0818fae
5c4053c18548bb386aa0b0ef3377416a683ff9b1
02032b15ecfc2a312f4f9938de60391c5f43bb44
0c8b5391846efbc1b0734909ed17f1a5edfaddc7
7f97f839a68ff500c71f18165ed02105e5958a85
1f9b6f59f47f231046ff9e4849e94603aabcd94c
fe61cb702576f0e711fa765170baee32d8973dca
```

## Blob objects returned by successful create_blob calls

```text
b49f205a4b07e5ae9d242f67e664b494cdc2a4c0
0e295f313dc1abd6ffa96603fe44eaebd46fe5e7
```

## Observed tool-contract failures

Several create_tree attempts returned HTTP 422 with the form:

```text
tree.sha <40-hex-object-id> is not a valid blob
```

Observed object IDs included:

```text
a56e4bd7676e0645d2d6b2396a1cddd4a568ef43
b49f205a4b07e5ae9d242f67e664b494cdc2a4c0
7ab496a48f4485fb0bb5694430e8e97d9bb50f9b
ba90046145eb1097d412f9992ef808d9f70f4368
86c50461bdae5f0963d1c3b1314cd2b8858b8653
5ffe5f838c2e84d80826c2c496dd5c1161f9c343
e41924475a9f294c48eedcc3c3448e20e293d38c
68b9bb049b6c98655ad9b381cb7580a447f25dbc
894feef151a88c6d07e366dd9fb8bf51ac9393f4
9f19255426c358bc900278f8128e0d1620c3518a
c9bb643d03ff2f8842272226c6aa2754c5aeacdc
0a99c7faff1db6eb0e03de4414f26e525bf3db72
a8e02b17698e75e500be08325956e5288658fc52
```

One fetch_blob attempt returned 404 for an object expected by an attempted tree construction. A separate fetch_blob succeeded for an object that was present.

## Evidence limit

This receipt does not prove that the current object-call behavior caused the external MNEMOSYNE-236 failure. The external 236 output does not preserve the exact failed path, requested encoding, request payload, returned error, or object SHA. The relationship is therefore an investigation hypothesis, not a verified common root cause.

No object listed here is authorized for reuse. No cleanup is authorized.
