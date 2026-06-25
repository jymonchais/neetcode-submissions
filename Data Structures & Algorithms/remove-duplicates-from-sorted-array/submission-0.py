class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1

        for i in range(1, size):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left += 1
    

        return left