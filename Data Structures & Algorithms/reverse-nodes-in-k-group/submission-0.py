# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev_group = ListNode()
        dummy.next = head
        left = right = head
        while True:
            cur = right
            for i in range(k-1):
                if cur is None:
                    return dummy.next
                cur = cur.next
            
            if cur is None:
                return dummy.next
            right = cur.next

            prev = None
            cur = left
            while cur != right:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            left.next = right
            prev_group.next = prev
            prev_group = left
            left = right
            


            