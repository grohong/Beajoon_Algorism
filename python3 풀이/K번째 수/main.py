input_setting = [int(x) for x in input().split()]
input_count = input_setting[0]
input_order = input_setting[1]

input_numbers = [int(x) for x in input().split()]
input_numbers.sort()

print(input_numbers[input_order]-1)