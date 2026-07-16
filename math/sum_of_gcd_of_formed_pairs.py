from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(x, mx))

        prefix.sort()

        ans = 0
        n = len(prefix)
        for i in range(n // 2):
            ans += gcd(prefix[i], prefix[n - 1 - i])

        return ans
