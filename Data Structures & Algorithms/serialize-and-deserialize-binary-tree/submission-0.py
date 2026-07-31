# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        queue = deque([root])
        while queue:
            root = queue.popleft()
            if not root: 
                res += "N,"
            else:
                res += str(root.val) + ","
                queue.append(root.left)
                queue.append(root.right)
        
        return res
    
    def get_data(self):
            value = ""
            if self.data[self.i] == "N":
                self.i += 2
                return None
            while self.data[self.i] != ",":
                value += self.data[self.i]
                self.i += 1
            self.i += 1
            root = TreeNode()
            root.val = value
            return root
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        self.data = data
        start = self.get_data()

        if not start: return None
        queue = deque([start])
        while queue:
            root = queue.popleft()
            left = self.get_data()
            right = self.get_data()
            if left: queue.append(left)
            if right: queue.append(right)
            root.left = left
            root.right = right
        
        return start

        
