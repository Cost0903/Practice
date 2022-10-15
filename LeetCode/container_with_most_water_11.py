class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = left = right = 0
        for i in range(len(height) - 1):
            left = height[i]
            for j in range(i+i, len(height)):
                right = height[j]
                result = max(result, min(left, rigth) * (j - i))
        return result
