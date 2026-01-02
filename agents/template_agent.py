from agents.base_agent import BaseAgent
import json
import os

class TemplateAgent(BaseAgent):
    def __init__(self):
        super().__init__("TemplateAgent")

    def run(self, context):
        os.makedirs("outputs", exist_ok=True)

        with open("outputs/product_page.json", "w") as f:
            json.dump(context["content_blocks"], f, indent=2)

        with open("outputs/faq.json", "w") as f:
            json.dump(context["questions"], f, indent=2)

        return context
