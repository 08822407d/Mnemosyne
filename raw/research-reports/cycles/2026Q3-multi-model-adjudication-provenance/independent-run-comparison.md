# Independent-Conversation DR07 Comparative Review

> Maintainer-side comparative assessment, not backend-model attestation and not substantive adoption of the reports' design recommendations.

## Compared runs

| Arm | Declared surface | Repository reads | Contract result | Maintainer score |
|---|---|---:|---|---:|
| Independent labeled Pro | Deep Research, labeled Pro | required six paths completed | substantially satisfied | 90/100 |
| Independent labeled 5.6sol Thinking | Deep Research, labeled 5.6sol Thinking | 0/6 | correctly returned `RESEARCH_INCOMPLETE_REPOSITORY_ACCESS` | 83/100 |

The scoring rubric was fixed before the independent Thinking report was reviewed:

- task-contract compliance: 20;
- source quality and reproducibility: 20;
- repository facts and authority boundaries: 15;
- analysis depth, counterexamples and calibration: 20;
- practical Mnemosyne decision value: 15;
- uncertainty and authority control: 10.

## Findings

### Relative reliability

The labeled-Pro report is the canonical primary research candidate for this cycle because it combines:

- correct task identity;
- completed bounded repository reads;
- full required report structure;
- complete final determinations;
- a failure register and incident protocol;
- Mnemosyne-specific application.

The labeled-Thinking report remains valuable because it:

- correctly understood the research topic;
- independently confirmed most external conclusions;
- obeyed the required stop/degrade behavior when repository access failed;
- avoided inventing repository-specific findings.

It cannot replace the Pro report for the repository-specific portion.

### Cross-run convergence

The two independent reports agree on 11 of 12 required determinations, including:

- visible model labels and model self-reports are not sufficient runtime provenance;
- behavioral depth does not reliably identify the backend;
- fresh same-family review has only limited independence;
- heterogeneous review should not be mandatory for every change;
- compact run records are justified;
- a heavy cryptographic provenance stack is not justified now;
- the problem is better framed as adjudication and evidence governance than as marker formatting alone.

The only determination-level difference concerns whether GPT Pro adjudication of GF-STEP-5 should proceed only after this research. The Thinking report downgraded that item because it could not verify the repository.

### Confounders and non-claims

The comparison supports:

```yaml
labeled_Pro_route_more_consistently_completed_the_assigned_task: true
independent_Thinking_run_can_produce_high_quality_on_topic_research: true
independent_Pro_report_best_complete_result: true
```

It does not prove:

```yaml
actual_backend_model_of_either_run: unknown
model_label_is_backend_attestation: false
model_tier_alone_caused_the_difference: not_established
response_length_or_style_proves_identity: false
```

### Project-internal round

The earlier Project-internal pair is excluded from the canonical research package. It may remain conversational history, but it is not part of the reliable checkpoint because:

- the Thinking arm executed an unrelated generic topic-selection task;
- Project context, task routing, repository invocation and orchestration were not controlled;
- including it adds storage burden without strengthening the next maintainer gate.

## Use boundary

This comparison may be used to select research evidence for later maintainer review. It does not:

- accept the reports' proposed policy;
- change `current/human-approved-spec.md`;
- accept or reject Fable findings;
- prove a model-routing incident;
- authorize repair or target-project work.
