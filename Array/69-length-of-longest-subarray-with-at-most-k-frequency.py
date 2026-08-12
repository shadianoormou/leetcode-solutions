from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        answer = 0

        for right, num in enumerate(nums):
            freq[num] += 1

            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
