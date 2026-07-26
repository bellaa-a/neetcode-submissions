# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0
        cur = cur1 = head

        while cur:
            num += 1
            cur = cur.next
        
        front = num - n + 1
        i = 1
        if n == num:
            head = head.next
            return head

        prev = None
        while cur1:
            if i == front:
                prev.next = cur1.next
            i += 1
            prev = cur1
            cur1 = cur1.next

        return head