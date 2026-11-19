from math import factorial

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = factorial(len(nums))
        used = [False]*len(nums)
        def backtrack(nums,path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                else:
                    continue
                backtrack(nums,path)
                path.pop()
                used[i] = False
        backtrack(nums,[])

        return res 
