class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            arr = []
            arr.append(1)
            if i > 0:
                for j in range(1, i):
                    num = result[i-1][j-1] + result[i-1][j]
                    arr.append(num)
                arr.append(1)
            result.append(arr)
        return result
