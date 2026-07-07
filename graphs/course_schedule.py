from typing import List
from collections import deque

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:
            current = queue.popleft()
            completed += 1

            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
