# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head
        second = first.next
        head.next = None
        while second != None:
            node = first
            first = second
            second = second.next
            first.next = node

        return first
            
            



        return head
        