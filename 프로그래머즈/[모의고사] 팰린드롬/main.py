# n 최소
# m 최대

def is_palindrome(num):
    num = str(num)

    right_flag = False
    idx = int(len(num) / 2)
    if len(num)%2 == 1:
        right_flag = True

    right = num[idx:]
    right = right[::-1]
    if right_flag:
        right = right[:len(right)-1]

    left = num[:idx]
    if right == left:
        return True

def solution(n, m):
    answer = 0

    for num in range(n,m+1):
        if is_palindrome(num):
            answer += 1

    return answer


print(solution(1,100))