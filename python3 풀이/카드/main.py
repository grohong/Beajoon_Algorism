input_count = int(input())
input_numbers = {}

for index in range(0, input_count):
    tmp = int(input())

    if input_numbers.get(tmp) == None:
        input_numbers.setdefault(tmp, 1)
    else:
        input_numbers[tmp] += 1


temp = [value for key, value in input_numbers.items()]
max_value = max(temp)

key_list = []
for key, value in input_numbers.items():
    if value == max_value:
        key_list.append(key)

print(min(key_list))