#!/usr/bin/env python3
"""Mechanical validator/filler for MNE V2-A A1 controller G2A template.

This tool does not authorize G2A. It extracts the exact inner payload template,
fills only the allowlisted G2A-time placeholders, and verifies byte-for-byte
that no other text changed.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Any

import yaml

BEGIN = "OWNER_G2A_PAYLOAD_TEMPLATE_BEGIN\n"
END = "\nOWNER_G2A_PAYLOAD_TEMPLATE_END"

ALLOWED = [
    "SOURCE_CONTROLLER_G2A_TEMPLATE_BLOB",
    "PROTECTED_MNEMOSYNE_MASTER_AT_G2A",
    "PROTECTED_META_AGENT_MASTER_AT_G2A",
    "CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL",
    "CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL",
    "ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL",
    "BETA_OWNER_AUTHORIZED_VISIBLE_LABEL",
    "EXECUTION_WINDOW_START_UTC",
]

WORKER_PLACEHOLDERS = [
    "__MNE_ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__",
    "__MNE_BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__",
]

HEX40 = re.compile(r"^[0-9a-f]{40}$")
ISO_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def fail(message: str) -> "NoReturn":
    print(f"BLOCKED: {message}", file=sys.stderr)
    raise SystemExit(2)


def load_text(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        fail(f"{path}: UTF-8 BOM is prohibited")
    if b"\r" in data:
        fail(f"{path}: CR/CRLF is prohibited; LF required")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path}: invalid UTF-8: {exc}")
    trailing = [i + 1 for i, line in enumerate(text.splitlines()) if line.endswith((" ", "\t"))]
    if trailing:
        fail(f"{path}: trailing spaces/tabs on lines {trailing[:10]}")
    return text


def extract_payload(template_text: str) -> str:
    if template_text.count(BEGIN) != 1 or template_text.count(END) != 1:
        fail("template must contain exactly one payload envelope")
    return template_text.split(BEGIN, 1)[1].split(END, 1)[0]


def load_values(path: Path) -> dict[str, str]:
    raw: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        fail("fill values must be a YAML mapping")
    extra = sorted(set(raw) - set(ALLOWED))
    missing = sorted(set(ALLOWED) - set(raw))
    if extra or missing:
        fail(f"fill key mismatch; extra={extra}, missing={missing}")
    values: dict[str, str] = {}
    for key in ALLOWED:
        value = raw[key]
        if not isinstance(value, str) or value == "":
            fail(f"{key}: non-empty string required")
        if "\r" in value or "\n" in value:
            fail(f"{key}: CR/LF forbidden")
        values[key] = value
    for key in [
        "SOURCE_CONTROLLER_G2A_TEMPLATE_BLOB",
        "PROTECTED_MNEMOSYNE_MASTER_AT_G2A",
        "PROTECTED_META_AGENT_MASTER_AT_G2A",
    ]:
        if not HEX40.fullmatch(values[key]):
            fail(f"{key}: exact lowercase 40-hex Git identity required")
    if not ISO_UTC.fullmatch(values["EXECUTION_WINDOW_START_UTC"]):
        fail("EXECUTION_WINDOW_START_UTC: require YYYY-MM-DDTHH:MM:SSZ")
    if values["CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL"] != values["CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL"]:
        fail("controller authorized/selected visible-label raw strings differ")
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--values", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    template_text = load_text(args.template)
    payload = extract_payload(template_text)
    values = load_values(args.values)

    expected = payload
    for key in ALLOWED:
        token = f"<{key}>"
        count = expected.count(token)
        if count == 0:
            fail(f"allowlisted placeholder absent: {token}")
        expected = expected.replace(token, values[key])

    unresolved_allowed = [f"<{key}>" for key in ALLOWED if f"<{key}>" in expected]
    if unresolved_allowed:
        fail(f"unresolved G2A-time placeholders: {unresolved_allowed}")

    wrapper_blocks = re.findall(
        r"MNE_A1_RUNTIME_WRAPPER_V1_BEGIN\n.*?MNE_A1_RUNTIME_WRAPPER_V1_END\n",
        expected,
        flags=re.DOTALL,
    )
    if len(wrapper_blocks) != 2:
        fail(f"expected exactly two canonical wrapper blocks, found {len(wrapper_blocks)}")
    for token, block in zip(WORKER_PLACEHOLDERS, wrapper_blocks, strict=True):
        if block.count(token) != 1:
            fail(f"role worker-launch placeholder must remain exactly once in its canonical block: {token}")
    if WORKER_PLACEHOLDERS[1] in wrapper_blocks[0] or WORKER_PLACEHOLDERS[0] in wrapper_blocks[1]:
        fail("worker-launch placeholders appear in the wrong role block")

    if "G2A_authorized: false" in expected or "NON_AUTHORIZING_TEMPLATE" in expected:
        fail("self-negating non-authorization text leaked into issueable payload")
    if "Owner_G2A_authorized: true" not in expected:
        fail("authority-bearing payload marker missing")

    args.output.write_bytes(expected.encode("utf-8"))
    reread = load_text(args.output)
    if reread != expected:
        fail("output reread differs from mechanically reconstructed payload")

    print("PASS")
    print(f"bytes: {len(expected.encode('utf-8'))}")
    print(f"sha256: {hashlib.sha256(expected.encode('utf-8')).hexdigest()}")
    print("G2A_issued: false  # generating/validating a file is not the Owner sending it")


if __name__ == "__main__":
    main()
