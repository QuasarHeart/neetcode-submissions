# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 1. 处理空树边界
        if not root:
            return ""
            
        res = []
        deq = deque([root])
        
        while deq:
            node = deq.popleft()
            if node:
                res.append(str(node.val))
                # 不管左右孩子是不是 None，都放进队列，留到出队时统一处理
                deq.append(node.left)
                deq.append(node.right)
            else:
                res.append("None")
                
        # 用 '#' 拼接列表，开头和结尾都不会有多余的 '#'
        return "#".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 1. 处理空树边界
        if not data:
            return None
            
        raw = data.split("#")
        # 2. 建出根节点，并放入队列准备认领左右孩子
        root = TreeNode(int(raw[0]))
        deq = deque([root])
        idx = 1  # 指向下一个待分配的孩子节点
        
        while deq:
            node = deq.popleft()
            
            # 3. 认领左孩子
            if raw[idx] != "None":
                node.left = TreeNode(int(raw[idx]))
                deq.append(node.left)  # 只有真实存在的节点才有资格拥有自己的孩子
            idx += 1
            
            # 4. 认领右孩子
            if raw[idx] != "None":
                node.right = TreeNode(int(raw[idx]))
                deq.append(node.right)
            idx += 1
            
        return root

            

