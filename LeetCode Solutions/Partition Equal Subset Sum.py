"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

"""

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int n : nums) sum += n;
        if (sum % 2) return false;
        int target = sum >> 1;
        vector<bool> dp(target+1, false);
        dp[0] = true;
        for (int n : nums) {
            for (int i = target; i >= n; --i) {
                if (dp[i-n]) dp[i] = true;
            }
        }
        return dp[target];
    }
};