"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 用字典建立 {原节点: 新节点} 的映射，预先放入 None 防止空指针报错
        old_to_new = {None: None}

        # 第一趟：复制所有节点的值，存入字典
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 第二趟：根据字典映射，连接 next 和 random 指针
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]

            



        