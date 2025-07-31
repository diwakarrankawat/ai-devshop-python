# ai-devshop-python

**AI Devshop Python Core**  
Backend foundation for a next-generation, agent-powered app builder.  
Orchestrates AI research, secure code editing, and workflow automation using OpenAI agents, Perplexity’s research APIs, and a modular tool system.

## Features (Planned)
- Multi-agent orchestration (research, code editing, prompt building)
- Real-time web knowledge via Perplexity API
- Secure, extensible code manipulation utilities
- Modular, standalone tools and services
- Ready for integration into desktop or web UI

## Core Structure
```
/agents/    # Specialized LLM-driven agents (Research, Code, Prompt)
 /tools/     # Utilities for research, code, validation
 /apis/      # Third-party integrations (Perplexity, openai, etc)
 /services/  # Workflow/business logic orchestration
 /schemas/   # Input/output data formats
 main.py     # Entry point
 config.py   # Config management
```

## Quick Start (Coming Soon)
* Clone repo  
* Install requirements  
* Set up `.env` for all keys

## Roadmap
1. API integration and config management
2. Agent base classes and wrappers
3. Tool functions for research/code ops
4. Workflow orchestration and services
5. Extended support, async, and plugins

**Principles:** Secure, modular, extensible, future-focused.