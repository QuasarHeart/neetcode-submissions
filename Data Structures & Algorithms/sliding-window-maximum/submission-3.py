from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        deq = deque()
        if length<k:
            return []
        # maximum = float('-inf')
        output = []
        first = 0
        # second = k-1
        # while second < length:
        #     # maximum = max(nums[first:second+1])
        #     # output.append(maximum)
        #     # second+=1
        #     # first+=1

        for second in range(length):
            if not deq:
                deq.append(second)
            else:
                while deq and nums[second]>=nums[deq[-1]]:
                    deq.pop()
                deq.append(second)

            if second-first+1 == k:
                output.append(nums[deq[0]])
                if deq[0] == first:
                    deq.popleft()
                first+=1
            

            

                
                
        return output

