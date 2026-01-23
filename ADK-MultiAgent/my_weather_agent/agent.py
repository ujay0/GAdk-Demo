from google.adk.agents.llm_agent import SequenceAgent , Agent




SequenceAgent = Agent(
    model='gemini-2.5-flash',
    name='SequenceAgent',
    description='An agent that handles weather-related queries by utilizing specialized sub-agents for different tasks.',
    instruction='Coordinate with sub-agents to provide accurate weather information based on user queries.',

    tools=[
        'get_current_weather_agent',
        'get_weather_forecast_agent',
    ],
)

get_current_weather_agent = Agent(
    model='gemini-2.5-flash',
    name='get_current_weather_agent',
    description='An agent that provides the current weather information for a specified city.',
    instruction='Use the weather API to fetch and return the current weather conditions for the given city.',

    tools=[
        'weather_api_tool',
    ],
)
get_weather_forecast_agent = Agent(
    model='gemini-2.5-flash',
    name='get_weather_forecast_agent',
    description='An agent that provides the weather forecast for the next 7 days for a specified city.',
    instruction='Use the weather API to fetch and return the 7-day weather forecast for the given city.',

    tools=[
        'weather_api_tool',
    ],
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Greetings with a friendly hello, and ask the user the current city they are in.',
    instruction='Use the provided tools to assist the user with weather information based on their location.',
)
