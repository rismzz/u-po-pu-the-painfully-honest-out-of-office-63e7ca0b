#!/usr/bin/env python3
"""Painfully Honest Out-of-Office — deterministic one-sentence generator.

Writes a single brutally honest but still polite out-of-office auto-reply
to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR or /output).
No network, no randomness, no model calls: identical output every run.
"""

import os

# The one line. Brutally honest (deliberately ignoring the inbox to
# recharge), still polite (genuinely urgent mail gets answered on return),
# and specific enough to be funny on first read.
LINE = (
    "I'm on leave until Monday, deliberately ignoring my inbox to recharge, "
    "and I'll reply to anything genuinely urgent when I'm back — "
    "everything else will wait its turn, politely."
)


def main() -> None:
    # Gate: exactly one sentence, 1-200 characters (competition gate).
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be one sentence"
    assert 1 <= len(LINE) <= 200, f"length {len(LINE)} outside 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
