class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s %s" % (self.x, self.y)

    def __lt__(self, other):
        if self.x == other.x:
            return self.y <= other.y
        else:
            return self.x <= other.y

input_count = int(input())
input_points = list()

for index in range(0, input_count):
    input_list = [int(x) for x in input().split()]
    input_points.append(point(input_list[0], input_list[1]))

input_points.sort()

for input_point in input_points:
    print(input_point)
