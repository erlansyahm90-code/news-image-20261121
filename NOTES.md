# NOTES — news-image-20261121 (Saturday 21 November 2026)

# Refresh 22 Nov 2026 (~01:00–01:30 UTC, 08:00 WIB) — 49 stories

Built from the research file
`~/workspace/goals/make-fun-token-radar-01-entry/hidden_files/news-image-20261121-refresh-research.md`
(35 new entries A1–A37 + updates A16/A38 + 3 conditional B10/B12/B13 +
16 rejections, section C). Final poster: **49 stories** (15 old + 34 new),
1024×1024, 255.025 bytes, SHA-256
`8fb40590eeeb7b8ff405ffa7250818f3bdd99a1514238216a00175defd243092`.
`main.py` unchanged in behaviour (still stdlib copy only) — verified:
`MAKEFUN_OUTPUT_DIR=/tmp/out-test python3 main.py` reproduces entry.png
byte-for-byte (same SHA-256).

## What changed vs the initial build
- **Story #4 Bitcoin — numbers replaced (A16):** low $55,130 (lowest
  since September 2024), rebound +9% to retake $60,000 on Saturday
  afternoon US time, ~$1.8bn leveraged liquidations in 24h. The old
  $57,135 / −7.9% figures (03:40 UTC snapshot) were stale by evening.
  Illustration text updated to "BTC $55,130 LOW / REBOUND +9% · RETOOK
  $60,000".
- **Story #5 Test India — updated to stumps, day 3 (A38):** Rahul finished
  136, India 486/4, leading by 118; all five top-order batters passed 50.
  Pant's 128 was NOT used — it is a day-4 (22 Nov) century.
- **New mediums #16–21 (illustrated):** 16 Hormuz tankers (A1, CLAIM),
  17 Sparta II (A2, CLAIM), 18 El Chapo Isidro (A3), 19 F1 qualifying
  (A19), 20 ATP final (A17+A18 merged into one entry), 21 France protests
  (A8). New illustrations: ill_sparta, ill_cartel, ill_f1q, ill_protest;
  ill_hormuz rewritten compact (see bug note below).
- **New Also items #22–49 (28 entries):** 22 FBI NCIC hack (A5),
  23 Trump credit-card cap (A6), 24 Trump backs Bonds/Clemens (A7),
  25 Gen Z Germany (A9), 26 Depardieu/Houellebecq probe (A10),
  27 NSW Mount Pleasant coal law (A11), 28 midwife-insurance rallies
  (A12), 29 Cyclone Xavier (A13), 30 Florida floods (A14), 31 IFFI
  Indian Panorama (A15), 32 Suns–Jazz (A20), 33 Nuggets–Rockets (A21),
  34 Lakers–Kings (A22), 35 76ers–Bucks (A23), 36 UCF/Toledo (A24),
  37 Clemson/Oregon/Air Force/New Mexico (A25), 38 Nebraska–Ohio State
  (A26), 39 Michigan–UCLA 3OT (A27; Washington–Indiana 27-24 OT from the
  same entry is not on the poster line — no room), 40 BYU–Kansas 3OT
  (A28; Texas 45-3 Arkansas and Tennessee 27-13 LSU from the same entry
  are not on the poster line), 41 Wake Forest/Alabama (A29; Florida
  34-27 Vanderbilt not on the line), 42 Leeds–Chelsea + Arsenal–Newcastle
  (A30), 43 Man City/Bournemouth/Tottenham/Coventry/Villa (A31),
  44 Real Madrid/Roma/Leipzig (A32), 45 PSG–Nice (A33), 46 England/
  France/Ireland rugby (A34), 47 Scotland/Wales/Fiji rugby (A35),
  48 India hockey 2-1 Korea (A36), 49 Anupama snooker title (A37).
- **Merged:** A17+A18 (ATP semi-finals) into one entry #20, so the total
  is 49 rather than 50 — still inside the 46–50 target.
- **Region tally:** Americas 25 · Europe 11 · Asia 5 · Middle East 2 ·
  Oceania 5 · Global 1 = 49.
