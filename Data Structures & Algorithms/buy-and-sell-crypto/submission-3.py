class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0, 1

        # if L < R, check that max price
        # next move it right

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right

            right += 1

        return maxP