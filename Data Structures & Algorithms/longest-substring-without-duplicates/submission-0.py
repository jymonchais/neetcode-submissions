class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxLen = 0
        l, r = 0, 0

        while r < len(s):
            # curr
            currStr = s[l:r]
            if s[r] not in currStr:
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                l += 1

        return maxLen