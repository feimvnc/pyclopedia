""" 
Graph is a non-linear data structure, represneted maps or networks.

BFS traversal: 
start with a vertex, print its value 
print all neighbors of current vertex
select above neigbors and print all their neighbors
until all the vertices are printed 

"""

# parameters: graph, start_point
def bfs(graph, start):
    queue = []   # define an empty array, dynamically append (add) or pop (remove)
    queue.append(start)
    visited = set()
    visited.add(start)

    while (len(queue)>0):
        vertex = queue.pop(0)
        nodes = graph[vertex]

        for w in nodes:
            if w not in visited:
                queue.append(w)
                visited.add(w)
        print(vertex)

# define a fully connected graph using map, point, and adjancent points
# a fully connected graph - we can reach all vertex from starting vertex 
graph = {
    'A': ['B', 'D', 'E', 'F'], 
    'D': ['A'], 
    'B': ['A', 'F', 'C'], 
    'F': ['B', 'A'], 
    'C': ['B'], 
    'E': ['A']
    }

if __name__ == "__main__":
    bfs(graph, 'A')