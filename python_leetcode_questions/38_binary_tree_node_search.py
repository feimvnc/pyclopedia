# Definition of a binary tree node.
# Search value in a binary tree 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right  

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val==root.val:
                return root 
            elif val > root.val:
                root = root.right 
            else:
                root = root.left 
        return None 

    def searchBSTRecursive(self, root: TreeNode, val: int) ->TreeNode:
        if root is None:
            return None 
        elif val == root.val:
            return root 
        elif val > root.val:
            return self.searchBSTRecursive(root.right, val)
        else:
            return self.searchBSTRecursive(root.left, val)

    def searchBSTRecursive_2(self, root: TreeNode, val: int)-> TreeNode:
        # base case
        if not root: return None 
        if root.val == val: return root 

        # recursion relation 
        if val > root.val:
            return self.searchBSTRecursive_2(root.right, val)
        else:
            return self.searchBSTRecursive_2(root.left, val)


t = TreeNode(5)
t.left=TreeNode(2)
t.left.left=TreeNode(1)
t.right=TreeNode(7)
t.right.left=TreeNode(6)
t.right.right=TreeNode(8)

target=TreeNode(1)
print(Solution().searchBST(t, target.val).val)

target=TreeNode(6)
print(Solution().searchBST(t, target.val).val)

target=TreeNode(5)
print(Solution().searchBSTRecursive(t, target.val).val)

target=TreeNode(10)
print(Solution().searchBSTRecursive_2(t, target.val).val)

