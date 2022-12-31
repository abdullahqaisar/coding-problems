class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = {}
        dictT = {}
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        for j in dictS:
            if dictS[j] != dictT.get(j, 0):
                return False

        return True
