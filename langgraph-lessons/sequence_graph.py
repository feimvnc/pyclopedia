"""
Create multiple Nodes that sequentially process and update different parts of the state.
Connect Nodes together in a graph.
Invoke the Graph and see how the state is transformed.
"""

from typing import TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    age: str
    final: str


def first_node(state: AgentState) -> AgentState:
    state["final"] = f"Hi {state['name']}"
    return state


def second_node(state: AgentState) -> AgentState:
    state["final"] = state["final"] + f"You are {state['age']} years old."
    return state


graph = StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")
app = graph.compile()

app.get_graph().print_ascii()
result = app.invoke({"name": "Bob", "age": "30"})
print(result)


"""
$ python sequence_graph.py 
 +-----------+   
 | __start__ |   
 +-----------+   
        *        
        *        
        *        
+------------+   
| first_node |   
+------------+   
        *        
        *        
        *        
+-------------+  
| second_node |  
+-------------+  
        *        
        *        
        *        
  +---------+    
  | __end__ |    
  +---------+    
{'name': 'Bob', 'age': '30', 'final': 'Hi BobYou are 30 years old.'}
"""
