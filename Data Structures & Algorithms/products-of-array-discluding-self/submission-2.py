class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        length = len(nums)
        for idx in range(length):
            if idx-1>=0:
                output[idx]=nums[idx-1]*output[idx-1]
        temp = 1   
        for idx in range(length):
            postfix = length-idx-1
            if postfix+1<=length-1:
                temp*=nums[postfix+1]   
                output[postfix]*=temp  
        return output
