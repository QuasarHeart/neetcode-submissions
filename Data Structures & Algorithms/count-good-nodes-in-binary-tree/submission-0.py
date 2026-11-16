# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maximum = [float('-inf')]
        self.count = 0
        def dfs(root):
            if not root:
                return 
            if root.val >= self.maximum[-1]:
                self.count+=1
                self.maximum.append(root.val)
                
            dfs(root.left)
            dfs(root.right)
            if root.val == self.maximum[-1]:
                self.maximum.pop()
            return 

        dfs(root)

        return self.count

        
