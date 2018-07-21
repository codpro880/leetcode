"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# Not sure if this is the most efficient thing to do, but we can just move nonzero elts down,
# 0s will bubble to top
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if self.get_first_zero_ind(nums) == -1:
            return nums
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    first_zero_ind = self.get_first_zero_ind(nums)
                    nums[i], nums[first_zero_ind] = nums[first_zero_ind], nums[i]
        return nums

    def get_first_zero_ind(self, arr):
        for i in range(len(arr)):
            if arr[i] == 0:
                return i
        return -1
                
if __name__ == "__main__":
    sol = Solution()
    input = [0,1,0,3,12]
    sol.moveZeroes(input)
    print(input)

    input2 = [1]
    sol.moveZeroes(input2)
    print(input2)
