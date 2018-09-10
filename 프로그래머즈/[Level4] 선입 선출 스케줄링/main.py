class Cpu:
    def __init__(self, time):
        self.work = False
        self.time = time
        self.work_time = 0

    def __repr__(self):
        return "time: %s {work: %s, work_time: %s}" % (self.time, self.work, self.work_time)

def solution(n, cores):

    CPUs = []
    CPUs_work = [False for _ in range(len(cores))]
    for core in cores:
        CPUs.append(Cpu(core))

    intent = 0
    while(True):
        if CPUs_work.count(False) != 0:
            idx = CPUs_work.index(False)
            CPUs_work[idx] = True
            CPUs[idx].work = True
            intent += 1

            if intent == n:
                return idx+1
        else:
            for cpu_idx, CPU in enumerate(CPUs):
                CPU.work_time += 1

                if CPU.work_time == CPU.time:
                    CPU.work = False
                    CPU.work_time = 0
                    CPUs_work[cpu_idx] = False



print(solution(6, [1,2,3]))