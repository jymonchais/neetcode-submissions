class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash map for each string 
        key = 0
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False

        #key value will be num of occur
        for i in range (len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        for j in sMap:
            if sMap[j] != tMap.get(j, 0):
                return False
                
        return True