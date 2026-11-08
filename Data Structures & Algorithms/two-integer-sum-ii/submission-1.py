class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        pre = 0
        post = length-1
        output = []
        while True:
            if numbers[pre]+numbers[post]>target:
                post-=1
            elif numbers[pre]+numbers[post]<target:
                pre+=1
            else:
                output.append(pre+1)
                output.append(post+1)
                break

        return output

                