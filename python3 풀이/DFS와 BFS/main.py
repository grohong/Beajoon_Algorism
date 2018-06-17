from collections import deque

class dfs:

    def __init__(self, point_info, point_count):
        self.point_info = point_info
        self.point_pass = [bool()]*point_count
        self.answer = []

    def order(self, start_point):
        if self.point_pass[start_point-1]:
            return

        self.point_pass[start_point-1] = True
        self.answer.append(start_point)

        for next_point in point_info[start_point]:
            if self.point_pass[next_point-1] == False:
                self.order(next_point)

    def print_answer(self):
        for point in self.answer:
            print(point, end=' ')

        print("")

class bfs:

    def __init__(self, point_info, point_count):
        self.point_info = point_info
        self.point_pass = [bool()]*point_count
        self.answer = []

    def order(self, start_point):
        queue = deque()
        queue.append(start_point)
        self.point_pass[start_point-1] = True

        while(len(queue) != 0):
            self.answer.append(queue.popleft())

            for next_point in point_info[start_point]:
                if self.point_pass[next_point-1] == False:
                    self.point_pass[next_point-1] = True
                    queue.append(next_point)

    def print_answer(self):
        for point in self.answer:
            print(point, end=' ')

        print("")

input_setting = [int(x) for x in input().split()]

point_count = input_setting[0]
line_count = input_setting[1]
start_point = input_setting[2]

point_info = dict()

for index in range(0, line_count):
    input_tmp = [int(x) for x in input().split()]

    if point_info.get(input_tmp[0]) == None:
        point_info.setdefault(input_tmp[0], []).append(input_tmp[1])
    else:
        point_info[input_tmp[0]].append(input_tmp[1])

    if point_info.get(input_tmp[1]) == None:
        point_info.setdefault(input_tmp[1], []).append(input_tmp[0])
    else:
        point_info[input_tmp[1]].append(input_tmp[0])

answer = dfs(point_info, point_count)
answer.order(start_point)
answer.print_answer()

answer_bfs = bfs(point_info, point_count)
answer_bfs.order(start_point)
answer_bfs.print_answer()
