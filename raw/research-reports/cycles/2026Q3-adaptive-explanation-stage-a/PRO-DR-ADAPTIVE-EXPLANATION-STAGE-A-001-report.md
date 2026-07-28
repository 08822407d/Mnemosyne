```yaml
input_integrity_receipt:
  research_id: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001
  exact_topic: How an AI text-dialogue tutor can diagnose local prerequisite state and select, evaluate, and repair understandable explanations for foundational university mathematics without relying on a global learner-level label
  full_task_text_available: true
  generic_or_substitute_topic_used: false
  previous_failed_outputs_used_as_evidence: false
  substantive_research_completed: true
```

```yaml
runtime_provenance:
  operator_visible_selection: unknown_unless_explicitly_available
  exact_served_backend: unknown_or_not_attestable
  response_speed_used_as_identity_evidence: false
  model_self_identification_used_as_evidence: false
```

# Adaptive Explanation and Local Prerequisite Diagnosis for University Mathematics Tutoring

## Executive conclusion

The strongest defensible conclusion is not that an AI tutor can infer a stable “learner level,” but that it can operate a **local, evidence-first diagnostic-and-repair loop** for a current mathematical question. The loop should preserve multiple competing explanations of the difficulty, use the least burdensome probe likely to change the teaching action, adapt representation and support, and verify learning through independent performance rather than conversational fluency alone.

This conclusion rests on several converging but uneven evidence traditions. Formative assessment supports adapting instruction from current evidence rather than broad impressions. Intelligent tutoring systems show that fine-grained, step-sensitive support can improve learning when knowledge components and feedback are well designed. Cognitive load, worked-example, fading, expertise-reversal, multiple-representation, self-explanation, conceptual-change, retrieval-practice, and open-learner-model research supply candidate design principles and warning conditions. Recent LLM-tutoring studies show both promise and substantial design dependence: carefully constrained help can produce learning gains, while unguarded or overly assistive systems can improve supported performance without improving—and sometimes while harming—independent learning. citeturn721351search0turn721351search1turn721351search4turn350604search0turn980680search0

The evidence supports a controlled Stage B text-dialogue pilot, but not immediate deployment of a production adaptive tutor or persistent learner profile. The proposed framework and experiment remain candidates. Ordinary dialogue cannot reliably distinguish every local failure hypothesis; the tutor must be able to record `unknown`, expose its evidence and assumptions, invite correction, and include its own explanation error as a live hypothesis.

**Load-bearing conclusions and evidence calibration**

| Conclusion | Support class | Maturity | Confidence | Boundary |
|---|---|---|---|---|
| Generic “explain simply” instructions are not an operational teaching policy. | Systematic review, formative-assessment theory, engineering synthesis | Peer-reviewed bounded + conceptual | Moderate-to-high | No direct head-to-head trial of this exact prompt versus the full proposed framework was found. |
| Local evidence and multiple hypotheses are preferable to a global learner label. | Formative assessment, diagnostic measurement, open learner models | Peer-reviewed bounded | Moderate-to-high | The integrated policy is a synthesis, not a replicated intervention. |
| Representation and guidance should depend on task and prior knowledge rather than a fixed learning style. | Meta-analysis and representation studies | Replicated peer-reviewed, heterogeneous | High for rejecting fixed style; moderate for specific selection rules | Selection rules remain context-dependent. |
| Independent performance, transfer, retention, burden, and overreliance must be measured separately from satisfaction and fluent dialogue. | Learning-versus-performance literature, transfer meta-analysis, illusion-of-depth research, AI-tutoring RCTs | Peer-reviewed | High | Exact measurement battery still needs pilot validation. |
| An adaptive local-diagnosis-plus-recovery condition is worth testing. | Cross-tradition synthesis and adjacent empirical evidence | Conceptual/engineering synthesis with direct component evidence | Moderate | Not yet validated as one combined policy. |
| Persistent learner memory should be deferred. | Governance, open-learner-model, privacy and evidence-validity considerations | Peer-reviewed bounded + engineering inference | Moderate-to-high | Stage A does not design persistence. |

## Problem model and evidence base

**Operational problem model and terminology.** The tutoring problem here is not “Who is this learner in general?” but “What is the most plausible reason this current mathematical explanation or question is failing, and what low-burden action is best next?” Formative-assessment theory converges on a process in which evidence is elicited, interpreted, and used to decide the next instructional action. That is a local control problem under uncertainty, not a static classification problem. citeturn721351search0turn350604search1

The following objects must remain separate:

| Object | Meaning | Examples | Not equivalent to |
|---|---|---|---|
| Learner-state evidence | What the learner has demonstrated, with scope, recency, assistance provenance, and uncertainty | Independent solution, error pattern, delayed test, user correction | Global ability or personality |
| Local explanation context | What matters for this concept, notation, task, and turn | Current target, candidate prerequisites, representation already used | Long-term mastery profile |
| Explanation action | What the tutor chooses now | Example, diagram, formal definition, bridge, probe, counterexample | Evidence that the action worked |
| Explanation-outcome evidence | What changed after the action | Near transfer, error correction, delayed retention, burden | Satisfaction alone |
| Presentation preference | What the learner says they prefer | Short answer, more intuition, fewer formulas | Proof of capability or fixed learning style |

