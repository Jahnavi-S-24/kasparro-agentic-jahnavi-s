# Kasparro Applied AI Engineer Assignment

This repository contains a modular multi-agent content generation system built as part of the Kasparro Applied AI Engineer challenge.

## Project Overview
The system takes structured product data as input and automatically generates multiple types of machine-readable content pages using a multi-agent architecture.

## What the System Does
- Parses and normalizes product data
- Generates categorized user questions
- Builds reusable content logic blocks
- Assembles FAQ, Product, and Comparison pages
- Outputs clean JSON files for downstream use

## Architecture
The system is designed using independent agents, each responsible for a single task:
- Data parsing
- Question generation
- Content logic creation
- Template-based page assembly

Agents are connected through a clear orchestration flow.

## How to Run
```bash
python main.py
## Agentic System Design

This project implements a true multi-agent architecture.

Each agent is an autonomous unit with a single responsibility and a shared interface (`BaseAgent`).
Agents do not call each other and are unaware of execution order.

A central Orchestrator dynamically coordinates agent execution by:
- Registering independent agents
- Passing a shared context object
- Controlling execution flow externally

This design ensures agent autonomy, modularity, and extensibility, aligning with real-world agentic system principles.


