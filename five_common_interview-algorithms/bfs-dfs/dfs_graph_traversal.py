""" 
In Depth First Search, 
-continue traverse downwards through linked nodes until reach thee end
-retrace steps to check which connected nodes not visited
-repeat the process

DFS is "deep dive the graph, backtrack when reach at the bottom".

We use stack data structure to keep track the visited nodes.
-Add node to stack 
-Marked it as visited 
-Check if this node has any adjaccent nodes:
    Yes, visit the node 
    No, remove from stack

DFS 
Time: O(n)
Data structures: HashSet, Stack
"""

from typing import Dict, List 

def dfs(graph: Dict[int, List[int]], start_node: int, visited: List[bool], results: List[int]):
    results.append(start_node)    # Use stack to store visited nodes 
    visited[start_node] = True    # Track if visited 

    # Traverse to each adjacent node of a node 
    for child_node in graph[start_node]:
        if not visited[child_node]:    # check if visited
            dfs(graph, child_node, visited, results)    # call recursively


if __name__ == "__main__":
    # Graph of noddes 
    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    start_node = 0     # starting node 
    visited = [ False ] * len(graph)    # init all visited nodes with False 
    results = []     # 
    dfs(graph, start_node, visited, results)    # start to traverse 
    print(f"{graph=}")
    print(f"{results=}")
    for i, visited in enumerate(visited):
        print(f"{i=} {visited=}")

# output 
# graph={0: [2], 1: [2, 3], 2: [0, 1, 4], 3: [1, 4], 4: [2, 3]}
# results=[0, 2, 1, 3, 4]
# i=0 visited=True
# i=1 visited=True
# i=2 visited=True
# i=3 visited=True
# i=4 visited=True    