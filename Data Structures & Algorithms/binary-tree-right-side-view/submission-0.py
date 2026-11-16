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
            tmp = []
            for _ in range(len(deq)):
                node = deq.popleft()
                tmp.append(node.val)

                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            output.append(tmp[-1])


        return output



            
