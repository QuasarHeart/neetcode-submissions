class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 既是结尾标记，又直接存完整单词


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 建树：把所有目标单词塞进 Prefix Tree
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w  # 在结尾处直接存下整个单词

        ROWS, COLS = len(board), len(board[0])
        res = []

        # 2. 定义网格 DFS 回溯函数
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # 如果当前节点存着完整单词，说明找到了！
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # 立刻核销，防止不同路径重复收集同一个词

            # 标记当前格子已走过（防止走回头路）
            board[r][c] = "#"

            # 向上下左右 4 个方向探索
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # 只有不出界、没走过、且在树里有对应路径时，才往下递归
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and board[nr][nc] != "#"
                    and board[nr][nc] in curr_node.children
                ):
                    dfs(nr, nc, curr_node)

            # 回溯：离开这个格子时，把 '#' 还原成原来的字母
            board[r][c] = char

            # 【满分剪枝优化】：如果当前节点下面已经没有任何子节点了，说明这条路彻底找完了
            # 直接从父节点里把它删掉，以后再也不走这条死胡同！
            if not curr_node.children:
                parent_node.children.pop(char)

        # 3. 遍历网格的每一个格子作为起点出发
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res

