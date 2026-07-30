# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        return self.dfs(root.left, -float("inf"), root.val) and self.dfs(root.right, root.val, float("inf"))


    def dfs(self, root, small, large):
        if not root: return True

        if root.val >= large or root.val <= small:
            return False

        return self.dfs(root.left, small, root.val) and self.dfs(root.right, root.val, large)


