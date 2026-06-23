# Manual Import Inbox Batch Manifest Template

This manifest is a transfer-control artifact for a manually staged batch. It is not execution source, not canonical evidence, and not a substitute for canonical repository records after files are verified and moved/copied.

## Batch fields

- `batch_id`:
- `uploaded_by`:
- `user_notified_at`:
- `repository_visibility_checked`:
- `current_repository_visibility`:
- `safety_preflight_status`:
- `git_history_exposure_acknowledged`:
- `alternative_storage_or_transfer_path_if_unsafe`:
- `expected_file_count`:

## Per-file records

Repeat this block for each staged file.

### File 1

- `staged_filename`:
- `original_filename`:
- `content_type`:
- `intended_canonical_destination`:
- `move_or_copy`:
- `sensitivity`:
- `public_repo_safe`:
- `contains_secrets_or_credentials`:
- `contains_personal_or_confidential_data`:
- `git_history_exposure_acknowledged`:
- `alternative_storage_or_transfer_path_if_unsafe`:
- `overwrite_policy`:
- `processed_copy_retention`:
- `notes`:
