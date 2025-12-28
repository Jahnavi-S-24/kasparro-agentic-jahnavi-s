import json
from agents.data_parser_agent import DataParserAgent

with open("data/product_data.json", "r") as file:
    raw_data = json.load(file)

parser = DataParserAgent(raw_data)
clean_data = parser.parse()

print(clean_data)
from agents.question_generator_agent import QuestionGeneratorAgent

question_agent = QuestionGeneratorAgent(clean_data)
questions = question_agent.generate_questions()

print("\nGenerated Questions:")
for category, qs in questions.items():
    print(f"\n{category}:")
    for q in qs:
        print("-", q)
from agents.content_logic_agent import ContentLogicAgent

logic_agent = ContentLogicAgent(clean_data)

print("\nContent Blocks:")
print("Overview:", logic_agent.build_overview_block())
print("Benefits:", logic_agent.build_benefits_block())
print("Usage:", logic_agent.build_usage_block())
print("Safety:", logic_agent.build_safety_block())
print("Price:", logic_agent.build_price_block())
print("Comparison:", logic_agent.build_comparison_block())
from agents.template_agent import TemplateAgent
import json

content_blocks = {
    "overview": logic_agent.build_overview_block(),
    "benefits": logic_agent.build_benefits_block(),
    "usage": logic_agent.build_usage_block(),
    "safety": logic_agent.build_safety_block(),
    "price": logic_agent.build_price_block(),
    "comparison": logic_agent.build_comparison_block()
}

template_agent = TemplateAgent(clean_data, questions, content_blocks)

faq_page = template_agent.generate_faq_page()
product_page = template_agent.generate_product_page()
comparison_page = template_agent.generate_comparison_page()

with open("outputs/faq.json", "w") as f:
    json.dump(faq_page, f, indent=2)

with open("outputs/product_page.json", "w") as f:
    json.dump(product_page, f, indent=2)

with open("outputs/comparison_page.json", "w") as f:
    json.dump(comparison_page, f, indent=2)

print("\nJSON pages generated in outputs folder")