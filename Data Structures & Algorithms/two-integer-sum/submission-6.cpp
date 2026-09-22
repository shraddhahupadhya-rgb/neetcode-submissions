class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {

        std::unordered_map<int, int> seen;

        

        for (int i = 0; i < nums.size(); i++) {

            int complement = target - nums[i];

            

            // Check if complement exists in hashmap

            if (seen.find(complement) != seen.end()) {

                return {seen[complement], i};

            }

            

            // Store current value and index

            seen[nums[i]] = i;

        }

        

        return {}; 
    }
};
