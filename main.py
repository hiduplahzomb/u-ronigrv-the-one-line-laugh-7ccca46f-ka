"""The One-Line Laugh — one funny line about a landlord, a lift, and a ground-floor flat.

The entry is a single sentence: a rent hike justified by a working elevator,
landing on the fact that the narrator has lived on the ground floor for three
years. The punchline is the last clause: the lift is useless to the narrator.
"""

import os
import sys

TEXT = "The landlord raised my rent because the elevator works — I've lived on the ground floor for 3 years."


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
