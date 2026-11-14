#!/usr/bin/env python3
"""Convert a questions-only quiz markdown file into a fillable PDF (AcroForm)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Flowable,
)
from reportlab.pdfbase import pdfform


BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
QUESTION_RE = re.compile(r"^(\d+)\.\s+(.*)$")


def md_inline_to_xml(text: str) -> str:
    """Light markdown → ReportLab XML for Paragraph."""
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    text = LINK_RE.sub(r"\1", text)
    text = BOLD_RE.sub(r"<b>\1</b>", text)
    text = ITALIC_RE.sub(r"<i>\1</i>", text)
    text = CODE_RE.sub(r"<font face='Courier'>\1</font>", text)
    return text


def strip_answer_key(markdown: str) -> str:
    patterns = [
        r"\n---\s*\n+##\s*Answer key[\s\S]*$",
        r"\n##\s*Answer key[\s\S]*$",
        r"\n##\s*Answers?[\s\S]*$",
        r"\n+Answer key:\s*\[[\s\S]*$",
    ]
    out = markdown
    for pat in patterns:
        next_out = re.sub(pat, "\n", out, flags=re.IGNORECASE)
        if next_out != out:
            out = next_out
            break
    return out.strip() + "\n"


def parse_quiz(markdown: str) -> tuple[str, list[str], list[tuple[str, str]]]:
    """Return (title, intro_paragraphs, [(number, question_text), ...])."""
    lines = markdown.splitlines()
    title = "Quiz"
    intro: list[str] = []
    questions: list[tuple[str, str]] = []
    i = 0

    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        i = 1
        while i < len(lines) and not lines[i].strip():
            i += 1

    # Collect intro until first numbered question
    buf: list[str] = []
    while i < len(lines):
        line = lines[i]
        if QUESTION_RE.match(line.strip()):
            break
        if line.strip() == "---":
            i += 1
            continue
        if not line.strip():
            if buf:
                intro.append(" ".join(buf))
                buf = []
        else:
            buf.append(line.strip())
        i += 1
    if buf:
        intro.append(" ".join(buf))

    while i < len(lines):
        line = lines[i].strip()
        m = QUESTION_RE.match(line)
        if m:
            num, text = m.group(1), m.group(2)
            i += 1
            cont: list[str] = []
            while i < len(lines):
                nxt = lines[i]
                if QUESTION_RE.match(nxt.strip()) or nxt.strip().startswith("## "):
                    break
                if nxt.strip() and nxt.strip() != "---":
                    cont.append(nxt.strip())
                i += 1
            if cont:
                text = text + " " + " ".join(cont)
            questions.append((num, text))
        else:
            i += 1

    return title, intro, questions


class AnswerField(Flowable):
    """Multiline AcroForm text field sized for a short written answer."""

    def __init__(self, name: str, width: float, height: float = 54):
        super().__init__()
        self.name = name
        self.box_width = width
        self.box_height = height
        self.width = width
        self.height = height

    def wrap(self, availWidth, availHeight):
        self.width = min(self.box_width, availWidth)
        return self.width, self.height

    def draw(self):
        form = self.canv.acroForm
        form.textfield(
            name=self.name,
            tooltip="Type your answer here",
            x=0,
            y=0,
            width=self.width,
            height=self.height,
            borderWidth=0.8,
            borderColor=HexColor("#2f6b66"),
            fillColor=HexColor("#f7fbfa"),
            textColor=HexColor("#0b1c24"),
            forceBorder=True,
            fontSize=10,
            fieldFlags="multiline",
        )


def build_pdf(src: Path, dest: Path) -> int:
    raw = src.read_text(encoding="utf-8")
    body = strip_answer_key(raw)
    title, intro, questions = parse_quiz(body)

    if not questions:
        print(f"skip (no numbered questions): {src}", file=sys.stderr)
        return 0

    dest.parent.mkdir(parents=True, exist_ok=True)

    page_w, page_h = letter
    margin = 0.75 * inch
    usable_w = page_w - 2 * margin

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "QuizTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=HexColor("#0b1c24"),
        spaceAfter=8,
    )
    meta_style = ParagraphStyle(
        "QuizMeta",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=HexColor("#3d5a5a"),
        spaceAfter=10,
    )
    body_style = ParagraphStyle(
        "QuizBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        textColor=HexColor("#12262f"),
        spaceAfter=8,
    )
    q_style = ParagraphStyle(
        "QuizQ",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        textColor=HexColor("#0b1c24"),
        spaceBefore=10,
        spaceAfter=4,
    )

    story: list = []
    story.append(Paragraph(md_inline_to_xml(title), title_style))
    story.append(
        Paragraph(
            "Fillable quiz — type answers in the fields. Blank copies are already under "
            "<font face='Courier'>my-work/quizzes/</font>; answer them in place. "
            "Answer keys are not included.",
            meta_style,
        )
    )
    for para in intro:
        story.append(Paragraph(md_inline_to_xml(para), body_style))

    for num, text in questions:
        story.append(Paragraph(f"<b>{num}.</b> {md_inline_to_xml(text)}", q_style))
        story.append(AnswerField(f"q{num}", usable_w))
        story.append(Spacer(1, 4))

    doc = BaseDocTemplate(
        str(dest),
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin,
        title=title,
        author="MailGuard Course",
    )
    frame = Frame(margin, margin, usable_w, page_h - 2 * margin, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame)])
    doc.build(story)
    # Ensure form catalog exists (reportlab registers fields during draw)
    _ = pdfform
    return len(questions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("src", type=Path, help="Quiz markdown (questions)")
    parser.add_argument("dest", type=Path, help="Output PDF path")
    args = parser.parse_args()
    count = build_pdf(args.src, args.dest)
    if count:
        print(f"wrote {args.dest} ({count} fields)")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
