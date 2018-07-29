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

        print("---------------------------")
        for y in range(self.size):
            print(self.array[y])

        print("---------------------------")
        for y in range(self.size):
            print(self.array_checker[y])

    def setarray(self):
        cnt = 1
        for y in range(self.size):
            for x in range(self.size):
                if self.array[y][x] == 1 and self.array_checker[y][x] == -1:
                    self.setbfs(y, x, cnt)
                    cnt += 1


    def setbfs(self, y, x, cnt):
        queue = deque()
        self.array[y][x] = cnt
        self.array_checker[y][x] = 0
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

    def getanswer(self):
        queue2 = deque()

        for y in range(self.size):
            for x in range(self.size):
                if self.array[y][x] != 0:
                    queue2.append(point(x, y))

        while(len(queue2) != 0):
            tmp_point = queue2.popleft()

            for direct_x, direct_y in zip(self.dx, self.dy):
                tmp_x = tmp_point.x + direct_x
                tmp_y = tmp_point.y + direct_y

                if 0 <= tmp_x and tmp_x < size and 0 <= tmp_y and tmp_y < size:
                    if self.array[tmp_y][tmp_x] == 0:
                        self.array[tmp_y][tmp_x] = self.array[tmp_point.y][tmp_point.x]
                        self.array_checker[tmp_y][tmp_x] = self.array_checker[tmp_point.y][tmp_point.x]+1
                        queue2.append(point(tmp_x, tmp_y))

        print("---------------------------")
        for y in range(self.size):
            print(self.array[y])

        print("---------------------------")
        for y in range(self.size):
            print(self.array_checker[y])

        ans = -1
        for y in range(self.size):
            for x in range(self.size):
                for direct_x, direct_y in zip(self.dx, self.dy):
                    tmp_x = x + direct_x
                    tmp_y = y + direct_y

                    if 0 <= tmp_x and tmp_x < size and 0 <= tmp_y and tmp_y < size:
                        if self.array[tmp_y][tmp_x] != self.array[y][x]:
                            if ans == -1 or ans > self.array_checker[tmp_y][tmp_x] + self.array_checker[y][x]:
                                ans = self.array_checker[tmp_y][tmp_x] + self.array_checker[y][x]

        return ans

size = int(input())

array = []
for y in range(size):
    tmp = [int(x) for x in input().split(" ")]
    array.append(tmp)

print(solution(array, size).getanswer())
