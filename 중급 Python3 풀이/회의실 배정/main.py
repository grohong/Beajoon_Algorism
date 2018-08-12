class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.end == other.end:
            return self.start < other.start

        return self.end < other.end

    def __repr__(self):
        return "(start time: %s, end time: %s)" % (self.start, self.end)


meeting_count = int(input())

meetings = []
for _ in range(meeting_count):
    meeting = [int(x) for x in input().split()]
    meetings.append(Meeting(meeting[0], meeting[1]))

meetings.sort()

now = 0
ans = 0

for meeting in meetings:
    if now <= meeting.start:
        now = meeting.end
        ans += 1

print(ans)