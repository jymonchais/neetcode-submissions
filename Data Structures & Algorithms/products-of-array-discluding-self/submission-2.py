class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [1] * size

        prefix = 1
        for i in range(1, size):
            prefix *= nums[i - 1]
            output[i] = prefix

        print("orefix: ", output)
        postfix = 1
        for i in range(size - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
    

        return output
        
