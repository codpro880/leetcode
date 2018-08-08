def remove_inv(s):
    stripped = strip_off_ends(s)
    invalids = get_invalid_parens(stripped)
    result = remove_invalids(invalids, stripped)
    return result

def strip_off_ends(s):
    if not s:
        return s
    start = 0
    stop = 0
    for i in range(len(s)):
        if s[i] != ')':
            start = i
            break
    for i in range(len(s))[::-1]:
        if s[i] != '(':
            stop = i + 1
            break
    return s[start:stop]

def get_invalid_parens(s):
    res = []
    s = [char for char in s if char == '(' or char == ')']
    for char in s:
        if char == '(':
            res.append('(')
        if char == ')':
            if res and res[-1] == '(':
                res.pop()
            else:
                res.append(')')
    return res

def remove_invalids(invalids, stripped):
    if not invalids:
        return [stripped]
    cur_rem = remove_all(invalids[0], [stripped])
    for paren in invalids[1:]:
        cur_rem = remove_all(paren, cur_rem)
    result = list(set(cur_rem))
    result = [r for r in result if is_valid(r)]
    return result

def remove_all(paren, cur_rem):
    res = []
    for rem in cur_rem:
        for i in range(len(rem)):
            if rem[i] == paren:
                res.append(rem[:i] + rem[i+1:])
    return res

def is_valid(r):
    stack = []
    for char in r:
        if char == '(':
            stack.append('(')
        if char == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    inp = "()())()"
    print(remove_inv(inp))
