# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # if len(set(nums)) >= 3:
        #     return sorted(set(nums))[-3]
        # else:
        #     return sorted(set(nums))[-1]

        # nums = set(nums)
        # if len(nums) < 3:
        #     return max(nums)
        # else:
        #     nums.remove(max(nums))
        #     nums.remove(max(nums))
        #     return max(nums)

        nums = set(nums)
        nums = list(nums)
        n = len(nums)
        
        first = float('-inf')
        for i in range(n):
            if nums[i] > first:
                first = nums[i]
        
        second = float('-inf')
        for i in range(n):
            if nums[i] > second and nums[i] < first:
                second = nums[i]
        
        third = float('-inf')
        for i in range(n):
            if nums[i] > third and nums[i] < second:
                third = nums[i]
        
        if n >= 3:
            return third
        else:
            return first        