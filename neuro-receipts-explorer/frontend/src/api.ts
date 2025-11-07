const API = "http://localhost:8787";
export async function getReceipts(){ return (await fetch(`${API}/receipts`)).json(); }
export async function getAgents(){ return (await fetch(`${API}/agents`)).json(); }