- **DATE CHECK box updated:** now also lists the UFO files batch (20 Nov),
  Sensex's Friday close, Bayern 1-1 Köln (20 Nov), PSG 5-0 Marseille
  (Sunday), Pant's 128 (22 Nov), the IFFI opening (20 Nov) and the
  JPMorgan breach (19 Nov).
- **Timeline strip updated:** now spans 00:01 → 20:05 UTC (Mamdani,
  Riyadh, Peru quake, F1 qualifying, Hormuz tankers, Sparta II, India
  hockey, Bitcoin retakes $60,000).
- **Layout redesign for 49 stories:** leads unchanged (4 in one row);
  mediums 3 rows × 4 columns (was 2 × 3), illustration strip 36 px,
  heads max 2 lines, bodies max 2 lines; Also list two columns × 17/16
  items, one line each (no sub-lines); map shrunk to 320×148. All text
  fit verified programmatically before render (script /tmp/check_fit.py —
  5 overflows found and fixed by shortening bodies).

## Deliberately NOT included
- **B10 Obi (Nigeria), B12 Trump EO on federal contractors, B13 Kryvyi
  Rih strike — all three conditional entries DROPPED.** Each event was
  Friday (20 Nov) with Saturday-only reporting; the poster already has
  49 verified Saturday stories, so the honest-date-label complication
  was not worth it.
- **NWSL final (Washington Spirit vs Kansas City Current) — NOT included.**
  Kickoff 01:00 UTC 22 Nov, exactly when this build ran (~01:10 UTC);
  no final result could exist yet. A web search at build time returned
  only a pre-match Sportradar "scheduled" page plus stale/junk
  aggregator scores (one claiming a 2-1 "final" 10 minutes after
  kickoff — not credible, no second source). Not guessed.
- **College football Saturday night (Georgia–South Carolina, Notre Dame–
  SMU, Miami–Virginia Tech, Utah–TCU) and NBA Saturday night (POR–NYK,
  MEM–MIN, NOP–SAS) — NOT included.** All kicked off ~00:30 UTC and
  were still in progress at build time; no finals yet. Not guessed.
