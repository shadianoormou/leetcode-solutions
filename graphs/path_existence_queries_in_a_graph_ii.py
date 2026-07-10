class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        order = sorted(range(n), key=lambda i: nums[i])

        values = [nums[i] for i in order]

        position = [0] * n
        for i, node in enumerate(order):
            position[node] = i

        farthest = [0] * n
        right = 0

        for left in range(n):
            if right < left:
                right = left

            while (
                right + 1 < n
                and values[right + 1] - values[left] <= maxDiff
            ):
                right += 1

            farthest[left] = right

        log = max(1, n.bit_length())

        jump = [farthest]

        for _ in range(1, log):
            previous = jump[-1]
            current = [0] * n

            for i in range(n):
                current[i] = previous[previous[i]]

            jump.append(current)

        answer = []

        for u, v in queries:
            if u == v:
                answer.append(0)
                continue

            left = position[u]
            right = position[v]

            if left > right:
                left, right = right, left

            current = left
            distance = 0

            for k in range(log - 1, -1, -1):
                next_node = jump[k][current]

                if current < next_node < right:
                    current = next_node
                    distance += 1 << k

            if jump[0][current] >= right:
                answer.append(distance + 1)
            else:
                answer.append(-1)

        return answer
