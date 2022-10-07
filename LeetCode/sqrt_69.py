class Solution:
    def mySqrt(self, x: int) -> int:
#         # 4 = 2 * 2
#         # 100 = 10 * 10
#         # x = 100
        if x == 0: return 0
        elif x == 1: return 1
        # elif x == 2: return 1
        for i in range(x+1):
            if x < i * i: return i - 1

a = Solution()
print(a.mySqrt(2))

