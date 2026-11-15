# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        # if root:
        #     return 0
        # def dfs(node):
        #     if node.left:
        #         self.count+=1
        #     if node.right:
        #         self.count+=1

        # dfs(root)
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.count = max(self.count, left+right)
            return max(left,right)+1

        dfs(root)

        return self.count
