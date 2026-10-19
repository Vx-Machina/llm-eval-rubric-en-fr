# Samples · Exemples

> ⚠️ **SAMPLE material.** Every prompt and response in `graded_samples.jsonl` was written for this repository to demonstrate the rubric. None is a real output from a specific model, project, client or employer. The responses deliberately include typical faults (calques, missed constraints, missing safety notes) so the grading can be shown.

Each line is a JSON object:
| Field | Meaning |
|---|---|
| `id` | Sample ID |
| `locale` | `en-GB` or `fr-FR` |
| `prompt` | The user request |
| `response` | The (sample) model answer being graded |
| `scores` | One 1–5 integer per rubric criterion (see `rubric/rubric.yaml`) |
| `critical_errors` | List of critical-error codes (`C1`–`C4`), or empty |
| `rationale` | One short justification per criterion |
| `expected_weighted` | The weighted score after caps, checked by `scripts/validate_samples.py` |
