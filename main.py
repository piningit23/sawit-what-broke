#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest, funny error copy.

Writes a single-line software error message (<=200 chars) to
/output/entry.txt. It names the real failure (the server ran out of
memory mid-save and lost the work), tells the user what to do next
(hit retry), and keeps the joke to one line a team could ship.
"""

import os

ENTRY = (
    "Our server ran out of memory mid-save and dropped your work "
    "like a hot potato. Nothing was backed up \u2014 hit retry while "
    "it still remembers your name."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
