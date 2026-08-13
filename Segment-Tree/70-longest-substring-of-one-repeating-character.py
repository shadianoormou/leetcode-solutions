from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        chars = list(s)

        size = 4 * n

        left_char = [""] * size
        right_char = [""] * size
        prefix = [0] * size
        suffix = [0] * size
        longest = [0] * size
        length = [0] * size

        def merge(node: int) -> None:
            left = node * 2
            right = left + 1

            length[node] = length[left] + length[right]
            left_char[node] = left_char[left]
            right_char[node] = right_char[right]

            prefix[node] = prefix[left]
            suffix[node] = suffix[right]
            longest[node] = max(longest[left], longest[right])

            if right_char[left] == left_char[right]:
                combined = suffix[left] + prefix[right]
                longest[node] = max(longest[node], combined)

                if prefix[left] == length[left]:
                    prefix[node] = length[left] + prefix[right]

                if suffix[right] == length[right]:
                    suffix[node] = length[right] + suffix[left]

        def build(node: int, l: int, r: int) -> None:
            if l == r:
                left_char[node] = chars[l]
                right_char[node] = chars[l]
                prefix[node] = 1
                suffix[node] = 1
                longest[node] = 1
                length[node] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def update(
            node: int,
            l: int,
            r: int,
            index: int,
            ch: str
        ) -> None:
            if l == r:
                left_char[node] = ch
                right_char[node] = ch
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, ch)
            else:
                update(node * 2 + 1, mid + 1, r, index, ch)

            merge(node)

        build(1, 0, n - 1)

        answer = []

        for index, ch in zip(queryIndices, queryCharacters):
            chars[index] = ch
            update(1, 0, n - 1, index, ch)
            answer.append(longest[1])

        return answer
