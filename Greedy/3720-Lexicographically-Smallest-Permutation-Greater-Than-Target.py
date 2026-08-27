from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        best_index = -1
        best_char = ""

        for i, ch in enumerate(target):
            for code in range(ord(ch) + 1, ord("z") + 1):
                c = chr(code)
                if cnt[c] > 0:
                    best_index = i
                    best_char = c
                    break

            if cnt[ch] == 0:
                break

            cnt[ch] -= 1

        if best_index == -1:
            return ""

        cnt = Counter(s)
        ans = []

        for i in range(best_index):
            ans.append(target[i])
            cnt[target[i]] -= 1

        ans.append(best_char)
        cnt[best_char] -= 1

        for code in range(ord("a"), ord("z") + 1):
            c = chr(code)
            ans.append(c * cnt[c])

        return "".join(ans)
