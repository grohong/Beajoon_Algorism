from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s %s" % (self.x, self.y)

def bfs(array, array_checker, x, y, cnt, array_size):
    queue = deque()
    queue.append(point(x, y))

    array_checker[y][x] = cnt

    while(len(queue) != 0):
        new_point = queue.popleft()
        x = new_point.x
        y = new_point.y

        for k in range(0, 4):
            new_x = x+dx[k]
            new_y = y+dy[k]
            if 0 <= new_x and new_x < array_size and 0<= new_y and new_y < array_size:
                if array[new_y][new_x] == 1 and array_checker[new_y][new_x] == 0:
                    queue.append(point(new_x, new_y))
                    array_checker[new_y][new_x] = cnt



array_size = int(input())
array = []

for _ in range(0, array_size):
    tmp = [int(x) for x in input()]
    array.append(tmp)

array_checker = [[0]*array_size for i in range(array_size)]
cnt = 0

for y in range(0, array_size):
    for x in range(0, array_size):
        if array[y][x] == 1 and array_checker[y][x] == 0:
            cnt += 1
            bfs(array, array_checker, x, y, cnt, array_size)

ans = [int()]*cnt
for y in range(0, array_size):
    for x in range(1, cnt+1):
        ans[x-1] += array_checker[y].count(x)

ans.sort()
print(cnt)
for an in ans:
    print(an)
