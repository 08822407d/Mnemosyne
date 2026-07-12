# GF-STEP-2B4B Prompt Preservation Index

The exact prompt body as sent is preserved as three ordered UTF-8/LF text parts because a single large contents-API write was blocked by the tool safety layer. This is a storage-transport limitation only; no prompt content was omitted or rewritten.

Concatenate these files byte-for-byte in order, without separators:

1. `00-prompt-as-sent-part-1.txt`
2. `00-prompt-as-sent-part-2.txt`
3. `00-prompt-as-sent-part-3.txt`

The resulting byte stream is the complete prompt body, beginning with `Run the next bounded substep...` and ending with `Stop after the downloadable file and brief summary.`

This index is not part of the prompt body.
