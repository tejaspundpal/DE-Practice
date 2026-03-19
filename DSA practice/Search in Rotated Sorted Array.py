# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return -1    
        if target < nums[0]:
            for item in reversed(nums):
                if item == target :
                    return nums.index(item)
                elif item > nums[0] or item == nums[0]:
                    return -1
        else:
            for item in nums:
                if item == target:
                    return nums.index(item)
                elif item < nums[0] or item == nums[-1]:
                    return -1                            