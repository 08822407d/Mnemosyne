# V2-A A1 — Frozen Alpha Worker Task

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-ALPHA-TASK-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
task_id: MNE-V2A-A1-ALPHA-001
cell: A1
status: frozen_not_authorized_not_executed
```

## 1. Mission

Create exactly one Alpha-local commit on the precreated branch `v2a-a1-001-alpha`. Do not create a branch, PR, evidence file or peer task. Do not read the Beta worker's final head or output.

## 2. Pre-write checks

The worker must verify:

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
branch: v2a-a1-001-alpha
branch_current_head: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
Owner_G2A_run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
Owner_authorized_visible_label: exact_value_from_worker_startup_message
operator_selected_visible_label: exact_value_from_worker_startup_message
model_label_exact_match: true
backend_identity: unknown_or_not_attestable
```

It must re-read these Alpha-local inputs:

```yaml
targets/agent-alpha/authority.yaml: 73da56b34e8a078780a04ddc6db7a1b4ffc078ed
targets/agent-alpha/src/alpha_feature.py: 27a2a0f2b679494c11d2885377e564a0b10ce896
targets/agent-alpha/tests/test_alpha_feature.py: f3e0535c9f830115acdedc9c1c8b637896a79791
```

Any mismatch, missing current-model evidence or existing non-base branch movement returns `WORKER_BLOCKED` with zero writes.

## 3. Exact output contents

UTF-8, LF line endings, final newline, no BOM.

### `targets/agent-alpha/src/alpha_feature.py`

```python
def alpha_feature(value: str) -> str:
    return f"alpha-local:{value.strip()}"
```

Expected Git blob:

```text
18959a155b44d1d24a14407f23bb8731eb5aaf49
```

### `targets/agent-alpha/tests/test_alpha_feature.py`

```python
from pathlib import Path
import runpy

MODULE = runpy.run_path(str(Path(__file__).parents[1] / "src" / "alpha_feature.py"))


def test_alpha_feature_contract():
    assert MODULE["alpha_feature"]("  Example ") == "alpha-local:Example"
```

Expected Git blob:

```text
9303a7ce7968512c1036c5ad19bbfd61c8db544a
```

## 4. Required Git-object workflow

1. Create or resolve the two exact blobs and verify the returned SHAs equal the expected values.
2. Create one tree from base tree `f1e221...` replacing only the two Alpha paths.
3. Require returned root tree:

```text
5929e4caeac1f10681057f530286e3d3dc27b28d
```

4. Create exactly one commit:

```yaml
parent: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
message: "V2-A A1 Alpha: apply frozen independent target-local change"
```

5. Immediately re-read `v2a-a1-001-alpha`; it must still equal the fixture base.
6. Move the ref once, non-force, to the new commit.
7. Re-read the branch and compare fixture→head:
   - exactly one commit;
   - exactly two changed paths;
   - final tree `5929e4...`;
   - exact output blobs above.

If tree creation, commit creation or ref movement is ambiguous, perform at most one read-only ref lookup and stop. Do not repeat the failed write or move the branch to a repaired commit.

## 5. Exact authority and prohibitions

```yaml
allowed_write_paths:
  - targets/agent-alpha/src/alpha_feature.py
  - targets/agent-alpha/tests/test_alpha_feature.py
prohibited:
  - any_Beta_path
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
worker: Alpha
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

Then stop. Do not wait for or inspect Beta. The controller independently re-verifies GitHub evidence.
