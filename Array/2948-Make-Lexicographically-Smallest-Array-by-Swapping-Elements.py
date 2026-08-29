from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted((num, i) for i, num in enumerate(nums))
        ans = nums[:]

        i = 0

        while i < n:
            j = i + 1

            while j < n and pairs[j][0] - pairs[j - 1][0] <= limit:
                j += 1

            values = [pairs[x][0] for x in range(i, j)]
            indices = sorted(pairs[x][1] for x in range(i, j))

            for idx, val in zip(indices, values):
                ans[idx] = val

            i = j

        return ans
