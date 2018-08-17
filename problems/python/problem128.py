"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
# Starts has tuples consisting of (length, end), where end is the key in ends. Ends is similar.
# Idea is to just keep track of starts and ends, and add elements to streaks as they come in.
# There's also some logic for merging these streaks (in_both)
def long_cons(nums):
    if not nums:
        return 0
    starts = {}
    ends = {}
    nums = set(nums)
    for num in nums:
        if num+1 not in starts and num-1 not in ends:
            in_neither(starts, ends, num)
        elif num+1 not in starts and num-1 in ends:
            end_only(starts, ends, num)
        elif num+1 in starts and num-1 not in ends:
            start_only(starts, ends, num)
        else:
            in_both(starts, ends, num)
    return max([starts[i][0] for i in starts])

def in_neither(starts, ends, num):
    starts[num] = [1, num]
    ends[num] = [1, num]

def end_only(starts, ends, num):
    cur = ends[num-1]
    ends.pop(num-1)
    ends[num] = [cur[0] + 1, cur[1]]
    starts[cur[1]][0] += 1
    starts[cur[1]][1] = num

def start_only(starts, ends, num):
    cur = starts[num+1]
    starts.pop(num+1)
    starts[num] = [cur[0] + 1, cur[1]]
    ends[cur[1]][0] += 1
    ends[cur[1]][1] = num

def in_both(starts, ends, num):
    real_end = starts[num+1][1]
    real_start = ends[num-1][1]
    starts.pop(num+1)
    ends.pop(num-1)
    incr = real_end - real_start + 1
    ends[real_end] = [incr, real_start]
    starts[real_start] = [incr, real_end]

class Solution(object):
    def longestConsecutive(self, nums):
        return long_cons(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print("result: ", sol.longestConsecutive(nums))
            
    nums = [123, 999, -1, 0, 998, 124, 918, 125, 126, 122, 121]
    print("result: ", sol.longestConsecutive(nums))
