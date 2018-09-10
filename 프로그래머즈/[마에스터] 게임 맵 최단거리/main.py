from collections import deque

class Point:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __repr__(self):
        return "x: %s, y: %s, cost: %s" % (self.x, self.y, self.cost)

def bfs(maps, dx, dy):
    m = len(maps)
    n = len(maps[0])

    cach = [[0 for _ in range(n)] for _ in range(m)]
    queue = deque()
    queue.append(Point(0,0,1))
    cach[0][0] = 1

    while(len(queue)):
        tmp_point = queue.popleft()

        for x, y in zip(dx, dy):
            if (0 <= tmp_point.x + x <= n-1 and 0 <= tmp_point.y + y <= m-1) and maps[tmp_point.y+y][tmp_point.x+x] == 1 and cach[tmp_point.y+y][tmp_point.x+x] == 0:
                queue.append(Point(tmp_point.x+x, tmp_point.y+y, tmp_point.cost+1))
                if cach[tmp_point.y+y][tmp_point.x+x] == 0 or cach[tmp_point.y+y][tmp_point.x+x] > tmp_point.cost+1:
                    cach[tmp_point.y + y][tmp_point.x + x] = tmp_point.cost+1

    return cach




def solution(maps):
    answer = -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cach = bfs(maps, dx, dy)

    if cach[len(maps)-1][len(maps[0])-1] != 0:
        answer = cach[len(maps)-1][len(maps[0])-1]

    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))