from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        """
            BFS: Start with rotten fruit -> explore nearby 

            deque
        """

        q = deque() #(rottent grids: (r,c))
        dirs = (
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        )
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                
                if grid[r][c] == 1:
                    fresh += 1
    
        time = 0
        while q and fresh:
            time += 1
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 0:
                    continue

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))



        return time if not fresh else -1
