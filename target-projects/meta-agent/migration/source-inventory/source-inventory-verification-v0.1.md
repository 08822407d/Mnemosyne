# Source inventory verification v0.1

## Scope and conclusion

Two independent, NUL-delimited recursive `git ls-tree` invocations at source
commit `8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb` were byte-identical. Every
recorded Git object was verified with `git cat-file -e`, and every blob was read
with `git cat-file blob`. The root subtree is
`4c1cd341777d46b3d6794abc62682e9c915ec46a`.

The parsed closure contains 45 trees, 226 blobs, and zero commit entries. The
raw recursive stream includes one Git-emitted pathspec ancestor tree
(`target-projects`); it is framing outside the pinned source subtree and is not
included in the subtree manifests.

## Reproducibility

The standard-library-only generator was run twice into separate empty temporary
directories. The closure and all three JSONL manifests were byte-identical.
No timestamps occur in deterministic outputs.

## Interpretation limits

Path-rule classification, status/history hints, and scalar front-matter
extraction are mechanical inputs to later frontier review. They are not final
migration dispositions. No destination repository write, live-navigation
change, target-truth change, initialization, shadow copy, or cutover occurred.
