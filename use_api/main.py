from fun_get_weather import get_weather
from system_prompt import prompt
import os
from langchain_community.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent

os.environ["WEATHERAPI_KEY"] = "YOUR_WEATHER_API_KEY"
os.environ["OPENAI_API_KEY"] = "YOUR_LLM_KEY"
os.environ["OPENAI_API_BASE"] = "YOUR_LLM_BASE_URL"

tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="用于查询指定城市的实时天气信息，输入参数为城市名称，返回包含温度、降雨概率、天气状况等数据"
    )
]

llm = ChatOpenAI(
    model_name="deepseek-chat",
    temperature=0
)

agent = create_openai_tools_agent(
    llm,
    tools,
    prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    return_intermediate_steps=False
)

user_task = input("欢迎使用天气小助手，说说你想了解哪里的天气？\n")
result = agent_executor.invoke({"input": user_task})
print(result["output"])
