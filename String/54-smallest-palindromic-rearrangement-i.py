from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        frequency = Counter(s)

        left_half = []
        middle = ""

        for character in sorted(frequency):
            left_half.append(character * (frequency[character] // 2))

            if frequency[character] % 2 == 1:
                middle = character

        left = "".join(left_half)

        return left + middle + left[::-1]
