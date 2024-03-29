""" 
An example of using bfs and decoupled functions, followinig coding style
"""
import collections

class UndirectedGraphNode:
    def __init__(self, label: str):
        self.label = label 
        self.neighbors = None 


class Solution:
    def cloneGraph(self, node):
        if  not node:
            return None 
       
        # step 1: find nodes 
        nodes = self.find_nodes_by_bfs(node)
        # step 2: copy nodes 
        mapping = self.copy_nodes(nodes)
        # step 3: copy edges 
        self.copy_edges(nodes, mapping)

        return mapping[node]

    def find_nodes_by_bfs(self, node):
        queue = collections.defaultdict([node])
        visited = set([node])
        while queue: 
            curt_node = queue.popleft()
            for neighbor in curt_node.neighbors:
                if neighbor in visited:
                    continue 
                visited.add(neighbor)
                queue.append(neighbor)
        return list(visited)

    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping 

    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

Solution()