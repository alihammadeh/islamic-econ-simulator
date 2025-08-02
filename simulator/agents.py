import random

class Agent:
    def __init__(self, agent_id, income, assets, agent_type="household"):
        self.agent_id = agent_id
        self.income = income
        self.assets = assets
        self.expenses = income * 0.7  # basic assumption
        self.agent_type = agent_type
        self.zakat_paid = 0
        self.wealth_history = []

    def update_assets(self):
        savings = self.income - self.expenses
        self.assets += savings
        self.wealth_history.append(self.assets)

    def eligible_for_zakat(self, nisab_threshold):
        return self.assets >= nisab_threshold

    def calculate_zakat_due(self, zakat_rate):
        return self.assets * zakat_rate if self.eligible_for_zakat(nisab_threshold=5000) else 0
