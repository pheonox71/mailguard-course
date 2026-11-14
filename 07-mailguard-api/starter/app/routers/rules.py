"""Rules CRUD + evaluate endpoints."""

from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from starter.app.store import MemoryStore, MessageIn, RuleRecord, evaluate

Decision = Literal["hold", "allow", "reject"]


class RuleCreate(BaseModel):
    name: str = Field(min_length=1)
    decision: Decision
    recipient_domain: str | None = None
    contains: str | None = None


class RuleOut(BaseModel):
    id: str
    name: str
    decision: Decision
    recipient_domain: str | None = None
    contains: str | None = None


class EvaluateIn(BaseModel):
    sender: str
    recipients: list[str] = Field(min_length=1)
    subject: str = ""
    body: str = ""
    default: Decision = "allow"


class EvaluateOut(BaseModel):
    decision: Decision


def build_rules_router(store: MemoryStore) -> APIRouter:
    r = APIRouter(tags=["rules"])

    @r.post("/rules", response_model=RuleOut, status_code=201)
    def create_rule(body: RuleCreate) -> RuleOut:
        rule = store.add_rule(
            RuleRecord(
                name=body.name,
                decision=body.decision,
                recipient_domain=body.recipient_domain,
                contains=body.contains,
            )
        )
        return RuleOut(
            id=rule.id,
            name=rule.name,
            decision=rule.decision,
            recipient_domain=rule.recipient_domain,
            contains=rule.contains,
        )

    @r.get("/rules", response_model=list[RuleOut])
    def list_rules() -> list[RuleOut]:
        return [
            RuleOut(
                id=rule.id,
                name=rule.name,
                decision=rule.decision,
                recipient_domain=rule.recipient_domain,
                contains=rule.contains,
            )
            for rule in store.list_rules()
        ]

    @r.get("/rules/{rule_id}", response_model=RuleOut)
    def get_rule(rule_id: str) -> RuleOut:
        rule = store.get_rule(rule_id)
        if rule is None:
            raise HTTPException(status_code=404, detail="rule not found")
        return RuleOut(
            id=rule.id,
            name=rule.name,
            decision=rule.decision,
            recipient_domain=rule.recipient_domain,
            contains=rule.contains,
        )

    @r.delete("/rules/{rule_id}", status_code=204)
    def delete_rule(rule_id: str) -> None:
        if not store.delete_rule(rule_id):
            raise HTTPException(status_code=404, detail="rule not found")

    @r.post("/evaluate", response_model=EvaluateOut)
    def evaluate_message(body: EvaluateIn) -> EvaluateOut:
        msg = MessageIn(
            sender=body.sender,
            recipients=tuple(body.recipients),
            subject=body.subject,
            body=body.body,
        )
        decision = evaluate(msg, store.list_rules(), default=body.default)
        return EvaluateOut(decision=decision)

    return r
