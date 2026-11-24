#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest, funny error copy.

The program writes a single-line software error message to
/output/entry.txt. The line names the real failure in plain words —
the server ran out of memory in the middle of a save and lost the
user's work — says what to do next (hit retry), and lands the joke
in one breath so a team could ship it in a real error dialog.
"""

import os
import sys

ENTRY = (
    "Our server ran out of memory mid-save and dropped your work "
    "like a hot potato. Nothing was backed up, so hit retry before "
    "it forgets your name too."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """A valid entry is one non-blank line of 1-200 characters."""
    if not text or text != text.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main():
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}: {text}")


if __name__ == "__main__":
    sys.exit(main())
