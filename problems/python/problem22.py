"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(sorted(self.generateParensHelper(n)))

    def generateParensHelper(self, n):
        if n == 0:
            return set([''])
        if n == 1:
            return set(['()'])
        else:
            prev_sol = self.generateParenthesis(n-1)
            result = set()
            for sol in prev_sol:
                result.add('(' + sol + ')')
                for i in range(len(sol)):
                    result.add(sol[:i] + '()' + sol[i:])
            return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(n=3))

    print(sol.generateParenthesis(n=4))

    our_result = sol.generateParenthesis(n=5)
    #our_result = ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())()()","(())(())()","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]
    real_result = ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]

    assert our_result == real_result
