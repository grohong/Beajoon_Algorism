def solution(land, P, Q):
    answer = -1

    ond_id = []
    for block in land:
        ond_id += block
    one_di = sorted(ond_id)
    layer = list(set(one_di))

    tmp_list = one_di
    tmp_block = 0
    for idx in layer:
        tmp_answer = 0
        if idx == layer[0]:
            for block in one_di:
                tmp = idx - block
                if tmp < 0:
                    tmp_block += tmp
                else:
                    tmp_block += tmp

            tmp_block = (tmp_block)*-1
            tmp_answer = (tmp_block*Q)
            answer = tmp_answer
        else:
            tmp_block -= (len(one_di)-one_di.index(idx))
            tmp_answer += tmp_block*Q
            tmp_answer += one_di.index(idx)*P

        if answer == -1 or answer > tmp_answer:
            answer = tmp_answer

    return answer


print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))
print(solution(	[[1, 2], [2, 3]], 3, 2))



# def solution(land, P, Q):
#     answer = -1
#
#     max_land = 0
#     min_land = 300
#     for block in land:
#         if max(block) >= max_land:
#             max_land = max(block)
#         if min(block) <= min_land:
#             min_land = min(block)
#
#     for idx in range(min_land, max_land+1):
#         tmp_answer = 0
#         for layer in land:
#             for block in layer:
#                 tmp = idx - block
#                 if tmp < 0:
#                     tmp_answer += -1*(tmp*Q)
#                 else:
#                     tmp_answer += tmp*P
#
#         if answer == -1 or answer > tmp_answer:
#             answer = tmp_answer
#
#     return answer