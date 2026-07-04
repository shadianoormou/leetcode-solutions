from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            needed = current_sum - k

            if needed in prefix_count:
                count += prefix_count[needed]

            prefix_count[current_sum] = (
                prefix_count.get(current_sum, 0) + 1
            )

        return count
