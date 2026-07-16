# GF-STEP-2C prompt-as-sent — exact multipart preservation index

The complete Fable task prompt generated in the designated long result-receiver conversation is preserved byte-for-byte in five ordered UTF-8/LF parts.

This index is not part of the original prompt.

## Source prompt artifact

```yaml
source_filename: FABLE5-GREENFIELD-001-GF-STEP-2C-task.md
size_bytes: 28649
sha256: 5eecff2b9a4b421bcd8e4f7929c401cabe8fdf7efcc44aa2b8bc45e962422472
expected_git_blob_sha_for_exact_whole_file: e1b9f6a0dd09ac61514a1a4d2aa3317332e19a31
encoding: utf-8
line_endings: lf
final_lf_present: true
normalization: none
```

## Ordered parts

Concatenate these files in the listed order with **no inserted delimiter**:

1. `00-prompt-as-sent-part-1.txt`
2. `00-prompt-as-sent-part-2.txt`
3. `00-prompt-as-sent-part-3.txt`
4. `00-prompt-as-sent-part-4.txt`
5. `00-prompt-as-sent-part-5.txt`

```yaml
parts:
  - file: 00-prompt-as-sent-part-1.txt
    size_bytes: 6672
    sha256: 8472beaa5b296d89824304f72b703c8769fc8a4b72d321b5d487da3283da4e17
    git_blob_sha: c721de6b6496d490cce739668bae463ca98da14f
  - file: 00-prompt-as-sent-part-2.txt
    size_bytes: 6068
    sha256: 924a6bcf9e500eb77f1f0f752593c600009e2d102a75dcf2160f93c7a545c2ad
    git_blob_sha: 4c7b59b22cfcc6d07e97befe871bdaff616cbec8
  - file: 00-prompt-as-sent-part-3.txt
    size_bytes: 4437
    sha256: 976a052e294481b61b940043bc9a0c85025819f49ba1de868170af35530aabdd
    git_blob_sha: 50022641fdc3fe7e46c3f401fd4ac7b8313988c7
  - file: 00-prompt-as-sent-part-4.txt
    size_bytes: 5794
    sha256: 437783d61b3abdb922063c1056ed5f5ab6675295d5405348129c43cef91e5f76
    git_blob_sha: f5620d18b2e886c21f9f837beb98705ddaec0894
  - file: 00-prompt-as-sent-part-5.txt
    size_bytes: 5678
    sha256: 7f269838447636183a905eae3349893c1e5ba047f2002dbdd5fb9960e4593028
    git_blob_sha: 50d1b4432ad298832a90056f9c57ac39dcbe33f4
```

Ordered concatenation produces exactly 28,649 bytes and the source SHA-256 above.
