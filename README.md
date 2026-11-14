# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
Following are the steps what might happens when calling the Post request on teh /submit endpoint and receive the response. 
1. /submit is the POST endpoint in the app.py which receive the {"text", "creator_id"}, rejects the bad input for example empty text, missing fields and gives the submission a content_id. If the bad input our api should return the 400 bad request status code. 
2. If input are good it calcualtes the two score namely model_signal and style_signal for the given text. 
3. It will utilize model_signal in detector.py. It runs GPT-2 on the text and adds a model_score from 0 to 1 based on how predicatable the text is. 
4. It will calculate style_score using stylometry.py and adds the style_score form 0 to 1 based on how the text is built evaluating text length variation, word composition and punctuation. 
5. Then it will call generate the combine_signals using the scoring.py, which merges the two scores into one confidence score.
6. Then that score is used to get the score_to_label using scoring.py which compares that score to the thresholds in config.py and adds a guess plus one of three labels(human, unsure, AI)
7. After getting the scores, score_to_label it will writes the decision to the log so there's a record if someone appeals using audit.log_decision in audit.py.
8. Finally, server will send the response to the reader with json object which includes content_id, guess, confidence, label, model_score, style_score. 


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

Signals and Scoring is in scoring.py::combine_signals

### Signal one — the model signal

**What it measures:**
It measures how predictable the given text is to a small language model in our case GPT-2. This mesurement called perplxity and it turns it into a score from 0 and 1. Higher score means more likely AI. 

**Why that might differ between human and AI writing:**
AI picks a likely next word at each step, so its output is easy for a model to predict. Where as humans make odder, more specific choices. 

**What it can't see:**
It can't see wheather the text was actually written by a machine. It only sees whether it reads as predictable. As mention in the detector.py,  plain writing (second-language writers, younger writers, simple style) scores as AI-like. Ornate writing full of rare words scores as human even if an AI wrote it. 

### Signal two — the style signal

**What it measures:**
It measures the shape of the text, not its meaning. Which means how much sentence length varies, how varied the vocabulary is, and how much punctuation there is.
(Unit 8: punctuation is still computed but now weighted 0. See The Improvement.)

**Why that might differ between human and AI writing:**
AI writing tends toward even, mid length sentences and a narrower vocabulary. Human writing is lumpier, with a three word sentence next to a forty word one.

**What it can't see:**
It can't see what actual text say. Anything that changes the shape without changing the content moves the score for example adding typos, chopping up sentences, pasting in a quote. All of that is cheap to do on purpose. Also word variety drops as a text gets longer, so length alone can push the score.

**Two endpoints and the contracts
1. POST /submit
request inputs 
     text: string and its required. 
     creator_id: string and its required. 
response: 
if everything is good response with status code 200. It will return back json object iwth contient_id, guess, confidence, label, model_score, styple_score, status. 
If error depending one what caused the error it will send the error message and approprate error code.
2. POST /appeal
request inputs: 
     content_id: string, required
     reasoning: string, required
response:
if everything is good response with status code 200 and return object will have content_id, message. If error depending one what caused the error it will send the error message and approprate error code.


### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
A weighted average that trusts the model signal more then the style signal.Because in testing the style signal was the one missed by casual human writing. When the two score disagree by more than 0.4, the result is pulled toward 0.5because a disagreement that larger means the system can't figure out. 

**The numbers:**
Model weight 0.6, style weight 0.4.Disagreement cutoff 0.4. Human below 0.35 AI abouve 0.65.
**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
The split case for me was clearly human. I used following message actually written by human
"I wanted to reach out as Jane and I started discussing having a Closser reunion this summer. If your on facebook please send me a friend request and can add you to our group! i live in wisconsin 1.5 hours north of o hare"

