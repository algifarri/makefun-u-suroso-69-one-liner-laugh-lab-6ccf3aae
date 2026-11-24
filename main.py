#!/usr/bin/env python3
"""One-Liner Laugh Lab entry for make.fun.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. The joke is deadpan detective
wordplay -- the vacuum ran a background check on the sock, and the
punchline turns on "holes": holes in a sock, and holes in a story.
One line, no trailing newline, so the judge reads exactly the joke.
Deterministic, standard library only.
"""

import os

LINE = "I ran a background check on the sock. No alibi, two holes in its story."


def main():
    # The gate allows 1-200 characters; the line is 71, and it is
    # written exactly, with no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
