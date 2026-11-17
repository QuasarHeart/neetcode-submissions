# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.res = []
        self.val = 0
        self.kth = 0
        def dfs(root,k):
            if not root:
                return 

            if root.left:
                dfs(root.left,k)
            
            self.kth+=1
            if self.kth == k:
                self.val = root.val

            if root.right:
                dfs(root.right,k)


        dfs(root,k)
        return self.val