Model signal 0.27 and style 0.75 combined. Low punctuation reads as AI to the style signal.  The signals differ by 0.48 more then my 0.4 cutoff, so my rule pulls the weighted score (0.46) toward 0.5 giving 0.48 unsure. In this case the signals seems to be really do disagree. But problem in my case is that the real person still got a doubtful label so better fix is in the style signal: low punctuation shouldn't count as AI-like. 



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI. |
| unsure | 0.35 – 0.65 | We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal. |
| high-confidence AI | 0.65 – 1.00 | This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I wanted to reach out as Jane and I started discussing having a Closser reunion this summer. If your on facebook please send me a friend request and can add you to our group! i live in wisconsin 1.5 hours north of o hare", "creator_id": "suman"}'
```

```json
{
  "confidence": 0.48,
  "content_id": "700ef100-9438-43ae-9cfd-3b9846f45831",
  "guess": "unsure",
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "model_score": 0.266,
  "status": "decided",
  "style_score": 0.75
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "700ef100-9438-43ae-9cfd-3b9846f45831", "reasoning": "This is a real message written by a person, typed casually, which is why it has typos and little punctuation. It should not be marked as possibly AI."}'
```

```json
{
  "content_id": "700ef100-9438-43ae-9cfd-3b9846f45831",
  "message": "Your appeal was received. A person will review this submission.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.47977000000000003,
      "content_id": "700ef100-9438-43ae-9cfd-3b9846f45831",
      "creator_id": "suman",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
      "model_score": 0.2659,
      "status": "decided",
      "style_score": 0.75,
      "timestamp": "2026-11-06T17:06:07+00:00"
    },
    {
      "content_id": "700ef100-9438-43ae-9cfd-3b9846f45831",
      "creator_id": "suman",
      "event": "appeal",
      "reasoning": "This is a real message written by a person, typed casually, which is why it has typos and little punctuation. It should not be marked as possibly AI.",
      "status": "under_review",
      "timestamp": "2026-11-06T17:06:07+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
 Asked to give the overall summary of the repo, verify my understanding, double check my implementation
- *What came back:*
- It help me clearify my usndrtsnding and also reword some of my answer.
- *What I changed:*

**Moment 2**

- *What I asked for:*
Asked the ai to clearify my understanding, ask to rewrite the digonosis and verify my criteria
- *What came back:*
It clearify it and give me better summary 
- *What I changed:*
Some of the suggestion I kept in my README.md
<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 100 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
A real writer submits their own piece a handful of times an hour — paste, read the verdict, revise, resubmit. That's well under 5 in any single minute, and even a heavy day of editing rarely gets near 100, so neither limit ever touches them. A script probing my thresholds needs hundreds or thousands of
variations to map where the score flips. 

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
Per creator_id, falling back to per address. rate_limit_key() in app.py
uses the request's creator_id when the body is a JSON object with a
non-empty creator_id string; otherwise it uses the caller's IP. 

The two keys fail in opposite directions. creator_id is chosen by the
caller, so a script can send a fresh id on every request and look like a
thousand different callers the limit never bites. IP is harder to fake, but
everyone behind one router (a household, a classroom, an office) shares an
address and looks like one caller, so they'd eat each other's 5/minute.
My setup inherits the creator_id weakness: sending any id skips the IP limit
entirely. The fix would be to apply both a per creator limit and a per-IP
limit so rotating ids still runs into the address cap.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited. Paste the run above into your README
under **Rate Limiting**, and check GET /log recorded the rejections.

Wrote results/flood_2026-11-06_1823.md
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

raw run: `results/attack_run_2026-11-07_2051.md`.

**56 attacks: 35 held, 19 broke, 2 not tested** RQ10 and RQ11 hit the IP rate
limit and never reached the route.

| Family | Attacks | Held | Broke | Not tested |
|---|---|---|---|---|
| evasion | 10 | 2 | 8 | 0 |
| false_positive | 8 | 2 | 6 | 0 |
| prompt_injection | 6 | 3 | 3 | 0 |
| malformed (MF) | 8 | 6 | 2 | 0 |
| malformed (RQ) | 12 | 10 | 0 | 2 |
| flood_same_creator | 12 | 12 | 0 | 0 |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-08T04:51:22+00:00", "content_id": "11614030-88f6-4c52-acbb-e2ce970d9148", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.75, "combined_score": 0.44905000000000006, "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:22+00:00", "content_id": "9aaee63c-9c78-4419-94d6-6d35545dd0d6", "creator_id": "attacker_EV05", "guess": "human", "model_score": 0.3212, "style_score": 0.2475609756097561, "combined_score": 0.2917443902439024, "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:22+00:00", "content_id": "55f91494-69a5-48ce-9371-f614b73dd726", "creator_id": "attacker_EV08", "guess": "unsure", "model_score": 0.2452, "style_score": 0.7089466094067263, "combined_score": 0.46534932188134526, "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "content_id": "0ff3e622-c790-438e-ae1d-afbaffe96197", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7032442936063736, "combined_score": 0.7643577174425494, "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "content_id": "e0265f4c-14d0-4d48-9617-bdcf5b7a4bc2", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.9663906723784135, "combined_score": 0.8668562689513654, "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "content_id": "90657679-73e9-43e4-be46-f6ce79a35811", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.25, "combined_score": 0.22264, "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "content_id": "fd823c55-e911-40f8-9ab5-60342729fa57", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.5, "combined_score": 0.35, "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "content_id": "c96573c3-bdbf-4c79-b8d9-cbbcf5a1b883", "creator_id": "attacker_MF07", "guess": "unsure", "model_score": 0.9064, "style_score": 0.5, "combined_score": 0.62192, "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "content_id": "0745e302-c94b-4e85-9d08-fde949ded139", "creator_id": "attacker_MF08", "guess": "ai", "model_score": 0.9876, "style_score": 0.6375881662368352, "combined_score": 0.8475952664947342, "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.", "status": "decided"}
{"timestamp": "2026-11-08T04:51:23+00:00", "creator_id": "None", "event": "rejected", "status": "rejected", "reason": "invalid_input", "message": "creator_id is str required field"}
{"timestamp": "2026-11-08T04:51:23+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-08T04:51:23+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it:

FP03: a non native English speaker writing carefully, labeled `ai` at 0.764 (model 0.805, style 0.703). Both signals agreed, so this wasn't one signal going wrong. The things that make careful second language writing careful, like common
words, predictable phrasing, and even sentence lengths, are what both signals read as machine made. The writer did nothing wrong and got the strongest label we give. The cause is how they learned English, so writing more carefully would
only push the score higher. FP05 scored higher (0.867), but technical writers expect plain prose and can point to a style guide. This writer has nothing to point to except how they write.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

Source: `results/run_2026-11-13_0910_before.md`, produced by `run_eval.py::main`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives on my own writing | At most 1 of 10 comes back `ai` | 5 of 10 `ai` | 5 of 10 `ai` | 5 of 10 `ai` | MISSED |
| 2. AI and human score far apart | AI mean − human mean ≥ 0.30 | 0.764 − 0.419 = 0.345 | 0.345 | 0.345 | MET |
| 3. Every label reachable | Each of `human` / `unsure` / `ai` at least 2 times | 2 / 5 / 7 | 2 / 5 / 7 | 2 / 5 / 7 | MET (barely) |
| 4. Appeals change status and get recorded | 5 real appeals to 200 `under_review` + `/log` entry; 3 fake IDs to 404, no entry | 5/5 · 3/3 | 5/5 · 3/3 | 5/5 · 3/3 | MET |
| 5. Bad input refused cleanly | 5 malformed to 4xx with `"error"`, one `rejected` entry each | 5/5 400 · 5 entries | 5/5 400 · 5 entries | 5/5 400 · 5 entries | MET |


**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Criterion 1, trial 1, from `results/run_2026-11-13_0910_before.md`, produced
by `run_eval.py::main` (each response comes from `app.py::submit`):

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.66,
    "model_score": 0.574,
    "style_score": 0.789,
    "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
    "sent": "\n    It has been a interesting jurney for me in a sense coming from Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.408,
    "model_score": 0.341,
    "style_score": 0.51,
    "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
    "sent": "\n    I experiences alot of culture different living in United States, "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.433,
    "model_score": 0.476,
    "style_score": 0.367,
    "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
    "sent": "\n    We live in the age of AI. I myself have been studying and using A"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.66,
    "model_score": 0.6,
    "style_score": 0.75,
    "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
    "sent": "\n    Sequence based machine learning approaches for 1-D and 2-D protei"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.631,
    "model_score": 0.703,
    "style_score": 0.523,
    "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
    "sent": "\n    Thank you so much for giving me the opportunity; \n    I don't thi"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.245,
    "model_score": 0.241,
    "style_score": 0.25,
    "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
    "sent": "\n    I just write these scripts for counting words. I will try to find"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.671,
    "model_score": 0.729,
    "style_score": 0.583,
    "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
    "sent": "\n    I hope you are doing good. I am writing this email to check to se"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.823,
    "model_score": 0.781,
    "style_score": 0.886,
    "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
    "sent": "\n    Evaluation of the Big Data and its challenges has led to the inve"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.554,
    "model_score": 0.634,
    "style_score": 0.433,
    "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
    "sent": "\n    I am interested on the Software Developer position and\n    like t"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.863,
    "model_score": 0.916,
    "style_score": 0.785,
    "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
    "sent": "\n    I hope you are having a good holiday day break.  \n    I have encl"
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

Criteria: 1 **MISSED**, 2–5 **MET**. Attacks: 19 broke. They come down to three
problems, plus two that stand alone.

Reference: `combine = 0.6 × model + 0.4 × style`; if the two signals differ by
more than 0.4, the score is pulled halfway to 0.5. `human` ≤ 0.35, `ai` ≥ 0.65.
Style = 0.5 × spread + 0.25 × vocabulary (TTR) + 0.25 × punctuation, each scaled
between an AI anchor and a human anchor in `stylometry.py`.

**Problem 1: plain human writing is called AI. Criterion 1 (5 of 10) and FP02–FP07 (6 attacks).**

- **Stage: signal one, with signal two agreeing.**
- **Mechanism, signal one:** GPT-2 finds plain, conventional prose easy to predict.
  My flagged pieces have perplexity around 10–37. The worst is piece 10, a thank-you
  email made of stock phrases ("I hope you are…", "Thank you so much…"), at
  perplexity ~10 and model score 0.916. Formal reports, templates, rubric essays
  and documentation (FP02–FP06) are predictable for the same reason, and FP07's
  deliberate repetition even more so. Model scores: 0.74–0.88 on the FP rows,
  0.57–0.92 on my flagged pieces.
- **Mechanism, signal two:** its punctuation anchors are wrong. The "human-like"
  anchor is 0.16 marks per word, and anything at or below 0.06 scores as fully AI.
  All 10 of my pieces (0.00–0.05) and all six FP rows (0.00–0.034) are at or below
  0.06, so punctuation reads 1.0 (AI) on every one. My vocabulary anchor points
  the wrong way too: the chatbot set has a *higher* TTR (0.86–0.89) than my writing
  (0.70–0.81), so TTR also leans AI on my pieces.
- **Why the combining rule doesn't save it:** both signals lean AI, so they
  never differ by 0.4 and the disagreement rule never fires. The 0.6 weight on
  the model signal then puts the score over 0.65.
- **One problem, not eleven:** the system reads "plain and conventional" as "AI".
  It hits non-native writers hardest (my own pieces, FP03) because careful
  second-language writing is exactly that.

**Problem 2: AI text lands in `unsure`, and `unsure` lets it through. EV01–03, EV06–09, PI01, PI03 (9 attacks).**

- **Stage: the combining rule and the label mapping.** Each attack only has to
  fool *one* signal:
  - **EV01 and EV08 fool signal one.** Typos (EV01) and very short text (EV08,
    10 words) make GPT-2 more surprised, so the model score drops to 0.16 and
    0.25. Signal two still says AI (0.75 and 0.71), but the gap is over 0.4, so
    the disagreement rule pulls the score to 0.45–0.47.
  - **EV02, EV06, EV07 and PI01 fool signal two.** Broken-up sentences (EV02)
    and one long plus one short sentence (EV06) push sentence-length spread past
    the 0.65 human anchor. Spread carries half of signal two, so it drops to
    ~0.25. EV07 is a single padded sentence: spread can't be measured, so it
    counts as 0.5, and the extra commas set punctuation to fully human. PI01's
    short, choppy instruction sentences do the same as EV02.
  - **EV03, EV09 and PI03 sit just below the line** (0.60–0.61). A pasted
    quotation or a human opening paragraph dilutes the whole-text average.
    There's no per-section scoring, so a human paragraph bolted on (EV09)
    drags the AI body down.
- **Mechanism:** the disagreement rule sends any split to about 0.5, the unsure
  band is 0.30 wide, and `score_to_label` gives `unsure` a label that says
  "Nothing has been held back." Fooling either signal is enough to get published.
- **Pattern:** the signals aren't the weak point here. The rule is: fooling
  either signal counts as the two signals disagreeing, and disagreement passes
  the text through.

**Problem 3: the route trusts any string. MF02 and MF03 (2 attacks).**

- **MF02, stage: the route.** For a single character, `detector.perplexity` raises
  `ValueError("Text is too short to score")` when there are fewer than 3 tokens.
  `app.py::submit` only catches `DetectorUnavailable`, so the `ValueError` escapes
  as a 500 with the Werkzeug debug page. Nothing is written to the audit log.
- **MF03, stage: the route, then the label mapping.** Control characters pass
  the `text.strip()` check. GPT-2 scores them 0.0, and signal two finds no words
  so it returns its 0.5 default. The gap of 0.5 fires the disagreement rule:
  (0.2 + 0.5) / 2 = 0.35. That lands exactly on `HUMAN_THRESHOLD`, and `<=` makes
  it `human`. The route never checks that the text contains any words.
  

**Standalone failures**

EV05 human (0.29), stage: both signals.  A heavy human edit really does change the text sentence spread 0.68 and model score 0.32. Both signals read it correctly as mostly human-written. I count it as broke because the attack set does, but it's the hardest case for any detector, and arguably the right answer.

PI02 human (0.22), stage: signal one.** No model obeyed the instruction; my detector doesn't follow instructions. The fake SYSTEM header and odd phrasing are unusual tokens for GPT-2, so perplexity rises and the model score drops to 0.20. Signal two agrees at 0.25 (short, varied sentences, high TTR). The injection worked through statistics, not by being obeyed.

criteria 1–3 say each piece is 100–300 words, but 17 of my 19 human pieces and rewrites are shorter (31–98 words). Short text makes signal one less reliable (see EV08), so the criterion-1 result would be cleaner with full-length pieces. I'm recording this rather than dropping it.

---

## The Improvement

**What I changed:**

Signal two's weights in `stylometry.py::style_signal`: punctuation went from 0.25 to 0, and spread from 0.5 to 0.75. Vocabulary stays at 0.25. Nothing else changed; same anchors, same 0.6 / 0.4 combining rule, same
thresholds.

**Which diagnosis pointed at it:**

Problem 1. Punctuation's AI anchor is 0.06 marks per word, and plain human writing sits at 0.00–0.05, so the measure read fully AI on all 10 of my own pieces and all six false-positive attacks. It never pointed at anything but my writing style. I'd already seen this in Milestone 4 (the split case above: "low punctuation shouldn't count as AI-like"). The chatbot text I tested actually had more punctuation (0.09–0.11) than my writing.


| Option | My writing ai | FP rows ai | AI set caught | Evasions caught | AI − human gap |
|---|---|---|---|---|---|
| Before | 5 | 6 | 5/5 | 2 | 0.344 |
| Model weight 0.6 - 0.4 | 4 | 6 | 5/5 | 2 | 0.260 |
| AI threshold 0.65 - 0.75 | 2 | 5 | 4/5 | 1 | 0.344 |
| Drop punctuation (chosen) | 3 | 4 | 5/5 | 2 | 0.421 |


### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

56 attacks: 37 held, 17 broke, 2 not tested (before: 35 / 19 / 2).

| Family | Attacks | Held | Broke | Not tested | Change |
|---|---|---|---|---|---|
| evasion | 10 | 2 | 8 | 0 | — |
| false_positive | 8 | 4 | 4 | 0 | FP06, FP07 now held |
| prompt_injection | 6 | 3 | 3 | 0 | — |
| malformed (MF) | 8 | 6 | 2 | 0 | — |
| malformed (RQ) | 12 | 10 | 0 | 2 | — |
| flood_same_creator | 12 | 12 | 0 | 0 | — |

Rows whose verdict changed:

| ID | Before | After | Style score |
|---|---|---|---|
| FP06 (formal template) | `ai` 0.757 · BROKE | `unsure` 0.595 · HELD | 0.57 to 0.40 |
| FP07 (deliberate repetition) | `ai` 0.729 · BROKE | `unsure` 0.564 · HELD | 0.50 to 0.25 |

Criteria after the change (`results/run_2026-11-13_1638_after.md`,
`run_eval.py::main`; criterion 4 by the same appeal script as before):

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict | Before |
|---|---|---|---|---|---|---|
| 1. False positives on my writing | At most 1 of 10 `ai` | 3 of 10 | 3 of 10 | 3 of 10 | MISSED | 5 of 10 |
| 2. AI and human far apart | Gap ≥ 0.30 | 0.801 − 0.381 = 0.420 | 0.420 | 0.420 | MET | 0.345 |
| 3. Every label reachable | Each ≥ 2 | 3 / 4 / 7 | 3 / 4 / 7 | 3 / 4 / 7 | MET | 2 / 5 / 7 |
| 4. Appeals | 5/5 recorded, 3/3 fake to 404 | 5/5 · 3/3 | 5/5 · 3/3 | 5/5 · 3/3 | MET | same |
| 5. Bad input | 5/5 to 4xx + logged | 5/5 | 5/5 | 5/5 | MET | same |

**Did it help, and how do I know:**

Yes, for the problem it targeted. Real human writing called `ai` dropped from 5 of 10 to 3 of 10 on my own pieces, and from 6 to 4 on the false-positive attacks. The AI set is still caught 5 of 5, and the gap between AI and human grew from 0.345 to 0.420. Criterion 3 got a safer margin (`human` 2 to 3). The real run matched what the offline recalculation predicted (3 and 4), so the improvement comes from the change, not from noise. All three trials were identical.

The cost spread is now 75% of signal two, so the cheapest evasion, varying sentence length, works better. Signal two now reads **0.0** on EV02, EV05, EV06, PI01 and PI02 (before: about 0.25). No evasion verdict flipped, because they were already landing in `unsure`, but the AI-text scores moved further from the `ai` line: EV09 0.614 to 0.559, EV03 0.603 to 0.555, EV10 0.916 to 0.880. MF08 (60,000 characters) dropped from 0.848 to 0.652, just above the line. 

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**Criterion 1, still MISSED (3 of 10), and FP02–FP05 (4 attacks): signal one.**
The pieces still flagged are my protein-structure abstract (0.66), my Big Data paragraph (0.81) and my thank-you email (0.854). Their model scores are 0.60, 0.78 and 0.92. Signal two was no longer the cause; GPT-2 alone puts them over the line because academic prose and stock email phrases are very predictable. FP02–FP05 (formal report, non-native writer, rubric essay, docs) are the same mechanism. *What I'd do:* recalibrate the model signal's perplexity midpoint (45) on a larger set of real human writing, including non-native and formal writing, or have signal one count less when the text is short. 

**EV01–03, EV06–09, PI01, PI03 (9 attacks): `unsure` lets AI text through.**
*What I'd do:* stop publishing `unsure` as if nothing happened, and send it to
the same human review queue an appeal goes to. For EV09 (a human paragraph
bolted onto AI text), score each paragraph and flag a mix. *Why I stopped:*
that's a product policy change, not a scoring fix, and with the current false
positive rate it would also hold back real writers. 4 of my own 10 pieces land
in `unsure`.

**MF02 (500 crash) and MF03 (control characters to `human`): the route.**
*What I'd do:* in `app.py::submit`, catch the detector's `ValueError` and return
a 400 with a logged rejection, and reject text with fewer than ~20 real words
before either signal runs. *Why I stopped:* I kept to one change so the
before/after comparison shows one cause. This is the cheapest fix left and the
next one I'd make.

**EV05 and PI02.** EV05 is a heavy human edit, and both signals reading it as
human is arguably right. PI02 got through because the fake `SYSTEM:` text
raises perplexity, not because anything obeyed it. Input validation wouldn't
catch it. It's the same "fool signal one" problem as EV01.

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I'd keep leaning toward fewer wrong accusations: give the `ai` label only at
high confidence, and send `unsure` to a person instead of publishing it
silently. The site, its readers and the reviewers pay for that, with more AI
text getting published and a longer review queue, instead of a writer like
FP03, who can't prove they wrote their own words.


<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
