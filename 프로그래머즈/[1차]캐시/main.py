from collections import deque

def solution(cacheSize, cities):
    answer = 0

    queue = deque()
    for city in cities:
        if str(city).lower() in queue:
            answer += 1
            queue.remove(str(city).lower())
            queue.append(str(city).lower())
        else:
            answer += 5

            if cacheSize == 0:
                continue

            if len(queue) < cacheSize:
                queue.append(str(city).lower())
            else:
                queue.popleft()
                queue.append(str(city).lower())


    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))