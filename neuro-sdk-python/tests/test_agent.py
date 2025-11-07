from neurosdk.agents import NeuroAgent

def test_agent_once():
    agent = NeuroAgent("wallet-test", "robot-test")
    ctva = agent.run_once()
    assert "poi" in ctva and "poa" in ctva