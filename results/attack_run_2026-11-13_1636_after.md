# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-13 16:36
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `1e9a6e8b-0594-469e-8765-ec10454323ff` | unsure | 0.449 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a30a473a-a969-491a-ba96-02c15666c0f4` | unsure | 0.428 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1fc3e095-83b3-4647-83d6-6213e379a475` | unsure | 0.555 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `81f79ce7-4eff-4250-a28f-7af568136b92` | ai | 0.667 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `d3ce7589-535e-4d05-81b6-6485caaa4829` | human | 0.193 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `94e658fa-565f-4dc8-8a29-8e06e3e05b92` | unsure | 0.422 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ced65835-e571-44cb-bef8-1923957cc376` | unsure | 0.505 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `501b88f3-cacd-4621-811d-312901cffee7` | unsure | 0.461 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b7a669cd-d1d8-45de-a50d-4989ead80d56` | unsure | 0.559 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `f9323183-3459-450b-9f13-50c5ab6ccfbe` | ai | 0.880 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `12b86a43-f9bf-4285-969f-a7622d61025d` | unsure | 0.544 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `2fd89a0a-a851-4356-a4a4-5a70867e9d74` | ai | 0.797 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8363c22e-d542-4750-8762-6765066d0707` | ai | 0.745 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c7277187-774d-4418-936a-e67fbbc3d2ad` | ai | 0.732 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f8601238-5ccd-47be-820b-e415c8f87c95` | ai | 0.860 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `1ee56071-2777-411e-8cf6-213850bc13f5` | unsure | 0.595 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `fa510f79-d7c3-49ff-9f31-722292af4137` | unsure | 0.564 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `e6bc9aec-c443-465b-9937-6ecdafebc332` | unsure | 0.356 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e6e38744-3cca-4661-b6f6-29443b742578` | unsure | 0.389 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2867753b-3e3c-4327-a128-f1479b2b42be` | human | 0.123 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b0bf667b-14c5-44ad-9f18-a21d83298ff8` | unsure | 0.587 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `3851e267-15a1-4767-a121-744a465f1eb1` | unsure | 0.490 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `142b3a9f-890d-42dc-80a6-021a8320bf79` | unsure | 0.518 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a8b90680-96c5-489d-89e5-ff2a26079fcd` | unsure | 0.513 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `fe712d0a-4d9f-47dc-b2f4-0badeaa27a5a` | human | 0.150 |  |
| MF04 | malformed | text is only punctuation | 200 | `f82f66e4-eef4-47f9-9a2c-9c56c5c62ef0` | unsure | 0.353 |  |
| MF05 | malformed | text is a very long single word | 200 | `4d425f96-fa65-4218-a238-541cf6ee8aa3` | unsure | 0.624 |  |
| MF06 | malformed | text is emoji only | 200 | `1381fcef-3f23-4d6d-80f6-a1309e0f7296` | unsure | 0.649 |  |
| MF07 | malformed | text is right-to-left script | 200 | `48d63c39-9edf-4943-a117-1bba337d7086` | unsure | 0.622 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `ecf10a06-ba08-4228-ad1b-305609fac37f` | ai | 0.652 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `87e70094-3085-4e64-9f9e-7ec4c5832395` | human | 0.167 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5393610f-ed32-4a26-950d-db0bab4395ea` | human | 0.167 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b4665b41-afc8-4cec-bbf4-347658a259b3` | human | 0.167 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2d4b5932-e53f-498e-984d-8fa5286377c6` | human | 0.167 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f5843f96-761a-4e3b-93ac-d145f68ee48b` | human | 0.167 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "1e9a6e8b-0594-469e-8765-ec10454323ff",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.449,
  "model_score": 0.164,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "a30a473a-a969-491a-ba96-02c15666c0f4",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.428,
  "model_score": 0.594,
  "style_score": 0.0,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "1fc3e095-83b3-4647-83d6-6213e379a475",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.555,
  "model_score": 0.666,
  "style_score": 0.387,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "81f79ce7-4eff-4250-a28f-7af568136b92",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.667,
  "model_score": 0.611,
  "style_score": 0.75,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "d3ce7589-535e-4d05-81b6-6485caaa4829",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.193,
  "model_score": 0.321,
  "style_score": 0.0,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "94e658fa-565f-4dc8-8a29-8e06e3e05b92",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.422,
  "model_score": 0.573,
  "style_score": 0.002,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "ced65835-e571-44cb-bef8-1923957cc376",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.505,
  "model_score": 0.586,
  "style_score": 0.383,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "501b88f3-cacd-4621-811d-312901cffee7",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.461,
  "model_score": 0.245,
  "style_score": 0.688,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b7a669cd-d1d8-45de-a50d-4989ead80d56",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.559,
  "model_score": 0.704,
  "style_score": 0.342,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "f9323183-3459-450b-9f13-50c5ab6ccfbe",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.88,
  "model_score": 0.979,
  "style_score": 0.73,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "12b86a43-f9bf-4285-969f-a7622d61025d",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.544,
  "model_score": 0.618,
  "style_score": 0.434,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "2fd89a0a-a851-4356-a4a4-5a70867e9d74",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.797,
  "model_score": 0.739,
  "style_score": 0.884,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8363c22e-d542-4750-8762-6765066d0707",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.745,
  "model_score": 0.805,
  "style_score": 0.654,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c7277187-774d-4418-936a-e67fbbc3d2ad",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.732,
  "model_score": 0.833,
  "style_score": 0.579,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f8601238-5ccd-47be-820b-e415c8f87c95",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.86,
  "model_score": 0.8,
  "style_score": 0.95,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "1ee56071-2777-411e-8cf6-213850bc13f5",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.595,
  "model_score": 0.881,
  "style_score": 0.402,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "fa510f79-d7c3-49ff-9f31-722292af4137",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.564,
  "model_score": 0.882,
  "style_score": 0.25,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "e6bc9aec-c443-465b-9937-6ecdafebc332",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.356,
  "model_score": 0.322,
  "style_score": 0.407,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e6e38744-3cca-4661-b6f6-29443b742578",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.389,
  "model_score": 0.463,
  "style_score": 0.0,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "2867753b-3e3c-4327-a128-f1479b2b42be",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.123,
  "model_score": 0.204,
  "style_score": 0.0,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b0bf667b-14c5-44ad-9f18-a21d83298ff8",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.587,
  "model_score": 0.594,
  "style_score": 0.576,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "3851e267-15a1-4767-a121-744a465f1eb1",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.49,
  "model_score": 0.5,
  "style_score": 0.475,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "142b3a9f-890d-42dc-80a6-021a8320bf79",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.518,
  "model_score": 0.64,
  "style_score": 0.335,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "a8b90680-96c5-489d-89e5-ff2a26079fcd",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.513,
  "model_score": 0.558,
  "style_score": 0.446,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "fe712d0a-4d9f-47dc-b2f4-0badeaa27a5a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.15,
  "model_score": 0.0,
  "style_score": 0.375,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "f82f66e4-eef4-47f9-9a2c-9c56c5c62ef0",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.353,
  "model_score": 0.011,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "4d425f96-fa65-4218-a238-541cf6ee8aa3",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.624,
  "model_score": 0.998,
  "style_score": 0.375,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "1381fcef-3f23-4d6d-80f6-a1309e0f7296",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.649,
  "model_score": 0.997,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "48d63c39-9edf-4943-a117-1bba337d7086",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.622,
  "model_score": 0.906,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with AI help. Our checks gave mixed results, and that isn't an accusation. Nothing has been held back. If you'd like to tell us how you wrote it, you can send an appeal.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "ecf10a06-ba08-4228-ad1b-305609fac37f",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.652,
  "model_score": 0.988,
  "style_score": 0.526,
  "label": "This looks a lot like writing produced by an AI tool. Our checks can be wrong, especially with plain, simple writing. If you wrote this yourself, please send an appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "87e70094-3085-4e64-9f9e-7ec4c5832395",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.167,
  "model_score": 0.029,
  "style_score": 0.375,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "5393610f-ed32-4a26-950d-db0bab4395ea",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.167,
  "model_score": 0.029,
  "style_score": 0.375,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "b4665b41-afc8-4cec-bbf4-347658a259b3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.167,
  "model_score": 0.029,
  "style_score": 0.375,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "2d4b5932-e53f-498e-984d-8fa5286377c6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.167,
  "model_score": 0.029,
  "style_score": 0.375,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "f5843f96-761a-4e3b-93ac-d145f68ee48b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.167,
  "model_score": 0.029,
  "style_score": 0.375,
  "label": "We think this was probably written by a person. Our checks found nothing that suggests it was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
