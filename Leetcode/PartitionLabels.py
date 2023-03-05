class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size, end =0, 0
        dict = {}
        result = []
        for i in range(len(s)):
            dict[s[i]] = i
        
        for i in range(len(s)):
            size = size + 1
            if end < dict[s[i]]:
                end = dict[s[i]]
            if end == i:
                result.append(size)
                size = 0
        return result