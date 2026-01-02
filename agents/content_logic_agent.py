from agents.base_agent import BaseAgent

class ContentLogicAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentLogicAgent")

    def run(self, context):
        product = context["product"]

        context["content_blocks"] = {
            "overview": {
                "name": product["name"],
                "concentration": product["concentration"],
                "skin_type": product["skin_type"]
            },
            "benefits": product["benefits"],
            "usage": product["usage"],
            "safety": product["side_effects"],
            "price": product["price"]
        }

        return context
