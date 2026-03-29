from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
root_agent = Agent(
    name="weather_agent",
    model=LiteLlm(model="ollama_chat/llama3.2"),
    description="you are a very helpfull assistant ",
    instruction="you are a very helpfull assistant help the user by answering the questions.and also greet user in the first converstion like hello!,welcome to weather chat bot made by Manjunath Y",
    tools=[]
)
    
    
    


    