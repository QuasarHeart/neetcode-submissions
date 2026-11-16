# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deq = deque()
        deq.append(root)
        output = []
        flag = True
        while flag:
            flag = False
            to_pop = deque()
            tmp = []
            while deq:
                node = deq.popleft()
                to_pop.append(node)
                tmp.append(node.val)
            output.append(tmp)

            while to_pop:
                node = to_pop.popleft()
                if node:
                    if node.left:
                        deq.append(node.left)
                        flag = True
                     
                    if node.right:
                        deq.append(node.right)
                        flag = True

        

        return output




