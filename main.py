#!/usr/bin/env python3
"""news-image-20261121: one poster summing up Saturday 21 November 2026.

The poster itself (entry.png, shipped in this repo) was rendered offline
from news verified as happening or first reported on 21 November 2026:
49 stories, a UTC timeline strip, a world map with pins, and a DATE CHECK
box naming the previous day's big stories that were deliberately left out.

This is the REFRESHED build (22 Nov, ~01:00 UTC) with 49 verified
stories; the initial mid-day build had 15, and the refresh added the
late-US news. See NOTES.md "Refresh 22 Nov 2026" for the changelog.

This program does no rendering at all: it only copies the bundled image
to the output directory, byte for byte, so repeated runs are identical.
Standard library only; no network, no fonts, no image libraries.
"""

import os
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"


def output_dir():
    """Where the harness wants the entry: env override, else /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(chosen) if chosen else Path("/output")


def main():
    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    payload = ENTRY.read_bytes()
    (destination / "entry.png").write_bytes(payload)


if __name__ == "__main__":
    main()
