# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        first = l1
        second = l2

        carry_over = 0
        while first or second:
            first_val = first.val if first else 0
            second_val = second.val if second else 0
            n = first_val + second_val + carry_over
            cur_val = n%10
            
            new_node = ListNode()
            new_node.val = cur_val
            node.next = new_node
            carry_over = int(n/10)

            node = node.next
            if first:
                first = first.next 
            if second:
                second = second.next
        
        if carry_over != 0:
            new_node = ListNode()
            new_node.val = carry_over
            node.next = new_node
        
        return dummy.next
