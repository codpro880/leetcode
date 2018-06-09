"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        for i in range(len(s)):
            if len(s) - i - 1 < longest:
                break
            num_unique_ascii_chars = 26 * 2 + 10 * 2 + 50
            cur = self.find_longest_substr_using_first_char(s[i:num_unique_ascii_chars])
            if cur > longest:
                longest = cur

        return longest

    def find_longest_substr_using_first_char(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_substr = []
        for char in s:
            if char in cur_substr:
                break
            else:
                cur_substr.append(char)

        return len(cur_substr)

if __name__ == "__main__":
    sol = Solution()
    print("Len: ", sol.lengthOfLongestSubstring("vbxpvwkkteaiob"))
