"""
Conditional Graph
Route flow of data to different nodes
Use START and END nodes to manage entry and exit points explicitly.
Multiple nodes to perform different operations (addition, substraction)
Create a router node to handle decision-making and control graph flow.

"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    finalNumber: int


def adder(state: AgentState) -> AgentState:
    state["finalNumber"] = state["number1"] + state["number2"]
    return state


def subtractor(state: AgentState) -> AgentState:
    state["finalNumber"] = state["number1"] - state["number2"]
    return state


def decide_next_node(state: AgentState) -> AgentState:
    if state["operation"] == "+":
        return "addition_operation"

    if state["operation"] == "-":
        return "subtraction_operation"


graph = StateGraph(AgentState)

graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state: state)  # passthrough function

graph.add_edge(START, "router")

graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        # Edge: Node
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node",
    },
)

graph.add_edge("add_node", END)
graph.add_edge("subtract_node", END)

app = graph.compile()
app.get_graph().print_ascii()

initial_state_1 = AgentState(number1=10, operation="-", number2=5)
print(app.invoke(initial_state_1))

initial_state_2 = AgentState(number1=10, operation="+", number2=5)
print(app.invoke(initial_state_2))


"""
$ python conditional_graph.py 
            +-----------+                
            | __start__ |                
            +-----------+                
                  *                      
                  *                      
                  *                      
             +--------+                  
             | router |                  
             +--------+                  
           ...         ...               
          .               .              
        ..                 ..            
+----------+          +---------------+  
| add_node |          | subtract_node |  
+----------+          +---------------+  
           ***         ***               
              *       *                  
               **   **                   
             +---------+                 
             | __end__ |                 
             +---------+                 
{'number1': 10, 'operation': '-', 'number2': 5, 'finalNumber': 5}
{'number1': 10, 'operation': '+', 'number2': 5, 'finalNumber': 15}
"""
