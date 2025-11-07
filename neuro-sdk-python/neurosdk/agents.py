from __future__ import annotations
from datetime import datetime
from typing import Dict, Any, List
import uuid
from .types import CTVA, EvaluatorScore, RoyaltyRule
from .receipts import generate_keypair, make_poi, make_poa
from .safety import cbc_envelope

class NeuroAgent:
    def __init__(self, agent_id: str, robot_id: str):
        self.agent_id = agent_id
        self.robot_id = robot_id
        self.priv_hex, self.pub_hex = generate_keypair()

    def sense(self) -> Dict[str, Any]:
        return {"vision": {"objects": ["cup", "book"]}, "tactile": {"force_n": 8.2}}

    def think(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        plan = {"goal": "place_cup_on_shelf", "steps": ["grasp", "move", "place"]}
        return plan

    def act(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        pose = (0.2, 0.1)
        safe = cbc_envelope(pose, ((-1.0, 1.0), (-1.0, 1.0)))
        return {"success": safe, "final_pose": pose}

    def learn(self, outcome: Dict[str, Any]) -> Dict[str, Any]:
        return {"delta": {"grasp": +0.01 if outcome.get("success") else -0.01}}

    def run_once(self) -> CTVA:
        inputs = self.sense()
        plan = self.think(inputs)
        outcome = self.act(plan)
        _ = self.learn(outcome)

        poi = make_poi(plan, self.priv_hex, self.pub_hex)
        poa = make_poa({"outcome": outcome}, self.priv_hex, self.pub_hex)

        ctva = CTVA(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow(),
            agent_id=self.agent_id,
            robot_id=self.robot_id,
            inputs=inputs,
            outputs=outcome,
            poi=poi,
            poa=poa,
            lineage=["init:v0"],
            evaluators=[EvaluatorScore(name="safety", score=1.0 if outcome["success"] else 0.0)],
            royalties=[RoyaltyRule(pct=0.02, receiver=self.agent_id)]
        )
        return ctva.model_dump()