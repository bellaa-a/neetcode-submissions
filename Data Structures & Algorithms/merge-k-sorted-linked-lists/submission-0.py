# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = node = ListNode()
        first = lists[0]

        for i in range(1, len(lists)):
            second = lists[i]
            while first and second:
                if first.val <= second.val:
                    node.next = first
                    first = first.next
                else:
                    node.next = second
                    second = second.next
                node = node.next
                
            if first: node.next = first
            if second: node.next = second

            first = dummy.next
            node = dummy
        
        return dummy.next
