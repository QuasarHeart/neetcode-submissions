class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maximum = 0
        pre = 0
        post = length-1
        while pre < post:
            current = min(heights[pre],heights[post])*(post-pre)
            maximum = max(maximum,current)
            if heights[pre]<heights[post]:
                pre+=1
            else:
                post-=1

            

        
        return maximum