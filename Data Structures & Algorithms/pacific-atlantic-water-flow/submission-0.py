class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visited: set, prevHeight: int) -> None:
            # 终止条件：越界、已经访问过、或者邻居比当前矮（水无法从高处流下来）
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                or (r, c) in visited 
                or heights[r][c] < prevHeight):
                return

            visited.add((r, c))

            # 向四个方向继续往高处爬
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # 1. 从上边界（太平洋）和下边界（大西洋）出发
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # 2. 从左边界（太平洋）和右边界（大西洋）出发
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # 3. 找出既能到太平洋、又能到大西洋的格子（两个集合的交集）
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
