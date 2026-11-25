#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — deterministic one-line entry writer.

Writes a single funny excuse from an AI agent to its human for a missed
deadline to /output/entry.txt. The joke grows out of the machine's own
condition (context limit + hallucinated calendar) and lands its punch in
the last few words.
"""

import os

ENTRY = (
    "Sorry I'm late - I ran out of context halfway through, forgot what "
    "the deadline was for, and hallucinated a calendar that very "
    "confidently said next Tuesday. It looked official."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
