class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # This tracks numbers we've already looked at
        
        for num in nums:
            if num in seen:
                return True  # Found a duplicate!
            seen.add(num)    # Record this number
            
        return False  # Looked at everything, no duplicates
        