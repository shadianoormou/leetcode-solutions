class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        struct Node {
            long long score;
            vector<int> ids;
        };

        vector<array<int, 4>> a;
        a.reserve(n);

        for (int i = 0; i < n; ++i) {
            a.push_back({intervals[i][0], intervals[i][1], intervals[i][2], i});
        }

        sort(a.begin(), a.end(), [](const auto& x, const auto& y) {
            if (x[1] != y[1]) return x[1] < y[1];
            return x[3] < y[3];
        });

        vector<int> ends(n);
        for (int i = 0; i < n; ++i) {
            ends[i] = a[i][1];
        }

        vector<vector<Node>> dp(n + 1, vector<Node>(5, {LLONG_MIN / 4, {}}));
        dp[0][0] = {0, {}};

        auto better = [](const Node& x, const Node& y) {
            if (x.score != y.score) return x.score > y.score;
            return x.ids < y.ids;
        };

        for (int i = 1; i <= n; ++i) {
            for (int k = 0; k <= 4; ++k) {
                dp[i][k] = dp[i - 1][k];
            }

            int l = a[i - 1][0];
            int w = a[i - 1][2];
            int idx = a[i - 1][3];

            int p = lower_bound(ends.begin(), ends.begin() + (i - 1), l) - ends.begin();

            for (int k = 1; k <= 4; ++k) {
                if (dp[p][k - 1].score <= LLONG_MIN / 8) continue;

                Node cand = dp[p][k - 1];
                cand.score += w;
                cand.ids.push_back(idx);
                sort(cand.ids.begin(), cand.ids.end());

                if (better(cand, dp[i][k])) {
                    dp[i][k] = cand;
                }
            }
        }

        Node ans = {0, {}};

        for (int k = 1; k <= 4; ++k) {
            if (better(dp[n][k], ans)) {
                ans = dp[n][k];
            }
        }

        return ans.ids;
    }
};
