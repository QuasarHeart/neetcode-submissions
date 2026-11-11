class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_d = [item for line in matrix for item in line]
        length = len(one_d)
        left = 0
        right = length-1

        while left <= right:
            mid = (right+left)//2
            if one_d[mid]==target:
                return True
            elif one_d[mid]>target:
                right = mid-1
            else:
                left = mid+1

        return False

            

        