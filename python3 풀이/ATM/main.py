input_count = int(input())
input_case = [int(x) for x in input().split(" ")]

input_case.sort()

ans = 0
tmp = 0
for case in input_case:
    tmp += case
    ans += tmp

print(ans)