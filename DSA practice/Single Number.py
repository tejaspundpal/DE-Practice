#https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=array

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # freq = [0]* len(nums)
        # for i in range(len(nums)):
        #     freq[nums[i]]+=1

        # # print(freq)
        # for i in range(len(freq)):
        #     if freq[i] == 1:
        #         return i  
        
        result = 0
        for num in nums:
            result ^= num
        return result