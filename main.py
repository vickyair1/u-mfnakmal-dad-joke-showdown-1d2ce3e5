#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Prints one original dad joke to stdout, deterministically: no randomness,
no network, no input — the same bytes on every run.
"""

import sys

JOKE = "I told my wife she should embrace her mistakes. She hugged me."

# The competition gate: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Enforce the same bound here so a bad edit fails
# loudly instead of shipping an invalid entry.
assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke violates the 200-char gate"


def main() -> None:
    sys.stdout.write(JOKE + "\n")


if __name__ == "__main__":
    main()
