from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        if n < m:
            return []

        # suffix[j] = rightmost possible index in word1
        # that can start an exact match of word2[j:]
        suffix = [-1] * m
        i = n - 1

        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suffix[j] = i
            i -= 1

        answer = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                answer.append(i)
                j += 1

            # Use our one allowed mismatch
            elif not changed:
                if j == m - 1 or (
                    suffix[j + 1] != -1 and i < suffix[j + 1]
                ):
                    answer.append(i)
                    j += 1
                    changed = True

        return answer if j == m else []
