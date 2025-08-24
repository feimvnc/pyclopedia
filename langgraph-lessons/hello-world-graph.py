from typing import Dict, TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    message: str


def greeting_node(state: AgentState) -> AgentState:
    """A node that addes a greeting message to the state."""

    state["message"] = "Hi " + state["message"] + ", how is your day?"

    return state


graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")
app = graph.compile()
app.get_graph().print_ascii()

result = app.invoke({"message": "Bob"})
print(result["message"])

"""
$ python hello-world-graph.py 
+-----------+  
| __start__ |  
+-----------+  
      *        
      *        
      *        
 +---------+   
 | greeter |   
 +---------+   
      *        
      *        
      *        
 +---------+   
 | __end__ |   
 +---------+   
Hi Bob, how is your day?
"""
