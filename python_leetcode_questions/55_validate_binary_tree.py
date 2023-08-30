""" 
Validate binary tree
Given a binary tree, validate if it is valid or not.
A validate binary tree is: left node < parent node < right node 

Approach: recursive, divide and conquer
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math 

class Solution:
    def isValidateBST(self, root: TreeNode) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:    # empty tree is valid BST
                return True 
            if node.val <= low or node.val >= high:    # valid value must be between
                return False  
            return (validate(node.right, node.val, high) and      # divide, and combine 
                    validate(node.left, low, node.val))

        return validate(root)

t = TreeNode(5)
t.left=TreeNode(2)
t.left.left=TreeNode(1)
t.right=TreeNode(7)
t.right.left=TreeNode(6)
t.right.right=TreeNode(8)

print(Solution().isValidateBST(t))

