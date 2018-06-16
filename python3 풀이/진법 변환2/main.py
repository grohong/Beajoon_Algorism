input_number_list = [int(x) for x in input().split()]

input_number = input_number_list[0]
method = input_number_list[1]

ans = ""

while (input_number>0):
    tmp = int(input_number%method)

    if tmp < 10:
        ans += str(tmp)
    else:
        ans += str(chr(tmp+87))

    input_number = int(input_number/method)

print(ans[::-1])
