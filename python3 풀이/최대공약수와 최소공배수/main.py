class solution():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def max(self):
        max_number = 1
        for i in range(2, min(self.number1, self.number2)+1):
            if (self.number1 % i == 0) and (self.number2 % i == 0):
                max_number = i

        return max_number

input_number_list = [int(x) for x in input().split()]

answer = solution(input_number_list[0], input_number_list[1])
print(answer.max())
print(int((input_number_list[0]*input_number_list[1])/answer.max()))