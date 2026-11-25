#!/usr/bin/env python3
"""One Star, Written in Sap — entry program.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The review: a fern complains that its owner waters it with ice cubes,
calls it "low maintenance", then gasps when it drops a leaf — as if the
leaf fell on purpose. The joke turns on one absurd, specific detail
(ice cubes on a tropical fern) and closes with a review-site sign-off
— "would not photosynthesise here again" — so it reads as a genuine
one-star review rather than a cute plant caption.

Gate: the text must be 1-279 characters, one line, UTF-8, not only
whitespace. This program asserts that before writing.
"""

import os

REVIEW = (
    "One star. She waters me with ice cubes, calls me 'low maintenance,' "
    "then gasps when I drop a leaf like I did it on purpose. I am a "
    "fern, not a cryotherapy clinic \u2014 would not photosynthesise "
    "here again."
)

MAX_CHARS = 279

# Stock phrases the judge brief explicitly penalises: never let one slip
# into the entry (drama-queen / dramatic-wilting / being-ignored tropes).
BANNED_PHRASES = ("drama queen", "dramatic", "wilting", "ignored")


def validate(text: str) -> str:
    """Enforce the gate and the judge brief's freshness rule."""
    text = text.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    lowered = text.lower()
    for phrase in BANNED_PHRASES:
        assert phrase not in lowered, f"banned stock phrase: {phrase}"
    return text


def main() -> None:
    text = validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
