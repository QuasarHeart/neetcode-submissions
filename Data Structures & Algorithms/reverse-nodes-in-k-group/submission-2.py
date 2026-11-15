# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # node = head
        # length = 0
        # while node:
        #     node = node.next
        #     length+=1
        
        # reverse_num = length//k
        # count = 0
        # slow = head
        # fast = head
        # while count < reverse_num:
        #     count_k = 0
        #     while count_k < k:
        #         fast = fast.next
        slow = head
        fast = head
        flag = True
        dummy = head
        tail = None
        while fast:
            count = 0 
            while count < k and fast:
                if count == k-1:
                    if flag:
                        dummy = fast
                        flag=False
                    if tail:
                        tail.next = fast

                fast = fast.next
                count +=1

            if count < k:
                if tail:
                    tail.next = slow
                break
            new_tail = slow 
            prev = None
            while slow!=fast:
                tmp = slow.next 
                slow.next = prev
                prev = slow
                slow = tmp

            tail = new_tail


        return dummy
            




                



        

        

        