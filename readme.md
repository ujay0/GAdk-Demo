adk create my_weather_agent

adk run my_agent

adk web --port 8000

adk create multi-agent-app  to generate a starter with  agent.py  and  .env . Get a free Gemini API key from Google AI Studio and add to  .env :  GOOGLE_API_KEY=your_key_here . In  agent.py , define a root agent that delegates to sub-agents (e.g., researcher and analyzer): use  Agent  with  sub_agents=research_agent, analysis_agent  for routing based on LLM decisions.