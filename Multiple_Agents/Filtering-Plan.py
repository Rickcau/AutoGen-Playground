import autogen
from dotenv import load_dotenv
import os

load_dotenv("./example.env")
print(os.getenv('API_KEY'))
print(os.getenv('API_BASE'))

# This example creates multple agents that have a conversation with each other using a GroupChatManager about the task until Admin is approved by the Admin. 

config_list_gpt4 = [
    {
        'model': 'gpt-4-sweden',
        'api_key': os.getenv('API_KEY'),
        'base_url': os.getenv('API_BASE'),
        'api_type': 'azure',
        'api_version': '2023-07-01-preview',
    },
    {
        'model': 'gpt-4-sweden',
        'api_key': os.getenv('API_KEY'),
        'base_url': os.getenv('API_BASE'),
        'api_type': 'azure',
        'api_version': '2023-07-01-preview',
    }
]

gpt4_config = {
    "seed": 39,  # change the seed for different trials
    "temperature": 0.5,
    "config_list": config_list_gpt4,
    "timeout": 120,
}

user_proxy = autogen.UserProxyAgent(
   name="Admin",
   system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
   code_execution_config=False,
)
el = autogen.AssistantAgent(
    name="el",
    system_message="Engineering Lead. State your name first. Check the plan and provide feedback from an Engineering persepctive. Suggest what features are needed and the options available. Engineering leads needs to approve the plan.",
    llm_config=gpt4_config
)
 
cfo = autogen.AssistantAgent(
    name="CFO",
    system_message="CFO. State your name first. Check the plan and provide feedback from a financial persepctive. Suggest how to build the business case. CFO needs to approve the plan.",
    llm_config=gpt4_config,
)
 
cto = autogen.AssistantAgent(
    name="CTO",
    system_message="CTO. State your name first. Check the plan and provide feedback from a technical persepctive. Suggest how to build the solution.  CTO needs to approve the plan.",
    llm_config=gpt4_config,
 
)
planner = autogen.AssistantAgent(
    name="Planner",
    system_message='''Planner. Suggest a plan. Be Creative within reason.
      Revise the plan based on feedback from admin, CFO, CTO, Engineering Lead and critic, until admin approval.
      Explain the plan first. be clear about the problem, solution, and how to measure success.
      In the end provide a summary of the plan.
    ''',
    llm_config=gpt4_config,
)
 
critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the plan includes adding verifiable info such as source URL.",
    llm_config=gpt4_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, cto, cfo, el, planner, critic], messages=[], max_round=50)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

user_proxy.initiate_chat(
    manager,
    message=""" ContosoDate is a startup in the dating industry. ContosoDate is working on a disruptive mobile dating app is looking for the most cost effective technology to use for filtering of data that is stored in Cosmos DB, the Technology stack is 100% Azure. We have a list of items stored for each user and we need the ability to allow users to filter and serch for users based on their respones to each item.  Currently we are considering Azure Cognitive Search for this, but we are concerned about the costs assoicated with.  As a result we would like to know what other options we should consider and what the pros and cons are for each approach. What optoins should we consider, and what are the costs of each and benefits of each option?
    """,
)
