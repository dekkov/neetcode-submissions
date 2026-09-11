class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = (
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        )
        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            temp = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                temp += dfs(nr,nc)
            
            return temp

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r,c))
        
        return ans