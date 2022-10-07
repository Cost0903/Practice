class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        a, b, c = 0, 1, 2
        while n > 2:
            a, b = b, c
            c = a + b
            n = n - 1
        return c

s = Solution()
print(s.climbStairs(5))
# 1 = 1
# 2 = 1,1 2
# 3 = 1,1,1  1,2  2,1
# 4 = 1,1,1,1  1,1,2  1,2,1  2,1,1  2,2  
# 5 = 1,1,1,1,1  1,1,1,2  1,1,2,1  1,2,1,1  2,1,1,1  1,2,2  2,1,2  2,2,1