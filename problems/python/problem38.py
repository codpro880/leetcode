"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
import numpy as np
class Solution(object):
    def countAndSay(self, n):
        return self.count_and_say_helper(n)

    def count_and_say_helper(self, n):
        result = "1"
        for i in range(1, n):
            result = self.count_digits(result)
        return result

    def count_digits(self, seq):
        int_list = [int(char) for char in seq]
        diffs = np.diff(int_list)
        if len(diffs) == 0: # all the same digit
            count = len(int_list)
            return "{0}{1}".format(count, int_list[0])
        else:
            split_points = np.where(diffs != 0)[0] + 1
            split_points = np.hstack((0, split_points, len(seq)))
            result = ""
            for split_start, split_end in zip(split_points, split_points[1:]):
                split = int_list[split_start:split_end]
                result += str(len(split)) + str(split[0])
            return result

if __name__ == "__main__":
    sol = Solution()
    print("111221? ", sol.count_digits("1211"))
    print("n = 1: ", sol.countAndSay(1))
    print("n = 2: ", sol.countAndSay(2))
    print("n = 3: ", sol.countAndSay(3))
    print("n = 4: ", sol.countAndSay(4))
    print("n = 5: ", sol.countAndSay(5))
