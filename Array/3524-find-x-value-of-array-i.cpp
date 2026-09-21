class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> ans(k, 0);
        vector<long long> dp(k, 0);

        for (int num : nums) {
            vector<long long> next(k, 0);
            int v = num % k;

            next[v]++;

            for (int r = 0; r < k; r++) {
                int nr = (long long)r * v % k;
                next[nr] += dp[r];
            }

            for (int r = 0; r < k; r++) {
                ans[r] += next[r];
            }

            dp = move(next);
        }

        return ans;
    }
};
