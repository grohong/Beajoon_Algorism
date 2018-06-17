from collections import deque

class bfs:
    def __init__(self, line_info, point_checker):
        self.line_info = line_info
        self.point_checker = point_checker
        self.queue = deque()

    def check(self, start_point):
        if self.point_checker[start_point] == True:
            return

        self.queue.append(start_point)
        self.point_checker[start_point] = True

        self.search()

    def search(self):
        while(len(self.queue) != 0):
            tmp = self.queue.popleft()

            for next_point in self.line_info[tmp]:
                if point_checker[next_point] == False:
                    self.point_checker[next_point] = True
                    self.queue.append(next_point)


input_setting = [int(x) for x in input().split()]

point_count = input_setting[0]
line_count = input_setting[1]

line_info = dict()

for index in range(0, line_count):
    input_tmp = [int(x) for x in input().split()]

    if line_info.get(input_tmp[0]) == None:
        line_info.setdefault(input_tmp[0], []).append(input_tmp[1])
    else:
        line_info[input_tmp[0]].append(input_tmp[1])

    if line_info.get(input_tmp[1]) == None:
        line_info.setdefault(input_tmp[1], []).append(input_tmp[0])
    else:
        line_info[input_tmp[1]].append(input_tmp[0])

point_checker = [bool()]*(point_count+1)
bfs_searcher = bfs(line_info, point_checker)
answer = 0

for index in range(1, len(point_checker)):
    if bfs_searcher.point_checker[index] == False:
        bfs_searcher.check(index)
        answer += 1

print(answer)
