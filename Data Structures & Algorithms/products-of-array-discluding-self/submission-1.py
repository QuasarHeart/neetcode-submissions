from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        hashmap = Counter(nums)
        for idx,num in enumerate(nums):
            temp = 1
            hashmap[num] -= 1
            for n,count in hashmap.items():
                temp = temp * n**count
            output[idx] = temp
            hashmap[num]+=1
                
        return output
