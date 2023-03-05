class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0 for i in nums]
        for i in range(len(nums)):
            for j in nums:
                if j < nums[i]:
                    result[i] += 1
        
        return result