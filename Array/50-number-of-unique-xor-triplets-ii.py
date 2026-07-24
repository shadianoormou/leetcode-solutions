from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        values = set(nums)

        pair_xors = set()
        for a in values:
            for b in values:
                pair_xors.add(a ^ b)

        triplet_xors = set()
        for pair_xor in pair_xors:
            for value in values:
                triplet_xors.add(pair_xor ^ value)

        return len(triplet_xors)
