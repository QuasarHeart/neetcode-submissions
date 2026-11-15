# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:  # 只要有一个为空（上面已排除了都为空），或值不等，直接 False
                return False
            
            # Python 的 and 自带“短路剪枝”：如果左边返回 False，右边根本不会执行！
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if not root:
            return False

        if isSameTree(root,subRoot):
            return True


        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)


        