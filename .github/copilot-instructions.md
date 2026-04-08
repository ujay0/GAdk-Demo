# Copilot Instructions for GAdk-Demo

## Project Overview

This is a mixed-purpose repository containing:
1. **ADK-MultiAgent**: Google AI Deployment Kit (ADK) multi-agent weather application using Gemini API
2. **UJay_Learning**: Python learning materials and problem-solving exercises covering fundamentals and DSA

## Architecture

### ADK-MultiAgent Component
- **Location**: `/ADK-MultiAgent/my_weather_agent/`
- **Pattern**: Hierarchical agent architecture with root agent delegating to specialized sub-agents
- **Key Files**:
  - [agent.py](../ADK-MultiAgent/my_weather_agent/agent.py): Defines root agent (SequenceAgent) and two specialized agents (get_current_weather_agent, get_weather_forecast_agent)
  - [requirement.txt](../ADK-MultiAgent/requirement.txt): Dependencies including google-adk, FastAPI, Pydantic

**Data Flow**: Root agent receives queries → delegates to weather sub-agents → sub-agents call weather_api_tool → returns results to root

### UJay_Learning Component
- **Location**: `/UJay_Learning/`
- **Purpose**: Educational materials following Durga Software Solutions YouTube curriculum
- **Structure**:
  - `Tut30Days/`: 30-day Python challenge (D1-D14+ completed covering fundamentals, OOP, inheritance, abstract classes)
  - `YT-PFF-B-DS/`: Basic Python Programming Fundamentals (40+ exercises covering types, operators, data structures)

## Critical Patterns

### Agent Definition Pattern (ADK)
Agents are defined using the `Agent` class from `google.adk.agents.llm_agent`:
```python
agent = Agent(
    model='gemini-2.5-flash',              # Always use gemini-2.5-flash
    name='agent_name',                     # Descriptive name
    description='What agent does',         # Clear purpose
    instruction='How agent behaves',       # LLM behavior instruction
    tools=['tool_name', 'another_tool'],   # List of available tools
    sub_agents=None                        # For hierarchical delegation (optional)
)
```

**Key Convention**: Root agents should coordinate with sub-agents. Sub-agents should focus on specific domains (weather current vs forecast). Always provide descriptive instructions for each agent role.

### Python Learning Files
- **Naming**: `V###-TopicName.py` or `D##TopicName.py` (version/day number + descriptive name)
- **Structure**: Each file is self-contained, often with brief docstring or comment explaining concept
- **Pattern**: Simple scripts demonstrating single concepts (e.g., data type operations, control flow)
- Include `if __name__ == '__main__':` blocks for standalone execution
- Use descriptive variable names reflecting the learning objective

## Development Workflows

### ADK Agent Development
1. **Setup**: Activate virtual environment (`.gadk/bin/activate`)
2. **Dependencies**: Install via `pip install -r requirement.txt` in ADK-MultiAgent
3. **Environment**: Set `GOOGLE_API_KEY` from Google AI Studio to `.env`
4. **Run**: Use `adk run my_weather_agent` (requires ADK CLI)
5. **Web Interface**: `adk web --port 8000` for testing

### Creating New Agents
Use `adk create <agent-name>` to scaffold new agents with starter files and `.env` template.

### Python Learning Exercises
- Files are standalone scripts intended for execution and learning
- Run directly: `python filename.py`
- No build/test infrastructure; focus is educational

## Integration Points

- **ADK-MultiAgent ↔ Weather API**: Sub-agents communicate through `weather_api_tool`
- **No cross-component integration**: UJay_Learning and ADK-MultiAgent are independent
- **External Dependencies**: Google Gemini API (via ADK), FastAPI for potential serving

## File Organization Conventions

- **ADK**: Flat structure with agent definitions in single `agent.py` file
- **Learning Materials**: Grouped by curriculum (Tut30Days, YT-PFF-B-DS) with README describing content
- **.gitignore**: Ignores `.gadk/` virtual environment directory

## Key Considerations

1. **API Keys**: Never commit `.env` files; document required keys in requirements/README
2. **Model Consistency**: All agents should use `gemini-2.5-flash` unless explicitly changing strategy
3. **Agent Naming**: Use descriptive, snake_case names that reflect agent responsibility
4. **Learning File Testing**: Files may have `input()` calls; provide stdin when running or modify to hardcoded values for testing
