#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single warning label (101 chars, within the 1-120 gate)
to /output/entry.txt.
Stdlib only; deterministic; never touches anything outside the
output directory, and never removes the output directory itself.
"""

import os

LABEL = (
    "WARNING: Do not meet yourself. If you must, do not lend "
    "yourself money \u2014 you never pay yourself back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LABEL
    if not 1 <= len(text) <= 120:
        raise ValueError("label must be 1-120 characters, got %d" % len(text))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
