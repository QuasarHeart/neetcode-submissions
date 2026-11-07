class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        
        # 使用 enumerate 可以同时拿到索引 i 和数值 num，写起来更地道
        for i, num in enumerate(nums):
            temp = target - num
            if temp in hashmap:
                return [hashmap[temp], i]  # 找到答案直接返回，天然是有序的
            hashmap[num] = i


        