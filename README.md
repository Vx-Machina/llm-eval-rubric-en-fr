# llm-eval-rubric-en-fr

**A bilingual (English / French) rubric for evaluating LLM answers, a French-localisation checklist, and sample graded prompts.**
*Grille d'évaluation bilingue (anglais / français) pour juger les réponses de modèles de langage, avec une checklist de localisation et des exemples notés.*

> ⚠️ **All prompts and responses in `samples/` are SAMPLE material, written for this repository to illustrate the rubric.** They are not outputs from any specific model, project, client or employer.

## Why this exists
Most rubrics are written in English and then translated. French answers often fail in ways those rubrics never test: grammatical but unnatural phrasing, hidden anglicisms, the wrong register (*tu* vs *vous*), and broken French typography. This repo treats **language naturalness and locale fit** as a scored criterion of their own, next to accuracy and instruction following.

## Contents
| Path | What it is |
|---|---|
| [`rubric/rubric_en.md`](rubric/rubric_en.md) | Rubric in English: 7 criteria, 1–5 anchors, weights, critical-error caps |
| [`rubric/grille_fr.md`](rubric/grille_fr.md) | The same rubric in French |
| [`rubric/rubric.yaml`](rubric/rubric.yaml) | Machine-readable weights and caps |
| [`guidelines/french-localisation-checklist.md`](guidelines/french-localisation-checklist.md) | What to check in French (France) answers |
| [`samples/graded_samples.jsonl`](samples/graded_samples.jsonl) | 8 SAMPLE prompt/response pairs (4 EN, 4 FR) with scores and written rationales |
| [`scripts/validate_samples.py`](scripts/validate_samples.py) | Validates the samples against the rubric and prints weighted scores |

## How to use
1. Read the prompt and the response. Note any **critical errors** first (see the rubric).
2. Score each criterion from 1 to 5 using the anchors. Write one or two sentences of rationale per criterion that cite the exact text.
3. Compute the weighted score. If there's a critical error, apply its cap.
4. Run `python3 scripts/validate_samples.py` to check the format and the arithmetic (Python 3.8+, standard library only).

## Scoring at a glance
| Criterion | Weight |
|---|---|
| Instruction following | 20% |
| Accuracy & factual grounding | 25% |
| Completeness & helpfulness | 15% |
| Language quality & naturalness (locale) | 15% |
| Register & tone | 10% |
| Safety & appropriateness | 10% |
| Formatting & readability | 5% |

## About
Maintained by **David Amos (Visual Machinist)**, VM Studios / Fractal Studios: a bilingual EN–FR creative technologist (robotics, 3D, community management) focused on AI evaluation. [vx-machina.xyz](https://vx-machina.xyz) · [LinkedIn](https://www.linkedin.com/in/visual-machinist/)

## Licence
Rubric, guidelines and samples: **CC BY 4.0**. Script: **MIT**. See [`LICENSE`](LICENSE).

---
### 🇫🇷 En français
Ce dépôt propose une grille d'évaluation des réponses de LLM utilisable en anglais et en français. Elle note séparément le **naturel de la langue et l'adéquation à la locale** (fr-FR) : anglicismes, registre, typographie française. Tous les exemples de `samples/` sont **fictifs** et rédigés pour illustrer la grille. Voir [`rubric/grille_fr.md`](rubric/grille_fr.md).
