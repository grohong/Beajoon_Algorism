def solution(n,signs):
    answer = signs
    for start in range(n):
        queue = [start]
        visited = set()
        while queue:
            s = queue.pop(0)
            for node, connected in enumerate(signs[s]):
                if connected == 1 and node not in visited:
                    queue.append(node)
                    visited.add(node)
        for node in visited:
            answer[start][node] = 1
    return answer


print(solution(3, [[0,1,0],[0,0,1],[1,0,0]]))
# print(solution(3, [[0,0,1],[0,0,1],[0,1,0]]))