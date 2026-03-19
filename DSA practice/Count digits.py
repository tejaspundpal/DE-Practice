class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1

        cnt = 0

        while n > 0:
            cnt += 1
            # print(n)
            n = n // 10
        return cnt

sol = Solution()
result = sol.countDigit(12345)
display(result)