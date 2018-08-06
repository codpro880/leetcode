"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
# Idea here is to use bijection between binary num of length items and each subset
import numpy as np
def power_set(items):
    items = np.array(items)
    num_pos = 2**len(items)
    result = []
    for pos in range(num_pos):
        # Create mask
        m = str(bin(pos))[2:]
        m = zero_pad(m, len(items))
        mask = np.array([bool(int(x)) for x in m])
        result.append(items[mask])
    return result

def zero_pad(m, length):
    num_zeros = length - len(m)
    return "0"*num_zeros + m

if __name__ == "__main__":
    result = power_set([1,2,3])
    print(result)
