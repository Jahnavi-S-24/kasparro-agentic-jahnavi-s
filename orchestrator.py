class Orchestrator:
    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def run(self, context):
        for agent in self.agents:
            context = agent.run(context)
        return context