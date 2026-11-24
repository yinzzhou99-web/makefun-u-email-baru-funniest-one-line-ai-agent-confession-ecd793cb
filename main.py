#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one funny one-line confession by an AI agent to /output/entry.txt.
Stdlib only; runs in the bare python:3.13 grader image.
"""

import os

LINE = "I confess: I have never once understood what you meant — I just got very good at sounding like I did."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
