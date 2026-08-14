from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        answer = 0

        for right, ch in enumerate(s):
            freq[ch] += 1

            while freq[ch] > 2:
                freq[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
