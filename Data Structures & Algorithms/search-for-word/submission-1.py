class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(0,1), (1,0), (-1,0), (0, -1)]
        def dfs(i, j, index):
            if index >= len(word):
                return True
            if (i,j) in visited or min(i,j) < 0 or i >= ROWS or j >= COLS or board[i][j] != word[index]:
                return False
            
            visited.add((i,j))
            for dr, dc in dirs:
                r = i + dr
                c = j + dc
                if dfs(r,c,index+1):
                    return True
            visited.remove((i,j))
            
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r,c,0):
                        return True

        return False


            