A broad statement such as “my foundations are weak” should be treated only as a cautious prior. It can justify slower abstraction jumps and more willingness to check prerequisites, but it does not identify which prerequisite is missing for the current target. Concept inventories and diagnostic measurement can provide more local evidence, but they remain domain- and instrument-specific. citeturn136199search5turn136199search9turn291392search0turn291392search2

**Evidence review by research tradition.** The evidence base is cross-disciplinary and uneven. Formative-assessment work contributes the strongest design principle: adapt instruction on the basis of current evidence, not broad impressions. ITS research contributes evidence that step-based or substep-sensitive tutoring can improve outcomes, but average effects conceal substantial variation in system design, comparison conditions, measures, and implementation. Kulik and Fletcher’s meta-analysis found a median effect of roughly 0.66 standard deviations across 50 controlled evaluations, but this is evidence for ITS as a broad class, not for the present LLM policy. citeturn721351search0turn721351search1

Knowledge-space theory, diagnostic classification models, Q-matrices, and concept inventories offer different representations of prerequisite and skill structure. They are useful, but every one requires assumptions about granularity, item-skill relations, alternative routes, and the meaning of mastery. Q-matrix validation research shows that misspecification can materially affect inference. Knowledge-space applications such as ALEKS demonstrate that granular readiness states can be operationalized at scale, but commercial implementation evidence does not establish a universal representation for open-domain dialogue tutoring. citeturn136199search2turn136199search8

Cognitive-load and worked-example research supports adapting support to prior knowledge and task complexity. The expertise-reversal meta-analysis across 60 studies and 5,924 participants supports the general principle that more guidance tends to help lower-prior-knowledge learners while less guidance can benefit higher-prior-knowledge learners, but moderators and task design matter. This evidence rejects fixed universal sequencing more strongly than it validates any one local diagnostic algorithm. citeturn255131search0

Multiple-representation research finds small average benefits with high heterogeneity. Benefits depend on representational competence and how representations are coordinated, so “always use a diagram” is not defensible. The relevant action is to choose a representation that addresses the current obstacle and make mappings among representations explicit. citeturn668372search0

Self-explanation, retrieval-practice, transfer, conceptual-change, and refutation-text research support using explanation, counterexamples, and transfer tasks as evidence and instructional tools. The transfer-of-test-enhanced-learning meta-analysis synthesized 192 effects from 122 experiments and found a moderate average transfer benefit, but with important moderators. Refutation-text meta-analysis supports misconception repair when the misconception is explicitly addressed, yet domain and implementation limits remain. citeturn255131search1turn719693search11turn666759search3

Open and negotiated learner models support transparency and contestability. Letting learners inspect, challenge, and negotiate a model can improve model accuracy and reflection, but the literature does not justify persisting every dialogue-based hypothesis. citeturn666759search1turn666759search2turn666759search11

Recent LLM tutoring evidence is promising but design-sensitive. Pardos and Bhandari found learning gains from ChatGPT-generated hints comparable to human-authored hints in a bounded mathematics-skills setting, while noting quality failures before mitigation. A physics-course RCT found a carefully structured AI tutor outperformed an active-learning class condition in that setting. Conversely, Bastani and colleagues found that unguarded generative AI improved practice performance but reduced unassisted exam performance, whereas a guarded tutoring design mitigated the harm. These findings support controlled design and independence measures, not a blanket claim that LLM tutoring works. citeturn721351search4turn980680search0turn350604search0

## Failure diagnosis and local adaptation framework

**Local failure-hypothesis validity and confounder matrix.** The table below is an evidence-calibrated synthesis, not a validated universal taxonomy. It combines direct empirical support where available with engineering inference where the literature is adjacent rather than exact. Ordinary dialogue can generate hypotheses, but many distinctions require stronger task evidence.

