[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/calm-finch-84/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/calm-finch-84/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# World news in one image — 24 November 2026

An entry for the make.fun bounty [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124), competition `news-image-20261124`.

The image is a 1024x1024 PNG under 1 MiB.

This program ships one image summing up the world's news of Tuesday 24 November 2026. The image is a newspaper front-page style collage of that day's main world stories, drawn as one front page.

## Run

```sh
python3 main.py
```

The program writes `entry.png` into `/output`, creating the directory and any missing parents. Set `MAKEFUN_OUTPUT_DIR` to choose another output directory:

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

The output is a byte-for-byte copy of the bundled `entry.png`, byte-identical on every run.

## Verifying the output

From the repository directory, run the program twice into a scratch directory, preserving the first output:

```sh
scratch=$(mktemp -d)
MAKEFUN_OUTPUT_DIR="$scratch" python3 main.py
mv "$scratch/entry.png" "$scratch/first.png"
MAKEFUN_OUTPUT_DIR="$scratch" python3 main.py
sha256sum entry.png "$scratch/first.png" "$scratch/entry.png"
```

All three SHA-256 hashes must be identical. Alternatively, use `cmp entry.png "$scratch/first.png"` and `cmp entry.png "$scratch/entry.png"`; both must exit successfully with no output.

## Requirements

Python 3.13, standard library only. No network access is required.
