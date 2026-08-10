class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        seen = set()
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(r, c):
            nonlocal res
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                res += 1
                return
            seen.add((r,c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr,nc) in seen:
                    continue
                else:
                    dfs(nr,nc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return res
        return res