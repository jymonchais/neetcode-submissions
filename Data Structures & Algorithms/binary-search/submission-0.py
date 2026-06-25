class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums) - 1


        while(lt <= rt):
            mid = (lt + rt) // 2

            if target > nums[mid]:
                lt = mid + 1
            elif target < nums[mid]:
                rt = mid - 1
            else:
                return mid

        return -1