| Failure hypothesis | Observable evidence | Confounders / false-positive risk | False-negative risk | Dialogue-only identifiability | Stronger evidence / stop rule |
|---|---|---|---|---|---|
| Missing prerequisite | Cannot complete a minimal isolating task; cannot explain prerequisite in own words; repeated independent errors | Ambiguous wording, anxiety, unfamiliar notation, low effort | Guessing or prompt-following can mask absence | Sometimes, but weak | Use an isolating item or artifact; record `unknown` if task validity is uncertain |
| Retrieval failure | Recognizes or performs after a minimal cue; later independent recall succeeds | Cue may teach rather than retrieve; familiarity illusion | Learner may compensate via another route | Limited | Compare cued and uncued performance, then delayed recall |
| Connection gap | Component ideas are correct, but learner cannot explain relation or transfer between them | Task may demand additional skill; representation mismatch | Familiar examples can hide the gap | Sometimes | Ask for mapping, comparison, or near transfer |
| Notation/terminology barrier | Can solve equivalent verbal/concrete version but fails symbolic form; misreads symbols consistently | Underlying concept may also be weak | Learner may infer notation from context | Often plausible | Translate both directions; use symbol-specific probe; do not generalize beyond topic |
| Misconception candidate | Systematic, coherent wrong prediction; selects misconception-aligned distractor; resists simple correction | Item may induce error; careless slip | Learner may avoid revealing misconception | Sometimes | Use contrasting cases/counterexample; require prediction and explanation |
| Unsupported abstraction jump | Follows each concrete step but cannot justify transition to general statement | Missing prerequisite, working-memory load, tutor omission | Learner may mimic formal language | Often plausible | Locate earliest unsupported step; bridge locally; record tutor-defect possibility |
| Representation mismatch | Performance changes materially when representation changes and mappings are clarified | Second representation may simply be easier; prior exposure | Learner may fail both representations for different reasons | Sometimes | Compare isomorphic tasks, ask mapping between representations |
| Learner task misunderstanding | Response addresses a different task; paraphrase reveals different goal | Tutor wording ambiguous; cultural/language difference | Learner may infer intent and hide misunderstanding | Often | Ask a concise task paraphrase or forced-choice interpretation |
| Tutor misunderstood learner question | Learner repeatedly redirects; tutor answer does not address requested relation or obstacle | Learner’s question ambiguous | Learner may accept irrelevant answer politely | Often | Tutor restates question and asks confirmation; preserve uncertainty |
| Cognitive load/pacing/environment | Performance deteriorates with long turns, dense notation, interruptions; improves with chunking | Knowledge gap or low motivation | Learner may persist despite overload | Weak to moderate | Reduce simultaneous demands; use burden measure; avoid trait inference |
| Defective/incorrect Agent explanation | Independent check reveals factual error; omitted step; misleading analogy; contradiction across turns | Learner misunderstanding may be blamed on tutor | Polished language can hide defects | Sometimes | Verify mathematics; compare with source/rubric; explicitly self-correct |
| Insufficient/non-identifiable evidence | Multiple hypotheses predict the same response; no valid discriminating probe | Pressure to personalize creates overconfidence | Hidden evidence may exist | High | Record `unknown`, offer safe explanation or ask user preference; do not persist a diagnosis |

The critical policy implication is that the tutor should maintain a **small competing-hypothesis set**, not select a single diagnosis after one utterance. The hypothesis set should be local to the target, carry evidence references and assistance provenance, and expire or be rechecked.

**Prerequisite-route and required-mastery representation options.** No single representation is sufficient. Prerequisite graphs are intuitive and useful for authoring, but they tend to overstate universality and underrepresent alternative valid solution routes. Knowledge-space and learning-space models can represent sets of feasible knowledge states, but they need carefully defined items and domains. Q-matrices and diagnostic classification models connect items to skills, but inference is sensitive to matrix quality. Learning progressions capture development over time, while concept inventories provide validated topic-specific anchors. Cognitive task analysis can expose hidden expert steps but may import one expert’s preferred procedure as though it were the only route.

A practical Stage B candidate should use a small, auditable hybrid:

```yaml
local_prerequisite_model:
  target_concept:
  alternative_routes:
    - route_id:
      prerequisite_nodes:
        - concept_or_skill:
          required_level_for_this_route:
          evidence_state: demonstrated | gap_candidate | misconception_candidate | retrieval_candidate | connection_gap_candidate | notation_candidate | unknown
          evidence_refs: []
          assistance_provenance:
          recency:
  selected_explanation_route:
  competing_routes: []
  expiry_or_recheck_trigger:
```

“Required mastery” should mean enough evidence for a specific target and explanation route, not a universal percentage. Multiple valid routes must be allowed. If the tutor cannot distinguish partial knowledge from an alternative strategy, it should preserve the ambiguity.

**Low-burden diagnostic policy candidates.** The tutor should behave as if probes have a cost. Formative-assessment research, mathematics diagnostic-question design, teach-back review work, self-explanation meta-analysis, and transfer literature all imply that more valid evidence usually requires more than free conversation, but constant assessment can increase burden and distort the interaction. citeturn721351search0turn719693search11turn255131search1

A candidate decision rule is:

1. Use recent, scoped evidence when it exists.
2. If the cost of a wrong explanation route is low, provide a provisional explanation without testing first.
3. Ask one diagnostic question only when two plausible hypotheses would lead to materially different actions.
4. Choose a probe that discriminates among those hypotheses.
5. Explain why the probe is being asked and allow the learner to request direct explanation.
6. Reuse the teaching interaction as evidence rather than creating a separate exam when possible.
7. Do not persist local hypotheses without stronger evidence and user-visible correction rights.

| Probe | Information value | Burden | Primary use | Main risk |
|---|---|---|---|---|
| Focused clarification question | Moderate | Low | Distinguish symbol vs concept vs relation | Self-report may be inaccurate |
| Teach-back/paraphrase | Moderate | Low–moderate | Detect task or relation misunderstanding | Fluency may mask gaps; can be socially demanding |
| Minimal isolating example | High | Moderate | Test prerequisite or misconception | Item validity and difficulty matter |
| Forced choice between interpretations | Moderate–high | Low | Distinguish conceptual alternatives | Guessing and oversimplification |
| Counterexample/prediction | High | Moderate | Misconception candidate | Can teach during diagnosis |
| Near-transfer item | High | Moderate | Test relation/application | Practice effect, task mismatch |
| Unfamiliar-transfer item | High | High | Robust understanding | Burden and domain knowledge confounds |
| First-broken-step question | High | Low–moderate | Locate abstraction or reasoning break | Learner may not introspect accurately |
| Provisional explanation first | Moderate | Low | Low-risk situations, cold start | Tutor may reinforce wrong assumptions |
| No question/safe default | Low | Lowest | Very short or preference-sensitive interaction | Missed personalization |

**Explanation-action selection framework.** The evidence suggests five recurring principles.

