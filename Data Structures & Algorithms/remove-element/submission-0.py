class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writePtr = 0
        
        for readPtr in range(len(nums)):
            if nums[readPtr] != val:
                nums[writePtr] = nums[readPtr]
                writePtr += 1


        return writePtr