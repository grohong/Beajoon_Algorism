class people:

    def __init__(self, age, name, order):
        self.age = age
        self.name = name
        self.order = order

    def __lt__(self, other):
        if self.age == other.age:
            return self.order < other.order
        else:
            return self.age < other.age

    def __str__(self):
        return "%s %s" % (self.age, self.name)

input_count = int(input())
input_peoples = list()

for index in range(0, input_count):
    input_list = [x for x in input().split()]
    input_peoples.append(people(int(input_list[0]), input_list[1], index))

input_peoples.sort()

for people in input_peoples:
    print(people)