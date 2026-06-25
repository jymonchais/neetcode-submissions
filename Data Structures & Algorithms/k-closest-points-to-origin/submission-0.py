class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x, y in points:
            val = (x ** 2 + y ** 2)
            dist.append([val, x, y])


        heapq.heapify(dist)
        output = []

        while k > 0:
            val, x, y = heapq.heappop(dist)
            output.append([x, y])
            k -= 1

        return output