# https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc_score = sorted(score, reverse=True)
        
        rank_map = {}
        for i, num in enumerate(desc_score):
            if i == 0:
                rank_map[num] = "Gold Medal"
            elif i == 1:
                rank_map[num] = "Silver Medal"
            elif i == 2:
                rank_map[num] = "Bronze Medal"
            else:
                rank_map[num] = str(i + 1)
        
        ranks = [rank_map[num] for num in score]
        return ranks