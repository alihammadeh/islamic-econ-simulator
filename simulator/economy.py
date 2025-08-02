from simulator.agents import Agent
from simulator.zakat import collect_zakat, distribute_zakat

class EconomySimulator:
    def __init__(self, agents, years=10):
        self.agents = agents
        self.years = years
        self.history = []

    def run(self):
        for year in range(self.years):
            for agent in self.agents:
                agent.update_assets()

            zakat_pool = collect_zakat(self.agents)
            distribute_zakat(self.agents, zakat_pool)

            self.history.append({
                "year": year,
                "total_zakat": zakat_pool,
                "avg_wealth": sum(a.assets for a in self.agents) / len(self.agents)
            })

        return self.history
