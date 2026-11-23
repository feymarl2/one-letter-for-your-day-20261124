#!/usr/bin/env python3
"""One Letter for Your Day — entry: the single letter F.

F stands for the word behind the day: Friday-feeling — the day carried a
Friday feeling, loose and fast and a little fried, the week's work landing
at once. The program writes exactly one character to /output/entry.txt.
Determinism: a single fixed constant, no clock, no randomness, no
environment reads, no network — the same byte on every run, under any
seed, locale, or timezone.
"""
import os

LETTER = "F"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
