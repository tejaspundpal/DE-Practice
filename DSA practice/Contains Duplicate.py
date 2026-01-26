# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # nums.sort()
        # n = len(nums)
        # for i in range(1, n):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False