from agents.base_agent import BaseAgent

class DataParserAgent(BaseAgent):
    def __init__(self):
        super().__init__("DataParserAgent")

    def run(self, context):
        raw = context["raw_product_data"]

        context["product"] = {
            "name": raw.get("product_name"),
            "concentration": raw.get("concentration"),
            "skin_type": raw.get("skin_type"),
            "ingredients": raw.get("key_ingredients"),
            "benefits": raw.get("benefits"),
            "usage": raw.get("how_to_use"),
            "side_effects": raw.get("side_effects"),
            "price": raw.get("price")
        }

        return context
