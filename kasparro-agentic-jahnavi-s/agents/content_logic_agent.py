class ContentLogicAgent:
    def __init__(self, product_data):
        self.product = product_data

    def build_overview_block(self):
        return {
            "name": self.product["name"],
            "concentration": self.product["concentration"],
            "skin_type": self.product["skin_type"]
        }

    def build_benefits_block(self):
        return {
            "benefits": self.product["benefits"]
        }

    def build_usage_block(self):
        return {
            "how_to_use": self.product["usage"]
        }

    def build_safety_block(self):
        return {
            "side_effects": self.product["side_effects"]
        }

    def build_price_block(self):
        return {
            "price": self.product["price"]
        }

    def build_comparison_block(self):
        product_b = {
            "name": "RadiantGlow Vitamin C Serum",
            "key_ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "price": 599
        }

        return {
            "product_a": {
                "name": self.product["name"],
                "ingredients": self.product["ingredients"],
                "benefits": self.product["benefits"],
                "price": self.product["price"]
            },
            "product_b": product_b
        }