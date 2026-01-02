# Kasparro Applied AI Engineer Assignment

This repository contains a modular **Agentic AI–based multi-agent content generation system** built as part of the Kasparro Applied AI Engineer challenge.

## Project Overview
The system takes structured product data as input and automatically generates multiple types of machine-readable content using a true agentic, multi-agent architecture.

The objective of this project is to demonstrate the design and implementation of **autonomous agents coordinated through orchestration**, rather than static or hard-coded control flow.

## What the System Does
- Parses and normalizes raw product data
- Dynamically generates categorized user questions
- Builds reusable content logic blocks
- Assembles FAQ, Product, and Comparison content
- Outputs clean, structured JSON files for downstream use

## Architecture
The system follows an **Agentic AI design pattern** where each agent is responsible for a single, well-defined capability:

- Data Parser Agent  
- Question Generator Agent  
- Content Logic Agent  
- Template Assembly Agent  

Agents are independent, modular, and reusable.  
They do not directly invoke one another or manage execution order.

## Agentic AI & Orchestration Design

This project implements a **true multi-agent, agentic AI architecture**.

Each agent:
- Operates autonomously
- Has a single responsibility
- Works on a shared context object
- Is unaware of other agents and execution order

A central **Orchestrator** is responsible for coordinating agent execution. The orchestrator:
- Registers agents dynamically
- Controls execution flow externally
- Passes shared context between agents

This design avoids static or manually wired logic and supports extensibility, autonomy, and real-world agentic system behavior.

## How to Run
```bash
python main.py
