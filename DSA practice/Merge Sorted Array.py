# https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1[m:] = nums2
        # nums1.sort()

        mindx = m - 1
        nindx = n - 1
        right = m + n - 1

        while nindx >= 0:
            if mindx >= 0 and nums1[mindx] > nums2[nindx]:
                nums1[right] = nums1[mindx]
                mindx -= 1
            else:
                nums1[right] = nums2[nindx]
                nindx -= 1
            right -= 1