- **Bayern 1-1 Köln and PSG 5-0 Marseille — NOT used** (20 Nov / Sunday).
  Correct Saturday scores used instead: Toledo 19-0 (not 16-0), Alabama
  47-0 (not 45-0), Scotland 67-5 (not 65-7), Bitcoin low $55,130.
  Hormuz written as "2 tankers Saturday" only (the "3 tanker" claim
  mixes in Friday's attack). LeBron James listed with the 76ers, not
  the Lakers.

## Verification done by the builder (not just trusting the research)
- Hormuz story #16 cross-checked independently at build time: Reuters
  (via KRRO and 8+ wire mirrors) confirms two tankers hit 05:00/05:50
  UTC near Khasab, no casualties, Iran mine claim separate — matches
  the poster text exactly.
- Poster viewed directly after render; Hallmark audit (5 points):
  typography consistent (serif heads / sans body, clear sizes);
  alignment grid-clean with rules between sections; hierarchy
  masthead → timeline → leads → mediums → map/also → date check →
  footer; spacing tight in medium rows (4 px gaps) but no overlaps;
  composition balanced. No invented numbers — every figure traces to
  the research file's 2+ sources.
- **Bug found and fixed during visual check:** ill_hormuz (legacy tall
  version), ill_sparta (first draft) and ill_cartel drew elements ABOVE
  their 36 px box (sea/burst/smoke at negative offsets, star radius 24
  in a 36 px strip), painting smoke and bursts over the heads and bodies
  of the cards above. All three were rewritten to stay strictly inside
  [y, y+h] (Hormuz sea/tanker/burst/mine, Sparta hull/containers/burst,
  cartel star r=15); medium strip height set to 36 px. Re-rendered and
  re-checked card by card — clean.
- main.py behaviour unchanged (copy only, stdlib, offline); output
  SHA-256 matches entry.png exactly.

---

## Initial build, 21 Nov 2026 ~06:30 UTC (13:30 WIB). 15 stories, all verified
from 2+ independent sources as having happened or first been reported on
Saturday 21 November 2026. A refresh on 22 Nov ~08:00 WIB will add the
late-US stories (ATP Finals semi-finals, F1 qualifying, college football
finals, European football, Saturday-evening US news).

## Stories on the poster

### Leads (1–4)
1. **Peru M6.8 earthquake** (01:09 UTC) — epicentre 30–34 km NW/N of Junín,
   depth 108–129 km; felt in Lima, Congress evacuated; civil defence chief
   reported 21 injuries; rockfalls on Carretera Central + Costa Verde cliffs,
   power outages in Pichanaqui; no deaths, no tsunami threat. Magnitude
   varies by agency (USGS 6.7, GFZ/IGP 6.8, SGC 6.9); poster uses 6.8 (IGP).
   Sources: Reuters, AP, GFZ, IGP, USGS.
2. **Mamdani sets 2032 to close Rikers Island** (00:01 UTC) — unveiled Friday
   evening NY; replace with 4 borough jails; 5 years after the Aug 2027 legal
   deadline. Sources: The Daily Short, LAS News, jabulaniradio.
3. **Saudi coalition intercepts 3 Houthi missiles over Riyadh** (00:51 UTC)
   — second Houthi attack on the capital in days (PIF Tower hit Thursday);
   Houthis threaten Saudi Red Sea ports, warn airlines to avoid Saudi
   airspace. Labelled CLAIM: the interception is the coalition's account.
   Sources: Reuters, Al Jazeera, Middle East Eye, Interfax, Jerusalem Post.
   (The Hodeidah port strike was Friday 20 Nov, NOT 21 Nov — excluded.)
4. **Bitcoin crashes below its 2026 low** — Finnhub live: $57,134.87 at
   03:40 UTC, day low $56,852, −7.87% on the day; 2026 low zone was $57,697.
   Coinbell daily brief: ETH $1,621 (−7.8%), total crypto market $2.04T
   (−7.6% 24h). Sources: Finnhub, Coinbell.

### Mediums (5–10)
5. **KL Rahul completes SENA set** — 100 off 207 balls, day 3, 1st Test vs NZ,
   Basin Reserve Wellington; first Indian opener with Test centuries in all
   4 SENA countries; India 344/2 at tea, trail NZ by 24. Sources: IANS,
   The Daily Short.
6. **F1 FP3: Russell fastest, Verstappen clash** — FP3 ran Fri 16:30 local =
   00:30 UTC Sat. Russell 1:34.041, Antonelli +0.911, Norris +0.974; Russell
   and Verstappen made contact, both summoned to stewards; Verstappen also
   investigated for erratic driving. Sources: formula1.com, FIA, PlanetF1,
   Speedcafe, The Race.
7. **Harden's 51 lifts Cavs; passes Kobe** — 51 pts (15/26 FG, 7/11 3PT,
   14/14 FT), 6 reb, 6 ast; Cavs 128–119 Pacers, NBA Cup Friday night
   (Sat 00:30 UTC); 26th career 50-point game, now 3rd all-time (Wilt 118,
   Jordan 31, Harden 26, Kobe 25). Sources: ESPN, SI, theScore, NBC Sports,
   Sportsnet, TSN, Sportradar.
8. **Modi tours 3 states in a day** — IIT Kharagpur Platinum Jubilee (9:45 AM
   IST = 04:15 UTC), ₹34,470-crore Bihar projects in Vaishali (Nitish Setu /
   Ganga Bridge), 5th Kaushal Deekshant Samaroh in Lucknow (5:30 PM IST).
   Sources: pmindia.gov.in, PIB, IANS, dainiknewslive, sambadenglish.
9. **Nepal PM Balen heads to Delhi on Sunday** — arrives Sunday for a 2-day
   state visit, first bilateral foreign trip since taking office in March;
   talks with Modi. Announced/reported 21 Nov. Sources: The Daily Short,
   careerindia.
