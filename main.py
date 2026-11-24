"""Dad Joke Showdown resubmit: one original dad joke.

Writes exactly one line to /output/entry.txt (no trailing newline)
and prints the same line to stdout. Deterministic, stdlib only.
"""

LINE = "My dad renamed our Wi-Fi '404 Not Found' so guests would stop asking for the password. Now the neighbours think we moved out."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
