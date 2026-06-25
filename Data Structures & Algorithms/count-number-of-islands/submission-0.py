class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #could be dfs due to be back tracking
        ROWS, COLS = len(grid), len(grid[0])

        #will be a set of (int, int) pairs
        visited = set()

        #will be a list of viable islands
        islands = []

        def dfs(r, c, comp) -> None:
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == "0" or (r, c) in visited):
                    return 

            
            visited.add((r, c))
            comp.add((r, c))

            dfs(r + 1, c, comp)
            dfs(r - 1, c, comp)
            dfs(r, c + 1, comp)
            dfs(r, c - 1, comp)

        # scan all cells and start a new component when we find unvisited land
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    comp  = set()
                    dfs(r, c, comp)
                    islands.append(comp)

    
        return len(islands)