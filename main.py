import json
from orchestrator import Orchestrator

from agents.data_parser_agent import DataParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.template_agent import TemplateAgent


# Load raw input data
with open("data/product_data.json", "r") as file:
    raw_data = json.load(file)

# Shared context for all agents
context = {
    "raw_product_data": raw_data
}

# Create orchestrator
orchestrator = Orchestrator()

# Register agents (order decided here, not inside agents)
orchestrator.register(DataParserAgent())
orchestrator.register(QuestionGeneratorAgent())
orchestrator.register(ContentLogicAgent())
orchestrator.register(TemplateAgent())

# Run orchestration
orchestrator.run(context)

print("Multi-agent orchestration completed successfully")
