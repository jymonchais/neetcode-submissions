class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Need to search through each row and col
        # For row, we can say broad[i] and make that the refernce
        # for cols, we say say board[x][j]
        # for the diagona, we do the /3 operation??
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set) # the ket is r // 3 and c // 3
        

        for r in range(9):
            for c in range(9):
                #row check, snce the col is increasing
                if board[r][c] == '.':
                    continue
                
                cell = board[r][c]

                if (cell in rows[r]) or (cell in cols[c]) or (cell in box[(r // 3), (c // 3)]):
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                box[(r//3), (c//3)].add(cell)

                
        return True