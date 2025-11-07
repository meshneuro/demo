import uuid, time, json
from typing import Dict

def connect_to_mesh(endpoint: str = "http://localhost:8787") -> Dict:
    # Stub that would negotiate node identity, auth, and capabilities
    return {"endpoint": endpoint, "session_id": str(uuid.uuid4())}

def publish_receipt(receipt: Dict) -> Dict:
    # Stub: In production, push to Solana / receipts service
    return {"status": "accepted", "id": receipt.get("id", str(uuid.uuid4())), "ts": int(time.time())}