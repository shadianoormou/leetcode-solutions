from functools import lru_cache


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Prime factors contributed by each digit:
        # (power of 2, power of 3, power of 5, power of 7)
        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        required = [0, 0, 0, 0]

        for i, prime in enumerate((2, 3, 5, 7)):
            while t % prime == 0:
                required[i] += 1
                t //= prime

        # Digits 1..9 cannot provide any other prime factor.
        if t != 1:
            return "-1"

        @lru_cache(None)
        def min_23(a: int, b: int) -> int:
            if a == 0 and b == 0:
                return 0

            answer = float("inf")

            for x, y in (
                (1, 0),  # 2
                (0, 1),  # 3
                (2, 0),  # 4
                (1, 1),  # 6
                (3, 0),  # 8
                (0, 2),  # 9
            ):
                if a > 0 or b > 0:
                    na = max(0, a - x)
                    nb = max(0, b - y)

                    if na != a or nb != b:
                        answer = min(
                            answer,
                            1 + min_23(na, nb)
                        )

            return answer

        def minimum_digits(req):
            a, b, c, d = req
            return min_23(a, b) + c + d

        def use_digit(req, digit):
            f = factors[digit]

            return [
                max(0, req[i] - f[i])
                for i in range(4)
            ]

        def build_suffix(length, req):
            result = []

            for pos in range(length):
                remaining = length - pos - 1

                for digit in range(1, 10):
                    new_req = use_digit(req, digit)

                    if minimum_digits(new_req) <= remaining:
                        result.append(str(digit))
                        req = new_req
                        break

            return "".join(result)

        n = len(num)
        req = required[:]
        best = None
        valid_prefix = True

        # Find the rightmost position that can be increased.
        for i in range(n):
            current = int(num[i])

            start = max(1, current + 1)

            for digit in range(start, 10):
                new_req = use_digit(req, digit)

                if minimum_digits(new_req) <= n - i - 1:
                    best = (i, digit, new_req)
                    break

            # We cannot keep a zero while remaining equal to num.
            if current == 0:
                valid_prefix = False
                break

            req = use_digit(req, current)

        # num itself already satisfies all conditions.
        if valid_prefix and minimum_digits(req) == 0:
            return num

        # Construct the smallest same-length number > num.
        if best is not None:
            i, digit, req = best

            suffix = build_suffix(
                n - i - 1,
                req
            )

            return num[:i] + str(digit) + suffix

        # Need a longer number.
        length = max(
            n + 1,
            minimum_digits(required)
        )

        return build_suffix(length, required[:])
