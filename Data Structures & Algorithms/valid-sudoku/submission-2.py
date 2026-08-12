from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        boxes = defaultdict(set) 

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val != ".":
                    if val in rows[r]:
                      return False
                    rows[r].add(val)
                    if val in cols[c]:
                        return False
                    cols[c].add(val)
                    if val in boxes[(r//3, c//3)]:
                        return False
                    boxes[(r//3, c//3)].add(val)
        return True