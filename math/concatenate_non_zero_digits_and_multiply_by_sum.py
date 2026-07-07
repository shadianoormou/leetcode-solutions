class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [digit for digit in str(n) if digit != '0']

        if not digits:
            return 0

        x = int(''.join(digits))
        digit_sum = sum(int(digit) for digit in digits)

        return x * digit_sum
