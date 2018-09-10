def solution(d, budget):
    sort_budget = sorted(budget)

    answer = 0
    for bud in sort_budget:
        if d-bud >= 0:
            d -= bud
            answer += 1
        else:
            break

    return answer


print(solution(9, [1,3,2,5,4]))