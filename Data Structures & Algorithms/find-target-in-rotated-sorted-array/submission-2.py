class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        if target > nums[-1]:
            left = 0
            right = right-1
        else:
            right = len(nums)-1    
        while left <= right:
            mid = (left+right)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid

        return -1
                

            
