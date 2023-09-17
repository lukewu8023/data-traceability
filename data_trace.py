import sys
import os

import langchain
from langchain_experimental.plan_and_execute import load_agent_executor
from langchain_experimental.plan_and_execute.agent_executor import PlanAndExecute
from langchain_experimental.plan_and_execute.planners.chat_planner import (
    load_chat_planner,
)
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.tools import BaseTool, StructuredTool, Tool, tool

import get_entity_tool

os.environ["OPENAI_API_KEY"] = ""


with open("prompt/prompt_data_trace.txt") as f:
    contents = f.read()

model = ChatOpenAI(
    openai_api_base="https://api.ohmygpt.com/v1",
    model="gpt-3.5-turbo-0613",
    temperature=0,
    max_tokens=1024,
)
system_prompt = contents

planner = load_chat_planner(model, system_prompt)

# tools = [
#    StructuredTool.from_function(get_entity_tool.get_meta_data)
# ]

tools = [
    Tool.from_function(
        func=get_entity_tool.get_meta_data,
        name="Get metadata",
        description="get metadata of a system for data traceability application, input parameter is the system name.",
    ),
    Tool.from_function(
        func=get_entity_tool.get_lineage_data,
        name="Get lineage data",
        description="get lineage information between systems for data traceability application, input parameter is the downstream system name, and return is the lineage information of it and its upstream system.",
    ),
    Tool.from_function(
        func=get_entity_tool.get_entity_data,
        name="Get data",
        description="get actual data in a system for data traceability application, input parameter is the system name.",
    ),
]
# tools = load_tools(tools, llm=model)
executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

langchain.debug = True
agent.run(
    "What is the security name of my security which id is 1234? My system name is B."
)
