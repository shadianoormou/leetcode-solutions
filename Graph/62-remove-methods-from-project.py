from typing import List


class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]

        for caller, called in invocations:
            graph[caller].append(called)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            method = stack.pop()

            for next_method in graph[method]:
                if not suspicious[next_method]:
                    suspicious[next_method] = True
                    stack.append(next_method)

        # কোনো non-suspicious method যদি suspicious method invoke করে,
        # তাহলে suspicious group remove করা সম্ভব নয়।
        for caller, called in invocations:
            if not suspicious[caller] and suspicious[called]:
                return list(range(n))

        return [
            method
            for method in range(n)
            if not suspicious[method]
        ]
