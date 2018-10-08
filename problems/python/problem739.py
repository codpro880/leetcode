def daily_temps(temperatures):    
    stack = []
    result = []
    for idx, temp in list(enumerate(temperatures))[::-1]:
        if not stack:
            result.append(0)
        else:
            stack_ind, stack_temp = stack[-1]
            while temp >= stack_temp and stack:
                stack_ind, stack_temp = stack.pop()
            if stack:
                result.append(stack_ind - idx)
                stack.append([stack_ind, stack_temp])
            else:
                result.append(0)

        stack.append([idx, temp])

    return result[::-1]

if __name__ == "__main__":
    test = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temps(test))
