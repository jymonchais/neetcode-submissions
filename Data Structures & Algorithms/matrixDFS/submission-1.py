class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def bfs(graph: List[List[int]], r: int, c: int, visit: set) -> int:
            count = 0

            #check if out of bounds or blocked
            if (min(r, c) < 0 or r == ROWS or c ==  COLS or graph[r][c] == 1
                or (r, c) in visit):
                return 0
            elif r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))

            count += bfs(graph, r - 1, c, visit)
            count += bfs(graph, r + 1, c, visit)
            count += bfs(graph, r, c + 1, visit)
            count += bfs(graph, r, c - 1, visit)

            visit.remove((r, c))
            return count


        return bfs(grid, 0, 0, seen)