class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        # Need to compare left and right pointer
        # need to skip over spaces as well
        # we cant strip the string, that operation is O(n)

        while L <= R:
            while L < R and not s[L].isalnum():
                L += 1

            while R > L and not s[R].isalnum():
                R -= 1

            if s[L].lower() != s[R].lower():
                print("Debug L:", s[L], "R:", s[R])
                return False
            L += 1
            R -= 1
                
        return True