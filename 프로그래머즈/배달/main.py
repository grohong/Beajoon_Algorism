def dfs(roads, start, cost, visited):

    tmp_visited = visited
    for idx, road_cost in enumerate(roads[start]):
        if road_cost != 0 and cost - road_cost > 0 and (idx+1 not in tmp_visited or tmp_visited[idx+1] < cost - road_cost):
            tmp_visited[idx+1] = cost - road_cost
            tmp_visited = dfs(roads, idx+1, cost - road_cost, visited)
        elif road_cost != 0 and cost - road_cost == 0:
            tmp_visited[idx + 1] = 0

    return tmp_visited



def solution(N, road, K):
    answer = 0

    road_info = dict()
    for info in road:
        if info[0] not in road_info:
            road_info[info[0]] = [0 for _ in range(N)]
            road_info[info[0]][info[1] - 1] = info[2]
        elif road_info[info[0]][info[1] - 1] == 0 or road_info[info[0]][info[1] - 1] > info[2]:
            road_info[info[0]][info[1] - 1] = info[2]

        if info[1] not in road_info:
            road_info[info[1]] = [0 for _ in range(N)]
            road_info[info[1]][info[0] - 1] = info[2]
        elif road_info[info[1]][info[0] - 1] == 0 or road_info[info[1]][info[0] - 1] > info[2]:
            road_info[info[1]][info[0] - 1] = info[2]

    cost = K
    for start in road_info:
        visited = dict()
        visited[1] = 0
        visited = dfs(road_info, start, cost, visited)

        if answer < len(visited):
            answer = len(visited)
            break


    return answer


# print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))