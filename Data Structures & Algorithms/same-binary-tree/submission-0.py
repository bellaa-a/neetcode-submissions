# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        self.dfs(p, q)
        return self.same

    def dfs(self, p, q):
        if p is None and q is not None:
            self.same = False
            return
        
        if q is None and p is not None:
            self.same = False
            return
        
        if p is None and q is None:
            return
            
        if p.val != q.val:
            self.same = False
        
        self.dfs(p.left, q.left)
        self.dfs(p.right, q.right)
