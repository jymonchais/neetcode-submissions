class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        out = [0] * size
        left = 0
        right = 0
        sum = 1

        # we can use two pointers
        # each will traverse the array, until hitting the ends

        #sum from the left
        # sum from the right

        
        for i in range(size):
            sum = 1
            for j in range(size):
                if i != j:
                    sum *= nums[j]
               
            out[i] = sum

        return out

        """
        for index in range(size):
            sum = 0
            left = index - 1 if index > 0 else False
            right = index + 1 if index < size else False

            if left:
                sum += nums[left]
                while left > 0:
                    left -= 1
                    sum *= nums[left]
                    print("sum ", sum)
            else:
                sum += nums[right]
            
            if right == size - 1:
                sum *= nums[right]
            else:
                while right < size - 1:
                    right += 1
                    sum *= nums[right]

            out[index] = sum
        """

        
