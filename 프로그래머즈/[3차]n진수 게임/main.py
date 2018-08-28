# n: 진법
# t: 구해야 되는 수의 갯수
# m: 게임에 참가하는 인원
# p: 튜브의 순
def convert(n, base):
    T = "0123456789ABCDEF"

    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''

    member = m
    point = p

    start = 0
    point_index = 1
    while(True):

        for x in convert(start, n):
            if point == point_index:
                answer += x

            if len(answer) == t:
                break

            point_index += 1
            if point_index == member+1:
                point_index = 1

        if len(answer) == t:
            break
        start += 1

    return answer


print(solution(16,16,2,2))