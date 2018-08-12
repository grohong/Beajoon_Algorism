from collections import deque

size = int(input())

tree = []
for _ in range(size):
    tree.append([])

for _ in range(size-1):
    tmp = [int(x) for x in input().split(" ")]
    tree[tmp[0]-1].append(tmp[1]-1)
    tree[tmp[1]-1].append(tmp[0]-1)

check = [False for _ in range(size)]
parent = [0 for _ in range(size)]

print(tree)
print(check)
print(parent)

queue = deque()
queue.append(0)
check[0] = True

while(len(queue) != 0):
    tmp = queue.popleft()
    for x in tree[tmp]:

        if check[x] == False:
            check[x] = True
            parent[x] = tmp
            queue.append(x)

for i, ans in enumerate(parent):
    if i==0:
        continue
    print(ans+1)