"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums):
        for i in range(1, len(nums))[::-1]:
            if nums[i] > nums[i-1]:
                place = i-1
                for k in range(place+1, len(nums))[::-1]:
                    if nums[k] > nums[place]:
                        nums[place], nums[k] = nums[k], nums[place]
                        nums[place+1:] = nums[place+1:][::-1]
                        return
            
        nums[:] = nums[::-1]
        return

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1]
    sol.nextPermutation(nums)
    assert nums == [1,2,3]

    nums = [1,2,6,5,4,3]
    sol.nextPermutation(nums)
    assert nums == [1,3,2,4,5,6]

    nums = [2,3,1]
    sol.nextPermutation(nums)
    assert nums == [3,1,2]
