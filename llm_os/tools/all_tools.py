from .calculator import calculator
from langchain_core.utils.function_calling import convert_to_openai_function


tools = [calculator]
tools = [convert_to_openai_function(tool) for tool in tools]


def execute_tool(tool, args):
    return tool(*args)
