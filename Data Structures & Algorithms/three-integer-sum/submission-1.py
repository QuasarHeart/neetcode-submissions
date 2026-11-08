class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        output = []
        nums.sort()
        for idx in range(length-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            if nums[idx] > 0:
                break

            pre = idx+1
            post = length-1

            while pre < post:
                current_sum = nums[idx] + nums[pre] + nums[post]

                if current_sum > 0:
                    post -= 1
                elif current_sum < 0:
                    pre+=1
                else:
                    output.append([nums[idx],nums[pre],nums[post]])

                    while pre<post and nums[pre] == nums[pre+1]:
                        pre+=1
                    while pre<post and nums[post] == nums[post-1]:
                        post-=1

                    pre+=1
                    post-=1


        return output

        

                    

            


        