"""Cat voicemail greeting entry.

Writes one funny voicemail greeting, recorded by a cat, to
/output/entry.txt. Deterministic: no clock, no randomness, no network,
standard library only.
"""

import os

PART1 = "You've reached Miso. I'm napping in the box you threw away. "
PART2 = "Leave a message after the beep \u2014 dinner is still at four."


def main():
    text = PART1 + PART2
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
