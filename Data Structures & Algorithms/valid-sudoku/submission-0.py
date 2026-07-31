class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(9)]
        col_sets = [set() for i in range(9)]
        square_sets = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in row_sets[r]:
                    return False
                else:
                    row_sets[r].add(num)
                
                if num in col_sets[c]:
                    return False
                else:
                    col_sets[c].add(num)

                square = (r // 3) * 3 + (c // 3)
                if num in square_sets[square]:
                    return False
                else:
                    square_sets[square].add(num)

        return True
        