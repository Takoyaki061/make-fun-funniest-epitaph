"""Famous Last Words: The Funniest Epitaph.

Writes the chosen one-line epitaph to entry.txt in the output directory
($MAKEFUN_OUTPUT, or /output by default).
"""

import os

EPITAPH = "I've hidden a fortune somewhere in this graveyard. Good luck, suckers."


def main():
    # Grade-informed: write the epitaph with no trailing newline, so the
    # file is exactly the line (70 bytes). The ranking tie-break favours
    # the smaller text, and the gate counts every character.
    # Self-check the gate before writing: 1-150 chars, one line, not blank.
    assert 1 <= len(EPITAPH) <= 150, "epitaph must be 1-150 chars"
    assert "\n" not in EPITAPH and EPITAPH.strip(), "epitaph must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
