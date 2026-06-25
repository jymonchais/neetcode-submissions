class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if( (i != j) and nums[i] + nums[j] == target):
                    values.append(i)
                    values.append(j)
                    return values
        

                  

        