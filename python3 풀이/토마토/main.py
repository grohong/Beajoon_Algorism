from collections import deque

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("%s, %s", x, y)

class solution:
    def __init__(self, array, xsize, ysize):
        self.array = array
        self.xsize = xsize
        self.ysize = ysize

        self.array_checker = []
        for y in range(ysize):
            tmp = [0]*xsize
            self.array_checker.append(tmp)

        for y in range(self.ysize):
            for x in range(self.xsize):
                if self.array[y][x] == -1:
                    self.array_checker[y][x] = -1

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def getanswer(self):
        queue = deque()

        zero = 0
        for y in range(self.ysize):
            zero += self.array[y].count(0)

        if zero == 0:
            return 0

        for y in range(self.ysize):
            for x in range(self.xsize):
                if self.array[y][x] == 1:
                    queue.append(point(x, y))
                    self.array_checker[y][x] = 1

        while(len(queue) != 0):
            queue_index = len(queue)

            print("---------------------------------------")
            for y in range(self.ysize):
                print(self.array_checker[y])

            for index in range(queue_index):
                tmp_point = queue.popleft()

                for xdirection, ydirection in zip(self.dx, self.dy):
                    tmp_x = tmp_point.x + xdirection
                    tmp_y = tmp_point.y + ydirection

                    if 0<=tmp_x and tmp_x<self.xsize and 0<=tmp_y and tmp_y<self.ysize:
                        if self.array[tmp_y][tmp_x] == 0 and self.array_checker[tmp_y][tmp_x] == 0:
                            queue.append(point(tmp_x, tmp_y))
                            self.array_checker[tmp_y][tmp_x] = self.array_checker[tmp_point.y][tmp_point.x]+1


        ans = max(max(self.array_checker))-1

        for y in range(self.ysize):
            if self.array_checker[y].count(0) != 0:
                return -1

        return ans



size = [int(x) for x in input().split()]

xsize = size[0]
ysize = size[1]

array = []
for y in range(ysize):
    tmp = [int(x) for x in input().split()]
    array.append(tmp)


print(solution(array, xsize, ysize).getanswer())