# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = root.val
        def dfs(root):
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left = max(dfs(root.left),0)
            if root.right:
                right = max(dfs(root.right),0)

            self.maximum = max(self.maximum,root.val + left + right)

            return root.val + max(left,right)
            

        dfs(root)
        return self.maximum