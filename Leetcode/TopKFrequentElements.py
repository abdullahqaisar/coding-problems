class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        bucket = [[] for i in range(len(nums)+1)]
        res = []

        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for num, freq in dict.items():
            bucket[freq].append(num)
        for e in range(len(bucket)-1,0,-1):
            for i in bucket[e]:
                res.append(i)
                if len(res) == k:
                    return res
                
            
        
