# Multi-Agent Content Generation System

## 1. Problem Statement

The objective of this project is to design and implement a modular, agent-based automation system that takes structured product data as input and automatically generates multiple types of structured, machine-readable content pages.

The system must demonstrate clear agent boundaries, reusable logic blocks, orchestration flow, and clean JSON outputs without relying on a single monolithic script.

---

## 2. Solution Overview

This solution implements a multi-agent architecture where each agent is responsible for a single, well-defined task in the content generation pipeline.

The system processes raw product data through multiple agents that clean data, generate questions, build reusable content logic blocks, and assemble final content pages using templates. The final output consists of three machine-readable JSON pages: FAQ, Product Page, and Comparison Page.

---

## 3. Scope and Assumptions

### Scope:
- The system operates only on the provided product dataset.
- No external research or additional product facts are introduced.
- The system supports automated generation of FAQ, Product, and Comparison pages.

### Assumptions:
- Product data follows a structured key-value format.
- Comparison product (Product B) is fictional and used only for demonstration.
- Content quality is rule-based rather than generative.

---

## 4. System Design (Most Important)

### 4.1 Agent Architecture

The system is composed of the following agents:

#### DataParserAgent
- Responsibility: Normalize and clean raw product input data.
- Input: Raw product JSON
- Output: Structured internal product representation

#### QuestionGeneratorAgent
- Responsibility: Automatically generate categorized user questions.
- Input: Clean product data
- Output: Categorized questions (Informational, Usage, Safety, Purchase, Comparison)

#### ContentLogicAgent
- Responsibility: Generate reusable content logic blocks.
- Blocks include overview, benefits, usage, safety, pricing, and comparison.
- Input: Clean product data
- Output: Structured content blocks

#### TemplateAgent
- Responsibility: Assemble final pages using templates and content blocks.
- Generates FAQ, Product, and Comparison pages.
- Output: Structured JSON pages

---

### 4.2 Orchestration Flow

The system follows a linear orchestration pipeline:

1. Raw product data is parsed by DataParserAgent.
2. Clean data is passed to QuestionGeneratorAgent.
3. ContentLogicAgent builds reusable logic blocks.
4. TemplateAgent assembles final pages.
5. JSON outputs are written to disk.

Each agent operates independently and communicates through explicit input/output contracts.

---

### 4.3 Design Principles

- Single Responsibility per agent
- No hidden global state
- Modular and extensible architecture
- Clear separation of logic, templates, and orchestration
- Machine-readable outputs

---

## 5. Output Structure

The system generates the following outputs:

- faq.json
- product_page.json
- comparison_page.json

Each output is structured, predictable, and suitable for downstream automation or integration.

---

## 6. Conclusion

This project demonstrates a production-style agentic system that emphasizes system design, modularity, and maintainability. The architecture is extensible and can easily support additional products, agents, or content templates in the future.
## Agentic AI Orchestration Architecture

This system is designed as a true multi-agent, agentic AI architecture.

Each agent is an autonomous module with a single responsibility and a shared interface.
Agents do not invoke one another directly and are unaware of execution order.

A dedicated Orchestrator coordinates agent execution by:
- Dynamically registering independent agents
- Managing execution flow externally
- Passing a shared context object between agents

This design avoids static or manually wired control flow and supports extensibility, autonomy, and real-world agentic system behavior.

