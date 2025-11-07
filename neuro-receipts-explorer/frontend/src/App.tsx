import React, { useEffect, useState } from "react";
import { getReceipts, getAgents } from "./api";
import ReceiptCard from "./components/ReceiptCard.tsx";
import NodeStatus from "./components/NodeStatus.tsx";
import NetworkGraph from "./components/NetworkGraph.tsx";

export default function App(){
  const [receipts, setReceipts] = useState<any[]>([]);
  const [agents, setAgents] = useState<any[]>([]);

  useEffect(() => {
    getReceipts().then(setReceipts);
    getAgents().then(setAgents);
  }, []);

  return (
    <div className="wrap">
      <header>
        <h1>NeuroMesh Receipts Explorer</h1>
        <p>CTV/A • PoI/PoA • Agents • “Superbrain” Topology</p>
      </header>

      <section className="grid">
        <div>
          <h2>Receipts</h2>
          {receipts.map(r => <ReceiptCard key={r.id} r={r} />)}
        </div>
        <div>
          <h2>Agents</h2>
          {agents.map(a => <NodeStatus key={a.agent_id} a={a} />)}
          <h2 style={{marginTop:24}}>Network</h2>
          <NetworkGraph agents={agents} receipts={receipts}/>
        </div>
      </section>
    </div>
  );
}