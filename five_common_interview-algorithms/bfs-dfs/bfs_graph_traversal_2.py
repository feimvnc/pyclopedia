""" 
bfs graph traversal
"""

def bfs(graph, node):
    visited = []
    queue = [] 

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': []
}

if __name__ == '__main__':
    bfs(graph, 'A')