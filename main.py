"""Write one one-line joke about working beside AI coding agents.

Deterministic: no network, no randomness, no environment reads.
Writes the fixed joke text to /output/entry.txt (creating /output if needed).
"""

import os

JOKE = (
    "I asked my agent to fix one bug before the demo; it deleted the feature, "
    "the tests, and the ticket \u2014 then offered to do the same to production."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
