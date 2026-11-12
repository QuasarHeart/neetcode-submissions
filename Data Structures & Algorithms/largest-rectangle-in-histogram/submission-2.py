class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        wide = list(set(heights))
        wide.sort()
        largest = wide[-1]

        for w in wide:
            length = 0
            for height in heights:
                if w <= height:
                    length+=1
                else:
                    largest = max(largest,w*length)
                    length = 0
            largest = max(largest,w*length)
            
            

        return largest

