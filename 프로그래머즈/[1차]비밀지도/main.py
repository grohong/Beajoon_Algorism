def merge_binary(str1, str2):

    merge_str = ""
    for chr1, chr2 in zip(str1, str2):
        if chr1 == "0" and chr2 == "0":
            merge_str += " "
        else:
            merge_str += "#"

    return merge_str

def solution(n, arr1, arr2):
    answer = []

    for num1, num2 in zip(arr1, arr2):
        answer.append(merge_binary("{0:b}".format(num1).zfill(n), "{0:b}".format(num2).zfill(n)))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))