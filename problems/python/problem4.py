"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return self.get_median(nums2)
        if not nums2:
            return self.get_median(nums1)

        # If they're both None/empty, the median isn't well defined...so do nothing (but crash)
        return self.findMedianNumpySortedArrays(nums1, nums2)

    def findMedianNumpySortedArrays(self, nums1, nums2):
        """
        Find median of each list. WLOG, say L1 is the smaller list. Then, if median(L1) < median(L2), kill off the bottom half of L1, and remove the same number of items from the top
        of L2. This preserves the global median between the two lists, but gets rid of approximately half the values. There's some 'off by one' shenangans I'm glossing over, but that's
        the main idea.
        """
        if not nums1:
            return self.get_median(nums2)
        if not nums2:
            return self.get_median(nums1)
        if len(nums1) == 1:
            x = self.bin_insert(nums1[0], nums2)
            return self.get_median(x)
        if len(nums2) == 1:
            x = self.bin_insert(nums2[0], nums1)
            return self.get_median(x)
        if len(nums1) == 2:
            nums2 = self.bin_insert(nums1[0], nums2)
            nums2 = self.bin_insert(nums1[1], nums2)
            return self.get_median(nums2)
        if len(nums2) == 2:
            nums1 = self.bin_insert(nums2[0], nums1)
            nums1 = self.bin_insert(nums2[1], nums1)
            return self.get_median(nums1)


        nums1_median = self.get_median(nums1)
        nums2_median = self.get_median(nums2)
        if len(nums1) > len(nums2):
            if nums1_median < nums2_median:
                new_nums2 = nums2[:int(len(nums2)/2) + 1]
                num_items_removed = len(nums2) - len(new_nums2)
                new_nums1 = nums1[num_items_removed:]
                return self.findMedianNumpySortedArrays(new_nums1, new_nums2)
            else:
                new_nums2 = nums2[int(len(nums2)/2) - 1:] if len(nums2) % 2 == 0 else nums2[int(len(nums2)/2):]
                num_items_removed = len(nums2) - len(new_nums2)
                new_nums1 = nums1[:-num_items_removed]
                return self.findMedianNumpySortedArrays(new_nums1, new_nums2)
        else:
            if nums1_median > nums2_median:
                new_nums1 = nums1[:int(len(nums1)/2) + 1]
                num_items_removed = len(nums1) - len(new_nums1)
                new_nums2 = nums2[num_items_removed:]
                return self.findMedianNumpySortedArrays(new_nums1, new_nums2)
            else:
                new_nums1 = nums1[int(len(nums1)/2) - 1:] if len(nums1) % 2 == 0 else nums1[int(len(nums1)/2):]
                num_items_removed = len(nums1) - len(new_nums1)
                new_nums2 = nums2[:-num_items_removed]
                return self.findMedianNumpySortedArrays(new_nums1, new_nums2)

    def get_median(self, nums):
        if len(nums) % 2 == 0:
            return (nums[int(len(nums)/2) - 1] + nums[int(len(nums)/2)]) / 2
        else:
            return nums[int(len(nums)/2)]

    def bin_insert(self, num, li):
        """ Assumes li sorted """
        if not li:
            return [num]
        if len(li) == 1:
            if num < li[0]:
                return [num, li[0]]
            else:
                return [li[0], num]

        median = self.get_median(li)
        if num < median:
            return self.bin_insert(num, li[0:int(len(li)/2)]) + li[int(len(li)/2):]
        elif num > median:
            return  li[:int(len(li)/2)] + self.bin_insert(num, li[int(len(li)/2):])
        else:
            return li[:int(len(li)/2)] + [num] + li[int(len(li)/2):]
                              
        
if __name__ == "__main__":
    sol = Solution()

    arr1 = [1,3]
    arr2 = [2]
    print("Starting unit tests...")
    assert sol.findMedianSortedArrays(arr1, arr2) == 2
    assert sol.findMedianSortedArrays(arr2, arr1) == 2


    arr1 = [1,2,3,4]
    arr2 = [5,6,7,8]
    assert sol.findMedianSortedArrays(arr1, arr2) == 4.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 4.5

    arr1 = [1]
    arr2 = [5,6,7,8]
    assert sol.findMedianSortedArrays(arr1, arr2) == 6
    assert sol.findMedianSortedArrays(arr2, arr1) == 6

    arr1 = [1, 5, 7, 13, 29, 33, 50, 67]
    arr2 = [2, 3, 4, 12, 17, 18]
    assert sol.findMedianSortedArrays(arr1, arr2) == 12.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 12.5

    arr1 = [1,4]
    arr2 = [2,3]
    assert sol.findMedianSortedArrays(arr1, arr2) == 2.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 2.5

    arr1 = [1,2,5]
    arr2 = [3,4,6]
    assert sol.findMedianSortedArrays(arr1, arr2) == 3.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 3.5

    arr1 = [0,10]
    arr2 = [1,2,3,4,5,6,7,8,9]
    assert sol.findMedianSortedArrays(arr1, arr2) == 5
    assert sol.findMedianSortedArrays(arr2, arr1) == 5

    arr1 = [1,2]
    arr2 = [3,4]
    assert sol.findMedianSortedArrays(arr1, arr2) == 2.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 2.5

    arr1 = [1,4,6]
    arr2 = [2,3,5]
    assert sol.findMedianSortedArrays(arr1, arr2) == 3.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 3.5

    arr1 = [1,2,6,7,8,9]
    arr2 = [3,4,5]
    assert sol.findMedianSortedArrays(arr1, arr2) == 5
    assert sol.findMedianSortedArrays(arr2, arr1) == 5

    arr1 = [3,4,5]
    arr2 = [1,2,6,7,8]
    assert sol.findMedianSortedArrays(arr1, arr2) == 4.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 4.5

    arr1 = [1,2,6,7]
    arr2 = [3,4,5,8]
    assert sol.findMedianSortedArrays(arr1, arr2) == 4.5
    assert sol.findMedianSortedArrays(arr2, arr1) == 4.5
    print("All tests passed!")    
