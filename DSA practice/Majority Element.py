# https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

        # count = 0
        # element = None

        # for num in nums:
        #     if count == 0:
        #         element = num
        #     count += (1 if num == element else -1)

        # return element