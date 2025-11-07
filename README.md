# NeuroMesh SDK (Python)

**NeuroMesh SDK** defines the *humanoid-first intelligence layer* that any robot or agent can install to become **software-defined**, **safety-bounded**, and **market-connected** within the Solana-based NeuroMesh Superbrain.

The SDK provides a local runtime and APIs for on-robot cognition, proof generation, and attested data ownership.  
Each agent runs autonomous reasoning loops (`sense → think → act → learn`), producing verifiable *Composite Thought/Action Vectors (CTV/A)* that encode perception, action, safety verification, evaluator scores, and royalty metadata.

---

## Architecture Overview

At its core, the SDK emulates the **NeuroOS-H** stack:

```
┌─────────────────────────────┐
│ Agent Runtime (NeuroAgent)  │
│  ├─ Perception (sense)      │
│  ├─ Planning (think)        │
│  ├─ Actuation (act)         │
│  └─ Adaptation (learn)      │
├─────────────────────────────┤
│ Proof System (PoI / PoA)    │
│  └─ Hash + Signature Chains │
├─────────────────────────────┤
│ Safety Envelope (CBC)       │
│  └─ Runtime invariant check │
├─────────────────────────────┤
│ Data Rights (DOC / PLID)    │
│  └─ Tokenised Data Assets   │
└─────────────────────────────┘
```

Each cognitive cycle emits a **CTV/A**, the atomic unit of verifiable intelligence in NeuroMesh.

---

## Core Features

| Feature | Description |
|----------|--------------|
| `NeuroAgent` | Base class implementing the full agent lifecycle with embedded Proof-of-Inference (PoI) and Proof-of-Action (PoA) generation. |
| **CTV/A Generator** | Bundles sensory inputs, planned actions, verification receipts, and evaluator results into an immutable object. |
| **CBC Safety Envelope** | Ensures motion/interaction constraints remain within certifiable bounds. |
| **Data Rights Minting** | Produces cryptographically verifiable Data Ownership Certificates (DOC) and Perception Lineage IDs (PLID). |
| **Network Hooks** | Simulated endpoints for mesh discovery and receipt publication. |

---

## Mathematical Background

The SDK models agentic intelligence density as

$$
I = \log N \times \bar{\beta} \times CI
$$

where \( N \) is the number of active robots, \( \bar{\beta} \) is the useful message rate, and \( CI \) the coherence index derived from evaluator consensus.

Safety invariants follow a simplified Control-Barrier-Certificate:

$$
P_{\text{unsafe}} \le \varepsilon_s
$$

such that the agent’s actuation remains within its local safety manifold.

---

## Example Usage

```bash
pip install -e .
python examples/run_agent_demo.py
```

This spins up a simulated robot node, runs a full cognitive loop, and publishes a mock CTV/A to the mesh.

⸻

Development Notes
	•	Written in Python 3.12 with Pydantic, Cryptography, and FastAPI dependencies.
	•	Fully type-hinted for static analysis.
	•	GitHub Actions CI included (commented out for manual enablement).
	•	Dockerfile: python:3.12-slim, exposing port 8787.



Related Components

neuro-receipts-explorer: Visual dashboard for agents, receipts, and network coherence.
compose.yaml: Unified runtime orchestrating backend + frontend for the full demo stack

NeuroMesh SDK establishes the substrate of tokenised intelligence—where every inference, action, and observation becomes an owned, verifiable digital asset.

---

## **`neuro-receipts-explorer/README.md`**

# NeuroMesh Receipts Explorer

The **NeuroMesh Receipts Explorer** provides a visual interface for the **Decentralised Superbrain**—a mesh of humanoid agents, each producing cryptographically attested cognitive artefacts (CTV/A).

It integrates a lightweight **FastAPI backend** (mock data service) with a **React/Vite frontend**, allowing researchers, developers, and institutional partners to visualise live metrics of the network’s agentic intelligence density, data rights flow, and robot participation.

---

##  Conceptual Overview

```
Humanoid Robots ─► CTV/A Receipts ─► Mesh Nodes ─► Explorer Dashboard
↑                                    │
└──── Proof-of-Inference / Proof-of-Action (PoI/PoA) ─────┘
```

Each entry in the dashboard corresponds to a verified *Composite Thought/Action Vector*, the fundamental RWA unit of NeuroMesh intelligence.

---

## System Architecture

| Layer | Technology | Function |
|--------|-------------|-----------|
| Frontend | React + Vite + TypeScript | UI rendering, live receipt polling, network visualisation |
| Backend | FastAPI (Python) | Serves mock receipts, agents, and health metrics |
| Data | Static JSON | Placeholder for on-chain or SDK-provided receipts |
| Deployment | Docker (Node 20-Alpine) | Compact build and runtime |

The backend and frontend communicate over simple REST endpoints (`/health`, `/receipts`), forming the public observation layer of the NeuroMesh network.

---

## Running the Explorer

### A. Standalone
```bash
cd backend
uvicorn main:app --port 8787

cd ../frontend
npx serve -s . -l 5173
````

Then visit http://localhost:5173.

## Unified Demo Stack

When used with the SDK backend:

```
docker compose up --build
```

	•	SDK API → http://localhost:8787
	•	Explorer UI → http://localhost:5173
