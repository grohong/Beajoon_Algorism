def preorder(tree, root):
    if root == -1:
        return

    print(chr(root+ ord('A')), end="")
    preorder(tree, tree[root][0])
    preorder(tree, tree[root][1])

def inorder(tree, root):
    if root == -1:
        return

    inorder(tree, tree[root][0])
    print(chr(root + ord('A')), end="")
    inorder(tree, tree[root][1])

def postorder(tree, root):
    if root == -1:
        return

    postorder(tree, tree[root][0])
    postorder(tree, tree[root][1])
    print(chr(root + ord('A')), end="")

size = int(input())

tree = [[None]*2 for _ in range(size)]

for _ in range(size):
    tmp = [x for x in input().split()]
    index = ord(tmp[0]) - ord('A')

    if tmp[1] == ".":
        tree[index][0] = -1
    else:
        tree[index][0] = ord(tmp[1]) - ord('A')

    if tmp[2] == ".":
        tree[index][1] = -1
    else:
        tree[index][1] = ord(tmp[2]) - ord('A')

print(tree)
preorder(tree, 0)
print()
inorder(tree, 0)
print()
postorder(tree, 0)