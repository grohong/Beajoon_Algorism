class Time:

    def __init__(self, time):
        time_list = str(time).split(" ")
        self.end_time_day = time_list[0]

        day_list = time_list[1].split(":")
        self.end_hour = int(day_list[0])
        self.end_min = int(day_list[1])
        self.end_sec = float(format(float(day_list[2]), "0.3f"))

        self.term = time_list[2].replace("s", "")
        self.set_start_time()

    def set_start_time(self):
        self.start_sec = float(format((float(self.end_sec) - float(self.term)), "0.3f"))
        self.start_min = self.end_min
        self.start_hour = self.end_hour
        self.start_time_day = self.end_time_day

        if float(self.start_sec) < 0:
            self.start_sec += 60.000
            self.start_sec = float(format(self.end_sec, "0.3f"))
            self.start_min = self.end_min - 1

        if int(self.start_min) < 0:
            self.start_min += 60
            self.start_hour = self.end_hour - 1

        if int(self.start_hour) < 0:
            self.start_time_day = "2016-09-14"
            self.start_hour += 60

        print("==================")
        print(self.term)
        print("+++++++++")
        print(self.start_time_day)
        print(self.start_hour)
        print(self.start_min)
        print(self.start_sec)
        print("-------------")
        print(self.end_time_day)
        print(self.end_hour)
        print(self.end_min)
        print(self.end_sec)

    def __contains__(self, item):
        # if self.start_hour == item.start_hour and self.start_min == item.start_min and self.start_sec == item.start_sec:
        #     return self.start_time_day.split("-")[0] <= item.start_time_day.split("-")[0] <= self.end_time_day.split("-")[0]
        # elif self.start_time_day == item.start_time_day and self.start_hour == item.start_hour:
        #     return self.start_min <= item.start_min <= self.end_min
        # elif self.start_time_day == item.start_time_day:
        #     return self.start_hour <= item.start_hour <= self.start_hour
        # else:
        #     return self.start_time_day.split("-")[0] <= other.start_time_day.split("-")[0] <=

        if self.start_time_day == item.start_time_day and self.start_hour == item.start_hour and self.start_min == item.start_min:
            return float(self.start_sec) <= float(item.start_sec) <= float(self.end_sec)
        elif self.start_time_day == item.start_time_day and self.start_hour == item.start_hour:
            return self.start_min <= item.start_min <= self.end_min
        elif self.start_time_day == item.start_time_day:
            return self.start_hour <= item.start_hour <= self.start_hour
        else:
            return self.start_time_day.split("-")[0] <= item.start_time_day.split("-")[0] <= self.end_time_day.split("-")[0]

    def __le__(self, other):
        if self.start_time_day == other.start_time_day and self.start_hour == other.start_hour and self.start_min == other.start_min:
            return float(self.start_sec) <= float(other.start_sec)
        elif self.start_time_day == other.start_time_day and self.start_hour == other.start_hour:
            return self.start_min <= other.start_min
        elif self.start_time_day == other.start_time_day:
            return self.start_hour <= other.start_hour
        else:
            return self.start_time_day.split("-")[0] <= other.start_time_day.split("-")[0]

    def __ge__(self, other):
        if self.start_time_day == other.start_time_day and self.start_hour == other.start_hour and self.start_min == other.start_min:
            return float(self.start_sec) >= float(other.start_sec)
        elif self.start_time_day == other.start_time_day and self.start_hour == other.start_hour:
            return self.start_min >= other.start_min
        elif self.start_time_day == other.start_time_day:
            return self.start_hour >= other.start_hour
        else:
            return self.start_time_day.split("-")[0] >= other.start_time_day.split("-")[0]

    def __lt__(self, other):
        if self.start_time_day == other.start_time_day and self.start_hour == other.start_hour and self.start_min == other.start_min:
            return float(self.start_sec) < float(other.start_sec)
        elif self.start_time_day == other.start_time_day and self.start_hour == other.start_hour:
            return self.start_min < other.start_min
        elif self.start_time_day == other.start_time_day:
            return self.start_hour < other.start_hour
        else:
            return self.start_time_day.split("-")[0] < other.start_time_day.split("-")[0]

    def __repr__(self):
        return "%s %s:%s:%s %s" % (self.start_time_day, str(self.start_hour).zfill(2), str(self.start_min).zfill(2), self.start_sec, self.term)

def solution(lines):
    answer = 0

    times = []
    for line in lines:
        times.append(Time(line))

    # sort_times = sorted(times)

    for time in times:
        tmp = 0
        for tmp_time in times:
            if tmp_time in time:
                tmp += 1

        if tmp > answer:
            answer = tmp


    return answer

# print(solution(["2016-09-15 20:59:57.421 0.351s",
#                 "2016-09-15 20:59:58.233 1.181s",
#                 "2016-09-15 20:59:58.299 0.8s",
#                 "2016-09-15 20:59:58.688 1.041s",
#                 "2016-09-15 20:59:59.591 1.412s",
#                 "2016-09-15 21:00:00.464 1.466s",
#                 "2016-09-15 21:00:00.741 1.581s",
#                 "2016-09-15 21:00:00.748 2.31s",
#                 "2016-09-15 21:00:00.966 0.381s",
#                 "2016-09-15 21:00:02.066 2.62s"]))

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))

# print(solution(["2016-09-15 00:00:1.000 2.002s"]))