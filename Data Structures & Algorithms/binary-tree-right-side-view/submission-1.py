# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        deq = deque([root])

        while deq:
            size = len(deq)
            for i in range(size):
                node = deq.popleft()

                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                if i == size-1:
                    output.append(node.val)

            


        return output



            
