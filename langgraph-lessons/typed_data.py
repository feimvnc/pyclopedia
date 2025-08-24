# Normal dictionary, lacks correct type or structure
movie = {"name": "Transformer", "year": 2019}

# Typed dictionary, a better approach
# Used in langgrap to define the state 
# Type safety, enhanced readability
from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int

movie = Movie(name="Transformer", year=2019)

# Union, flexible, type safety
from typing import Union
def squares(x: Union[int, float]) -> float:
    return x * x

x = 5           # ok
x = 3.14        # ok
x = 'e=mc^2'    # will fail

# Optional
from typing import Optional

def nice_message(name: Optional[str]) -> None:
    # name can be either String or None
    if name is None:
        print("Hi welcome")
    else:
        print(f"Hi {name}")

# Any, anything and everything is allowed
from typing import Any

def print_value(x: Any):
    print(x)

print_value("e roughly equals 2.71828")

# Lambda function (a shortcut to write small functions)
square = lambda x: x * x
square(42)

# map 
nums = list(range(5))  # [0, 1, 2, 3, 4]
squares = list(map(square, nums))
print(squares)

squares = list(map(lambda x: x * x, nums))
print(squares)

# State, a shared data structure that holds the 
# current information or context of the entire application.
# Like the application's memeory of vars and nodes

# Node, individual function or operation performing specific tasks
# Node receives input, process it, produces output or update state

# Graph, maps different tasks (nodes) connected and executed
# Graph represents workflow, sequence and conditional paths
# between various operations

# Edge, connection between nodes, determins the flow of execution
# Tells which node should be executed after current node 
# completing its task.

# Conditional Edge, specialized connections that decide the
# next node to execute based on specific conditions or logic
# applied to the current state.

# Start node: entry point in LangGraph, where workflow begins
# Does not perform any operations, but serves starting point.

# End node, signifies the conclusion of workflow.

# Tools are specialized functions or utilities that nodes
# can utilize to perform specific tasks such as fetching data from an API.
# Tools are functionalities used within nodes.
# Tools in toolbox (a node)

# ToolNode, a special kind of node whose main job is to run a tool.
# Connects the tools output back into the State so other 
# nodes can use that information

# StateGraph, a class to build and compile the graph structure.
# Manages nodes, edges, and overall state, ensuring in a 
# Unified way and that data flows correctly between components.

# Runnable, a standardized executable component that performs
# a specific task within an AI workflow.
# A fundamental building block, to create modular systems.

# Messages:
# Human message 
# System message 
# Function message 
# AI message
# Tool message 


