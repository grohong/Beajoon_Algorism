from collections import deque

def solution(msg):
    answer = []
    ord_index = 64

    cach = dict()
    queue = deque()
    cach_index = 27
    for string in msg:
        if len(queue) == 0:
            queue.append(string)
        elif len(queue) != 0:
            queue.append(string)
            queue_string = ''.join(queue)

            if queue_string not in cach.keys():
                cach[queue_string] = cach_index
                cach_index += 1

                tmp = queue.popleft()
                if len(tmp) == 1:
                    answer.append(ord(tmp) - ord_index)
                else:
                    answer.append(cach[tmp])

            else:
                queue.clear()
                queue.append(queue_string)

    tmp = queue.popleft()
    if len(tmp) == 1:
        answer.append(ord(tmp) - ord_index)
    else:
        answer.append(cach[tmp])

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
