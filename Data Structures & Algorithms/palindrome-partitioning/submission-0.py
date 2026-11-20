class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start: int):
            # 1. 终止条件：已经切到字符串末尾
            if start == len(s):
                res.append(path.copy())
                return

            # 2. 遍历当前层所有可能的切割终点 end
            for end in range(start, len(s)):
                sub = s[start : end + 1]
                
                # 剪枝：如果切出来的子串不是回文，直接跳过，不往下走
                if sub != sub[::-1]:
                    continue
                
                # 3. 做选择：把合法的回文子串加入路径
                path.append(sub)
                
                # 4. 递归：从 end + 1 的位置继续切剩下的字符串
                backtrack(end + 1)
                
                # 5. 撤销选择（回溯）
                path.pop()

        backtrack(0)
        return res