First, match support to current evidence and task complexity, not a fixed learner style. Expertise-reversal evidence supports changing guidance with prior knowledge, while multiple-representation meta-analysis shows representation benefits are heterogeneous. citeturn255131search0turn668372search0

Second, make the relation among representations explicit. A diagram, example, or physical analogy helps only if the learner can map it to the symbols and concept. Representational competence is a distinct issue; adding more representations can increase extraneous load. citeturn668372search0

Third, use progressive formalization. Begin with a reachable anchor when appropriate, but label intuition, state analogy limits, and connect to the formal definition rather than replacing it with a false rule.

Fourth, use worked examples and fading conditionally. Worked examples can reduce load for novices, while completion problems and fading can move responsibility to the learner. Higher prior knowledge can make redundant guidance harmful. citeturn255131search0

Fifth, make action selection inspectable. The tutor should be able to state: “I am using a minimal example because the obstacle may be notation rather than the concept; if this example is easy, I will switch to the symbolic form.” This is not a claim about a stable learner type.

A candidate action record is:

```yaml
explanation_action:
  target:
  leading_hypotheses: []
  selected_entry_point:
  representation:
  sequence:
  abstraction_step:
  terminology_density:
  probe_or_no_probe:
  modality:
  rationale:
  expected_evidence:
  stop_or_switch_trigger:
```

**Explanation-failure recovery framework.** A repair loop should do seven things: locate the earliest unsupported step, preserve multiple hypotheses, keep tutor error live, change explanation dimensions meaningfully, run a minimal discriminating check, switch representation when useful, and stop with uncertainty when evidence remains inadequate.

```text
learner reports confusion or produces contradictory evidence
  -> restate target and identify earliest break
  -> audit tutor explanation for correctness and omitted steps
  -> update competing hypotheses
  -> choose one materially different repair action
  -> obtain minimal evidence
  -> continue, bridge, switch, or stop
  -> record outcome without globalizing the hypothesis
```

Repair actions include: replacing an analogy with structural explanation; adding the missing relation between known components; translating notation; reducing an abstraction jump; using a contrasting case or refutation; switching between verbal, symbolic, graphical, and tabular forms; asking the learner to identify the first non-following step; and explicitly retracting an incorrect tutor statement. Refutation-text and conceptual-change evidence supports directly addressing misconceptions, but these methods can backfire or become burdensome when the presumed misconception is wrong. citeturn666759search3

**Accessibility without false simplification.** Accessibility does not mean stripping away structure until only a slogan remains. The research supports making the next step reachable while preserving the future path to rigor: use a concrete anchor, declare analogy limits, state what is being temporarily omitted, distinguish motivation from definition, and progressively restore formal structure. A tutor should never invent a convenient false rule merely because it is easier to say.

## Measurement and experimentation

**Outcome and measurement framework.** The literature is unusually clear on one point: performance during explanation is not the same as learning. Learners can feel fluent, repeat phrasing correctly, or express confidence while lacking transferable understanding. The illusion-of-explanatory-depth literature and learning-versus-performance work support measuring what the learner can do independently after support is removed. citeturn719693search8turn710343search0turn710343search2

Stage B should distinguish:

| Outcome | Candidate measure | Main caveat |
|---|---|---|
| Immediate comprehension | Brief independent item and explanation | Can reflect short-term cueing |
| Near transfer | Isomorphic problem with changed surface features | May still be pattern matching |
| Unfamiliar transfer | New representation or application | Higher burden and domain confounds |
| Delayed retention | Reassessment after delay without transcript | Attrition and intervening study |
| Independent performance | No tutor/hint condition | Must record prohibited assistance |
| Calibration | Confidence before answer versus correctness | Confidence scales need clear interpretation |
| Error reduction | Change in misconception-aligned or reasoning errors | Item comparability matters |
| Repair success | Recovery after deliberately or naturally failed explanation | Ethical design and standardization needed |
| Burden/cognitive load | Paas-type mental effort, NASA-TLX subset, time, dropout | Self-report and task time are imperfect |
| Autonomy/overreliance | Help requests, copying, answer acceptance, unassisted performance | Context and trust effects |

AI tutoring evidence makes independence essential. Bastani et al. show why supported accuracy cannot be the primary outcome: unrestricted AI can improve practice performance while harming later unassisted performance. The OECD’s 2026 synthesis similarly emphasizes purposeful educational use and the distinction between task completion and learning. citeturn350604search0turn291392search1

**Controlled experiment design.** A feasible initial study should compare four prompting/policy conditions:

| Condition | Tutor behavior | Key difference |
|---|---|---|
| C0 Generic simple instruction | “Explain simply to a learner with weak foundations” | No explicit local diagnostic or recovery policy |
| C1 Fixed representation | Always begins with an intuitive or worked example | More structured, but not locally adaptive |
| C2 Adaptive local diagnosis | Maintains bounded hypotheses, uses low-burden evidence, adapts explanation | Tests local diagnosis/action selection |
| C3 Adaptive plus recovery | C2 plus explicit tutor-audit, failure recovery, self-correction, and stop/unknown rules | Tests repair and Agent-error handling |

**Topics.** Use three matched microdomains:

- Calculus: function/limit-to-derivative relation or derivative as local linear approximation.
- Linear algebra: span/linear independence or solution structure of systems.
- Probability/statistics: conditional probability/Bayes or sampling-distribution interpretation.

