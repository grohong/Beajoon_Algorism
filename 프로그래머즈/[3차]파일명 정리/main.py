class File_name:

    def __init__(self, head, number, tail=None):
        self.head = head
        self.number = number
        self.tail = tail

    def __repr__(self):
        return """
        HEAD: %s,
        NUMBER: %s,
        TAIL: %s
        """ %(self.head, self.number, self.tail)

    def __str__(self):
        return "%s%s%s" % (self.head, self.number, self.tail)

    def __lt__(self, other):
        return ((self.head.lower(), int(self.number)) < (other.head.lower(), int(other.number)))

def solution(files):
    answer = []
    file_names = []

    for file in files:
        head = ""
        number = ""
        tail = ""

        head_flag = False
        number_flag = False
        for string in file:
            if head_flag == False and (ord("0")>ord(string) or ord(string)>ord("9")):
                head += string

            elif number_flag == False and (ord("0")<=ord(string)<=ord("9")) and len(number)<5:
                number += string
                head_flag = True

            elif head_flag:
                tail += string
                number_flag = True

        file_names.append(File_name(head, number, tail))

    # print(file_names)
    for file_name in sorted(file_names):
        answer.append(str(file_name))


    return answer


in_example1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
in_example2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
in_example3 = ["img2.JPG","img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF"]
in_example4 = ["img2bbb.JPG","img12.png", "img10.png", "img02aaa.png", "img1.png", "IMG01.GIF"]
in_example5 = ["img020001.JPG","img12.png", "img10.png", "img020000.png", "img1.png", "IMG01.GIF"]
print(solution(in_example2))
print(solution(in_example1))
print(solution(in_example3))
print(solution(in_example4))
print(solution(in_example5))