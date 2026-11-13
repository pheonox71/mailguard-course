#!/usr/bin/env python3
"""Ensure each quiz markdown has a matching answer key with the same item count."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEM = re.compile(r"^\d+\.\s+")


def count_items(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if ITEM.match(line))


def main() -> int:
    errors: list[str] = []
    quizzes = sorted(ROOT.glob("*/quizzes/*.md"))
    for quiz in quizzes:
        if quiz.name.startswith("README"):
            continue
        key = quiz.parent / "answer-keys" / quiz.name
        if not key.exists():
            errors.append(f"missing answer key for {quiz.relative_to(ROOT)}")
            continue
        qc, kc = count_items(quiz), count_items(key)
        if qc < 5:
            errors.append(f"{quiz.relative_to(ROOT)} has {qc} items (want 5–8)")
        if qc != kc:
            errors.append(
                f"count mismatch {quiz.relative_to(ROOT)}={qc} vs {key.relative_to(ROOT)}={kc}"
            )
    # Module 00 must not ship quizzes
    if list((ROOT / "00-setup").glob("quizzes/**/*.md")):
        errors.append("00-setup must not contain quizzes")
    if errors:
        print("Quiz/answer-key check failed:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Quiz/answer-key counts OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
