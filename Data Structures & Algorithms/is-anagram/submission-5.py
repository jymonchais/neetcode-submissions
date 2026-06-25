class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cS = {}
        cT = {}

        for char in s:
            if char in cS:
                cS[char] += 1
            else:
                cS[char] = 1
        
        for char in t:
            if char in cT:
                cT[char] += 1
            else:
                cT[char] = 1
    
        return cS == cT

        
            