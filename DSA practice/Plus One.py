# https://leetcode.com/problems/plus-one/submissions/1880775485/?envType=problem-list-v2&envId=array

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r=''
        a=[]
        for i in digits:
            r+=str(i)
        r=int(r)+1
        r=str(r)
        for i in r:
            a.append(int(i))
        return a
    
        # carry = 1
        # for i in range(len(digits) - 1, -1, -1):
        #     s = digits[i] + carry
        #     digits[i] = s % 10
        #     carry = s // 10
        # if carry:
        #     digits = [1] + digits
        # return digits