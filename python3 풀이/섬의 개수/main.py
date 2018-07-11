from collections import deque

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s %s" % (self.x, self.y)


def bfs(array, array_checker, x, y, cnt, x_size, y_size):
    queue = deque()
    queue.append(point(x, y))

    array_checker[y][x] = cnt

    while(len(queue) != 0):
        tmp_point = queue.popleft()
        x = tmp_point.x
        y = tmp_point.y

        for k in range(8):
            tmp_x = x+dx[k]
            tmp_y = y+dy[k]

            if 0 <= tmp_x and tmp_x < x_size and 0 <= tmp_y and tmp_y < y_size:
                if array[tmp_y][tmp_x] == 1 and array_checker[tmp_y][tmp_x] == 0:
                    queue.append(point(tmp_x, tmp_y))
                    array_checker[tmp_y][tmp_x] = cnt



while(True):
    size = [int(x) for x in input().split()]

    if size.count(0) == 2:
        break

    x_size = size[0]
    y_size = size[1]
    array = []

    for _ in range(y_size):
        tmp = [int(x) for x in input().split()]
        array.append(tmp)
    array_checker = [[0]*x_size for _ in range(y_size)]

    cnt = 0
    for y in range(y_size):
        for x in range(x_size):
            if array[y][x] == 1 and array_checker[y][x] == 0:
                cnt += 1
                bfs(array, array_checker, x, y, cnt, x_size, y_size)

    print(cnt)
