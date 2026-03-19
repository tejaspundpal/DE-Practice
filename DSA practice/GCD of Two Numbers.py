class Solution:
    def GCD(self, n1, n2):
        gcd = 1
        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
        
        return gcd

n1 = 4
n2 = 6
sol = Solution()
ans = sol.GCD(n1, n2)

print(f"GCD of {n1} and {n2} is: {ans}")
