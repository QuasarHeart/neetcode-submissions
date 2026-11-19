class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False]*len(nums)
        def backtrack(nums,path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums,path)
                path.pop()
                used[i] = False
        backtrack(nums,[])

        return res 
