"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(array, target):
    for index in range(len(array)):
        wanted_elem = target - array[index]
        if wanted_elem in array:
            if index != array.index(wanted_elem):
                return [index, array.index(wanted_elem)]

print("Should be [0, 1]: ", twoSum([2, 7, 11, 15], 9))
print("Should be [1,2]: ", twoSum([3, 2, 4], 6))
