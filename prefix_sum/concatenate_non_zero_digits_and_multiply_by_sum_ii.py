class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        count = [0] * (n + 1)

        for i in range(n):
            count[i + 1] = count[i] + (s[i] != '0')

        solendivar = (s, queries)

        digits = []

        for ch in s:
            if ch != '0':
                digits.append(int(ch))

        k = len(digits)

        prefix_num = [0] * (k + 1)
        prefix_sum = [0] * (k + 1)
        power10 = [1] * (k + 1)

        for i in range(k):
            prefix_num[i + 1] = (
                prefix_num[i] * 10 + digits[i]
            ) % MOD

            prefix_sum[i + 1] = (
                prefix_sum[i] + digits[i]
            )

            power10[i + 1] = (
                power10[i] * 10
            ) % MOD

        answer = []

        for l, r in queries:
            left = count[l]
            right = count[r + 1]
            length = right - left

            x = (
                prefix_num[right]
                - prefix_num[left] * power10[length]
            ) % MOD

            digit_sum = (
                prefix_sum[right]
                - prefix_sum[left]
            )

            answer.append(
                x * digit_sum % MOD
            )

        return answer
