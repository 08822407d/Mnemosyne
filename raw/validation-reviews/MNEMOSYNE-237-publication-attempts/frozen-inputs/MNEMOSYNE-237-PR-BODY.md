## Summary

Publishes the frozen F2 G2A-composition and handoff-protocol audit evidence, the consolidated Pro adjudications and repairs, and the accepted pre-execution HVAL design as one exact recovery commit.

This is the additive recovery successor to two permanently blocked publication runs:

- `MNEMOSYNE-235` stopped after executor-side path-case drift during pre-commit tree staging.
- `MNEMOSYNE-236` stopped during an insufficiently evidenced blob-write failure before final-tree construction.

Neither blocked task is retried. Prior unreferenced Git objects are disclosed, not reused and not cleaned up.

## Publication shape

- Base: `master@e726dea818dca9418181775d0e7dcd62eb6c464a`
- Head: `mnemosyne-235-f2-g2a-and-handoff-audit-closeout`
- One reachable commit with parent equal to the frozen base
- Exact changed-path count: **69**
- Publication architecture: deterministic authenticated local Git worktree, one non-force push
- Post-push readback: every changed path verified against the external manifest

The 69 paths preserve the earlier Fable 005/006 originals and Pro repairs, both new Fable result sets and receipts, the 235/236/current-Pro incident evidence, four bounded current/registry/TODO/pointer updates, and the MNEMOSYNE-237 publication contracts and tools.

## Formal dispositions

### F2 / G2A

- Packages 004→003→002→001 readiness: PASS back to the Owner gate
- Fable composite candidate: preserved as evidence but not directly issuable
- Pro-corrected two-layer G2A issuance template: published for later exact path/blob readback
- `G2A_issued: false`
- `A1_execution_authorized: false`
- No Package 005

### Handoff protocol / HVAL

- Repository-only handoff audit: accepted with Pro corrections
- Failure taxonomy repaired to a parseable 12-case derivative while preserving the original
- HVAL design 001: repair required
- HVAL design 002: accepted for **separate** Owner authorization
- Design 002 contains 23 scenarios, a 24-receiver ceiling and a six-Pro-turn ceiling
- No fixture publication, HVAL execution or quota authorization occurs in this PR

### Publication failures

- 235 cause: sufficiently determined executor path-case drift with a contributory task-contract gap
- 236 cause: partial only because the failing request/response was not preserved
- Selected recovery architecture: local deterministic Git primary; receipt-disciplined object API fallback only
- Sequential Contents-API commits are rejected because they can leave reachable partial state

## Explicit exclusions

This PR does **not** modify:

- `commands/`
- active guards
- `current/human-approved-spec.md`
- the validation repository
- Meta-Agent or any real target

It does not issue G2A, execute A1, publish/execute HVAL fixtures, clean historical unreferenced objects, merge itself, or authorize automatic retry.

## Verification

The publication executor requires:

- exact payload ZIP and manifest identities;
- manifest-derived paths only;
- explicit add-vs-modify base checks;
- no case-sensitive duplicate or case-insensitive collision;
- exact staged and committed path/operation maps;
- exact index and post-push bytes/SHA-256 for all 69 paths;
- unchanged primary master and validation master/A1 branch state;
- one commit, one non-force push and one Ready PR.

Any failed gate closes `MNEMOSYNE-237` as blocked with a preserved exact execution receipt and no retry or cleanup.

## Merge and next gate

**Recommendation: `RECOMMEND_MERGE`.** This recommendation does not assume a comprehensive human diff review; the agent-side semantic and mechanical checks are the stated basis.

After merge, the next gate is:

1. exact final-master readback of the corrected G2A template, its manifest, validator and route status;
2. fill only the authorized dynamic fields from current repository and direct Owner evidence;
3. run the mechanical validator;
4. obtain a separate explicit Owner decision whether to issue the A1 controller G2A.

Do not issue G2A or execute A1 merely because this PR merges.
