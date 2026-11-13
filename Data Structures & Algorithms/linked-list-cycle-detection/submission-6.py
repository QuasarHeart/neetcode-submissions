# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # count = 0
        # node = head
        # while count < 1001:
        #     if node == None:
        #         return False
        #     node = node.next
        #     count+=1       
        # return True
        # if not head:
        #     return False
        # slow = head
        # fast = slow.next

        # while fast != None:
        #     if fast == slow:
        #         return True
        #     slow = slow.next
        #     fast = fast.next
        #     if fast != None:
        #         fast = fast.next

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

        