""" 
Implement binary tree postorder traversal.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [(root, "visit")]
        while stack:
            node, label = stack.pop()
            if label == "visit":
                stack.append((node, "visited"))
                if node.right:
                    stack.append((node.right, "visit"))
                if node.left:
                    stack.append((node.left, "visit"))
            else:
                result.append(node.val)
        return result


""" 
1 
  \ 
   2 
  /
3
"""
node1 = TreeNode(1)
node1.right = TreeNode(2)
node1.right.left = TreeNode(3)

print(Solution().postorderTraversal(node1))
