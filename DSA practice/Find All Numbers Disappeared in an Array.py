# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        nums1 = []
        result = []
        for i in range(1,len(nums)+1):
            nums1.append(i)

        for num in nums1:
            if num not in nums_set:
                result.append(num)

        return result
