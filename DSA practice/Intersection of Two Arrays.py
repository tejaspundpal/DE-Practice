# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        nums1set = set(nums1)

        for element in nums2:
            if element in nums1set:
                if element not in ans:
                    ans.append(element)

        return ans         
        
        