def dfs(graph, visited, now):
    color = 1
    visited[now] = color
    stack = [now]
    while len(stack) != 0:
        tmp = stack.pop()
        color = visited[tmp]
        for i in graph[tmp]:
            if visited[i] == visited[tmp]:
                return False
            elif visited[i] == 0:
                visited[i] = 3 - color
                stack.append(i)

    return True




def solution(edges):
    edges = edges.split('\n')
    for i in range(len(edges)):
        edges[i] = edges[i].split(' ')
        edges[i] = list(map(int, edges[i]))

    graph = {key: [] for key in range(1, edges[0][0] + 1)}
    for i in range(1, edges[0][1]+1):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])


    visited = [0 for i in range(edges[0][0] + 1)]
    for i in range(1, len(visited)):
        if visited[i] == 0:
            flag = dfs(graph, visited, i)
            if not flag:
                return 'NO'
    return 'YES'



if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        print(solution(f.read().strip('\n')))
