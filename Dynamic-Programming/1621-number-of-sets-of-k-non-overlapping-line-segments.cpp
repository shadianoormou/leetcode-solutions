class Solution {
public:
    int numberOfSets(int n, int k) {
        const int MOD = 1000000007;

        vector<vector<long long>> dp(n, vector<long long>(k + 1));
        vector<vector<long long>> prefix(n, vector<long long>(k + 1));

        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
            prefix[i][0] = i + 1;
        }

        for (int j = 1; j <= k; j++) {
            for (int i = 1; i < n; i++) {
                dp[i][j] = dp[i - 1][j] + prefix[i - 1][j - 1];
                dp[i][j] %= MOD;

                prefix[i][j] = prefix[i - 1][j] + dp[i][j];
                prefix[i][j] %= MOD;
            }
        }

        return dp[n - 1][k];
    }
};
