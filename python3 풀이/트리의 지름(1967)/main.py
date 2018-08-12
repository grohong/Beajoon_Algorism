from collections import deque

class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

    def __repr__(self):
        return "(to: %s, cost: %s)"%(self.to, self.cost)

def bfs(nodeCount, lastNode, tree, start):
    check = [bool()]*nodeCount
    dist = [0]*nodeCount
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
                if to < lastNode:
                    queue.append(to)
                check[to] = True

    return dist



nodeCount = int(input())

nodeInfos = []
for _ in range(nodeCount-1):
    node = [int(x) for x in input().split(" ")]
    nodeInfos.append(node)

lastNode = len(nodeInfos)-1
treeInfos = [[] for _ in range(nodeInfos[lastNode][0])]

for nodeInfo in nodeInfos:
    treeInfos[nodeInfo[0]-1].append(Edge(nodeInfo[1]-1, nodeInfo[2]))

print(treeInfos)
dist = bfs(nodeCount, nodeInfos[lastNode][0], treeInfos, 0)
print(dist)