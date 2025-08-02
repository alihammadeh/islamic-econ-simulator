def collect_zakat(agents, zakat_rate=0.025, nisab_threshold=5000):
    zakat_pool = 0
    for agent in agents:
        if agent.eligible_for_zakat(nisab_threshold):
            zakat_due = agent.calculate_zakat_due(zakat_rate)
            agent.assets -= zakat_due
            agent.zakat_paid += zakat_due
            zakat_pool += zakat_due
    return zakat_pool


def distribute_zakat(agents, zakat_pool):
    eligible_agents = [a for a in agents if a.assets < 2000]
    if not eligible_agents:
        return

    share = zakat_pool / len(eligible_agents)
    for agent in eligible_agents:
        agent.assets += share
