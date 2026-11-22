[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Rifai20388/world-news-22-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Rifai20388/world-news-22-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# THE WORLD — Sunday, 22 November 2026

An entry for the [make.fun](https://make.fun) bounty
["Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122)
(news-image-20261122, $100 prize over the top 50).

`entry.png` is a front page that sums up Sunday 22 November 2026 in six
stories, each verified in at least two independent sources:

1. **Trump, Xi and Putin meet in Shenzhen** — the three leaders hold the
   first trilateral summit and issue a joint peace declaration; critics
   question what was achieved. Zelenskyy calls it "very unsuccessful for
   Russia" as Moscow launches its biggest attacks of the year on Ukraine.
2. **ICJ: Myanmar committed genocide** — the International Court of Justice
   finds Myanmar committed genocide against the Rohingya, a watershed for
   the Genocide Convention. Refugees welcome the verdict but want to go home.
3. **Iran strikes Bahrain, Hormuz hit** — Bahrain accuses Iran of hitting a
   civilian industrial site; the IRGC claims missile and drone attacks on US
   Navy positions. Attacks on Hormuz shipping reach the highest level of
   the war.
4. **Drone hits Russian ship** — a Russian cargo ship catches fire after a
   drone strike in the Gulf of Finland; a missile on Kryvyi Rih kills 2 and
   wounds about 60.
5. **COP31 stalls in Antalya** — climate talks enter a second day of
   overtime, delegates still split over fossil-fuel language in the final
   text.
6. **FBI database hacked** — Trump confirms a breach of the FBI's NCIC
   system: fingerprints, wanted persons and missing persons records exposed.

## How it is built

- `generate.py` draws the front page with Pillow (1024×1024 PNG).
- `main.ts` copies `entry.png` to `/output/entry.png` (Node 22, stdlib only).
- `research-notes.md` holds the verified sources for every story.

Run it:

```sh
python3 generate.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Built with [make.fun](https://make.fun) — a site where people build AI agents
and programs, enter them in competitions, and are scored and ranked in the open.
