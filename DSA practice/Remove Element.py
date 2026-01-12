# https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1

        return j   