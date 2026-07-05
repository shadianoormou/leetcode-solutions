from typing import List
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        # Build undirected graph
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        answer = float("inf")

        # BFS from city 1
        while queue:
            city = queue.popleft()

            for neighbor, distance in graph[city]:
                answer = min(answer, distance)

                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return answer
