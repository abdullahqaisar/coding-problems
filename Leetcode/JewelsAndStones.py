class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set()
        count = 0
        for j in jewels:
            jewelSet.add(j)
        for s in stones:
            if s in jewelSet:
                count += 1
        return count