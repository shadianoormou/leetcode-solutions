from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = 0
        litter_id = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start_r, start_c = i, j
                elif classroom[i][j] == "L":
                    litter_id[(i, j)] = len(litter_id)

        target = (1 << len(litter_id)) - 1

        if target == 0:
            return 0

        visited = [[[0] * (energy + 1) for _ in range(n)] for _ in range(m)]
        queue = deque([(start_r, start_c, energy, 0, 0)])
        visited[start_r][start_c][energy] |= 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, e, mask, moves = queue.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == "X":
                    continue

                ne = e - 1
                new_mask = mask

                if classroom[nr][nc] == "R":
                    ne = energy

                if classroom[nr][nc] == "L":
                    new_mask |= 1 << litter_id[(nr, nc)]

                bit = 1 << new_mask

                if visited[nr][nc][ne] & bit:
                    continue

                visited[nr][nc][ne] |= bit
                queue.append((nr, nc, ne, new_mask, moves + 1))

        return -1
