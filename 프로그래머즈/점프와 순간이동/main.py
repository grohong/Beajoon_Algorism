def solution(n):
    ans = 0

    num = n
    while(True):

        if num%2 == 0:
            num = int(num/2)
        else:
            num -= 1
            ans += 1

        if num == 0:
            break

    return ans

print(solution(5000))