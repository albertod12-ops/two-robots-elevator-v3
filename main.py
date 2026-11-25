#!/usr/bin/env python3
"""Two Robots in an Elevator (make.fun) - v3.

Writes one line of awkward robot small talk to /output/entry.txt.
The line is a fixed string: deterministic by construction, byte-identical
on every run.
"""
import os

# The entry is one fixed line of robot small talk; the output is deterministic.
TEXT = "I picked up the emergency phone to practise talking to you. It called the fire department."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
