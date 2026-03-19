# https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # ans = []
        # rows = [
        #     "qwertyuiop",
        #     "asdfghjkl",
        #     "zxcvbnm"
        # ]
        
        # for word in words:
        #     for row in rows:
        #         if all([x in row for x in word.lower()]):
        #             ans.append(word)
        # return ans2

        l1="qwertyuiop"
        l2="asdfghjkl"
        l3="zxcvbnm"
        res=[]
        for word in words:
            w=word.lower()
            if len(set(l1+w))==len(l1) or len(set(l2+w))==len(l2) or len(set(l3+w))==len(l3) :
                res.append(word)
        return res
        