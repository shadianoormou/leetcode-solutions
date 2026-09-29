class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int len = m + n - 1;

        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(' || len % 2 == 1) {
            return false;
        }

        vector<vector<vector<char>>> dp(
            m, vector<vector<char>>(n, vector<char>(len + 1, 0))
        );

        dp[0][0][1] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;

                int add = grid[i][j] == '(' ? 1 : -1;

                for (int bal = 0; bal <= len; bal++) {
                    bool reachable = false;

                    if (i > 0 && dp[i - 1][j][bal]) {
                        reachable = true;
                    }

                    if (j > 0 && dp[i][j - 1][bal]) {
                        reachable = true;
                    }

                    if (!reachable) continue;

                    int nextBal = bal + add;

                    if (nextBal >= 0 && nextBal <= len) {
                        dp[i][j][nextBal] = 1;
                    }
                }
            }
        }

        return dp[m - 1][n - 1][0];
    }
};
