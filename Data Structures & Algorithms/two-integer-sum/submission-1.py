class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        output=[]
        hashmap={}
        # for i in range(length):
        #     for j in range(i+1,length):
        #         if nums[i]+nums[j] == target:
        #             output.append(i)
        #             output.append(j)
        for i in range(length):
            temp = target-nums[i]
            if temp in hashmap:
                output.append(i)
                output.append(hashmap[temp])
                output.sort()
                break
            else:
                hashmap[nums[i]]=i

        return output
                





        return output

        