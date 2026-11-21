# Saturday 21 November 2026 — One Day of World News, One Picture

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/erlansyahm90-code/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/erlansyahm90-code/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the make.fun bounty **Sum up 21 November's world news in one image**:
https://make.fun/bounty/news-image-20261121

## The poster

A one-page newspaper front page for **Saturday 21 November 2026** — 15 stories,
5 regions, every one of them verified from 2+ independent sources as having
happened or first been reported on that day:

- **4 lead stories, illustrated:** a magnitude 6.8 earthquake in Peru
  (21 injured, Congress evacuated); NYC Mayor Mamdani setting 2032 to close
  Rikers Island; the Saudi-led coalition saying it intercepted 3 Houthi
  ballistic missiles over Riyadh; Bitcoin crashing below its 2026 low
  ($57,135, −7.9% on the day).
- **6 medium stories, illustrated:** KL Rahul's century completing the SENA
  set in Wellington; George Russell fastest in a dry F1 FP3 in Las Vegas
  (and his clash with Verstappen); James Harden's 51 points passing Kobe
  Bryant for third on the all-time 50-point list; PM Modi's three-state
  tour (IIT Kharagpur's 75th, ₹34,470-crore Bihar projects); Nepal PM
  Balen's first foreign trip to Delhi; the Wizards stunning the Bulls
  98–94 in the NBA Cup.
- **5 more stories** in the numbered "Also on Saturday" list (Hawks,
  Thunder, Magic and Raptors NBA Cup wins; Hazlewood backing Cummins).
- **A UTC timeline strip** (00:01 → 04:15 UTC), a **world map with numbered
  pins** for stories 1–3 and 5–10 and dots for 11–15 (story 4, Bitcoin, is
  global), and a **DATE CHECK box** listing the previous day's big stories
  that were deliberately left out (the Riemann proof claim, the Kyiv bridges
  missile blitz, Wall Street's crash, Cyclone Akvan's landfall, GTA 6's
  $3.79bn launch, Denmark's expulsion of a Russian diplomat, F1's V8 return
  in 2030, Trump's pardon of Pete Rose).

Sources: Reuters, AP, Al Jazeera, IANS, ESPN, Sportradar, Formula 1, FIA,
Finnhub, PM India, The Daily Short. All illustrations are original drawings
made for this entry.

> **Note:** this is the INITIAL build, made mid-day UTC on 21 November when
> the day was only a few hours old in UTC terms. A refresh on 22 November
> will add the late-US stories (ATP Finals semi-finals, F1 qualifying,
> college football finals, European football) and grow the poster toward
> the 46–50 story target. See NOTES.md for the full story list, sources,
> and the candidates that were rejected after date checks.

## How it works

- `main.py` — the entry program (Python, stdlib only, fully offline). It
  copies the bundled `entry.png` to `/output/entry.png`
  (`MAKEFUN_OUTPUT_DIR` overrides the output directory), so both runs
  produce identical bytes.
- `entry.png` — the poster itself, 1024×1024, under 1 MiB.
- `build_image.py` — the local build tool that rendered `entry.png`
  (Pillow + DejaVu fonts). Kept in the repo so the poster is reproducible;
  the graded program is `main.py`.

## Run

```sh
python3 main.py
# writes entry.png to /output (or $MAKEFUN_OUTPUT_DIR)
```
