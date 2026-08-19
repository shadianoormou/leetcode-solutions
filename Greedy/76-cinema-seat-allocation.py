from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(
        self,
        n: int,
        reservedSeats: List[List[int]]
    ) -> int:

        rows = defaultdict(set)

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row].add(seat)

        answer = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(seat not in seats for seat in (2, 3, 4, 5))
            middle = all(seat not in seats for seat in (4, 5, 6, 7))
            right = all(seat not in seats for seat in (6, 7, 8, 9))

            if left and right:
                answer += 2
            elif left or middle or right:
                answer += 1

        return answer
