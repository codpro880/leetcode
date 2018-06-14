"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        reindexed = self.reindex(s, numRows)
        result = self.create_string_from_indecies(reindexed, numRows)
        return result

    def reindex(self, s, numRows):
        def reindex_generator(numRows):
            while True:
                for i in range(numRows):
                    yield i
                for i in range(numRows)[1:-1][::-1]:
                    yield i

        result = []
        gen = reindex_generator(numRows)
        for char in s:
            result.append((char, next(gen)))

        return result

    def create_string_from_indecies(self, reindexed, numRows):
        result = []
        for row in range(numRows):
            for char, index in reindexed:
                if row == index:
                    result.append(char)

        return "".join(result)

if __name__ == "__main__":
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"
