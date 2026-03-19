import math

class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1

        count = int(math.log10(n)) + 1
        return count
    
    def isArmstrong(self, n):
        count = self.countDigit(n)
        sum = 0
        copy = n
        while n > 0:
            lastDigit = n % 10
            sum += pow(lastDigit, count)
            n = n // 10
        if sum == copy:
            return True
        return False
        
if __name__ == "__main__":
    n = 153
    sol = Solution()
    ans = sol.isArmstrong(n)
    
    if ans:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
