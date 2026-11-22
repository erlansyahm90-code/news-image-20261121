# Saturday 21 November 2026 — One Day of World News, One Picture

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/erlansyahm90-code/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/erlansyahm90-code/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the make.fun bounty **Sum up 21 November's world news in one image**:
https://make.fun/bounty/news-image-20261121

## The poster

A one-page newspaper front page for **Saturday 21 November 2026** — 49 stories,
6 regions, every one of them verified from 2+ independent sources as having
happened or first been reported on that day:

- **4 lead stories, illustrated:** a magnitude 6.8 earthquake in Peru
  (21 injured, Congress evacuated); NYC Mayor Mamdani setting 2032 to close
  Rikers Island; the Saudi-led coalition saying it intercepted 3 Houthi
  ballistic missiles over Riyadh; Bitcoin plunging to $55,130 — its low
  since September 2024 — then rebounding 9% to retake $60,000, with $1.8bn
  in leveraged positions liquidated.
- **12 medium stories, illustrated:** KL Rahul's 136 putting India on top
  on day 3 in Wellington (486/4, leading by 118); George Russell fastest
  in a dry F1 FP3 in Las Vegas (and his clash with Verstappen); James
  Harden's 51 points passing Kobe Bryant for third on the all-time 50-point
  list; PM Modi's three-state tour (IIT Kharagpur's 75th, ₹34,470-crore
  Bihar projects); Nepal PM Balen's first foreign trip to Delhi; the
  Wizards stunning the Bulls 98–94 in the NBA Cup; two tankers hit by
  projectiles in the Strait of Hormuz (Iran's mine claim unverified);
  the Russian cargo ship Sparta II hit by drones in the Gulf of Finland;
  Mexico capturing FBI Top 10 fugitive "El Chapo Isidro"; Antonelli
  fastest in Las Vegas qualifying but Verstappen inheriting pole; Alcaraz
  and Zverev setting up the ATP Finals title match; France's protests
  shrinking for a sixth straight Saturday (82,500 marchers).
- **33 more stories** in the numbered "Also on Saturday" list — the FBI
  probing a hack of its crime database, Trump's 10% credit-card cap vow
  and Hall of Fame backing for Bonds and Clemens, Gen Z rallies in
  Germany, the Mount Pleasant coal law and midwife-insurance rallies in
  Australia, Cyclone Xavier, record Florida flooding, the IFFI Indian
  Panorama opening, Saturday's NBA and college football finals, the
  Premier League and European football, the Nations Championship rugby
  round, India's hockey win over South Korea, and Anupama Ramachandran
  defending her world snooker title.
- **A UTC timeline strip** (00:01 → 20:05 UTC), a **world map with numbered
  pins** for stories 1–3, 5–10 and 16–21 and dots for 11–15 and 22–49
  (story 4, Bitcoin, is global), and a **DATE CHECK box** listing the
  previous day's big stories that were deliberately left out (the Riemann
  proof claim, the Kyiv bridges missile blitz, Wall Street's crash,
  Cyclone Akvan's landfall, GTA 6's $3.79bn launch, the UFO files batch,
  Sensex's Friday close, Bayern 1–1 Köln, PSG 5–0 Marseille, Pant's 128,
  the IFFI opening, the JPMorgan breach).

Sources: Reuters, AP, Al Jazeera, IANS, ESPN, Sportradar, Formula 1, FIA,
Finnhub, CoinDesk, CNN, NCAA, USA Today, Hockey India, PTI, PM India,
The Daily Short. All illustrations are original drawings made for this entry.

> **Note:** this is the REFRESHED build, made 22 November ~01:00 UTC with
> the full Saturday in view — the late-US news (ATP Finals semi-finals,
> F1 qualifying, college football finals, European football, Saturday
> evening US news) is in, growing the poster from 15 to 49 stories.
> The initial build (mid-day UTC, 21 Nov) had only 15 stories because
> the day was a few hours old. See NOTES.md for the full story list,
> sources, the refresh changelog, and the candidates that were rejected
> after date checks.

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
