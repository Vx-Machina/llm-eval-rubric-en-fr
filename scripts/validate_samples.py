#!/usr/bin/env python3
"""Validate samples/graded_samples.jsonl against rubric/rubric.yaml and print weighted scores.

Standard library only (a tiny parser reads the simple rubric.yaml layout used here).
Usage: python3 scripts/validate_samples.py [path/to/samples.jsonl]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_rubric(path):
    weights, caps, section = {}, {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("criteria:"):
            section = "criteria"
        elif line.startswith("critical_errors:"):
            section = "caps"
        m = re.match(r"\s+(\w+):\s*\{(weight|cap):\s*([\d.]+)", line)
        if m:
            (weights if section == "criteria" else caps)[m.group(1)] = float(m.group(3))
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        raise SystemExit(f"Rubric weights sum to {sum(weights.values())}, expected 1.0")
    return weights, caps


def weighted(scores, weights, errors, caps):
    value = round(sum(scores[k] * w for k, w in weights.items()), 2)
    if errors:
        value = min(value, min(caps[c] for c in errors))
    return value


def main():
    weights, caps = load_rubric(ROOT / "rubric" / "rubric.yaml")
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "samples" / "graded_samples.jsonl"
    problems = 0
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        s = json.loads(line)
        sid = s.get("id", f"line {n}")
        errs = []
        if set(s["scores"]) != set(weights):
            errs.append(f"criteria mismatch: {sorted(set(s['scores']) ^ set(weights))}")
        elif not all(isinstance(v, int) and 1 <= v <= 5 for v in s["scores"].values()):
            errs.append("scores must be integers 1-5")
        if set(s.get("rationale", {})) != set(weights):
            errs.append("rationale must have one entry per criterion")
        unknown = [c for c in s.get("critical_errors", []) if c not in caps]
        if unknown:
            errs.append(f"unknown critical errors: {unknown}")
        if not errs:
            got = weighted(s["scores"], weights, s.get("critical_errors", []), caps)
            if abs(got - s.get("expected_weighted", -1)) > 0.005:
                errs.append(f"expected_weighted {s.get('expected_weighted')} != computed {got}")
            flag = ",".join(s.get("critical_errors", [])) or "-"
            print(f"{sid:<8} {s['locale']:<6} {got:>4.2f}  caps:{flag}")
        for e in errs:
            print(f"{sid}: ERROR {e}")
        problems += len(errs)
    print("OK" if not problems else f"{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
