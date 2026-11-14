from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                return num
            else:
                nums_map[num] = 1

            

        return -1

        