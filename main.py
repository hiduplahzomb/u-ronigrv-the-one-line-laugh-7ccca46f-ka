"""The One-Line Laugh — one funny line about a landlord, a lift, and a ground-floor flat.

The entry is a building notice, not a ledger: the paradox lands in the
first words (ground-floor flat, elevator access), the middle twists the
knife (stairs sold separately — the thing you actually use is the add-on),
and the punchline is the billing itself: a lift fee due in full for
zero rides taken, with zero refunds given — you pay for the lift
precisely because you never use it. No amounts, no IDs, no status
stamp — a notice stays in effect, and so does the invoice.
"""

import os
import sys

TEXT = "NOTICE: your ground-floor flat now includes elevator access — stairs sold separately. Lift fee due in full: 0 rides taken, 0 refunds given."
# Notice framing: ground floor + elevator access up front, stairs sold
# separately, and the punchline is the billing — a fee due in full for
# zero rides, zero refunds.


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
