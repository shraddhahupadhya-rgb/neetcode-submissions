class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequency of each number using a hash map
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Step 2: Create buckets where index = frequency count
        # Length is len(nums) + 1 because frequency can go from 0 to len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        # Step 3: Iterate backwards from the highest frequency bucket to collect k elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res