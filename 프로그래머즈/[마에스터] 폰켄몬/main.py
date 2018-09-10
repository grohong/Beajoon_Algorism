def solution(nums):
    answer = 0

    sort_num = int(len(nums)/2)
    set_nums = set(nums)

    if len(set_nums) > sort_num:
        answer = sort_num
    else:
        answer = len(set_nums)

    return answer