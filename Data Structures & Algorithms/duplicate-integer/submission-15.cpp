#include <vector>
#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;

        for (int num : nums) {
            // If the element is already in the set, a duplicate is found
            if (seen.count(num) > 0) {
                return true;
            }
            // Otherwise, insert the element into the set
            seen.insert(num);
        }

        return false;
    }
};