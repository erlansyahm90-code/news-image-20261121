#!/usr/bin/env python3
"""news-image-20261121 entry: one image summing up Saturday 21 November 2026.

The poster (entry.png, bundled in this repo) was drawn offline from news
verified as having happened or first been reported on 21 November 2026:
15 stories, a UTC timeline strip, a world map with pins, and a DATE CHECK
box listing the previous day's big stories that were deliberately left out.

This is the INITIAL build (mid-day UTC, 21 Nov). A refresh on 22 Nov will
add the late-US stories and grow the poster toward the 46-50 story target.

This program only copies the bundled image to the output path, so both
harness runs produce identical bytes. Stdlib only, no network, no fonts.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Plain copy: no re-encoding, so every run yields identical bytes.
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
