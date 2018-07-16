"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        result = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            if interval.start <= result[-1].end:
                result[-1].end = max(interval.end, result[-1].end)
            else:
                result.append(interval)
        return result

if __name__ == "__main__":
    sol = Solution()
    input = [Interval(s=1, e=3),Interval(2,6),Interval(8,10),Interval(15,18)]
    result = sol.merge(input)
    result_p = [[interval.start, interval.end] for interval in result]
    print(result_p)
