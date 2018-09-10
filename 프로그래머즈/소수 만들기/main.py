def isDecimal(num):
    answer = True
    for idx in range(2, num):
        if num % idx == 0:
            answer = False
            break

    return answer

def solution(nums):
    answer = 0

    for idx1 in range(len(nums)-2):
        for idx2 in range(idx1+1, len(nums)-1):
            for idx3 in range(idx2+1, len(nums)):
                # print("======")
                # print(nums[idx1])
                # print(nums[idx2])
                # print(nums[idx3])
                tmp = nums[idx1] + nums[idx2] + nums[idx3]
                if isDecimal(tmp):
                    answer += 1


    return answer

# print(solution(	[1, 2, 3, 4]))
print(solution([1,2,7,6,4]))
