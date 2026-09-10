class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Loop through the grid first
            dfs(i,j)
            Do DFS on the any time we see a "1"
                explore all path possible then mark it with 0 or "#" -> we don't run into it / recompute it again
        """

        ROWS, COLS = len(grid), len(grid[0])
        dirs = ([0,1], [1,0], [-1,0], [0,-1])
        def dfs(i, j):
            if min(i,j) < 0 or i >= ROWS or j >= COLS or grid[i][j] != "1":
                return
            
            grid[i][j] = "#"

            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                dfs(nr, nc)

        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    ans += 1
        
        return ans
        
        