class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res+=[curr + [num] for curr in res]

        return [list(x) for x in set(tuple(sorted(t)) for t in res)]