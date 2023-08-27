""" 
Given tree, delete node, return forest
Input: root = [1,2,3,4,5,6,7], to_delete=[3,5]
Output: [[1,2,null,4],[6],[7]]

Breadth first search, using queue
"""

from typing import List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:

    def __init__(self):
        self.output = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root.val not in to_delete:
            self.output.append(root)

        queue = [root]
        while queue:
            node = queue.pop(0)    # popup from beginning
            if node.val in to_delete:
                if node.left:
                    self.delNodes(node.left, to_delete)
                if node.right:   
                    self.delNodes(node.right, to_delete)

            print(node.val)    # traverse tree 
            if node.left:
                queue.append(node.left)
                if node.left.val in to_delete:
                    node.left = None 

            if node.right:
                queue.append(node.right)
                if node.right.val in to_delete:
                    node.rght = None 

        return self.output

tr = TreeNode(1)
tr.left = TreeNode(2)
tr.right = TreeNode(3)
tr.left.left = TreeNode(4)
tr.left.right = TreeNode(5)
tr.right.left = TreeNode(6)
tr.right.right = TreeNode(7)

print(list(Solution().delNodes(tr, [3,5]))        )