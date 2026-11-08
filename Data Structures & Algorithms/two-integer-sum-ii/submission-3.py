class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        pre = 0
        post = length-1
        while True:
            if numbers[pre]+numbers[post]>target:
                post-=1
            elif numbers[pre]+numbers[post]<target:
                pre+=1
            else:
                return [pre+1,post+1]


        return []

                