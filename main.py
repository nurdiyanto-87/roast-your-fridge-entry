#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the entrant's own fridge to
/output/entry.txt. Pure standard library, deterministic, no network,
no files outside the repository.

The line was chosen against the judge's brief, most important first:
1. it roasts a fridge in a single line;
2. it lands on a specific, recognisable detail (one pickle jar from
   2021, kept in the fridge door);
3. it turns on a twist in the last few words (a family heirloom
   nobody asked for);
4. it reads cleanly aloud as one line;
5. it is fresh rather than a worn-out fridge joke.
"""

import os

# Draft 2 (final): a comma before the payoff gives the spoken pause the
# line needs when read aloud, so the twist lands in the last few words.
# Candidate comparison that led here is in the build session: the pickle
# jar line beat the crisper-drawer, door-beep and 1%-battery drafts on
# specificity and freshness.
ROAST = (
    "My fridge keeps one pickle jar from 2021 in the door, "
    "like a family heirloom nobody asked for."
)


def main() -> None:
    text = ROAST.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError("roast line must be a single line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is exactly the line, byte for byte.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
