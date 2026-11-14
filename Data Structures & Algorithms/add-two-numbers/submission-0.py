# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        node1 = l1
        node2 = l2
        n1 = 0
        n2 = 0
        while node1:
            sum1+=node1.val*pow(10,n1)
            node1 = node1.next
            n1+=1
        
        while node2:
            sum2+=node2.val*pow(10,n2)
            node2 = node2.next
            n2+=1
        sum12 = sum1+sum2

        digit = sum12%10
        head = ListNode(digit)
        sum12 = sum12//10
        newnode = head
        while sum12 != 0:
            digit = sum12%10
            newnode.next = ListNode(digit)
            newnode = newnode.next
            sum12 = sum12//10

        return head


