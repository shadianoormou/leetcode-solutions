from typing import List


class SparseTable:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.st = [nums[:]]

        k = 1
        while (1 << k) <= n:
            prev = self.st[-1]
            length = n - (1 << k) + 1
            curr = [0] * length
            half = 1 << (k - 1)

            for i in range(length):
                curr[i] = max(prev[i], prev[i + half])

            self.st.append(curr)
            k += 1

    def query(self, left: int, right: int) -> int:
        length = right - left + 1
        k = length.bit_length() - 1
        return max(
            self.st[k][left],
            self.st[k][right - (1 << k) + 1]
        )


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        s: str,
        queries: List[List[int]]
    ) -> List[int]:

        total_ones = s.count("1")

        # zero_start[i], zero_len[i]:
        # information about the i-th zero block.
        zero_start = []
        zero_len = []

        # zero_id[pos] = index of the latest zero block at/before pos.
        zero_id = [-1] * len(s)

        for i, ch in enumerate(s):
            if ch == "0":
                if i > 0 and s[i - 1] == "0":
                    zero_len[-1] += 1
                else:
                    zero_start.append(i)
                    zero_len.append(1)

            zero_id[i] = len(zero_len) - 1

        m = len(zero_len)

        if m == 0:
            return [total_ones] * len(queries)

        # merge[i] represents:
        # zero_len[i] + zero_len[i + 1]
        #
        # The 1-block between these two zero-blocks can be removed,
        # after which both zero-blocks merge and become 1s.
        merge = [
            zero_len[i] + zero_len[i + 1]
            for i in range(m - 1)
        ]

        sparse = SparseTable(merge) if merge else None

        answer = []

        for left, right in queries:
            best_gain = 0

            left_zero = zero_id[left]
            right_zero = zero_id[right]

            # Number of zeros available from left boundary's zero-block.
            if s[left] == "0":
                left_part = (
                    zero_start[left_zero]
                    + zero_len[left_zero]
                    - left
                )
            else:
                left_part = 0

            # Number of zeros available from right boundary's zero-block.
            if s[right] == "0":
                right_part = right - zero_start[right_zero] + 1
            else:
                right_part = 0

            # Fully contained zero-block range.
            first_full = left_zero + 1

            if s[right] == "1":
                last_full = right_zero
            else:
                last_full = right_zero - 1

            # Case 1: choose two fully-contained adjacent zero-blocks.
            # Their separating 1-block is removed.
            first_pair = first_full
            last_pair = last_full - 1

            if first_pair <= last_pair:
                best_gain = max(
                    best_gain,
                    sparse.query(first_pair, last_pair)
                )

            # Case 2: left boundary cuts through a zero-block.
            if s[left] == "0" and first_full <= last_full:
                best_gain = max(
                    best_gain,
                    left_part + zero_len[first_full]
                )

            # Case 3: right boundary cuts through a zero-block.
            if (
                s[right] == "0"
                and right_zero - 1 >= first_full
            ):
                best_gain = max(
                    best_gain,
                    zero_len[right_zero - 1] + right_part
                )

            # Case 4: substring begins and ends inside two consecutive
            # zero-blocks.
            if (
                s[left] == "0"
                and s[right] == "0"
                and left_zero + 1 == right_zero
            ):
                best_gain = max(
                    best_gain,
                    left_part + right_part
                )

            answer.append(total_ones + best_gain)

        return answer
