from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(Counter(word).values(), reverse=True)

        pushes = 0

        for index, frequency in enumerate(frequencies):
            cost = index // 8 + 1
            pushes += frequency * cost

        return pushes
