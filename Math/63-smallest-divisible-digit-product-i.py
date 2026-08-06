class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(number: int) -> int:
            product = 1

            while number > 0:
                product *= number % 10
                number //= 10

            return product

        while digit_product(n) % t != 0:
            n += 1

        return n
