from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # 初始化 n x n 的棋盘，全部填满 '.'
        board = [["."] * n for _ in range(n)]
        
        cols = set()   # 记录已占用的列号: c
        diag1 = set()  # 记录已占用的主对角线（左上到右下）: r - c
        diag2 = set()  # 记录已占用的副对角线（右上到左下）: r + c

        def backtrack(r: int):
            # 终止条件：第 0 行到第 n-1 行都已经成功放上了皇后
            if r == n:
                # 把每一行的字符列表拼成字符串，存入结果集
                res.append(["".join(row) for row in board])
                return

            # 遍历当前第 r 行的每一列 c
            for c in range(n):
                # 剪枝：如果当前列或两条对角线已经有皇后了，直接跳过
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # 1. 做选择：在 (r, c) 放上皇后，并登记三个集合
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                # 2. 递归：去下一行 (r + 1) 放皇后
                backtrack(r + 1)

                # 3. 撤销选择（回溯）：拿走皇后，并从三个集合中注销
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        # 从第 0 行开始放皇后
        backtrack(0)
        return res
