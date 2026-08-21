# MNEMOSYNE-236 — Blocked Publication Incident

```yaml
task_id: MNEMOSYNE-236
disposition: BLOCKED_CLOSED_NO_RETRY
repository: 08822407d/Mnemosyne
base: e726dea818dca9418181775d0e7dcd62eb6c464a
reachable_content_commit_created: false
pull_request_created: false
G2A_issued: false
A1_executed: false
```

The source/manifest, exact 31-path plan, branch recoverability, bounded target blobs and G2A/A1 gates all passed. The run stopped during a failed blob write before final-tree construction.

Not preserved: exact failed path, encoding, request body, HTTP/connector status, verbatim error response, returned SHA, count and sequence of prior successful blobs, and timestamp. The specific cause is therefore unknown. Encoding, request-shape and connector behavior remain candidates; no exact error is reconstructed.

Unreferenced blobs may exist. No cleanup, retry or object reuse is authorized.
