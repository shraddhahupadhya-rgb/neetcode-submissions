class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # 1. Memory storage: { number: index }
        
        for i, n in enumerate(nums): # 2. Loop through numbers one by one
            diff = target - n        # 3. Calculate the missing piece needed
            
            if diff in prevMap:      # 4. Have we seen this missing piece before?
                return [prevMap[diff], i] # 5. If yes, return both indices!
            
            prevMap[n] = i           # 6. If no, store current number & index