# MNEMOSYNE-032 Risk, Gap, and Open Question Log

Status: MNEMOSYNE-032 dry-run artifact; not execution source; pending independent verification.

## Risks
- Authority drift: evidence, review records, active context, or handoff could be mistaken for execution source.
- Over-claiming capability: current models may not reliably follow layered memory rules without diff checks.
- PDF evidence gap: visual/table/layout evidence in six PDF reports is still pending manual review.
- Missing prompt gap: six light research original prompts are missing and cannot be reconstructed.
- Automation temptation: auto-index/writeback/RAG/MCP/GitHub Actions are attractive but out of v0.1/v0.2 current authority.
- Privacy/retention: raw preservation can conflict with sensitive data handling.

## Gaps
- No formal privacy/redaction/access-control policy for raw originals.
- No validated software-test-like memory-system evaluation method.
- No concrete file-level permission policy for ordinary target-project Agents.
- No finalized minimal/standard/rich target memory schemas.
- No research refresh cadence or capability-version naming rule.

## Outdated or weak assumptions
| source | assumption | risk | possible modern alternative | research_refresh_needed |
|---|---|---|---|---|
| user restatement | GitHub/Markdown remains the best substrate. | May become too Markdown/GitHub-centric. | Abstract backend layer; compare repos, databases, vector stores, managed memory products. | yes |
| user restatement | Manual files can organize all useful memory. | Large systems may need indexing/retrieval. | Human-approved automated indexing prototype in later task. | yes |
| user restatement | Memory debugging can resemble software testing. | AI memory behavior may be non-deterministic. | Eval harness, scenario tests, trace replay, observational checks. | yes/deep |
| user restatement | Ordinary Agents can respect permission boundaries. | Agents may over-edit or misread authority. | Explicit permissions, protected-file checks, task result records. | dry-run validation |
| current evidence | Codex/GitHub workflow is enough for now. | Platform capabilities and limitations change. | Periodic capability boundary refresh. | yes |

## Research refresh needs
- Current state of ChatGPT/Claude/Codex/Cursor memory and repository-write capabilities.
- AI evaluation patterns for persistent-memory systems and multi-Agent continuity.
- Privacy-aware raw-record storage and redaction practices.
- Practical alternatives to Markdown/GitHub for durable, auditable AI memory.

## Open questions
- What exact approval form promotes candidate material into execution source?
- Which PDF figures/tables should be manually reviewed first?
- Can memory-system testing/debugging be reliable enough for current models?
- Should target projects have a memory-system issue log?
- What is the minimum index format and refresh cadence?
- Which first real scenario should follow this self-validation dry-run?

## Possible next actions
1. Independent verification of this dry-run.
2. PDF figure/table/image review for RPT-2026Q2-0002 through 0007.
3. Research refresh on memory-system testing/debugging and modern platform capabilities.
4. Candidate cleanup for restatement-derived requirements.
5. User review of template packs before any real target delivery.
