# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. 用哈希表记录 inorder 中每个值的下标，实现 O(1) 查找
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 记录当前处理到了 preorder 的第几个元素
        self.pre_idx = 0

        # left 和 right 代表当前子树在 inorder 中的左右边界
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            # 区间为空，说明没有节点了
            if left > right:
                return None

            # 2. 从 preorder 取出当前根节点，并将指针后移一位
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # 3. O(1) 查出根节点在 inorder 中的位置，切分左右子树区间
            mid = inorder_map[root_val]

            # 4. 必须先建左子树，再建右子树（与 preorder 的顺序严格一致）
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)

            
            
            

                









        

        