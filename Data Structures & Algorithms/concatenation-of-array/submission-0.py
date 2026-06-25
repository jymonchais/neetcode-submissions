class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        oldSz = len(nums)
        newSz = oldSz * 2

        ans = [0] * newSz
        
        #pointer that will take over at the midpoint
        rightPtr = (newSz // 2)

        for leftPtr in range(newSz):
            if leftPtr < rightPtr:
                ans[leftPtr] = nums[leftPtr]
            else:
                ans[leftPtr] = nums[leftPtr - oldSz]


        return ans