Each domain should include several validated or expert-reviewed prerequisite structures, misconception candidates, notation barriers, and transfer items. Existing concept inventories can anchor item design but should not be treated as complete curricula.

**Population and phases.** Begin with a public/synthetic protocol pre-pilot using scripted learner traces, adversarial cases, and expert annotation to test whether conditions behave as specified. This cannot establish learning efficacy. A later real-participant study should recruit adult or university-level learners with varied prior knowledge and record inclusion, language, accessibility, and prior AI-use assumptions.

**Design choice.** A between-subject design minimizes carryover among prompting policies but requires more participants. A within-subject design increases efficiency but risks participants learning the diagnostic structure and comparing tutors. A sequential/adaptive design best matches the intervention but complicates causal attribution. The recommended first real pilot is stratified between-subject by pretest and domain, with identical base model, content, tool access, time budget, and temperature/settings where controllable.

**Pretest and evidence.** Use a short domain pretest plus local prerequisite items. Do not infer a global learner level. Record every hint, worked step, answer reveal, external tool, and assistance event.

**Assessments.** Administer immediate independent items, near transfer, one unfamiliar-transfer item, and delayed unassisted reassessment. Use blind or independent scoring for explanations and reasoning where practical. Measure burden, time, dropout, help-seeking, and confidence.

**Contamination controls.** Separate practice and outcome items, prevent answer leakage, standardize system prompts and source material, and record model/prompt/tool/date. Do not claim exact hidden backend identity. Analyze attrition, carryover, demand characteristics, and tutor-model drift.

**Safety and privacy.** Use public or synthetic material first. For real participants, require consent, minimal data, clear retention limits, contestable inferences, and a no-penalty option to skip diagnostic probes. Avoid collecting sensitive educational records unless separately justified.

**Analysis.** Pre-register primary outcomes. Treat independent performance and transfer as primary; satisfaction as secondary. Report null and adverse effects. Do not invent a sample size; conduct power/precision planning from pilot variance and a smallest effect of educational interest.

**Minimum viable text-dialogue pilot.** The recommended MVP is a **two-week, stratified, between-subject pilot** with all four conditions and three microtopics only: one from calculus, one from linear algebra, and one from probability/statistics. Each participant stays in one condition, completes the same pretest, three tutor sessions, immediate independent items, near-transfer items, one unfamiliar-transfer item per domain, and a delayed posttest. This pilot can establish protocol feasibility, adherence, burden, and preliminary outcome patterns. It cannot establish a universal adaptive policy, long-term retention, cross-domain generalization, or persistent learner-model validity.

## Governance and operational boundaries

**Safety, fairness, privacy, autonomy, and non-manipulation.** The tutoring system should never infer or store stable personality, “learning style,” intelligence, or clinical categories from small amounts of dialogue. Open-learner-model research supports making evidence contestable and inspectable, while fairness requires checking whether diagnostic probes and language-dependent explanations work differently across language backgrounds, disabilities, and prior educational exposure. citeturn666759search1turn666759search2turn666759search11

The tutor should disclose when it is making a local hypothesis, why a probe is being asked, how the result will be used, and when the evidence is too weak. The learner must be able to correct the record, decline a probe, request direct explanation, and obtain an explanation of the tutor’s rationale. Adaptive support must not become covert persuasion, emotional dependence, or a mechanism for restricting opportunities.

**Implications for a later memory system without designing persistent learner memory now.** The evidence reviewed here suggests what a later memory system would need **if** one were considered in a future stage, without endorsing or designing it now. The useful unit is not a stable learner profile but a scoped evidence object containing source, target concept, timestamp, assistance provenance, uncertainty, competing interpretations, user correction, expiry, and permitted purpose. Local hypotheses should default to session-local. Persistent storage should require stronger evidence and a separate governance decision. Shared or cross-Agent use is outside Stage A.

**Findings that must remain open questions.** Several questions remain genuinely open. The strongest are: how accurately a text-only tutor can distinguish retrieval failure from absence of knowledge; which micro-probes maximize information per burden unit in university mathematics; when two representations are equivalent enough for diagnostic comparison; how well diagnosis rules transfer across mathematical domains and language backgrounds; how frequently tutor self-audit catches real errors without creating excessive latency; whether adaptive explanations improve delayed transfer and autonomy; and which local evidence, if any, should persist.

**Adoption, stop, rollback, and falsification criteria.** Adoption should require improvement on **independent** posttest and transfer measures with no worsening of burden, dropout, or overreliance. Rollback should occur if adaptive conditions mainly improve tutor-assisted accuracy or satisfaction while independent performance stagnates or declines; if diagnostic errors produce systematically inappropriate instruction; if burdens or disparities increase; if the tutor persists in false learner hypotheses; or if privacy/contestability controls fail.

The framework is falsified or materially weakened if C2/C3 do not outperform the simpler C0/C1 conditions on independent learning or repair, if diagnostic probes add burden without useful discrimination, or if benefits disappear under delayed and unfamiliar-transfer tests. Null findings should reduce complexity rather than motivate ever-more invasive profiling.

## Portable source table and final verdict

