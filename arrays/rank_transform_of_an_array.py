class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {
            value: index + 1
            for index, value in enumerate(sorted(set(arr)))
        }

        return [rank[value] for value in arr]
