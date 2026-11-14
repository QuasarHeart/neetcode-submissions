from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_map = Counter(nums)
        for key,val in nums_map.items():
            if val > 1:
                return key

        return -1

        