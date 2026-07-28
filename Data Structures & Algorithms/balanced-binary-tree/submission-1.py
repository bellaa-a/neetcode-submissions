# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.dfs(root)
        return self.balanced
    
    def dfs(self, root):
        if root is None:
            return 0
        depth_left = self.dfs(root.left) if root.left else 0
        depth_right = self.dfs(root.right) if root.right else 0
        if abs(depth_left - depth_right) > 1:
            self.balanced = False
        return max(depth_left, depth_right) + 1