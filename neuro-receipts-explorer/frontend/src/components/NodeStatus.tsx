import React from "react";

export default function NodeStatus({ a }: { a: any }){
  const color = a.status === "online" ? "#00c78b" : "#c70039";
  return (
    <div className="card">
      <div className="row">
        <strong>Agent</strong> <code>{a.agent_id}</code>
      </div>
      <div className="row">
        <span>Status</span> <span style={{color}}>{a.status}</span>
      </div>
      <div className="row">
        <span>Location</span> <span>{a.location}</span>
      </div>
    </div>
  );
}