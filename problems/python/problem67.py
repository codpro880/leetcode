"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec_a = int(a, 2)
        dec_b = int(b, 2)
        
        return bin(dec_a + dec_b)[2:]

if __name__ == "__main__":
    sol = Solution()
    result = sol.addBinary("11", "1")
    print(result)
