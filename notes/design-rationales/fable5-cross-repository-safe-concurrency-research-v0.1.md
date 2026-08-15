# Design Rationale — Fable F2 Cross-Repository Safe Concurrency Research v0.1

```yaml
rationale_id: MNE-FABLE5-F2-RESEARCH-DESIGN-RATIONALE-001
task_id: MNEMOSYNE-214
research_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
status: preparation_evidence_not_execution_source
```

## Problem and goal

The target-local operating model needs evidence about which target work can proceed concurrently, which cross-repository operations must serialize, and how to handle stale refs, partial failure, privacy, rollback and no-dual-writer proof without adopting a heavyweight orchestrator prematurely.

## Why now

The roadmap schedules F2 after a public/synthetic cross-repository behavior test or in parallel with its result review. V1 has produced exact branch, write-set, isolation, no-write and restore evidence. Its final Pro adjudication is pending, but the complete bundle is sufficient as provisional evidence for an independent challenge.

## Alternatives considered

### Wait for final V1 Pro adjudication

Advantage: one more reviewed input. Disadvantage: unnecessarily serializes two independent high-capability reviews and loses the roadmap's intended heterogeneous parallel challenge.

### Start F2 from design files only

Rejected because the roadmap explicitly wanted behavior evidence first.

### Copy raw V1 results into Mnemosyne

Rejected because V1 raw-result ingestion remains separately gated. The Fable task reads exact public files directly from the synthetic repository controller branch.

### Selected option

Prepare one fresh Fable 5 Research task that:

- treats V1 results as provisional evidence;
- preserves the pending protocol discrepancy;
- compares lightweight and heavyweight coordination architectures;
- uses one Project and one Research invocation;
- performs no writes or validation;
- returns to fresh Pro adjudication.

## Risks and controls

- **V1 review changes interpretation:** F2 cites exact controller identities and separates provisional execution evidence from accepted conclusions.
- **Project contamination:** fresh one-run Project, exact 30-file manifest and G0 coverage gate.
- **Overfitting to V1:** require external primary research and adversarial failure classes absent from V1.
- **False backend claims:** record visible selection only; hidden backend remains unattestable.
- **Parallel-route interference:** no writes to the validation repository, V1 branches, Meta-Agent or real targets.

## Validation/falsification

The task design is defective if Fable cannot recover all 30 inputs, confuses provisional V1 results with authority, requires live connector writes, or cannot produce a decision-relevant comparison without inventing target requirements.
