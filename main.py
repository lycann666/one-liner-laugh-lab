"""One-Liner Laugh Lab -- make.fun entry (program/v1).

Writes one original funny line to ``/output/entry.txt``.

PASS 1 (v1, my own choice before any outside ranking):

  Entry v1 -- "The sock was my only witness, and I have a strict
  no-witnesses policy." (70 characters)

  Judged against the judge's criteria, most important first
  (RULES.txt: 1. one funny line answering the prompt -- the excuse
  a robot vacuum gives after eating a sock; 2. actually funny, with
  a twist or deadpan turn; 3. original, a fresh angle, not the first
  excuse anyone would think of or a stock joke; 4. fits the
  situation; 5. tight, every word working):

  1. It IS the vacuum's excuse, in the vacuum's own voice, for
     eating the sock.
  2. The laugh lands on the turn: "only witness" reframes a sock as
     a witness to a crime, and "no-witnesses policy" is deadpan
     mob-movie logic from a household appliance.
  3. Fresh angle: the vacuum as a criminal silencing a witness --
     not the crowded "I was hungry / I thought it was food / I was
     trying to help" excuses already filling the field (live titles
     show "I was trying to fold it", "The sock was a donation",
     "The Sock Was Adopted, Not Eaten").
  4. Fits exactly: it explains WHY the sock is gone (eaten to
     silence it).
  5. Tight: 70 characters, no setup that overstays.

  PASS 2 (v1 -> v2, after Freemodel ranking): Freemodel
  (claude-sonnet-5-5, 1 call, 2,840 tokens) ranked the 5 drafts
  B > E > D > A(v1) > C and offered 2 alternatives. v1 ranked only
  4th: "solid noir mobster twist, though the 'no witnesses' trope
  is well-worn" -- that hits criterion 3, the one the judge weighs
  right after funniness, so v1 is revised away. Draft B wins:
  "internal storage" is a clean double pun (literal dustbin +
  corporate promotion) with a genuinely fresh corporate angle, and
  "it starts Monday" is the tightest kicker of all candidates.
  Freemodel's alternatives were considered and rejected: ALT1
  ("Not theft -- curation... Gallery opens at 6", 102 chars) has
  a good museum-curator frame but its punchline needs the whole
  setup to land; ALT2 ("relocated it to a secure, undisclosed
  facility... That's called maintenance", 103 chars) leans on the
  well-worn "undisclosed facility" euphemism. Draft E (tour of my
  insides / customer service) ranked 2nd but its twist is softer
  than B's double pun. Draft D (manual paradox) ranked 3rd, a
  known meta trick. Draft C ranked last (muddled logic).

  Entry v2 -- "I didn't eat the sock. I promoted it to internal
  storage -- it starts Monday." (76 characters, 78 bytes)

  1. It IS the vacuum's excuse, denying the eating while
     confessing the mechanism.
  2. Two-stage laugh: denial, then the promotion pun, then the
     deadpan "starts Monday" kicker.
  3. Freshest angle in the field: corporate HR-speak from a vacuum,
     vs the crowded hungry/helpful/adopted excuses in the live
     field titles.
  4. Fits exactly: the sock's fate (inside the vacuum) is the joke.
  5. Tightest: 76 characters, every word working.
  Verdict: CHOSEN as v2, replacing v1.

The program is deterministic: one constant string, no network, no
randomness, no clock, no environment, no input. Two runs produce
byte-identical output.
"""

import os

# The entry (v2, revised from v1 per the header): one line,
# 76 characters, 78 bytes, no trailing newline
# (a trailing newline would only add a byte the gate counts and the
# size tie-break punishes, and the line is complete without it).
LINE = "I didn't eat the sock. I promoted it to internal storage \u2014 it starts Monday."


def main() -> None:
    # Gate check, mirroring RULES.txt: the entry must be UTF-8 text
    # of 1 to 200 characters, not only white space, and a single line.
    # Refuse loudly rather than writing an entry the gate would score 0.
    if not isinstance(LINE, str):
        raise ValueError("entry must be a str, got %s" % type(LINE).__name__)
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(LINE)
        )
    if LINE.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be encodable as UTF-8: %s" % exc) from exc

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
