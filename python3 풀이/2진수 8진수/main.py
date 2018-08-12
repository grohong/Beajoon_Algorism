input_number = input()
numbers = list(input_number)[::-1]

ans = 0
for i, number in enumerate(numbers):
    ans += int(number)*pow(2, i)

print(ans)