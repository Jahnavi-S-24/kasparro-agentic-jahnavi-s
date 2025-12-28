class DataParserAgent:
    def __init__(self, raw_product_data):
        self.raw_data = raw_product_data

    def parse(self):
        parsed_data = {
            "name": self.raw_data.get("product_name"),
            "concentration": self.raw_data.get("concentration"),
            "skin_type": self.raw_data.get("skin_type"),
            "ingredients": self.raw_data.get("key_ingredients"),
            "benefits": self.raw_data.get("benefits"),
            "usage": self.raw_data.get("how_to_use"),
            "side_effects": self.raw_data.get("side_effects"),
            "price": self.raw_data.get("price")
        }
        return parsed_data