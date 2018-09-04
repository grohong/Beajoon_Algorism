def solution(dartResult):
    answer = 0

    num = ""
    answer_list = []
    for char in dartResult:

        if ord("0") <= ord(char) <= ord("9"):
            num += char
            continue

        if char == "S":
            answer_list.append(int(num))
            num = ""
            continue
        elif char == "D":
            answer_list.append(pow(int(num), 2))
            num = ""
            continue
        elif char == "T":
            answer_list.append(pow(int(num), 3))
            num = ""
            continue

        if char == "*":
            if len(answer_list) == 1:
                answer_list[0] = answer_list[0]*2
            else:
                answer_list[len(answer_list)-1] = answer_list[len(answer_list)-1]*2
                answer_list[len(answer_list)-2] = answer_list[len(answer_list)-2]*2
            continue
        elif char == "#":
            if len(answer_list) == 1:
                answer_list[0] = answer_list[0]*-1
            else:
                answer_list[len(answer_list)-1] = answer_list[len(answer_list)-1]*-1
            continue


    for ans in answer_list:
        answer += ans


    return answer


print(solution("1T2D3D#"))