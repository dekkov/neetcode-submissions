from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
        

        dirs = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]
        distance = 0
        while q:
            distance += 1
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = distance
                    q.append([nr,nc])
        

