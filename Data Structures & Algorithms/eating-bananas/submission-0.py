class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we know the uppper bound will be h
        low, high = 1, max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / k)
            if time <= h:
                res = k
                high = k-1
            else:
                low = k + 1
        return res

        


