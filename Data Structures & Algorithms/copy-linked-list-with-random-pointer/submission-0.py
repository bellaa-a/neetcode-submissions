"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashmap = {}
        cur = head

        dummy = node = Node(0)
        while cur:
            new_node = Node(cur.val)
            node.next = new_node
            hashmap[cur] = new_node

            node = node.next
            cur = cur.next
        
        cur = head
        node = dummy.next
        while cur:
            if cur.random:
                node.random = hashmap[cur.random]
            else:
                node.random = None
            node = node.next
            cur = cur.next
        
        return dummy.next