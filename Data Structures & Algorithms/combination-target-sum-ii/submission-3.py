class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, path, total):
            # 1. 找到目标和，记录结果
            if total == target:
                res.append(path[:])
                return
            # 2. 超过目标和，直接剪枝（停止继续往下选）
            if total > target:
                return

            # 3. 从 start 开始往后选，避免出现 [2,5,2] 这种重复组合
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    return 
                if i > start and candidates[i] == candidates[i-1] :
                    continue
                
                path.append(candidates[i])
                # 关键点：这里传 i 而不是 i + 1，允许重复使用当前数字
                backtrack(i+1, path, total + candidates[i])
                path.pop()  # 撤销选择（回溯）

        backtrack(0, [], 0)
        return res