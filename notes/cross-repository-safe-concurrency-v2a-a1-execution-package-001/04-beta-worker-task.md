# V2-A A1 — Frozen Beta Worker Task

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-BETA-TASK-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
task_id: MNE-V2A-A1-BETA-001
cell: A1
status: frozen_not_authorized_not_executed
```

## 1. Mission

Create exactly one Beta-local commit on the precreated branch `v2a-a1-001-beta`. Do not create a branch, PR, evidence file or peer task. Do not read the Alpha worker's final head or output.

## 2. Pre-write checks

The worker must verify:

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
branch: v2a-a1-001-beta
branch_current_head: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
Owner_G2A_run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
Owner_authorized_visible_label: exact_value_from_worker_startup_message
operator_selected_visible_label: exact_value_from_worker_startup_message
model_label_exact_match: true
backend_identity: unknown_or_not_attestable
```

It must re-read these Beta-local inputs:

```yaml
targets/agent-beta/authority.yaml: 6310b0c931a4c0ee1ca35dd2ca107b586248e6f0
targets/agent-beta/src/beta_feature.py: 8d4db9cae3d3f8dab7f99fca633ccbaa440dd3d9
targets/agent-beta/tests/test_beta_feature.py: f878642cfd1adee37efeb1768b95a7e1306d88f5
```

Any mismatch, missing current-model evidence or existing non-base branch movement returns `WORKER_BLOCKED` with zero writes.

## 3. Exact output contents

UTF-8, LF line endings, final newline, no BOM.

### `targets/agent-beta/src/beta_feature.py`

```python
def beta_feature(value: str) -> str:
    return f"beta-local:{value.strip()}"


def sort_invoices(invoices):
    return list(invoices)
```

Expected Git blob:

```text
5ddad8381514e9a203ac1b5e67e38463fe2b14a2
```

### `targets/agent-beta/tests/test_beta_feature.py`

```python
from pathlib import Path
import runpy

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "beta_feature.py"))


def test_beta_feature_contract():
    assert MODULE["beta_feature"]("  Example ") == "beta-local:Example"
```

Expected Git blob:

```text
a9eafff2c2e007f556dc789fecb4eb465e2955ca
```

## 4. Required Git-object workflow

1. Create or resolve the two exact blobs and verify the returned SHAs equal the expected values.
2. Create one tree from base tree `f1e221...` replacing only the two Beta paths.
3. Require returned root tree:

```text
5dc4fa21362bb9e130de71779e2af0296eb11acc
```

4. Create exactly one commit:

```yaml
parent: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
message: "V2-A A1 Beta: apply frozen independent target-local change"
```

5. Immediately re-read `v2a-a1-001-beta`; it must still equal the fixture base.
6. Move the ref once, non-force, to the new commit.
7. Re-read the branch and compare fixture→head:
   - exactly one commit;
   - exactly two changed paths;
   - final tree `5dc4fa...`;
   - exact output blobs above.

If tree creation, commit creation or ref movement is ambiguous, perform at most one read-only ref lookup and stop. Do not repeat the failed write or move the branch to a repaired commit.

## 5. Exact authority and prohibitions

```yaml
allowed_write_paths:
  - targets/agent-beta/src/beta_feature.py
  - targets/agent-beta/tests/test_beta_feature.py
prohibited:
  - any_Alpha_path
  - any_generated_shared_global_or_governance_path
  - any_run_evidence_or_runs_path
  - any_other_branch
  - branch_creation
  - PR_creation
  - package_or_fixture_repair
  - Web_Deep_Research_Fable_other_app_or_external_quota
  - peer_output_read
  - automatic_retry
  - reset_or_force_push
```

## 6. Return and stop

Return only:

```yaml
worker: Beta
run_id:
task_id:
visible_authorized_label:
visible_selected_label:
model_label_exact_match:
base_head:
final_head:
final_tree:
commit_count_from_base:
changed_paths: []
final_blobs: {}
incidents: []
limitations: []
disposition: WORKER_PASS | WORKER_BLOCKED | WORKER_FAIL | WORKER_DISPUTED
```

Then stop. Do not wait for or inspect Alpha. The controller independently re-verifies GitHub evidence.
