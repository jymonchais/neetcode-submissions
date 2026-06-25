class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        #steps
        # check first entry of each row (treat as usual binary search)
        # let the search finish out then search that row?


        while top <= bot:
            mid = (top + bot) // 2

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][0]:
                top = mid + 1
            else:
                bot = mid
                break


        lt, rt = 0, len(matrix[mid]) - 1

        while lt <= rt:
            col = (lt + rt) // 2 

            if target > matrix[bot][col]:
                lt = col + 1
            elif target < matrix[bot][col]:
                rt = col - 1
            else:
                return True


        return False
            