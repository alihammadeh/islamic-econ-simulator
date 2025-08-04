import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from simulator.agents import Agent
from simulator.economy import EconomySimulator
from simulator.agent_factory import create_agents
import pandas as pd
from datetime import datetime

# Setup
NUM_AGENTS = 100
YEARS = 10

# Generate population
agents = create_agents(num_agents=1000)

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

time = datetime.now().strftime("%Y%m%d_%H%M%S")
wealth_df.to_csv(f"data/results/wealth_over_time_{time}.csv")
print("✅ Simulation complete. Results saved.")
