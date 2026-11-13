# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 快慢指针找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 断开链表，并反转后半部分
        second = slow.next
        slow.next = None  # 切断前半部分与后半部分的联系，防止成环
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. 交错合并前半部分（head）和反转后的后半部分（prev）
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



            

            



        