def dfs(graph, visited, now, count_edge, sorted_list):
    stack = [now]
    while len(stack) != 0:
        tmp = stack.pop()
        if (visited[tmp] == 0) and (count_edge[tmp] == 0):
            sorted_list.append(tmp)
            stack.extend(graph[tmp])
            visited[tmp] = 1
            for i in graph[tmp]:
                count_edge[i] -= 1

def solution(edges):
    edges = edges.split('\n')
    for i in range(len(edges)):
        edges[i] = edges[i].split(' ')
        edges[i] = list(map(int, edges[i]))

    graph = {key: [] for key in range(1, edges[0][0] + 1)}
    count_edge = [0 for i in range(edges[0][0] + 1)]
    for i in range(1, edges[0][1] + 1):
        graph[edges[i][0]].append(edges[i][1])
        count_edge[edges[i][1]]+= 1

    visited = [0 for i in range(edges[0][0] + 1)]
    sorted_list = []
    for i in range(1, len(visited)):
        if (count_edge[i] == 0) and (visited[i] == 0):
            dfs(graph, visited, i, count_edge, sorted_list)

    for i in range(1, len(visited)):
        if visited[i] == 0:
            return '-1'
    return ' '.join(map(str, sorted_list))






if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(solution(f.read().rstrip('\n')))