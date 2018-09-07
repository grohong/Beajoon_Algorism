def solution(A, B):
    answer = 0

    sort_A = sorted(A, reverse=True)
    sort_B = sorted(B, reverse=True)

    for a in sort_A:
        if a >= sort_B[0]:
            sort_B.remove(sort_B[len(sort_B)-1])
        else:
            sort_B.remove(sort_B[0])
            answer += 1

    answer += len(sort_B)

    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))