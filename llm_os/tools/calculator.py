import re
from langchain.tools import tool


@tool
def calculator(expression: str) -> float:
    """
    Evaluate a mathematical expression and return the result.
    The expression can contain basic arithmetic operations: +, -, *, /, and parentheses.
    """
    # Remove any whitespace from the expression
    expression = expression.replace(" ", "")

    # Check if the expression is a valid mathematical expression
    if not re.match(r"^[\d+\-*/()\.]+$", expression):
        raise ValueError("Invalid mathematical expression")

    try:
        # Evaluate the expression using eval() in a restricted environment
        result = eval(expression, {"__builtins__": None}, {})
        return float(result)
    except (SyntaxError, ZeroDivisionError, TypeError, ValueError) as e:
        raise ValueError(f"Error evaluating expression: {str(e)}")
