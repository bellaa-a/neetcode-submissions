# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            root = queue.popleft()
            res.append(root.val)
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
            
            for _ in range(len(queue)-1):
                root = queue.popleft()
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)   
            
        return res