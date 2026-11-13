# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        node = head
        while count < 1001:
            if node == None:
                return False
            node = node.next
            count+=1
            

        return True