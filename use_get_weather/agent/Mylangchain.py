from langchain_community.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from .fun_get_weather import get_weather
from .system_prompt import prompt
import os

os.environ["OPENAI_API_BASE"] = "YOUR_LLM_BASE_URL"
os.environ["OPENAI_API_KEY"] = "YOUR_LLM_KEY"

tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="用于查询指定城市的天气信息，输入参数为城市名称，返回值包含城市名、该城市当前温度、当日最高温、最低温、降雨概率和湿度的JSON数据"
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
