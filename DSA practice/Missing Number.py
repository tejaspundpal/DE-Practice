# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n * (n+1))/2
        list_sum = 0
        for num in nums:
            list_sum += num

        return int(sum - list_sum)    