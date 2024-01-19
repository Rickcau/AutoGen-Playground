import random
import autogen
import os
import gradio as gr
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

TIMEOUT = 60

def random_response(message, history):
    return random.choice(["Yes", "No"])

def initialize_agents(config_list):
        assistant = AssistantAgent(
            name="assistant",
            max_consecutive_auto_reply=5,
            llm_config={
                # "seed": 42,
                "timeout": TIMEOUT,
                "config_list": config_list,
            },
        )

        userproxy = UserProxyAgent(
            name="userproxy",
            human_input_mode="NEVER",
            is_termination_msg=_is_termination_msg,
            max_consecutive_auto_reply=5,
            # code_execution_config=False,
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,  # set to True or image name like "python:3" to use docker
            },
        )

        # assistant.register_reply([Agent, None], update_agent_history)
        # userproxy.register_reply([Agent, None], update_agent_history)

        return assistant, userproxy

def get_description_text():
    return """
    # Microsoft AutoGen: Retrieve Chat Demo

    This demo shows how to use the RetrieveUserProxyAgent and RetrieveAssistantAgent to build a chatbot.

    #### [AutoGen](https://github.com/microsoft/autogen) [Discord](https://discord.gg/pAbnFJrkgZ) [Blog](https://microsoft.github.io/autogen/blog/2023/10/18/RetrieveChat) [Paper](https://arxiv.org/abs/2308.08155) [SourceCode](https://github.com/thinkall/autogen-demos)
    """

with gr.Blocks() as demo:
    def initialize_agents(config_list):
        assistant = AssistantAgent(
            name="assistant",
            max_consecutive_auto_reply=5,
            llm_config={
                # "seed": 42,
                "timeout": TIMEOUT,
                "config_list": config_list,
            },
        )

        userproxy = UserProxyAgent(
            name="userproxy",
            human_input_mode="NEVER",
            is_termination_msg=_is_termination_msg,
            max_consecutive_auto_reply=5,
            # code_execution_config=False,
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,  # set to True or image name like "python:3" to use docker
            },
        )
    with gr.Row() as params:
        txt_model = gr.Dropdown(
            label="Model",
            choices=[
                "gpt-4",
                "gpt-35-turbo",
                "gpt-3.5-turbo",
            ],
            allow_custom_value=True,
            value="gpt-35-turbo",
            container=True,
        )
    chatbot = gr.Chatbot(
        [],
        elem_id="chatbot",
        bubble_full_width=False,
        avatar_images=(
            "human.png",
            (os.path.join(os.path.dirname(__file__), "autogen.png")),
        ),
        render=False,
        height=600,
    )

## clear = gr.ClearButton([txt_input, chatbot])
## demo = gr.ChatInterface(random_response)
dem = demo.launch()




