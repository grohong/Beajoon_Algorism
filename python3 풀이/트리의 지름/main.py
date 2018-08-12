from collections import deque

class Edge:

    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

    def __repr__(self):
        return "(to: %s, cost: %s)" % (self.to, self.cost)


def bfs(pointCount, tree, start):
    check = [bool()]*pointCount
    dist = [0]*pointCount
    queue = deque()

    check[start] = True
    queue.append(start)

    while(len(queue)!=0):
        tmp = queue.popleft()

        for node in tree[tmp]:
            to = node.to
            cost = node.cost

            if check[to] == False:
                dist[to] = dist[tmp] + cost
                queue.append(to)
                check[to] = True

    return dist

pointCount = int(input())
treeInfos = []

for i in range(pointCount):
    nodeInfo = [int(x) for x in input().split(" ")]
    treeInfos.append(nodeInfo)

tree = [[Edge]]*pointCount

for treeInfo in treeInfos:
    to = 0
    cost = 0

    nodeInfo = []
    start = 0
    for idx, j in enumerate(treeInfo):

        if idx == 0:
            start = j-1

        if idx%2 == 1:
            to = j-1

        if idx%2 == 0:
            cost = j
            nodeInfo.append(Edge(to, cost))

    tree[start] = nodeInfo

dist = bfs(pointCount, tree, 0)
print(max(dist))