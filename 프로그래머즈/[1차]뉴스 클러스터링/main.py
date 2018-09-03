from collections import deque

def parse_list(str):
    a = 97
    z = 122

    queue = deque()
    pair_list = []
    for char in str:
        if a <= ord(char) <= z:
            queue.append(char)
        else:
            queue.clear()

        if len(queue) == 2:
            pair_list.append(''.join(queue))
            queue.popleft()

    return pair_list

def parse_dic(list):

    dic = dict()
    for string in list:
        if string not in dic.keys():
            dic[string] = 1
        else:
            dic[string] += 1

    return dic

def J(dic1, dic2):
    unions = dict()
    intersections = dict()

    for dic_key in dic1.keys():
        if dic_key in dic2:
            if dic2[dic_key] > dic1[dic_key]:
                unions[dic_key] = dic2[dic_key]
                intersections[dic_key] = dic1[dic_key]
            else:
                unions[dic_key] = dic1[dic_key]
                intersections[dic_key] = dic2[dic_key]
        else:
            unions[dic_key] = dic1[dic_key]

    for dic_key in dic2:
        if dic_key not in unions.keys():
            unions[dic_key] = dic2[dic_key]

    print(unions)
    print(intersections)

    tmp_inter = 0
    tmp_union = 0

    for inter in intersections.values():
        tmp_inter += inter

    for union in unions.values():
        tmp_union += union

    if tmp_inter == 0 and tmp_union == 0:
        return 65536
    elif tmp_inter == 0 and tmp_union != 0:
        return 0

    return int((tmp_inter/tmp_union)*65536)



def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1_dic = parse_dic(parse_list(str1))
    str2_dic = parse_dic(parse_list(str2))

    print(str1_dic)
    print(str2_dic)

    answer = J(str1_dic, str2_dic)


    return answer

print(solution("aa1+aa2", "AAAA12"))
print(solution("handshake", "shake hands"))
print(solution("FRANCE", "french"))