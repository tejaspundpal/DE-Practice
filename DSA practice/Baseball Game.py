# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for val in operations:
            if val == 'C':
                popped_element = ans.pop()
            elif val == 'D':
                ans.append(ans[-1]*2)
            elif val == '+':
                ans.append(ans[-1]+ans[-2])
            else:
                ans.append(int(val))

        return sum(ans)