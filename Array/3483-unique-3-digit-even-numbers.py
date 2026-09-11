class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue

                    nums.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return len(nums)
