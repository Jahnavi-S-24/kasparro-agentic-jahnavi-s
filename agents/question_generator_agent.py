from agents.base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("QuestionGeneratorAgent")

    def run(self, context):
        product = context["product"]

        context["questions"] = {
            "Informational": [
                f"What is {product['name']}?",
                "What are the key ingredients?",
                "Who is this product suitable for?"
            ],
            "Usage": [
                f"How should {product['name']} be used?",
                "When should it be applied?",
                "How often can it be used?"
            ],
            "Safety": [
                "Are there any side effects?",
                "Is it safe for sensitive skin?",
                "Can it be used daily?"
            ]
        }

        return context
