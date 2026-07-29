from collections import Counter
from math import factorial


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        frequency = Counter(s)

        middle = ""
        half_count = {}

        for character, count in frequency.items():
            half_count[character] = count // 2

            if count % 2 == 1:
                middle = character

        remaining = sum(half_count.values())

        # Number of distinct permutations of the left half.
        total_permutations = factorial(remaining)

        for count in half_count.values():
            total_permutations //= factorial(count)

        if k > total_permutations:
            return ""

        left_half = []
        characters = sorted(half_count)

        while remaining > 0:
            for character in characters:
                count = half_count[character]

                if count == 0:
                    continue

                # Permutations beginning with this character.
                permutations = (
                    total_permutations * count // remaining
                )

                if k > permutations:
                    k -= permutations
                else:
                    left_half.append(character)
                    half_count[character] -= 1
                    remaining -= 1
                    total_permutations = permutations
                    break

        left = "".join(left_half)

        return left + middle + left[::-1]
