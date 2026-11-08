class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        length = len(height)
        total = 0
        right = length-1
        left = 0
        right_max = height[right]
        left_max = height[left]
        while right > left:
            if left_max < right_max:
                left+=1
                left_max = max(left_max,height[left])
                total += left_max-height[left]
            else:
                right-=1
                right_max = max(right_max,height[right])
                total+=right_max-height[right] 

                   

        return total

        