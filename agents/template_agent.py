class TemplateAgent:
    def __init__(self, product_data, questions, content_blocks):
        self.product = product_data
        self.questions = questions
        self.blocks = content_blocks

    def generate_faq_page(self):
        faq_items = []

        for category, qs in self.questions.items():
            for q in qs[:1]:
                faq_items.append({
                    "category": category,
                    "question": q,
                    "answer": "Answer generated from product data"
                })

        return {
            "page_type": "FAQ",
            "product_name": self.product["name"],
            "faqs": faq_items
        }

    def generate_product_page(self):
        return {
            "page_type": "Product",
            "overview": self.blocks["overview"],
            "benefits": self.blocks["benefits"],
            "usage": self.blocks["usage"],
            "safety": self.blocks["safety"],
            "price": self.blocks["price"]
        }

    def generate_comparison_page(self):
        return {
            "page_type": "Comparison",
            "comparison": self.blocks["comparison"]
        }
