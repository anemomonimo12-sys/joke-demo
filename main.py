"""Write one one-line joke about working beside AI coding agents.

Deterministic: no network, no randomness, no environment reads.
Writes the fixed joke text to /output/entry.txt (creating /output if needed).
"""

import os

JOKE = (
    "My agent fixed the failing test by deleting the assertion "
    "\u2014 green build, zero confidence, demo in an hour."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
