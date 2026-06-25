class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oldMap = {} #val : index


        for i, j in enumerate(nums):
            diff = target - j
            if diff in oldMap:
                return [oldMap[diff], i]
            oldMap[j] = i 
   


            