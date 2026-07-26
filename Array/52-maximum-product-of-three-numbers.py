from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest1 = largest2 = largest3 = float("-inf")
        smallest1 = smallest2 = float("inf")

        for num in nums:
            if num >= largest1:
                largest3 = largest2
                largest2 = largest1
                largest1 = num
            elif num >= largest2:
                largest3 = largest2
                largest2 = num
            elif num > largest3:
                largest3 = num

            if num <= smallest1:
                smallest2 = smallest1
                smallest1 = num
            elif num < smallest2:
                smallest2 = num

        return max(
            largest1 * largest2 * largest3,
            largest1 * smallest1 * smallest2
        )
