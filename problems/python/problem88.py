"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
import bisect
import numpy as np
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        zero_inds = [ind for ind, elt in enumerate(nums1) if elt == 0]
        start_of_last_zeros = np.where(np.diff(zero_inds) != 1)[0] + 1
        if start_of_last_zeros:
            hi = zero_inds[start_of_last_zeros[0]]
        else:
            hi = zero_inds[0]

        for num in nums2:
            ind_to_insert = bisect.bisect_left(nums1, num, hi=hi)
            hi += 1
            for i in range(ind_to_insert, len(nums1)-1)[::-1]: # Push everything up one index
                nums1[i+1] = nums1[i]
            nums1[ind_to_insert] = num

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    sol.merge(nums1, -1, nums2, -2)
    print(nums1)

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    nums2 = [1,2,2]
    sol.merge(nums1, -1, nums2, -2)
    print(nums1)
