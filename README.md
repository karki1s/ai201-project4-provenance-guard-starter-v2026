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
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



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
