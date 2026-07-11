from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        complete_components = 0

        for node in range(n):
            if visited[node]:
                continue

            stack = [node]
            visited[node] = True
            vertex_count = 0
            degree_sum = 0

            while stack:
                current = stack.pop()
                vertex_count += 1
                degree_sum += len(graph[current])

                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            if degree_sum == vertex_count * (vertex_count - 1):
                complete_components += 1

        return complete_components
