import os, json, hashlib, secrets
from dataclasses import dataclass
from typing import Dict, Tuple
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization

def _sha256(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()

def generate_keypair() -> Tuple[str, str]:
    priv = Ed25519PrivateKey.generate()
    pub = priv.public_key()
    priv_hex = priv.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    ).hex()
    pub_hex = pub.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    ).hex()
    return priv_hex, pub_hex

def sign(priv_hex: str, payload: Dict) -> str:
    priv = Ed25519PrivateKey.from_private_bytes(bytes.fromhex(priv_hex))
    message = json.dumps(payload, sort_keys=True).encode()
    sig = priv.sign(message)
    return sig.hex()

def verify(pub_hex: str, payload: Dict, sig_hex: str) -> bool:
    pub = Ed25519PublicKey.from_public_bytes(bytes.fromhex(pub_hex))
    message = json.dumps(payload, sort_keys=True).encode()
    try:
        pub.verify(bytes.fromhex(sig_hex), message)
        return True
    except Exception:
        return False

def make_poi(inference_plan: Dict, priv_hex: str, pub_hex: str) -> Dict:
    h = _sha256({"inference_plan": inference_plan})
    sig = sign(priv_hex, {"hash": h})
    return {"kind": "PoI", "hash_hex": h, "signature_hex": sig, "public_key_hex": pub_hex}

def make_poa(action_trace: Dict, priv_hex: str, pub_hex: str) -> Dict:
    h = _sha256({"action_trace": action_trace})
    sig = sign(priv_hex, {"hash": h})
    return {"kind": "PoA", "hash_hex": h, "signature_hex": sig, "public_key_hex": pub_hex}