10. **Wizards stun Bulls 98–94 in NBA Cup** — Friday night (Sat 01:00 UTC);
    Anthony Davis 36 pts, 11 reb; rookie AJ Dybantsa 20 pts, 10 reb, 6 ast;
    Wizards 2–1 in group play. Sources: ESPN, Sportradar, NBC Sports.

### Also (11–15)
11. **Hawks beat Hornets 111–97** (NBA Cup, Sat 00:00 UTC); Jalen Johnson 26
    pts; Atlanta's third straight win, now 10–6. Sources: AP/theScore,
    YouTube (NBA), Sportradar, NBC Sports.
12. **Thunder beat Pelicans 126–120** (NBA Cup, Sat 01:00 UTC); OKC 10–6,
    Pelicans 5–12. Sources: ESPN Southwest Louisiana, Sportradar.
13. **Magic edge Nets 113–111** (NBA Cup, Sat 00:30 UTC); Orlando 3–0 in
    group play, top of its group. Sources: SI, Sportradar.
14. **Raptors beat Pistons 105–102** (NBA Cup, Sat 00:30 UTC); Raptors 6–10,
    Pistons 10–5. Sources: VAVEL, Sportradar.
15. **Hazlewood backs Cummins** — hints at rethinking his future in the
    Australian Test side if Cummins is stripped of the captaincy over 2018
    Sandpapergate allegations. Sources: IANS, LAS News.

### Region tally (by event location)
Americas 9 · Asia 2 · Middle East 1 · Oceania 2 · Global 1 = 15.
(Rahul's century is in Wellington, NZ → Oceania, even though he is Indian;
same location convention as F1 in Las Vegas → Americas.)

## Rejected after date checks (do NOT use as 21 Nov stories)

These looked like 21 Nov stories but were verified as earlier — several are
in the poster's DATE CHECK box:
- **Riemann hypothesis proof claim** (Levent Alpöge + Claude) — announced
  Fri 20 Nov (Scientific American, phys.org). Claim unverified; 17M lines
  of Lean code; not independently reviewed.
- **Kyiv bridges missile blitz** — 20 Nov (110+ missiles, 400+ drones, ≥9 dead).
- **Wall Street crash** — 20 Nov (S&P −3.7%, Nasdaq −5.3%).
- **Poland missiles / Tusk provocation** — 20 Nov.
- **GTA 6 $3.79bn day-one sales** — announced Fri 20 Nov.
- **Cyclone Akvan landfall** — Fri 20 Nov morning (Gopalpur, Odisha).
- **Denmark expels Russian attaché (Kyivstoner plot)** — 20 Nov.
- **Trump calls for Nvidia to reinstate Jensen Huang** — Fri 20 Nov WH press
  conference. (SEC scrutinizing Nvidia accounting — Reuters Nov 20.)
- **F1 V8 engines return 2030** — announced 20 Nov (BBC/Sky).
- **Trump pardons Pete Rose** — 20 Nov (BBC).
- **Harry Kane ankle ligament tear** — Bayern confirmed 20 Nov (Guardian).
- **Pochettino seeks control at Man United** — 20 Nov (Guardian).
- **F1 FP1/FP2 Las Vegas** — Thu evening local = 20 Nov UTC (Russell fastest
  in wet FP2; FP1 washed out).
- **Gen Z protests across Europe** — main day of action Fri 20 Nov (25
  countries; London 10 arrested; Italy general strike). Further protests
  planned 21–22 Nov; no distinct Saturday development verified by build time.
- **FPI record ₹1.22 lakh crore into Indian shares** — Hindu Business Line
  article published 20 Nov (data Nov 2–20).
