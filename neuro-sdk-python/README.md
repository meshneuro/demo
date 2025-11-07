# neuro-sdk-python

NeuroMesh defines a **humanoid-first intelligence layer on Solana** that any robot can install to become **software-defined, safety-bounded, and market-connected**. Each robot runs agentic cognition locally (on-robot CPU/NPU/GPU), generating verifiable “thoughts” and “actions” recorded as **Composite Thought/Action Vectors (CTV/A)** with lineage, evaluator scores, and royalty rules.

This SDK provides a realistic local interface to:
- Build **agents** with a clear lifecycle (`sense → think → act → learn`)
- Emit **PoI** (Proof-of-Inference) and **PoA** (Proof-of-Action) receipts
- Package receipts into **CTV/A** with lineage + evaluator scores
- Mint **per-robot data rights** (nDATA-R) via DOC/PLID stubs
- Run a basic **CBC safety envelope** check

> Note: This is an MVP/dev toolkit; the Solana on-chain integration and hardware attestation are stubbed but the code and APIs are structured to scale.

## Quickstart

```bash
pip install -e .
python examples/run_agent_demo.py
python examples/simulate_safety_check.py
python examples/mint_data_rights.py
```