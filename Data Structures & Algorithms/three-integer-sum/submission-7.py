

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums)):
            # If the fixed number is > 0, no 3 numbers can sum to 0 (since array is sorted)
            if nums[i] > 0:
                break

            # Skip duplicate values for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two Pointers search for the remaining two numbers
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate values for the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res