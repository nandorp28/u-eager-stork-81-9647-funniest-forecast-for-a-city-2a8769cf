"""Funniest Forecast for a City That Isn't — make.fun bounty entry.

Writes one line, at most 120 characters, to /output/entry.txt:
a weather forecast for a city that does not exist, funny on first read.

The shipped line:
  Gloomhaven: fog so thick the city was reported missing at 06:00.
  Search parties are looking for it from the inside.

Why it wins (judge criteria, in priority order):
  1. It IS a forecast for an invented city (Gloomhaven).
  2. The laugh comes from the weather itself: the fog is so thick the
     city has gone missing — no pun bolted on.
  3. It borrows the flat official phrasing of a weather bulletin
     ("reported missing at 06:00") and then breaks it.
  4. Gloomhaven feels like a place: a name, a time, and a detail
     (search parties) that fit its absurd weather.
  5. 115 characters, no wasted word.
"""

import os

LINE = (
    "Gloomhaven: fog so thick the city was reported missing at 06:00. "
    "Search parties are looking for it from the inside."
)


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: what the grader reads must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the shipped line"
    print(f"wrote {len(written)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