- **Zecler verdict** (3 Paris police sentenced) — Fri 20 Nov.
- **Palisades Fire conviction** — Fri 20 Nov.
- **Daraxonrasib combination data** — presented 20 Nov at ENA 2026.
- **NHL Thursday games** (incl. McDavid streak ending) — Thu night US = 20 Nov UTC.
- **NBA Thursday games** (Memphis 126–98 Golden State etc.) — 20 Nov UTC.
- **India women's hockey 4–1 Malaysia** — Thu 19 Nov (Bhopal). India play
  South Korea Sat 21 Nov 19:00 IST — result for the refresh.
- **Senegal migrant boat sinks** — capsized overnight 17–18 Nov (Yenne);
  Reuters dateline 19 Nov.
- **Japan M5.7 Shizuoka quake (22 injured)** — Sun 8 Nov, NOT 21 Nov.
  (Al Jazeera's country page re-lists it as "latest" — stale item.)
- **Gaza Jabaliya drone strike (2 killed)** — Sat 14 Nov, NOT 21 Nov.
  (Al Jazeera's EU-access article is a Nov 14 piece re-crawled 21 Nov.)
- **Gaza ground operation** — launched Wed 18 Nov, withdrew Thu 19 Nov.
- **Houthi strike on Hodeidah port** — Fri 20 Nov (coalition statement).
- **IRGC MQ-9 drone claim** — 20 Nov.
- **Phumzile Mlambo-Ngcuka dies** — Fri 20 Nov 20:56 GMT (Mail & Guardian).
- **Kenya Mrima Hill mining deal** — 19 Nov.
- **Bukele seeks third term** — registered Thu 19/20 Nov.
- **Tesla opens first Argentina store** — Fri 20 Nov (Reuters).
- **Brazil tourism target** — data released 16 Nov.
- **AtlasIntel poll (42% Brazilians believe election fraud)** — published Fri 20 Nov.
- **Mount Pleasant coalmine law / midwives insurance warning (Australia)** —
  worldinsummary "first published 21 Nov" is Sydney time; underlying
  Guardian dates unverified as 21 Nov local — held for refresh verification.
- **Cyclone Xavier new marine warning** — single source (AppiSToS), held.
- **US declassifies UFO footage** — single source (jabulaniradio), held.
- **JPMorgan/Visa/Mastercard cyberattack on vendors** — single source
  (jagranjosh roundup), held.
- **IFFI Goa opens** — single source (Last24Hrs), held.
- **Japan record tourism 3.91M / Milky Way 5-trillion-particle simulation** —
  single source (japan.co.jp Nov 21 edition), held.
- **Obi vows to end kidnappings (Nigeria)** — single source (Punch), held.
- **College football Friday night** (UCF 48–17 Iowa State, Toledo, Clemson,
  Oregon, Air Force, Wyoming games) — mostly in progress or conflicting
  scores at build time; finals for the refresh. (UCF game started 23:00 UTC
  Fri 20 Nov — a 20 Nov game by start time.)
- **NBA Friday late games** (Jazz–Suns, Nuggets–Rockets, Lakers–Kings) —
  still LIVE at build time (~06:00 UTC); results for the refresh.
- **F1 qualifying** — Sat 04:00 UTC, in progress at build time; result for
  the refresh. (Race is Sat 20:00 local = Sun 04:00 UTC 22 Nov.)

## Verification notes
- **Date convention:** US Friday-evening sports count as 21 Nov because they
  start at/after 00:00 UTC Saturday (the same convention the 20 Nov poster
  used for Thursday-night games). Asia-Pacific stories count by local date.
- **Al Jazeera mirror caution:** the edgeone.app Al Jazeera mirror re-lists
  old articles with fresh crawl timestamps — always check the URL date and
  cross-reference (this caught the Japan quake, Gaza drone strike, and
  Gaza EU-access items, all stale).
- **ScoreZaap dates are unreliable** (lists Fri 20 Nov matches as Nov 21).
- **OneTurn "today" page was the 20 Nov edition** until ~05:00 UTC.
- **School-assembly roundups (jagranjosh, careerindia, educationtimes)**
  mix 20 Nov and 21 Nov items — every item needs independent date checks
  (this caught the hockey match and the Sensex Friday close).
