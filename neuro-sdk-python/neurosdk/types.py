from __future__ import annotations
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Evidence(BaseModel):
    kind: str
    hash_hex: str
    signature_hex: Optional[str] = None
    public_key_hex: Optional[str] = None

class EvaluatorScore(BaseModel):
    name: str
    score: float
    notes: Optional[str] = None

class RoyaltyRule(BaseModel):
    pct: float = Field(ge=0, le=1)
    receiver: str

class CTVA(BaseModel):
    id: str
    timestamp: datetime
    agent_id: str
    robot_id: str
    inputs: Dict
    outputs: Dict
    poi: Evidence
    poa: Evidence
    lineage: List[str] = []
    evaluators: List[EvaluatorScore] = []
    royalties: List[RoyaltyRule] = []