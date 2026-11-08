class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if not nums:
            return 0
        nums.sort()
        longest = 1
        length = len(nums)
        current = 1
        for i in range(1,length):
            if nums[i]-nums[i-1]==1:
                current+=1
            elif current>longest:
                longest = current
                current = 1
            else:
                current = 1
        if current > longest:
            longest = current
            


        return longest