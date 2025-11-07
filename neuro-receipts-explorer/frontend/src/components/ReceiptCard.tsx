import React from "react";

export default function ReceiptCard({ r }: { r: any }) {
  return (
    <div className="card">
      <div className="row">
        <strong>CTV/A</strong> <span>{r.id}</span>
      </div>
      <div className="row">
        <span>Agent</span> <code>{r.agent_id}</code>
      </div>
      <div className="row">
        <span>Robot</span> <code>{r.robot_id}</code>
      </div>
      <div className="row">
        <span>PoI</span> <code>{r.poi.hash_hex}</code>
      </div>
      <div className="row">
        <span>PoA</span> <code>{r.poa.hash_hex}</code>
      </div>
      <div className="row">
        <span>Safety</span> <b>{r.eval?.safety}</b>
      </div>
    </div>
  );
}