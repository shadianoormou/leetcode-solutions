class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        active = s.count('1')

        zero_runs = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '1':
                i += 1
                continue

            j = i
            while j < n and s[j] == '0':
                j += 1

            zero_runs.append(j - i)
            i = j

        best_gain = 0

        # Two consecutive zero-runs have a block of 1s between them.
        for i in range(1, len(zero_runs)):
            best_gain = max(
                best_gain,
                zero_runs[i - 1] + zero_runs[i]
            )

        return active + best_gain
