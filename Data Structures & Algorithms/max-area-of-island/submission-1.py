class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(r,c):
            
            if r < 0 or c < 0 or c >= cols or r >= rows or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            
            return 1+dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1)
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    curr = dfs(i,j)
                    maxArea = max(maxArea,curr)

        return maxArea



        

            