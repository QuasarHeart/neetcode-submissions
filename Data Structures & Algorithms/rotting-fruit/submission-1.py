from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 1. 遍历整个网格：统计新鲜橘子数量，并把所有初始腐烂橘子同时入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # 如果一开始就没有新鲜橘子，0 分钟就全部完成了
        if fresh == 0:
            return 0

        time = 0

        # 2. 多源 BFS：只要还有腐烂橘子在扩散，且还有新鲜橘子没被感染
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # 注意：包含 0 边界，且只感染新鲜橘子 (== 1)
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            # 扩散完一圈，时间 + 1
            time += 1

        # 3. 如果还有新鲜橘子残留，说明无法全部腐烂，返回 -1
        return time if fresh == 0 else -1

                

        