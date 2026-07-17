from bisect import bisect_right
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)

        # frequency[x] = how many times x occurs in nums
        frequency = [0] * (max_num + 1)
        for num in nums:
            frequency[num] += 1

        # exact_gcd[g] = number of pairs whose GCD is exactly g
        exact_gcd = [0] * (max_num + 1)

        # Process from larger GCDs to smaller GCDs.
        for gcd_value in range(max_num, 0, -1):
            divisible_count = 0

            # Count numbers divisible by gcd_value.
            for multiple in range(gcd_value, max_num + 1, gcd_value):
                divisible_count += frequency[multiple]

            # Every pair of these numbers has a GCD divisible by gcd_value.
            pair_count = divisible_count * (divisible_count - 1) // 2

            # Remove pairs whose GCD is a larger multiple of gcd_value.
            for multiple in range(2 * gcd_value, max_num + 1, gcd_value):
                pair_count -= exact_gcd[multiple]

            exact_gcd[gcd_value] = pair_count

        # prefix[g] = number of pairs having GCD <= g
        prefix = [0] * (max_num + 1)
        for gcd_value in range(1, max_num + 1):
            prefix[gcd_value] = (
                prefix[gcd_value - 1] + exact_gcd[gcd_value]
            )

        # Query is a 0-based index, so find the first prefix > query.
        return [bisect_right(prefix, query) for query in queries]
