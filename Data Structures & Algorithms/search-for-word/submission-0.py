from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # 剪枝 1：统计字符数量，如果棋盘字符不够直接返回 False
        board_count = Counter(char for row in board for char in row)
        word_count = Counter(word)
        for char, count in word_count.items():
            if board_count[char] < count:
                return False
                
        # 剪枝 2：如果首字母比尾字母出现次数多，反转单词从更稀疏的一端开始搜
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def backtrack(r: int, c: int, index: int) -> bool:
            # 终止条件：所有字符都匹配成功
            if index == len(word):
                return True
            
            # 剪枝 3：越界、已访问('#')、或当前字符不匹配
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # 做选择：临时标记当前格子为已访问
            temp = board[r][c]
            board[r][c] = '#'
            
            # 向四个方向探索，只要有一条路走通就立刻返回 True（短路求值）
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            # 撤销选择（回溯）：恢复现场
            board[r][c] = temp
            
            return found

        # 遍历棋盘上的每一个格子作为起点
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
                    
        return False

        


        


        
        