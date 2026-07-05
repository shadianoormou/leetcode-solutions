"""
LeetCode 1301 - Number of Paths with Max Score

Difficulty: Hard
Topics: Dynamic Programming, Matrix, Path Counting

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # Maximum score achievable at each cell
        max_score = [[-1] * n for _ in range(n)]

        # Number of ways to achieve that maximum score
        ways = [[0] * n for _ in range(n)]

        # Start from the bottom-right cell 'S'
        max_score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        # Process the board from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Skip the starting cell
                if i == n - 1 and j == n - 1:
                    continue

                # Skip obstacles
                if board[i][j] == "X":
                    continue

                best = -1
                count = 0

                neighbors = [
                    (i + 1, j),
                    (i, j + 1),
                    (i + 1, j + 1),
                ]

                for ni, nj in neighbors:
                    if 0 <= ni < n and 0 <= nj < n:
                        if ways[ni][nj] > 0:

                            if max_score[ni][nj] > best:
                                best = max_score[ni][nj]
                                count = ways[ni][nj]

                            elif max_score[ni][nj] == best:
                                count = (
                                    count + ways[ni][nj]
                                ) % MOD

                # No valid path reaches this cell
                if best == -1:
                    continue

                value = 0

                # Add numeric cell value to the score
                if board[i][j].isdigit():
                    value = int(board[i][j])

                max_score[i][j] = best + value
                ways[i][j] = count

        # No path from S to E
        if ways[0][0] == 0:
            return [0, 0]

        return [
            max_score[0][0],
            ways[0][0] % MOD,
        ]
