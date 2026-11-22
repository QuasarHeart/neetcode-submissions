from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # 1. 先把所有宝箱 (0) 全部找出来，作为初始起点同时入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # 2. 从所有宝箱同时向外一圈圈扩散
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # 只要在网格内，且还是未访问过的空陆地 (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # 距离直接等于当前格子的距离 + 1（同时起到了标记已访问的作用）
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))



        


                    

