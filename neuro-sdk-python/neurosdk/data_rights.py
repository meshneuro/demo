import hashlib, json, time, os
from typing import Dict

def _h(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()

def mint_doc(robot_did: str, operator_did: str, modality: dict, site: str) -> Dict:
    doc = {
        "robot_did": robot_did,
        "operator_did": operator_did,
        "site": site,
        "modality": modality,
        "issued_at": int(time.time())
    }
    doc["doc_hash"] = _h(doc)
    return doc

def mint_plid(window_hashes: list[str]) -> Dict:
    merkle_root = _h(window_hashes)
    return {"plid": merkle_root, "leaves": window_hashes}

def mint_ndatar_lot(doc: Dict, plid: Dict, royalty_curve: Dict) -> Dict:
    lot = {
        "doc_hash": doc["doc_hash"],
        "plid": plid["plid"],
        "royalty_curve": royalty_curve,
        "id": _h({"doc": doc["doc_hash"], "plid": plid["plid"]})
    }
    return lot