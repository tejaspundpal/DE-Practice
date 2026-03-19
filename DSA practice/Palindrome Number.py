class Solution:
    def isPalindrome(self, n):
        revNum = 0
        orginal = n
        while n > 0:
            lastDigit = n % 10
            revNum = (revNum * 10) + lastDigit
            n = n // 10

        print(f'Reverse No: {revNum} \nOriginal : {orginal}')
        if revNum == orginal:
            return True
        else:
            return False    
        
sol = Solution()
print(sol.isPalindrome(121))        