#!/usr/bin/env python3
"""One letter for the whole day: Z.

The bounty asks for exactly one character, A to Z, standing
for the word that describes the sender's day. This entry
sends Z -- the word behind it is "zombie". After a night
of nonstop work, half-awake and running on nothing, the
day is a zombie day: shambling, slow, and still going.
Z is the sharpest initial for it -- an uncommon letter for
an unmistakable picture -- and it lands at once, funny
because it is true.

The program checks the gate (exactly one ASCII letter,
A to Z) and writes the letter to /output/entry.txt.
"""

import string
from pathlib import Path

DESTINATION = Path("/output/entry.txt")

# Z for "zombie": the day after a night with zero sleep.
LETTER = "Z"
WORD_BEHIND_IT = "zombie"


def main():
    if len(LETTER) != 1 or LETTER not in string.ascii_uppercase:
        raise SystemExit("entry must be exactly one letter, A to Z")
    if LETTER != WORD_BEHIND_IT[0].upper():
        raise SystemExit("the letter must be the hidden word's initial")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
