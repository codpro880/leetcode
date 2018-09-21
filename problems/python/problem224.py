class Solution(object):
    def calculate(self, s):
        tokens = self.tokenize(s)
        res = 0
        sign = 1
        stack = []
        for token in tokens:
            if token == "+":
                sign = 1
            elif token == "-":
                sign = -1
            elif token == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif token == ")":
                sign = stack.pop()
                cur_res = stack.pop()
                res = sign * res + cur_res
            else: # digit
                res += int(token) * sign
        return res
        

    def tokenize(self, s):
        stripped = s.strip()
        res = []
        non_digits = ["+", "-", "(", ")"]
        for char in stripped:
            if char in non_digits:
                res.append(char)
            else:
                if not res or res[-1] in non_digits:
                    res.append(char)
                else:
                    res[-1] += char
        return res

if __name__ == "__main__":
    sol = Solution()
    s = "1 + 1"
    print("2: ", sol.calculate(s))

    s = " 2-1 + 2 "
    print("3: ", sol.calculate(s))

    s = "(1+(4+5+2)-3)+(6+8)"
    print("23: ", sol.calculate(s))
