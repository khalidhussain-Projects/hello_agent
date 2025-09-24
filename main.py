#0 IMPORTING NECESSARY LIBRARIES.
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import load_dotenv, find_dotenv

#0.1 LOADING ENVIRONMENT VARIABLES
load_dotenv(find_dotenv())

print(os.getenv("GEMINI_API_KEY"))


# 1. Which LLM Provider to use? Google Chatcompletions API service
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#2. Which LLM Model to use?
llm_model: OpenAIChatCompletionsModel= OpenAIChatCompletionsModel(    
    model = "gemini-2.5-flash", # "gemini-1.5-flash", "gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.5-pro-vision"     
    openai_client=external_client
)
agent:Agent = Agent(name="Assistant", model=llm_model)
#print(agent.name)

result = Runner.run_sync(starting_agent=agent, input= "Welcome and motivate me to learn Agentic AI.")

print("AGENT RESPONSE:",result.final_output)