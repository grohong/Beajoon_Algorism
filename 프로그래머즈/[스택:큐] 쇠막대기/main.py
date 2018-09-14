def solution(arrangement):
    answer = 0
    stack = []

    for idx, ele in enumerate(arrangement):
        if ele == '(':
            stack.append(idx)
        else:
            if stack[-1] + 1 == idx:
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1

    return answer

print(solution("()(((()()))((())()))(())"))