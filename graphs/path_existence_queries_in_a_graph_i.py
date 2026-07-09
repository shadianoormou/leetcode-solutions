from typing import List


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        component = [0] * n
        group = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group += 1

            component[i] = group

        answer = []

        for u, v in queries:
            answer.append(component[u] == component[v])

        return answer


if __name__ == "__main__":
    solution = Solution()

    n = 4
    nums = [2, 5, 6, 8]
    maxDiff = 2
    queries = [[0, 1], [0, 2], [1, 3], [2, 3]]

    result = solution.pathExistenceQueries(
        n,
        nums,
        maxDiff,
        queries
    )

    print(result)
