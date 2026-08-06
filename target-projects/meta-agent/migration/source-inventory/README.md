# Meta-Agent source inventory v0.1

This directory is the mechanical E0 inventory of `target-projects/meta-agent/`
at the pinned source commit. It is evidence for later frontier mapping, not an
authority decision or final migration disposition. It performs no destination
initialization, shadow copy, or cutover.

Regenerate with:

```bash
python3 generate-source-inventory.py \
  --source-commit 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb \
  --source-root target-projects/meta-agent/ \
  --output-dir /tmp/meta-agent-source-inventory
```

The closure receipt binds the recursive Git stream to each canonical manifest.
The front-matter parser intentionally extracts only selected top-level scalars;
all classifications remain preliminary and non-authoritative.
