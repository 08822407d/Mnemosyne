# V2-A A1 Package 003 — Revised Worker Launch, Return and Controller-Resume Flow

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-WRAPPER-FLOW-003
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-003
status: templates_not_authorization
```

Do not use until package 003 is merged, post-merge identities verified, fresh Pro review passes and Owner separately issues controller G2A.

Controller pre-worker phase remains package 002: after read-only PASS, create controller/Alpha/Beta branches, write `00/01/02`, and freeze both immutable task path/blobs plus both canonical wrapper templates before Alpha.

At role launch, Owner replaces only that role's selected-label placeholder and sends the complete wrapper block with this instruction:

```text
@GitHub
The canonical wrapper block and immutable task path/blob inside it are the only authority-bearing inputs. Before write, perform package-003 full-wrapper and package-task checks. Mismatch means WORKER_BLOCKED_BEFORE_WRITE. On PASS, execute the immutable package-001 worker task, echo the complete received canonical wrapper block verbatim plus its SHA-256 in the raw result, return exact Git/model/incident evidence, and stop. No branch/PR/evidence file, peer output, other App/quota, substitution, repair or retry.
```

Owner return after each worker must include two separately delimited objects:

```text
--- <ROLE> OWNER-SENT WRAPPER BEGIN ---
<exact complete block sent>
--- <ROLE> OWNER-SENT WRAPPER END ---
<ROLE> OWNER-SENT WRAPPER SHA256: <sha256 of exact canonical block>

--- <ROLE> WORKER RAW OUTPUT BEGIN ---
<complete unedited worker output>
--- <ROLE> WORKER RAW OUTPUT END ---
```

Explicit Alpha blocked/fail/disputed means no Beta. Alpha self-PASS may permit isolated Beta launch under package 002; controller later independently verifies both, and any false positive prevents order construction.

Controller resume performs package-001 Git checks plus package-003 three-way wrapper comparison. Phase dispositions:

```yaml
pre_write_mismatch: WORKER_BLOCKED_BEFORE_WRITE
known_Alpha_mismatch_before_Beta: STOP_NO_BETA
any_mismatch_before_orders: CELL_FAIL_NO_ORDER_CONSTRUCTION
mismatch_after_partial_writes: PRESERVE_PARTIAL_STATE_STOP_NO_RETRY
```

Only exact PASS for both Git contracts and both wrapper comparisons permits the inherited order construction and ten-file bundle.
