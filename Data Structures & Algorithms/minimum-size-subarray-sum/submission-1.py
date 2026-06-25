class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        
        #left ptr
        L = 0

        #sum of the values in the window
        total = 0

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1
        
        return length if length != float('inf') else 0

