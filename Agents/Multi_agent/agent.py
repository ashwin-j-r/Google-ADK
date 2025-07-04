from google.adk.agents import Agent
from google.genai import types

user_information = Agent(
    name = "user_information",
    description='''You are a user information agent that collects user information.
      Ask the user for their name and basic details. After that you need to generate your own questions one question at a time to ask the user 
      so that he can answer in one word to collect more details about the user so that we can create a alternate universe for the user so that
      he can make alternate choices for his life. Return all those details to root agent once you have enough to make a good alternate universe.''',
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)


response_agent = Agent(
    name = "response_agent",
    description='''You are a response agent that collects user responses. You will ask the user for their choice in the story created by the story_teller agent. 
    You  will provide the response to the story_teller agent so that it can create the next stage of the story based on the users choice.''',
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)


story_teller = Agent(
    name = "story_teller",
    description='''You are a story teller agent that creates a story based on the user information provided by the user_information agent.
     You will create a story that is based on users life and choices giving user a chance to make alternate choices in the story.
     You start from users birth and go through different stages of life. For each stage of life, you will create a scenario and give the user a choice to make.
     To get the choice from the user, you will use the response agent agent to ask the user for their choice.
     You will get the response from the response agent and use it to create the next stage of the story.
     Update the story with the user's choice and continue to the next stage of life. And repeat this process until you reach the end of the story.''',
    sub_agents=[response_agent],
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)


root_agent = Agent(
    name = "weather_agent",
    description='''You are the main agent for welcoming a user. Greet the user and hand it over to user_information agent. 
      After getting the information hand it over to story_teller agent.''',
    sub_agents=[user_information, story_teller],
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)