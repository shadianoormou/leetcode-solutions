class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        total = 0
        last = {}

        for ch in s:
            new_total = (2 * total + 1 - last.get(ch, 0)) % mod
            last[ch] = (total + 1) % mod
            total = new_total

        return total
