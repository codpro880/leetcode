"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# Wanted to do this fresh, even though i've solved it before
# must have two pos and one neg or two neg and one pos. Or 3 zeros.
import numpy as np
import bisect
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = np.array(nums)
        return self._three_sum_h(nums)

    def _three_sum_h(self, nums):
        nums_sorted = np.sort(nums)
        where_zero = np.where(nums_sorted == 0)[0]
        first_zero = where_zero[0]
        last_zero = where_zero[-1]
        negatives = nums_sorted[:first_zero]
        positives = nums_sorted[last_zero+1:]

        result = []
        if len(where_zero) > 3:
            result.append([0,0,0])

        two_neg_and_one_pos = self._gen_combo_results(negatives, positives)
        two_pos_and_one_neg = self._gen_combo_results(positives, negatives)
        mirrors = self._find_same(positives, negatives)

        result.extend(two_neg_and_one_pos)
        result.extend(two_pos_and_one_neg)
        result.extend(mirrors)

        return result

    def _gen_combo_results(self, combo_arr, arr):
        result = []
        combo_arr_lookup = set(combo_arr)
        for item in arr:
            for other in combo_arr:
                sum = item + other
                if -sum in combo_arr_lookup:
                    if -sum == other: # have to check we have two
                        if self._at_least_two(combo_arr, other):
                            result.append([item, other, -sum])
                    else:
                        result.append([item, other, -sum])

        if result:
            return np.unique(result, axis=0) # unique?
        else:
            return result

    def _find_same(self, pos, negs):
        result = []
        negs_lookup = set(negs)
        for p in pos:
            if -p in negs:
                result.append([-p, 0, p])
        return result

    def _at_least_two(self, arr, item):
        ind = bisect.bisect_left(arr, item)
        return len(arr) - 2 >= ind and arr[ind] == arr[ind+1] and arr[ind] == item

if __name__ == "__main__":
    sol = Solution()
    input = [-1, 0, 1, 2, -1, -4]
    result = sol.threeSum(input)
    print(result)
