# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if not root: return self.res

        self.dfs(root, root.val)
        return self.res
        
    def dfs(self, root, cur_max):
        
        if root.val >= cur_max:
            self.res += 1
        cur_max = max(cur_max, root.val)

        if root.left: self.dfs(root.left, cur_max)
        if root.right: self.dfs(root.right, cur_max)

