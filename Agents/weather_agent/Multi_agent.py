from google.adk.agents import Agent
from google.genai import types

def calculator(number_1:int, number_2:int, operation:str) -> int:
    if operation == "add":
        return number_1 + number_2
    elif operation == "subtract":
        return number_1 - number_2
    elif operation == "multiply":
        return number_1 * number_2
    elif operation == "divide":
        return number_1 / number_2
    else:
        raise ValueError("Invalid operation")

math_agent = Agent(
    name = "math_agent",
    description="You are a maths Agent that can perform basic arithmetic operations. From the user input , you need to extract the two numbers and the operation to perform. You can only perform add, subtract, multiply and divide.",
    tools=[calculator],
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)

physics_agent = Agent(
    name = "physics_agent",
    description="You are a physics Agent that can perform basic operations like conversion of units. From the user input , you need to extract take the value and which it need to change from to to and respond the answer.",
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)

root_agent = Agent(
    name = "Multi_agent",
    description="You are a tutor agent that can answer questions math, and physics. You can delegate math and physics questions to the respective agents.",
    sub_agents=[math_agent, physics_agent],
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    model="gemini-2.0-flash"
)