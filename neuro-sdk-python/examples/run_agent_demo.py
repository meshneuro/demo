from neurosdk.agents import NeuroAgent
from neurosdk.network import connect_to_mesh, publish_receipt

def main():
    agent = NeuroAgent(agent_id="wallet_ABC123", robot_id="robot-emu-001")
    session = connect_to_mesh()
    print("Connected:", session)

    ctva = agent.run_once()
    print("CTV/A:", ctva)

    result = publish_receipt(ctva)
    print("Publish:", result)

if __name__ == "__main__":
    main()