class Solution:
    def merge(self, intervals):
        intervals.sort()

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged


if __name__ == "__main__":
    solution = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    result = solution.merge(intervals)

    print(result)
