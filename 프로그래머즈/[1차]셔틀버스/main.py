class Time:

    def __init__(self, time):
        times = time.split(":")
        self.hour = int(times[0])
        self.min = int(times[1])

    def add_time(self, time):
        self.min += time

        if int(self.min/60) != 0:
            self.hour += int(self.min/60)
            self.min = int(self.min % 60)

        if self.min == -1:
            self.min = 59
            self.hour -= 1

    def __str__(self):
        return "%s:%s" % (str(self.hour).zfill(2), str(self.min).zfill(2))

    def __repr__(self):
        return "%s:%s" % (str(self.hour).zfill(2), str(self.min).zfill(2))

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.min < other.min
        else:
            return self.hour < other.hour

    def __eq__(self, other):
        return str(self) == str(other)


def solution(n, t, m, timetable):
    answer = ''

    bus_num = n
    bus_term = t
    bus_person = m

    start_bus_time = Time("09:00")

    times = []
    for time in timetable:
        times.append(Time(time))

    times = sorted(times)

    tmp_time = Time("00:00")
    full_flag = False
    tmp_person = 0
    idx = 0
    while(True):
        if len(times) == idx:
            break

        time = times[idx]

        if bus_num == 1:
            if full_flag == False and (start_bus_time > time or start_bus_time == time):
                tmp_person += 1
                tmp_time = time
                idx += 1

                if bus_person == tmp_person:
                    full_flag = True
                    break
            else:
                break

        else:
            if start_bus_time > time or start_bus_time == time:
                if tmp_person == bus_person:
                    start_bus_time.add_time(bus_term)
                    tmp_person = 0
                    bus_num -= 1
                else:
                    tmp_person += 1
                    idx += 1
            else:
                start_bus_time.add_time(bus_term)
                bus_num -= 1
                tmp_person = 0




    if full_flag == False:
        answer = str(start_bus_time)
    elif full_flag == True:
        tmp_time.add_time(-1)
        answer = str(tmp_time)

    return answer



# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03", "08:58"]))
# print(solution(2, 60, 2, ["08:00", "08:13", "08:14", "10:00"]))
print(solution(2, 1, 1, ["09:02", "00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(1, 1, 1, ["09:01"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(10, 60, 5, ["09:01","09:01", "09:01", "09:01", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))