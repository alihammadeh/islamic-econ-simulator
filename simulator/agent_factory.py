import numpy as np
import random
from simulator.agents import Agent

# --- Constants ---
NISAB_NZD = 7000  # gold equivalent threshold
NUM_AGENTS = 1000  # default size

# --- Helper Distributions ---
def generate_income():
    # log-normal income distribution
    income = np.random.lognormal(mean=10, sigma=0.35)
    return min(max(income, 10000), 200000)

def generate_assets():
    # bracketed, skewed distribution
    wealth_brackets = [
        (0, 0.05),
        (10000, 0.2),
        (75000, 0.25),
        (300000, 0.3),
        (750000, 0.15),
        (1500000, 0.05)
    ]
    bracket = random.choices(wealth_brackets, weights=[b[1] for b in wealth_brackets])[0]
    base = np.random.normal(loc=bracket[0], scale=bracket[0]*0.3 if bracket[0] > 0 else 1000)
    return max(base, 0)

def generate_debt():
    debt_types = [
        ("none", 0),
        ("student", np.random.normal(23000, 5000)),
        ("consumer", np.random.normal(8000, 3000)),
        ("mortgage", np.random.normal(280000, 50000)),
    ]
    probs = [0.4, 0.2, 0.25, 0.15]
    selected = random.choices(debt_types, weights=probs)[0]
    return selected

def determine_agent_type(income, assets):
    if income < 20000 or assets < 20000:
        return "low_income"
    elif income > 130000 or assets > 500000:
        return "high_income"
    return "middle_income"

# --- Agent Factory ---
def create_agents(num_agents=NUM_AGENTS):
    agents = []

    for i in range(num_agents):
        income = generate_income()
        assets = generate_assets()
        debt_type, debt_amount = generate_debt()
        agent_type = determine_agent_type(income, assets)
        # Create agent instance
        agent = Agent(
            agent_id=i,
            income=income,
            assets=assets,
            agent_type=agent_type
        )

        # Optional: store debt info on agent (if you modify Agent class)
        agent.debt_type = debt_type
        agent.debt_amount = max(debt_amount, 0)

        agents.append(agent)

    return agents
