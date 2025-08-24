"""
Implement looping logic to route the flow of data back to nodes.
Create a single conditional edge to handle decision-making
and control graph flow.
"""

import random
from typing import Dict, List, TypedDict

from langgraph.graph import END, StateGraph


class AgentState(TypedDict):
    name: str
    numbers: List[int]
    counter: int


def greeting_node(state: AgentState) -> AgentState:
    state["name"] = f"Hi there, {state['name']}"
    state["counter"] = 0
    return state


def random_node(state: AgentState) -> AgentState:
    state["numbers"].append(random.randint(0, 10))
    state["counter"] += 1
    return state


def should_continue(state: AgentState) -> AgentState:
    if state["counter"] < 5:
        print("ENTERING LOOP", state["counter"])
        return "loop"
    else:
        return "exit"


# greeting -> random -> random -> random -> random -> random -> END

graph = StateGraph(AgentState)

graph.add_node("greeting", greeting_node)
graph.add_node("random", random_node)
graph.add_edge("greeting", "random")

graph.add_conditional_edges(
    "random",  # source node
    should_continue,  # action
    {
        "loop": "random",  # self-loop back to same node
        "exit": END,  # End of graph
    },
)

graph.set_entry_point("greeting")

app = graph.compile()
# app.get_graph().print_ascii().  # not work

result = app.invoke({"name": "Bob", "numbers": [], "counter": -1})
print(result)

"""
$  python looping_graph.py 
ENTERING LOOP 1
ENTERING LOOP 2
ENTERING LOOP 3
ENTERING LOOP 4
{'name': 'Hi there, Bob', 'numbers': [0, 10, 4, 7, 6], 'counter': 5}
"""
