class subject:

    def __init__(self, name, guk, eng, su):
        self.name = name
        self.guk = guk
        self.eng = eng
        self.su = su

    def __str__(self):
        return "%s" % (self.name)

    def __lt__(self, other):
        if self.guk == other.guk and self.eng == other.eng and self.su == other.su:
            return self.name < other.name
        elif self.guk == other.guk and self.eng == other.eng:
            return self.su > other.su
        elif self.guk == other.guk:
            return self.eng < other.eng
        else:
            return self.guk > other.guk

input_count = int(input())
subjects = list()

for index in range(0, input_count):
    input_list = [x for x in input().split()]
    subjects.append(subject(input_list[0], int(input_list[1]), int(input_list[2]), int(input_list[3])))

subjects.sort()

for subject in subjects:
    print(subject)

