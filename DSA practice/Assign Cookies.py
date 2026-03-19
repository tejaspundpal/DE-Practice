# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0

        while i < len(s) and j < len(g):
            if g[j] <= s[i]:
                j+=1
            i += 1    

        return j