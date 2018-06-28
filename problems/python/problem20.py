"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True

        stack = []
        matches = {'(': ')',
                   '[': ']',
                   '{': '}'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
                else:
                    match = stack.pop()
                    if char != matches[match]:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") == True
