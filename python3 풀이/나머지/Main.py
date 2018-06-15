input_number_list = [int(x) for x in input().split()]

a = input_number_list[0]
b = input_number_list[1]
c = input_number_list[2]

print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)



