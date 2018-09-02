def total(works):
    total = 0

    for work in works:
        total += work*work

    return total

def solution(no, works):
    result = 0
    works_list = sorted(works)

    for _ in range(no):
        tmp = 0
        tmp_result = 0
        tmp_list = list(works_list)

        for idx, work in enumerate(tmp_list):
            if work != tmp:
                tmp_works = list(tmp_list)
                tmp = work
                tmp_works[idx] = work-1

                if tmp_result == 0:
                    tmp_result = total(tmp_works)
                    works_list = tmp_works
                else:
                    tmp_result = min(tmp_result, total(tmp_works))
                    works_list = tmp_works

        result = tmp_result

    return result

# import queue
# def solution(no, works):
#     pq = queue.PriorityQueue(len(works))
#     for work in works:
#         pq.put_nowait(-work)
#     for _ in range(no):
#         work = pq.get_nowait()
#         if work == 0:
#             break
#         pq.put_nowait(work+1)
#
#     answer = 0
#     while not pq.empty():
#         answer += pq.get_nowait()**2
#     return answer


print(solution(2, [3,3,3]))
print(solution(4, [4,3,3]))
print(solution(7, [4,51,32,51,35,32,4]))