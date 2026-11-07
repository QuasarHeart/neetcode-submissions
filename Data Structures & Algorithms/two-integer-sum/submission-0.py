class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        output=[]
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    output.append(i)
                    output.append(j)


        return output

        