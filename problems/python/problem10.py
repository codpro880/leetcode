"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
import numpy as np
class Solution:
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        
    

if __name__ == "__main__":
    sol = Solution()

    print("FIRST")
    s = "aa"
    p = "a"
    assert sol.isMatch(s, p) == False

    print("SECOND")
    s = "aa"
    p = "a*"
    assert sol.isMatch(s, p) == True
    
    print("THIRD")
    s = "ab"
    p = ".*"
    assert sol.isMatch(s, p) == True

    print("FOURTH")
    s = "aab"
    p = "c*a*b"
    assert sol.isMatch(s, p) == True
    
    print("FIFTH")
    s = "mississippi"
    p = "mis*is*p*."
    assert sol.isMatch(s, p) == False

    print("SIXTH")
    s = "aaa"
    p = "a*a"
    assert sol.isMatch(s, p) == True

    print("SEVENTH")
    s = "aaa"
    p = "a.a"
    assert sol.isMatch(s, p) == True

    print("EIGHTH")
    s = "a"
    p = "ab*a"
    assert sol.isMatch(s, p) == False

    print("NINETH")
    s = "ab"
    p = ".*.."
    assert sol.isMatch(s, p) == True

    print("TENTH")
    s = "ab"
    p = ".*..c*"
    assert sol.isMatch(s, p) == True

    print("11th")

    s = "aasdfasdfasdfasdfas"
    p = "aasdf.*asdf.*asdf.*asdf.*s"
    assert sol.isMatch(s, p) == True

    
    print("12th")
    s = "aa"
    p = "."
    assert sol.isMatch(s, p) == False

    print("13th")
    s = ""
    p = ".*"
    assert sol.isMatch(s, p) == True

    print("14th")
    s = ""
    p = ".*a*b*"
    assert sol.isMatch(s, p) == True

    print("15th")
    s = "abc"
    p = "a*b*c*"
    assert sol.isMatch(s, p) == True

    print("15th")
    s = "abc"
    p = "a*b*c*c"
    assert sol.isMatch(s, p) == True

    print("16th")
    s = "abcd"
    p = "a*ab*bc*cd"
    assert sol.isMatch(s, p) == True

    print("17th")
    s = "abcd"
    p = "a*aab*bc*cd"
    assert sol.isMatch(s, p) == False

    print("18th")
    s = "abcd"
    p = ".*.*.*.*.*.*"
    assert sol.isMatch(s, p) == True

    print("19th")
    s = "abcdefghijklmnopppptxt"
    p = "a.*.p*txt*"
    assert sol.isMatch(s, p) == True

    print("20th")
    s = "abcdefghijklmnopppptxtx"
    p = "a.*.p*txt*"
    assert sol.isMatch(s, p) == True

    print("21")
    s = ""
    p = "."
    assert sol.isMatch(s, p) == False

    print("22")
    s = ""
    p = ".*b"
    assert sol.isMatch(s, p) == False

    print("23")
    s = "aabcbcbcaccbcaabc"
    p = ".*a*aa*.*b*.c*.*a*"
    assert sol.isMatch(s, p) == True

    print("24th")
    s = "aaa"
    p = "ab*a*c*a"
    assert sol.isMatch(s, p) == True

    print("25th")
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"
    assert sol.isMatch(s, p) == False

    print("26th")
    s = "bbabacccbcbbcaaab"
    p = "a*b*a*a*c*aa*c*bc*"
    assert sol.isMatch(s, p) == False
