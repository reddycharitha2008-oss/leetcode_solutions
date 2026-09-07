class Solution:
    def sortedSquares(self, nums):
        ans = []
        for num in nums:
            ans.append(num * num)
        ans.sort()
        return ans