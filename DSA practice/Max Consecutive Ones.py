#https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            ans = max(cnt,ans)

        return ans    

        # Generic code for maximum consecutive count 

        # if len(nums) == 1 and nums[0] == 1:
        #     return 1
        # if len(nums) == 1 and nums[0] != 1:
        #     return 0    
        # for i in range(len(nums)):
        #     if nums[i] == element:
        #         cnt += 1
        #     else:
        #         element = nums[i]
        #         cnt = 1
        #     ans = max(cnt,ans)

        # return ans    