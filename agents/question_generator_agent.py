class QuestionGeneratorAgent:
    def __init__(self, product_data):
        self.product = product_data

    def generate_questions(self):
        questions = {
            "Informational": [],
            "Usage": [],
            "Safety": [],
            "Purchase": [],
            "Comparison": []
        }

        # Informational questions
        questions["Informational"].append(
            f"What is {self.product['name']}?"
        )
        questions["Informational"].append(
            f"What are the key ingredients in {self.product['name']}?"
        )
        questions["Informational"].append(
            f"What skin types is {self.product['name']} suitable for?"
        )

        # Usage questions
        questions["Usage"].append(
            f"How should I use {self.product['name']}?"
        )
        questions["Usage"].append(
            "When is the best time to apply this product?"
        )
        questions["Usage"].append(
            "How many drops should be used per application?"
        )

        # Safety questions
        questions["Safety"].append(
            "Are there any side effects?"
        )
        questions["Safety"].append(
            "Is this product suitable for sensitive skin?"
        )
        questions["Safety"].append(
            "Can this product be used daily?"
        )

        # Purchase questions
        questions["Purchase"].append(
            "What is the price of this product?"
        )
        questions["Purchase"].append(
            "Is this product value for money?"
        )
        questions["Purchase"].append(
            "Where can I buy this product?"
        )

        # Comparison questions
        questions["Comparison"].append(
            "How does this product compare to other Vitamin C serums?"
        )
        questions["Comparison"].append(
            "Is this product better than cheaper alternatives?"
        )
        questions["Comparison"].append(
            "What makes this product different from others?"
        )

        return questions
