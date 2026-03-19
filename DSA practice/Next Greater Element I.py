# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result = []
        # for num in nums1:
        #     index = nums2.index(num)
            
        #     nextGreater = -1
        #     for j in range(index + 1, len(nums2)):
        #         if nums2[j] > num:
        #             nextGreater = nums2[j]
        #             break
            
        #     result.append(nextGreater)
        # return result

        # optimized way : monotonic stack method

        result = []
        stack = []
        mapping = {}

        if not nums2:
            return None

        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        for element in stack:
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])

        return result                   
