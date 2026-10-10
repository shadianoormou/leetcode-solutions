
class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2,
                               int k1, int k2) {
        int n = nums1.size();
        long long k = (long long)k1 + k2;

        vector<int> diff(n);
        int left = 0, right = 0;

        for (int i = 0; i < n; i++) {
            diff[i] = abs(nums1[i] - nums2[i]);
            right = max(right, diff[i]);
        }

        while (left < right) {
            int mid = left + (right - left) / 2;
            long long operations = 0;

            for (int d : diff) {
                if (d > mid) {
                    operations += d - mid;
                }
            }

            if (operations <= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        long long ans = 0;
        long long remaining = k;
        long long count = 0;

        for (int d : diff) {
            int val = min(d, left);
            remaining -= d - val;
            ans += 1LL * val * val;

            if (val == left && left > 0) {
                count++;
            }
        }

        if (left > 0) {
            long long changes = min(remaining, count);
            ans -= changes * (2LL * left - 1);
        }

        return ans;
    }
};
