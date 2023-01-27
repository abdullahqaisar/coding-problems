class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'{': '}', '(': ')', '[': ']'}
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p in dict and dict[p] != i:
                    return False
        if len(stack) != 0:
            return False
        return True
