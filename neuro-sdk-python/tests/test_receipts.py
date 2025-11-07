from neurosdk.receipts import generate_keypair, make_poi, verify

def test_poi_sign_verify():
    priv, pub = generate_keypair()
    plan = {"goal": "demo"}
    poi = make_poi(plan, priv, pub)
    assert verify(poi["public_key_hex"], {"hash": poi["hash_hex"]}, poi["signature_hex"])