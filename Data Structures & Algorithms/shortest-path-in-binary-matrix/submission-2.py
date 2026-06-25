class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[len(grid) - 1][len(grid)-1]:
            return -1
        
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([(0, 0, 1)])
        visited = set((0, 0))

        while queue:
            r, c, length = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            for rMove, cMove in moves:
                newr = r + rMove
                newc = c + cMove
                if (0 <= newr < ROWS and 0 <= newc < COLS and
                   grid[newr][newc] == 0 and (newr, newc) not in visited):
                        queue.append((newr, newc, length + 1))
                        visited.add((newr, newc))
            

        return -1