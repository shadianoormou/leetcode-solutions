class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(x):
            count = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                lcm_value = 1

                for i in range(n):
                    if mask & (1 << i):
                        lcm_value = lcm(lcm_value, coins[i])

                        if lcm_value > x:
                            break

                bits = mask.bit_count()

                if bits % 2 == 1:
                    count += x // lcm_value
                else:
                    count -= x // lcm_value

            return count >= k

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
