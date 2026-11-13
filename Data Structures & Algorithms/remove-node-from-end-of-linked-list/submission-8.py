# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy
        count = 0
    
        while count < n:
            fast = fast.next
            count += 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = temp.next
        temp.next = None
        head = dummy.next
        return head

        