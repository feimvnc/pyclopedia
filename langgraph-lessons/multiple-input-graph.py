# More complex AgentState
# Operations on list data
# Handle multiple inputs

from typing import List, TypedDict

from langgraph.graph import StateGraph


class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str


def process_values(state: AgentState) -> AgentState:
    """This function handles multiple different inputs."""
    print(f"Before {state}")
    state["result"] = f"Hi {state['name']}! Your sum = {sum(state['values'])}"
    print(f"After {state}")
    return state


graph = StateGraph(AgentState)
graph.add_node("processor", process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")
app = graph.compile()

app.get_graph().print_ascii()

answers = app.invoke({"values": [1, 2, 3], "name": "Bob"})
print(f"{answers=}")
print(f"{answers['result']=}")


"""
$ python multiple-input-graph.py 
+-----------+  
| __start__ |  
+-----------+  
      *        
      *        
      *        
+-----------+  
| processor |  
+-----------+  
      *        
      *        
      *        
 +---------+   
 | __end__ |   
 +---------+   
Before {'values': [1, 2, 3], 'name': 'Bob'}
After {'values': [1, 2, 3], 'name': 'Bob', 'result': 'Hi Bob! Your sum = 6'}
answers={'values': [1, 2, 3], 'name': 'Bob', 'result': 'Hi Bob! Your sum = 6'}
answers['result']='Hi Bob! Your sum = 6'

"""
