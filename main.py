"""solmara-funniest-office: one-line office joke for make.fun.

The entry is a single joke about office life, held in the JOKE constant.
Running this module prints the joke and writes it to /output/entry.txt,
the file the bounty gate reads. The gate requires UTF-8 text of 1 to
200 characters that is not only white space, so the joke is validated
against those bounds before anything is written.
"""

from __future__ import annotations

import sys
from pathlib import Path

JOKE = (
    "I told my boss the meeting could have been an email \u2014 "
    "so now he emails me the meeting invite, "
    "then calls a meeting to discuss the email."
)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Check the entry against the bounty gate's rules."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")


def main() -> int:
    validate(JOKE)
    print(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
