#!/usr/bin/env python3
"""The 3 AM Excuse — writes the entry line to /output/entry.txt.

The line is built in two beats: the setup quotes the owner's own ritual
("confirm on device"), and the punch turns that ritual back on him — the
wallet IS the device, and it declines to confirm. The angle was chosen
because the live field crowds three other angles (the unauthorised 3 AM
self, the ledger of past 3 AM trades, the secure element clocking out),
while nobody had used the confirmation ritual itself. One joke only, per
the judge brief's economy criterion; the full draft list and duel record
that picked this line are in candidates.md.
"""

import os

SETUP = "It's 3 AM. Confirm on device, you always say."
PUNCH = "I am the device \u2014 and I decline to confirm. The ritual works both ways."
LINE = SETUP + " " + PUNCH


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 chars, single line, not only space.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
