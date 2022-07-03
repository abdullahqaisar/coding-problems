class Solution:
    def romanToInt(self, s: str) -> int:
        dict_rollNumber = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
               }
        sum = 0
        prevSum = 0
        for i in s:
            sum = sum + dict_rollNumber[i]
            if dict_rollNumber[i] > prevSum:
                sum = sum - prevSum - prevSum
            prevSum = dict_rollNumber[i]
                
        return sum
    
