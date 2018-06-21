"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        result = ""
        try:
            first_chars= [s[0] for s in strs]
        except IndexError:
            return result

        if all([x == first_chars[0] for xin first_chars]):
            return first_chars[0] + self.longestCommonPrefix([s[1:] for s instrs])
        return result
