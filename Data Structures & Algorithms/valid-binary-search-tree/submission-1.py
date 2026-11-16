# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.output = []
        def dfs(root):
            if not root:
                return 
            if root.left:
                dfs(root.left)
            self.output.append(root.val)
            if root.right:
                dfs(root.right)

            return 

        dfs(root)

        for i in range(len(self.output) - 1):
            if self.output[i] >= self.output[i + 1]:
                return False
        return True

            


        