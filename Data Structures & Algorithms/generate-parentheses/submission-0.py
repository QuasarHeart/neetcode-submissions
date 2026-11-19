class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, left, right):
            # 1. 终止条件：左右括号都放满了（总长度达到 2n）
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # 2. 选择一：只要左括号还有剩余，就可以放左括号
            if left < n:
                path.append("(")
                backtrack(path, left + 1, right)
                path.pop()  # 撤销选择

            # 3. 选择二（核心剪枝）：只有当右括号数量严格小于左括号时，才能放右括号
            if right < left:
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()  # 撤销选择

        backtrack([], 0, 0)
        return res


