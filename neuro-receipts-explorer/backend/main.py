from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json, os, time

app = FastAPI(title="NeuroMesh Receipts API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

BASE = os.path.join(os.path.dirname(__file__), "data")

@app.get("/health")
def health():
    return {"ok": True, "ts": int(time.time())}

@app.get("/receipts")
def receipts():
    with open(os.path.join(BASE, "receipts.json")) as f:
        return json.load(f)

@app.get("/agents")
def agents():
    with open(os.path.join(BASE, "agents.json")) as f:
        return json.load(f)