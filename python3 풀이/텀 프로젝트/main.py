class solution:

    def __init__(self, graplist):
        self.graplist = graplist
        self.checkpoint = [bool()]*len(graplist)

    def getAnswer(self):
        for x in range(0, len(self.graplist)):
            self.checkpoint[x] = self.dfs(x)

        return self.checkpoint.count(False)

    def dfs(self, start):
        team = False
        tmp = [bool()]*len(graplist)

        index = start
        for _ in range(0, len(self.graplist)):
            tmp[index] = True
            index = graplist[index]-1

            if tmp[index] == True:
                if index == start:
                    
                    team = True
                break
            else:
                tmp[index] = True

        return team


testnum = int(input())

while(testnum>0):
    graphnum = int(input())
    graplist = [int(x) for x in input().split()]

    print(solution(graplist).getAnswer())

    testnum -= 1
