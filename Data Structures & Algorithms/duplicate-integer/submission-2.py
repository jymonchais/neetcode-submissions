class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}

        for val in nums:
            dupMap[val] = dupMap.get(val, 1) - 1

        return any(i < 0 for i in dupMap.values())

        
   