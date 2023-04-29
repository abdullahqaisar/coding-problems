class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = nums
        for i in range(1, len(nums)):
            sums[i] = nums[i]+sums[i-1]
        sums= [0]+sums+[0]
        for i in range(1, len(nums)+1):
            ls = sums[i-1]
            rs = sums[len(nums)]-sums[i]
            if ls == rs:
                return i-1
        return -1