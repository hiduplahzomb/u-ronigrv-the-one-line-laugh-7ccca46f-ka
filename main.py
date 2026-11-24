"""The One-Line Laugh — one funny line about a landlord, a lift, and a ground-floor flat.

The entry is a rent-ledger line item, not a sentence: the fields carry the
joke. Unit 101 sits on floor 0, is billed $42/mo elevator maintenance,
pays +$85/mo rent, and has taken 0 elevator trips — closed with STATUS: PAID.
No conjunctions, no explanation; the conflicting data points are the irony —
floor 0, elevator fee, 0 trips, rent up, paid anyway.
"""

import os
import sys

TEXT = "LEDGER #4471: unit 101, floor 0 — elevator maintenance $42/mo, rent +$85/mo, elevator trips: 0. STATUS: PAID."
# Ledger fields only: floor 0, elevator fee $42, trips 0, rent +$85, PAID.
# The contradiction between the fields is the joke — no sentence explains it.


def main() -> int:
    text = TEXT
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        print(f"gate failed: entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "rb") as f:
        if f.read() != encoded:
            print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
            return 1
    print(f"wrote {path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
