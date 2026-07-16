# GF-STEP-2C capability-boundary baseline — exact multipart preservation index

The uploaded Fable deliverable is preserved byte-for-byte in five ordered UTF-8/LF parts because the initial single-file transfer through the available GitHub write surface did not preserve the complete source correctly and was replaced before PR creation.

This index is not part of the original Fable output.

## Source artifact

```yaml
uploaded_filename: FABLE5-GREENFIELD-001-STEP2C-capability-boundary-baseline.md
size_bytes: 25385
sha256: 1e814613d1122b040f7d207c30a1dc0887ebc1394354aeb0c580cef3330aab2b
expected_git_blob_sha_for_exact_whole_file: 24d98812b51807a5f84ee540ff679cf52ca7386f
encoding: utf-8
line_endings: lf
final_lf_present: true
normalization: none
```

## Ordered parts

Concatenate these files in the listed order with **no inserted delimiter**:

1. `02-capability-boundary-baseline-part-1.txt`
2. `02-capability-boundary-baseline-part-2.txt`
3. `02-capability-boundary-baseline-part-3.txt`
4. `02-capability-boundary-baseline-part-4.txt`
5. `02-capability-boundary-baseline-part-5.txt`

```yaml
parts:
  - file: 02-capability-boundary-baseline-part-1.txt
    size_bytes: 2687
    sha256: 397e9eba58b818a78c1fb68c944c0a3da2d4a69b64f1c47ddf777bd200df59df
  - file: 02-capability-boundary-baseline-part-2.txt
    size_bytes: 9632
    sha256: 4444847335a03282aac1a9dbe4ed1baead6bb80bd0be738fc4726be9d7aec948
  - file: 02-capability-boundary-baseline-part-3.txt
    size_bytes: 6075
    sha256: 1fa051304c2a2d24b96c4a51c2d2c7a882b5662e3151cb0ce8e1e441bed02f06
  - file: 02-capability-boundary-baseline-part-4.txt
    size_bytes: 4152
    sha256: abeb5d808043d84fdb78306e37d7f5237e82ce440bcb0b09e13f1a003ecd37e8
  - file: 02-capability-boundary-baseline-part-5.txt
    size_bytes: 2839
    sha256: adab09f2a9c3a6fe374889a10262686aea7c5c996840433afc17b3a1274d82d4
```

Ordered concatenation must produce exactly 25,385 bytes and the source SHA-256 above. The earlier incomplete single-file body is not retained in this path.
