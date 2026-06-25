class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in count:
                return [count[complement], i]
            
            count[n] = i

        

                  

        