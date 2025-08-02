import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from simulator.agents import Agent
from simulator.economy import EconomySimulator
import pandas as pd

# Setup
NUM_AGENTS = 100
YEARS = 10

# Generate population
agents = [
    Agent(
        agent_id=i,
        income=random.randint(1000, 10000),
        assets=random.randint(1000, 10000)
    )
    for i in range(NUM_AGENTS)
]

# Run simulation
simulator = EconomySimulator(agents, years=YEARS)
results = simulator.run()

# Output summary
df = pd.DataFrame(results)
os.makedirs("data/results", exist_ok=True)
df.to_csv("data/results/simulation_summary.csv", index=False)

# Agent-level data
wealth_df = pd.DataFrame({
    f"agent_{a.agent_id}": a.wealth_history for a in agents
}).T
wealth_df.to_csv("data/results/wealth_over_time.csv")
print("✅ Simulation complete. Results saved.")
