from collections import deque

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class solution:
    def __init__(self, array, size):
        self.array = array
        self.size = size

        self.array_checker = []
        for y in range(self.size):
            tmp = [-1]*self.size
            self.array_checker.append(tmp)

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

        self.setarray()

    def setarray(self):
        cnt = 1
        for y in range(self.size):
            for x in range(self.size):
                if self.array[y][x] == 1 and self.array_checker[y][x] == -1:
                    self.setbfs(y, x, cnt)
                    cnt += 1


    def setbfs(self, y, x, cnt):
        queue = deque()
        queue.append(point(x, y))

        while(len(queue) != 0):
            tmp_point = queue.popleft()

            for direct_x, direct_y in zip(self.dx, self.dy):
                tmp_x = tmp_point.x + direct_x
                tmp_y = tmp_point.y + direct_y

                if 0<=tmp_x and tmp_x<size and 0<=tmp_y and tmp_y<size:
                    if self.array[tmp_y][tmp_x] != 0 and self.array_checker[tmp_y][tmp_x] == -1:
                        queue.append(point(tmp_x, tmp_y))
                        self.array_checker[tmp_y][tmp_x] = 0
                        self.array[tmp_y][tmp_x] = cnt




size = int(input())

array = []
for y in range(size):
    tmp = [int(x) for x in input().split(" ")]
    array.append(tmp)

solution(array, size)
