# AutoGen Examples
This is a simple repo to store the various AutoGen examples I am playing with, it's a work in-progress and I am using it to play with AutoGen.  I hope you find it useful as well. 

Needs to have a Azure Open AI rescource with a GPT4.0 model deployed.

For more details. look at MS repo:
https://github.com/microsoft/autogen

## Run this to install Autogen:
pip install pyautogen

## Different ways to load the AI LLM settings
If you are running this in GitHub Code spaces you will need to get the abspath as the path on Github will be different, but you can use the following as an example:

'''
       here = os.path.abspath(os.path.dirname(__file__)) + "/OAI_CONFIG.JSON"
'''
If this becomes a challenge for you, you can just load the settings with a JSON object and use this for LLM settings for AutoGen.  If you don't want to use load_dotenv() to get your API_KEY or API_BASE just use the string values for them.  

'''
       load_dotenv("example.env")
       print(os.getenv('API_KEY'))
       print(os.getenv('API_BASE'))
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

'''

## Modify the OAI_CONFIG.json file to point to your models

'''
       [
        {
            "model": "<Deployment Name, not the model name>",
            "api_key": "<API KEY>",
            "base_url": "https://<your-instance>.openai.azure.com/",
            "api_type": "azure",
            "api_version": "2023-07-01-preview"
        },
        {
            "model": "<Deployment Name, not the model name>,
            "api_key": "<API KEY>"",
            "base_url": "https://<your-instance>.openai.azure.com/",
            "api_type": "azure",
            "api_version": "2023-07-01-preview"
        }
      ]
,,,

## Simple-Two-Agent (Simply-Two-Agents.py)
The idea here is to demostrate how a Human UserProxy can interact with two Assistants that produce two different outcomes.  This is fundemental to AutoGen 

1. load the LLMs from a .json file.  
2. create two Assisants, one that can generate code blocks and one that does not.
3. create one UserProxyAgent that is capable of executing code.
4. start a chat with the first Assisant asking it to plot a chart of two stocks
5. start another chat with the first Assisant asking it to plot the YTD gain for META and TESLA.
6. start another chat with the 2nd Assisant asking it to do the same thing as item 5.

Now, that you understand the purpose of the example, run it and try to understand why you are seeing the results you are seeing.

## New-Product-Plan (New-Product-Plan.py)
Thi1s example is more complex and it demostrates how multiple agents can be used without Human input to create a very creative outcome.  It leverages the idea of having an Admin, Planner, CTO, CFO, CPO and Critic come up with a plan to launch a new product.  It leverages a total of 6 agents that converse with each other until the Admin approves the plan.  It leverages a concept in AutoGen called GroupChat, which allows the agents to converse with each other.

1. First we build the LLM data using an inline JSON object
2. Then we create the 6 agents
3. We build the groupchat and the manager for the groupchat
4. Next, we initiate the group chat with the UserProxy agent passing in the groupchat Manger and a message about the Company and our desire to launch a new product.
5. Which the magic of AutoGen as the Agents converse with each other and how they come up with a final plan

