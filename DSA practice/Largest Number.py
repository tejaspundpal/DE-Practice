#https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # str_nums = [str(num) for num in nums]

        # from functools import cmp_to_key
        # str_nums.sort(key = cmp_to_key(lambda a,b: -1 if a + b > b + a else 1))

        # if str_nums[0] == "0":
        #     return "0"

        # ans = "".join(str_nums)

        # return ans

        nums = [str(i) for i in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)

        if nums[0] == '0':
            return '0'

        return ''.join(nums)