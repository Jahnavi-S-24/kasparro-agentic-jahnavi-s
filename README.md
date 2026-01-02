# Kasparro Applied AI Engineer Assignment

This repository contains a modular **Agentic AI-based multi-agent content generation system** built as part of the Kasparro Applied AI Engineer challenge.

## Project Overview
The system takes structured product data as input and automatically generates multiple types of machine-readable content using an agentic, multi-agent architecture.

The goal of the project is to demonstrate the design of **autonomous agents coordinated through orchestration**, rather than static or hard-coded control flow.

## What the System Does
- Parses and normalizes raw product data
- Generates categorized user questions dynamically
- Builds reusable content logic blocks
- Assembles FAQ, Product, and Comparison pages
- Outputs clean JSON files for downstream consumption

## Architecture
The system is implemented using an **Agentic AI design pattern** where each agent is responsible for a single capability:

- Data Parsing Agent
- Question Generation Agent
- Content Logic Agent
- Template Assembly Agent

Agents are **independent, modular, and reusable**.  
They do not directly invoke one another.

## Agentic AI & Orchestration Design

This project implements a **true agentic AI system**.

Each agent:
- Is autonomous
- Has a single responsibility
- Operates on a shared context
- Is unaware of execution order or other agents

A central **Orchestrator** coordinates agent execution by:
- Registering agents dynamically
- Passing a shared context object
- Managing execution flow externally

This architecture avoids static or manually wired logic and enables extensibility, autonomy, and real-world agentic behavior.

## How to Run
```bash
python main.py
```
## Orchestration Architecture

This system follows a true multi-agent design with an explicit orchestration layer.

Each agent is an autonomous module with a single responsibility and a shared interface.
Agents do not invoke each other directly and are unaware of execution order.

A dedicated Orchestrator coordinates agent execution by:
- Registering independent agents dynamically
- Managing execution order externally
- Passing a shared context object between agents

This approach avoids hard-coded or static control flow and enables modular, extensible agent coordination aligned with real-world agentic system principles.



