class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int i, j, flag = 0;
        int n = nums.size();
        for (i = 0; i < n; i++) {
            for (j = i + 1; j < n; j++) {
                if (nums[i] == nums[j]) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 1) break;
        }

        if (flag == 1)
            return true;
        else
            return false;
    }
};