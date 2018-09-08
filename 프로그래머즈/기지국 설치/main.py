def solution(n, stations, w):
    answer = 0

    start = 0
    terms = []
    for station in stations:
        if ((station - w) - 1 - start) > 0:
            terms.append((station - w) - 1 - start)
        start = station + w
        if start > n:
            break

    if start < n:
        terms.append(n-start)

    width = (2*w) + 1
    for term in terms:
        answer += int(term/width)
        if term%width != 0:
            answer += 1


    return answer


print(solution(11, [2, 5, 8], 10))
# print(solution(16, [9], 2))