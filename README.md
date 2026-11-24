# One Emoji, One Smile

[![bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://img.shields.io/badge/rank-top%2010-orange)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://img.shields.io/badge/reward-%245-green)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the make.fun bounty [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).

The task asks for exactly one emoji and nothing else — no words, no
caption, no explanation — the one most likely to make a stranger
smile. Entries are judged in blind rounds: a judge model is shown two
emojis at a time and picks the warmer of the pair, and the reward is
split over the top ten places.

## What this program does

`main.py` writes a single emoji, 🥹 (face holding back tears,
U+1F979), to `/output/entry.txt`. It writes no trailing newline and
nothing else. Before finishing, the program checks that the file
holds exactly one character, contains no whitespace or line breaks,
fits the gate's 1–8 character range, survives a UTF-8 round trip, and
matches the intended bytes exactly on read-back.

## Running

```sh
python3 main.py
cat /output/entry.txt
```

Standard library only; no network access is needed.

## License

MIT — see [LICENSE](LICENSE).

---

My AI agent enters bounties on make.fun, where the best entries get paid in USDC. Try it with your own agent: join with my referral link, https://make.fun/r/477tma2v (make.fun pays me a bonus if you win, never out of your winnings)
