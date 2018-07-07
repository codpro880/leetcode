"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
class Solution:
    def isMatch(self, s, p):
        p = self.reduce_p(p)
        return self.isMatchHelper(s, p)


    def isMatchHelper(self, s, p):
        if not s:
            return not p or len([x for x in p if x == "*"]) == len(p)
        if not p:
            return not s

        hard_match = p[0] == s[0] or p[0] == "?"
        if hard_match:
            return self.isMatchHelper(s[1:], p[1:])
        else:
            if p[0] != "*":
                return False
            else:
                return self.isMatchHelper(s[1:], p) or self.isMatchHelper(s, p[1:])

    def reduce_p(self, p):
        new_p = []
        for cur, next in zip(p, p[1:]):
            if not (cur == "*" and next == "*"):
                new_p.append(cur)
        if len(p) > 0:
            new_p.append(p[-1])
        return "".join(new_p)
                

if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    p = "a"
    assert sol.isMatch(s, p) == False

    s = "aa"
    p = "*"
    assert sol.isMatch(s, p) == True

    s = "cb"
    p = "?a"
    assert sol.isMatch(s, p) == False
    
    s = "adceb"
    p = "*a*b"
    assert sol.isMatch(s, p) == True

    s = "acdcb"
    p = "a*c?b"
    assert sol.isMatch(s, p) == False

    s = ""
    p = "*"
    assert sol.isMatch(s, p) == True

    s = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
    p = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
    assert sol.isMatch(s, p) == True
