from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            costs.append(cost)

        if not costs:
            return -1

        # Topological sort because the graph is DAG
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for nei, cost in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        def can(score):
            INF = 10**30
            dist = [INF] * n
            dist[0] = 0

            for node in topo:
                if dist[node] > k:
                    continue

                if node != 0 and node != n - 1 and not online[node]:
                    continue

                for nei, cost in graph[node]:
                    if cost < score:
                        continue

                    if nei != n - 1 and not online[nei]:
                        continue

                    new_cost = dist[node] + cost

                    if new_cost < dist[nei] and new_cost <= k:
                        dist[nei] = new_cost

            return dist[n - 1] <= k

        unique_costs = sorted(set(costs))

        left = 0
        right = len(unique_costs) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            score = unique_costs[mid]

            if can(score):
                answer = score
                left = mid + 1
            else:
                right = mid - 1

        return answer
