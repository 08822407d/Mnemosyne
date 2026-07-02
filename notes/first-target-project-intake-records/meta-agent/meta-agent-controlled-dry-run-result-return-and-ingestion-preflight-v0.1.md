# Meta-Agent Controlled Dry-Run Result Return and Ingestion Preflight v0.1

## Positioning

- Non-execution-source note for handling the later dry-run result.
- Does not execute the dry-run.
- Does not approve repository ingestion by itself.

## Expected returned file

```text
META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md
```

## Maintainer handling

After the dry-run conversation returns the result:

1. Upload the result file to the current Mnemosyne maintainer conversation.
2. Review whether it includes required metadata and no-write evidence.
3. Do not stage it in `manual-import-inbox/` until maintainer review says it is safe.
4. If safe and complete, generate a later Codex task to ingest it as a non-execution-source dry-run result/evidence record.
5. If incomplete or unsafe, request a corrected result or mark the dry-run result blocked/failed.

## Minimum pre-ingestion checks

```yaml
minimum_pre_ingestion_checks:
  full_body_present:
  dry_run_id_matches:
  repo_write_performed_false:
  target_workspace_created_false:
  notes_target_project_dry_runs_created_false:
  target_materials_ingested_false:
  target_repository_written_false:
  mnemosyne_execution_source_modified_false:
  no_write_evidence_statement_present:
  contains_secrets_or_credentials:
  contains_private_source:
  contains_personal_or_confidential_data:
  contains_raw_target_materials:
  safe_for_repo_visibility:
```
