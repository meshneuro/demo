import React, { useMemo } from "react";

export default function NetworkGraph({ agents, receipts }: { agents:any[]; receipts:any[] }){
  const edges = useMemo(() => receipts.map((r:any) => ({
    from: r.agent_id, to: r.robot_id
  })), [receipts]);

  return (
    <div className="card">
      <div className="row"><strong>Superbrain Mesh (schematic)</strong></div>
      <pre style={{whiteSpace:"pre-wrap"}}>
{JSON.stringify({nodes: agents.map(a=>a.agent_id), edges}, null, 2)}
      </pre>
    </div>
  );
}