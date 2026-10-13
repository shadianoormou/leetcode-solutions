
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        
        n = len(squares)
        negative_count = n // 2
        
        ans = 0
        
        for i in range(n):
            if i < negative_count:
                ans -= squares[i]
            else:
                ans += squares[i]
        
        return ans
