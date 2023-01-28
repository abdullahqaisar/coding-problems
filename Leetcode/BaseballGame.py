class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D': 
                stack.append(int(stack[-1]*2))
            elif op == '+':
                stack.append(int(stack[-1]+stack[-2]))
            else:
                stack.append(int(op))
        for i in stack:
            sum += i
        return sum