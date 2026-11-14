"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

TTR_WINDOW = 50

# (AI-like value, human-like value) for each measure. Starting guesses —
# recalibrate against the Milestone 4 calibration inputs.
SPREAD_ANCHORS = (0.25, 0.65)
TTR_ANCHORS = (0.70, 0.85)
PUNCT_ANCHORS = (0.06, 0.16)

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Using the stddev and mean calcualting the coefficient of variation of words per sentence.
    Roughly 0.0–1.0+; higher means more varied, which reads as more human.
    Fewer than two sentences returns 0.0 there's no spread to measure, and
    `style_signal` treats that case as "no evidence" rather than as AI.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    To stop length from driving it, this is a moving average, the plain ratio inside every 50 word window, averaged. Texts shorter than
    one window fall back to the plain ratio. Empty text returns 0.0.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    if len(tokens) <= TTR_WINDOW:
        return len(set(tokens)) / len(tokens)
    ratios = [
        len(set(tokens[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(tokens) - TTR_WINDOW + 1)
    ]
    return statistics.mean(ratios)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Commas, semicolons, colons, dashes, parentheses, and ! / ? per
    word. Full stops are left out; every sentence has one, so they mostly
    measure sentence length again. Roughly 0.0–0.3; higher reads as more
    human. Empty text returns 0.0.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    marks = re.findall(r"[,;:()!?\u2014\u2013]|(?<=\s)-(?=\s)|--", text)
    return len(marks) / len(tokens)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Choices:
      - All three measures point the same way higher raw value reads as
        more human so all three get flipped.
      - Each is scaled with `_scale` between an "AI-like" and a "human-like"
        anchor (below), then clamped to 0–1.
      - Weights: spread 0.75, vocabulary 0.25, punctuation 0. Spread gets
        the most because it's the measure the AI/human difference is clearest
        on; punctuation habits vary most between individual people.
      - Under two sentences, spread is unknown, so it counts as 0.5.
    """
    if not words(text):
        return 0.5

    if len(sentences(text)) < 2:
        spread_ai = 0.5
    else:
        spread_ai = _scale(sentence_length_spread(text), *SPREAD_ANCHORS)
    ttr_ai = _scale(type_token_ratio(text), *TTR_ANCHORS)
    punct_ai = _scale(punctuation_density(text), *PUNCT_ANCHORS)

    return 0.75 * spread_ai + 0.25 * ttr_ai + 0.0 * punct_ai


def _scale(value: float, ai_like: float, human_like: float) -> float:
    """0.0 at or past `human_like`, 1.0 at or past `ai_like`, linear between."""
    position = (value - human_like) / (ai_like - human_like)
    return min(1.0, max(0.0, position))


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
