class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        for i, ch in enumerate(s):
            if ch == "1":
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]
            cur = s[left:right + 1]

            if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                ans = cur

        return ans
