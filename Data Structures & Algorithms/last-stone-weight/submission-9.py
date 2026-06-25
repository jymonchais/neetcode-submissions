class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0]

        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            print(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first == second:
                print("hit equal case")
                continue
            if first < second:
                print("hit new val case")
                val = abs(second - first)
                heapq.heappush(stones, -val)


        return abs(stones[0]) if len(stones) > 0 else 0