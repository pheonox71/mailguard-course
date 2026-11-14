#!/usr/bin/env python3
"""Capstone demo runner for the outbound mail filter.

Prints the demo path, then invokes katas.mail_filter when the student has
implemented it. Safe to run against stubs: catches NotImplementedError and
shows the remaining steps.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _banner(step: str) -> None:
    print(f"\n==> {step}")


def main() -> int:
    _banner("Capstone demo — MailGuard outbound filter")
    print(
        "This script walks a stranger-friendly demo path.\n"
        "Implement katas/mail_filter.py until pytest -q is green, then re-run."
    )

    steps = [
        "Load sample outbound messages (sender, recipients, subject, body)",
        "Load ordered rules (first match wins: hold / allow / reject)",
        "Evaluate each message; collect the hold queue",
        "Print decisions for the operator demo notes",
    ]
    for i, step in enumerate(steps, start=1):
        print(f"  {i}. {step}")

    try:
        from katas.mail_filter import Message, Rule, evaluate, held_queue
    except ImportError as exc:
        print(f"\nCould not import katas.mail_filter: {exc}", file=sys.stderr)
        return 1

    messages = [
        Message(
            sender="alice@corp.example",
            recipients=("bob@corp.example",),
            subject="Weekly notes",
            body="Internal sync notes.",
        ),
        Message(
            sender="alice@corp.example",
            recipients=("cfo@partner.example",),
            subject="Urgent wire instructions",
            body="Please process the attached payment today.",
        ),
        Message(
            sender="alice@corp.example",
            recipients=("vendor@evil.example",),
            subject="Invoice copy",
            body="See attached W-2 forms for all staff.",
        ),
    ]

    rules = [
        Rule(name="block-w2", decision="reject", contains="w-2"),
        Rule(
            name="hold-external-urgent",
            decision="hold",
            contains="urgent",
            require_external=True,
        ),
        Rule(
            name="hold-partner-domain",
            decision="hold",
            recipient_domain="partner.example",
        ),
    ]

    _banner("Evaluate sample messages")
    try:
        for msg in messages:
            decision = evaluate(msg, rules)
            print(f"  [{decision:6}] {msg.subject!r} -> {', '.join(msg.recipients)}")

        held = held_queue(messages, rules)
        _banner(f"Hold queue ({len(held)} message(s))")
        for msg in held:
            print(f"  - {msg.subject!r} from {msg.sender}")
    except NotImplementedError:
        print(
            "\nkatas/mail_filter.py still has NotImplementedError stubs.\n"
            "Implement is_external, matches, evaluate, and held_queue, then:\n"
            "  cd 19-capstone && pytest -q && python3 starter/run_demo.py"
        )
        return 2

    _banner("Demo complete")
    print("Next: fill assignments/capstone_self_grade.md under my-work/assignments/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
