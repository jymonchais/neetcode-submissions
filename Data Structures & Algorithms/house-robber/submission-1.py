class Solution:
    def rob(self, nums: List[int]) -> int:
        #somehow keep track of the previous house
        #while also our total sum of robbed houses 
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        h1 = 0
        h2 = 0

        for money in nums:
            current = max(h1, h2 + money)

            h2 = h1

            h1 = current

        return h1