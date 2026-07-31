# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = preorder[0]
        node = TreeNode()
        node.val = root

        mid = 0
        while root != inorder[mid]:
            mid += 1

        node.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return node
