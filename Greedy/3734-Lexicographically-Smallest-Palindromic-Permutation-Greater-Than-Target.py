from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2

        freq = Counter(s)
        odds = [ch for ch in freq if freq[ch] % 2 == 1]

        if len(odds) > 1:
            return ""

        mid = odds[0] if n % 2 else ""

        half = [0] * 26
        for ch in freq:
            half[ord(ch) - 97] = freq[ch] // 2

        target_half = target[:m]

        def build(left: str) -> str:
            return left + mid + left[::-1]

        cnt = half[:]
        matched = 0

        while matched < m:
            idx = ord(target_half[matched]) - 97
            if cnt[idx] == 0:
                break
            cnt[idx] -= 1
            matched += 1

        if matched == m:
            candidate = build(target_half)
            if candidate > target:
                return candidate

            if m == 0:
                return ""

            matched -= 1
            cnt[ord(target_half[matched]) - 97] += 1

        for i in range(matched, -1, -1):
            start = ord(target_half[i]) - 97 + 1

            for c in range(start, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    rest = []
                    for j in range(26):
                        rest.append(chr(j + 97) * cnt[j])

                    left = target_half[:i] + chr(c + 97) + "".join(rest)
                    return build(left)

            if i > 0:
                cnt[ord(target_half[i - 1]) - 97] += 1

        return ""
