# def quicksort(data):
#     if len(data) < 1:
#         return data
#
#     pivot = data[0]
#     left = []
#     right = []
#
#     for x in range(1, len(data)):
#         if data[x] <= pivot:
#             left.append(data[x])
#         else:
#             right.append(data[x])
#
#     left = quicksort(left)
#     right = quicksort(right)
#     foo = [pivot]
#
#     return left + foo + right

def quicksort(data):

    if len(data) < 1:
        return data

    pivot = data[0]
    left = []
    right = []

    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]

    return left + foo + right




test1 = [6,4,1,8,9,2,7,5,3]
test2 = [6,4,2,10,9,1,7,11,5,3,0,8]

print(quicksort(test1))
print(quicksort(test2))