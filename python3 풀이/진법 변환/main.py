input_string_list = [str(x) for x in input().split()]

number = list(input_string_list[0])
method = int(input_string_list[1])

ans = 0

for num in number:
    tmp = ord(num)

    if ord('0') <= tmp and tmp <= ord('9'):
        ans = ans * method + (tmp - ord('0'))
    else:
        ans = ans * method + (tmp - ord('A') + 10)

print(ans)