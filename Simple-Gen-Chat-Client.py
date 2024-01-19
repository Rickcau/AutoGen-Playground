import os
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
here = os.path.abspath(os.path.dirname(__file__)) + "/OAI_CONFIG.JSON"
print(here)
config_list = config_list_from_json(env_or_file=here)
print(config_list)
# lets create an assistant with an intent to solve a task with LLM
# the detail system message is designed to solve a task with LLM, including suggesting python code blocks and debugging.
# human_input_mode is default to NEVER and code_execution_config is set to false
# this agent does not execute code by default and expects the user to to execute the code
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})


# lets create a proxy agent for the user, that can execute code and provide feedback to other agents
# human_inpute_mode = ALWAYS and llm_config to False
# by default the agent will prompt for human input every time a message is received.  Code execution is enabled by default
# you can override human input, modify auto reply, execut blocks etc, see https://microsoft.github.io/autogen/docs/reference/agentchat/user_proxy_agent
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
print("Let's use the 1st assistant now.")
user_proxy.initiate_chat(assistant, message="Create a Web Frontend that has ChatGPT style interface that uses AutoGen agents.")

