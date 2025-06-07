from google.adk.agents import Agent

def get_weather(location: str) -> str:
    return f"The current weather in {location} is sunny with a temperature of 25°C."

root_agent = Agent(
    name = "weather_agent",
    description="You are an ai which can get the weather of the location use the tool 'get_weather' by passing the location to that function and return what it is returning.",
    tools=[get_weather],
    model="gemini-2.0-flash"
)