**Portable source table.** The table below includes the sources used for load-bearing claims, with literal URLs, stable identifiers where available, dates, type, claim mapping, support status, and key limitations. “Direct” means the source bears directly on the claim in this report; “analogical” means it informs the design by adjacent evidence rather than exact domain matching.

| Title | Authors / organization | Literal URL | Stable identifier | Publication / update date | Access date | Source type | Claim / section mapping | Direct or analogical support | Access / verification limitation |
|---|---|---|---|---|---|---|---|---|---|
| Revising the Definition of Formative Assessment / FAST-SCASS definition | CCSSO FAST SCASS / Michigan MDE mirror | `https://www.michigan.gov/mde/-/media/Project/Websites/mde/OEAA/Formative-Assessment-Process/Revising-the-Definition-of-Formative-Assessment.pdf?hash=62C0D664EEEAB137F377A670CFF970D5&rev=a13ec5f94a5b49368c1deea9648b4645` | None shown | 2018 update document | 2026-07-28 | Official guidance / standard-style definition | Executive conclusion; problem model; object separation | Direct | State-hosted mirror rather than original CCSSO page. |
| Formative Assessment in Mathematics Education: A Systematic Review | Karolin Maskos et al. | `https://link.springer.com/article/10.1007/s11858-025-01696-x` | DOI: `10.1007/s11858-025-01696-x` | 2025-05-20 | 2026-07-28 | Systematic review | Executive conclusion; evidence review; low-burden policy; experiment design | Direct | School-math emphasis, not exclusively university students. |
| Designing Formative Assessment in Mathematics | Malcolm Swan | `https://www.dcu.ie/sites/default/files/smec/pdfs/MSwan-Designing-formative-assessment-in-mathematics.pdf` | None shown in file | 2014 | 2026-07-28 | Conceptual / design-research paper | Evidence review; diagnostic policy; experiment design | Direct | Practice-oriented; not a controlled efficacy paper. |
| On Formative Assessment in Math: How Diagnostic Questions Can Help | Craig Barton | `https://eric.ed.gov/?id=EJ1182085` | ERIC: `EJ1182085` | 2018 | 2026-07-28 | Peer-reviewed / descriptive article record | Failure matrix; low-burden probes | Direct | ERIC page is a record/abstract page, not full full-text article. |
| Focus on Formative Feedback | Valerie J. Shute | `https://journals.sagepub.com/doi/10.3102/0034654307313795` | DOI: `10.3102/0034654307313795` | 2008 | 2026-07-28 | Review article | Evidence review; repair loop; outcome framework | Direct | Broad education review, not mathematics-specific. |
| The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems | Kurt VanLehn | `https://eric.ed.gov/?id=EJ946764` | ERIC: `EJ946764` | 2011 | 2026-07-28 | Review article / ERIC record | Executive conclusion; ITS evidence base | Direct | ERIC record summary rather than publisher full text. |
| Effectiveness of Intelligent Tutoring Systems | James A. Kulik, J. D. Fletcher | `https://journals.sagepub.com/doi/10.3102/0034654315581420` | DOI: `10.3102/0034654315581420` | 2016-03-01 online | 2026-07-28 | Meta-analysis | Executive conclusion; ITS evidence base | Direct | Abstract/preview lines accessible; full article not fully parsed here. |
| A systematic review of AI-driven intelligent tutoring systems in K-12 education | Angélique Létourneau et al. | `https://www.nature.com/articles/s41539-025-00320-7` | DOI from article page | 2025-05-14 | 2026-07-28 | Systematic review | Evidence review; experiment justification | Analogical | K-12 focus, but directly relevant to ITS evidence and ethics. |
| A practical perspective on knowledge space theory: ALEKS and its data | Eric Cosyn et al. | `https://jmatayoshi.github.io/publications/JMP2021_KST_ALEKS_preprint.pdf` | Preprint for Journal of Mathematical Psychology article | 2021 preprint | 2026-07-28 | Peer-reviewed article preprint | Prerequisite representation options; local state modeling | Direct | Preprint copy used; commercial ALEKS context may limit generalization. |
| Primer on Diagnostic Classification Models | Andrė A. Rupp | `https://www.nciea.org/wp-content/uploads/2023/02/Primer-on-Diagnostic-Classification-Models-Rupp-Feb-2023-Version-2.0.pdf` | None shown | 2023-02-06 | 2026-07-28 | Measurement primer / official guidance | Representation options; learner-state evidence framing | Direct | Primer, not original empirical research. |
| Cognitive Diagnostic Models and how they can be useful | James Williamson | `https://www.cambridgeassessment.org.uk/Images/701443-cognitive-diagnostic-models-and-how-they-can-be-useful.pdf` | None shown | 2023 | 2026-07-28 | Measurement review | Representation options; Q-matrix vulnerability | Direct | Applied review, not a single empirical study. |
| Using machine learning to improve Q-matrix validation | H. Qin et al. | `https://link.springer.com/article/10.3758/s13428-023-02126-0` | DOI on article page | 2024 | 2026-07-28 | Peer-reviewed methods paper | Representation options; caution on Q-matrix misspecification | Direct | Methods focus, not tutoring outcomes. |
| There are Open Learner Models About! | Susan Bull, Judy Kay | `https://dl.acm.org/doi/10.1109/TLT.2020.2978473` | DOI on ACM page | 2020 | 2026-07-28 | Peer-reviewed overview | Safety, fairness, contestability; memory implications | Direct | Overview article; access via abstract page. |
| Negotiated learner modelling to maintain today’s learner models | Susan Bull et al. | `https://pmc.ncbi.nlm.nih.gov/articles/PMC6302918/` | PMCID: `PMC6302918` | 2016 | 2026-07-28 | Peer-reviewed article | Safety, contestability, memory implications | Direct | Web opener hit reCAPTCHA, so metadata relied on search result. |
| The More the Better? A Systematic Review and Meta-Analysis of the Benefits of More than Two External Representations in STEM Education | E. Rexigel et al. | `https://link.springer.com/article/10.1007/s10648-024-09958-y` | DOI: `10.1007/s10648-024-09958-y` | 2024 | 2026-07-28 | Systematic review and meta-analysis | Explanation-action selection; representation mismatch; accessibility | Direct | STEM-wide, not math-only; high heterogeneity. |
| The relation of representational competence and conceptual knowledge in science education | P. A. Edelsbrunner et al. | `https://pmc.ncbi.nlm.nih.gov/articles/PMC10285021/` | PMCID: `PMC10285021` | 2023 | 2026-07-28 | Peer-reviewed article | Object separation; representation mismatch | Analogical | Science education domain, generalized cautiously to mathematics. |
| First year university students’ difficulties with mathematical symbols | Ruth Pierce et al. | `https://files.eric.ed.gov/fulltext/ED589460.pdf` | ERIC full-text PDF | 2017 | 2026-07-28 | Conference / research paper | Failure matrix; notation barrier; accessibility | Direct | Lecturer/tutor perspective, not direct experimental manipulation. |
| Assumed Mathematics Knowledge: the Challenge of Symbols | C. Bardini, R. Pierce | `https://www.researchgate.net/publication/274375150_Assumed_Mathematics_Knowledge_the_Challenge_of_Symbols` | None shown | 2015 | 2026-07-28 | Conference paper / accessible copy | Failure matrix; symbol-load caution | Direct | ResearchGate-accessible version; not ideal primary landing page. |
| A meta-analysis of the expertise reversal effect | Leonard Tetzlaff et al. | `https://www.sciencedirect.com/science/article/pii/S0959475225000660` | DOI on publisher page | 2025 | 2026-07-28 | Meta-analysis | Explanation selection; guidance adaptation | Direct | Search-result abstract used due publisher access limits. |
| The Guidance Fading Effect | John Sweller, Slava Kalyuga | `https://cogscisci.wordpress.com/wp-content/uploads/2019/08/sweller-guidance-fading.pdf` | None shown | 2011 text available via PDF copy | 2026-07-28 | Review chapter / PDF copy | Worked examples; explanation sequencing | Direct | Secondary hosting of PDF copy. |
| Inducing Self-Explanation: a Meta-Analysis | Kiran Bisra et al. | `https://gwern.net/doc/psychology/spaced-repetition/2018-bisra.pdf` | DOI in original article | 2018 | 2026-07-28 | Meta-analysis | Low-burden probes; repair loop; action selection | Direct | PDF mirror used. |
| Transfer of Test-Enhanced Learning: Meta-Analytic Review and Synthesis | Steven C. Pan, Timothy C. Rickard | `https://pubmed.ncbi.nlm.nih.gov/29733621/` | DOI: `10.1037/bul0000151` | 2018-05-07 epub | 2026-07-28 | Meta-analysis | Outcome framework; transfer measures | Direct | PubMed entry used for metadata and abstract. |
| The misunderstood limits of folk science: an illusion of explanatory depth | Leonid Rozenblit, Frank Keil | `https://pmc.ncbi.nlm.nih.gov/articles/PMC3062901/` | DOI on page / PMCID | 2002 | 2026-07-28 | Peer-reviewed article | Outcome framework; why “I understand” is insufficient | Direct | Original publisher page also available; PMC used. |
| Refutation Text Facilitates Learning: a Meta-Analysis of Between-Subjects Experiments | Nicholas L. Schroeder, Aaron Kucera | `https://pubmed.ncbi.nlm.nih.gov/35095236/` | DOI from PubMed record | 2022 | 2026-07-28 | Meta-analysis | Misconception repair; accessibility without false simplification | Direct | PubMed abstract used; full text not opened due reCAPTCHA. |
| Effectiveness of conceptual change strategies in science education: A meta-analysis | Ceren Pacaci et al. | `https://open.metu.edu.tr/bitstream/handle/11511/104711/J%20Res%20Sci%20Teach%20-%202023%20-%20Pacaci%20-%20Effectiveness%20of%20conceptual%20change%20strategies%20in%20science%20education%20A%20meta%E2%80%90analysis.pdf` | DOI within PDF references | 2023 | 2026-07-28 | Meta-analysis | Repair loop; refutation/counterexample use | Analogical | Science education domain, generalized cautiously. |
| Learning from errors and failure in educational contexts | Susanne Narciss et al. | `https://pmc.ncbi.nlm.nih.gov/articles/PMC11803059/` | PMCID on page | 2024 | 2026-07-28 | Review article | Repair loop; error-first design | Analogical | PMC open failed via reCAPTCHA during view; relied on search synopsis. |
| The Development of a Function Concept Inventory | Ann O’Shea, Sinéad Breen, Barbara Jaworski | `https://link.springer.com/article/10.1007/s40753-016-0030-5` | DOI: `10.1007/s40753-016-0030-5` | 2016-06-17 | 2026-07-28 | Peer-reviewed instrument paper | Representation options; measurement anchors | Direct | Function concept, not all calculus. |
| Calculus Concept Inventory | LASSO Education / cites Gleason et al. | `https://lassoeducation.org/calculus-concept-inventory/` | Inventory registry listing | Current listing accessed 2026 | 2026-07-28 | Instrument registry | Measurement anchors; pilot topic selection | Direct | Registry points to validity literature rather than being primary validation article. |
| Statistics Concept Inventory | LASSO Education | `https://lassoeducation.org/statistics-concept-inventory/` | Inventory registry listing | Current listing accessed 2026 | 2026-07-28 | Instrument registry | Measurement anchors; probability/statistics pilot | Direct | Registry notes validation ongoing. |
| Predictive Validity of the Algebra Concept Inventory | Claire Wladis et al. | `https://journals.sagepub.com/doi/10.1177/23328584261419497` | DOI: `10.1177/23328584261419497` | 2026-04-04 | 2026-07-28 | Peer-reviewed article | Why broad “weak foundations” is a weak prior; validated local measures | Direct | Algebra-focused and recent. |
| ChatGPT-generated help produces learning gains equivalent to human tutor-authored help on mathematics skills | Zachary A. Pardos, Shreya Bhandari | `https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0304013` | DOI: `10.1371/journal.pone.0304013` | 2024 | 2026-07-28 | Peer-reviewed primary study | Direct LLM tutoring evidence | Direct | Focuses on generated help rather than fully adaptive dialogue tutoring. |
| Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues | Alexander Scarlatos et al. | `https://arxiv.org/abs/2503.06424` | DOI: `10.48550/arXiv.2503.06424`; related DOI `10.1007/978-3-031-98414-3_18` | 2025-03-09; revised 2025-07-28 | 2026-07-28 | Conference paper / arXiv version | Direct LLM tutoring evidence; adaptive dialogue design | Direct but preprint/conference-level | Not yet a large-scale replicated intervention study. |
| AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting | Scientific Reports article | `https://www.nature.com/articles/s41598-025-97652-6` | DOI in article URL | 2025-06-03 | 2026-07-28 | Peer-reviewed RCT | Direct LLM tutoring evidence; structured pedagogy matters | Direct | Physics course setting, not foundational math. |
| Generative AI without guardrails can harm learning | Hamsa Bastani et al. | `https://www.pnas.org/doi/10.1073/pnas.2422633122` | DOI: `10.1073/pnas.2422633122` | 2025 | 2026-07-28 | Peer-reviewed primary study | Overreliance; stop/rollback criteria; independence outcomes | Analogical but close | High-school math rather than university math. |
| OECD Digital Education Outlook 2026: Exploring Effective Uses of Generative AI in Education | OECD | `https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html` | DOI: `10.1787/062a7394-en` | 2026-01-19 | 2026-07-28 | Official guidance / evidence synthesis | Executive conclusion; safety; autonomy; pilot governance | Direct | Policy synthesis, not a single experimental study. |
| Students' Reliance on AI in Higher Education: Identifying Contributing Factors | Griffin Pitts et al. | `https://scale.stanford.edu/ai/repository/students-reliance-ai-higher-education-identifying-contributing-factors` | arXiv link on page: `2506.13845v1` | 2025-06 | 2026-07-28 | Preprint repository summary | Autonomy; overreliance measurement | Direct but preprint | Programming-task context, not mathematics. |
| Teach-back: A systematic review of implementation and impacts | Jacqueline Talevski et al. | `https://journals.plos.org/plosone/article/file?id=10.1371%2Fjournal.pone.0231350&type=printable` | DOI: `10.1371/journal.pone.0231350` | 2020 | 2026-07-28 | Systematic review | Teach-back/paraphrase as probe | Analogical | Health education domain, generalized cautiously. |
| Misconceptions in Linear Algebra: the Case of Undergraduate Students | N. Aygör, H. Özdağ | `https://www.sciencedirect.com/science/article/pii/S1877042812017314` | DOI on publisher page | 2012 | 2026-07-28 | Peer-reviewed primary study | Linear algebra misconception examples | Direct | Narrow topic focus on matrices/determinants. |
| Evidence of probability misconception in engineering students about test concepts: The case of misconception of chance | M. Kaplar et al. | `https://link.springer.com/article/10.1186/s40594-021-00279-y` | DOI on article page | 2021 | 2026-07-28 | Peer-reviewed primary study | Probability misconception examples | Direct | Engineering-student sample; focuses on selected misconceptions. |

**Confidence-calibrated final verdict.** The evidence is strong enough to support a **local, evidence-first tutoring framework** and a **controlled text-dialogue pilot**. It does **not** justify a production claim that an AI tutor can reliably infer stable learner types, nor that ordinary dialogue alone can always identify the true source of explanation failure. The most defensible current position is narrower: adaptive explanation in foundational university mathematics should be **local, route-specific, evidence-tagged, contestable, self-correcting, and evaluated on independent learning**.

```yaml
final_disposition:
  - evidence_supports_controlled_text_pilot
  - evidence_supports_candidate_framework_but_not_intervention
  - mixed_evidence_requires_narrower_scope
confidence: moderate
```
