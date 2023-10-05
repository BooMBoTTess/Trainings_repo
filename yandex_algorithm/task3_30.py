def dfs(graph, visited, now):
    visited[now] = True
    for neibor in graph[now]:
        if not visited[neibor]:
            dfs(graph, visited, neibor)

def Solution(matrix):
    matrix = matrix.split('\n')
    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(' ')
        matrix[i] = [int(num) for num in matrix[i]]
    #print(matrix)

    graph = {}
    for i in range(matrix[0][0] + 1):
        graph[i] = []
    for i in range(1, len(matrix)):
        graph[matrix[i][0]].append(matrix[i][1])
        graph[matrix[i][1]].append(matrix[i][0])

    visited = [0] * (matrix[0][0] + 1)
    dfs(graph, visited, 1)

    answer = []
    for i in range(len(visited)):
        if visited[i]:
            answer.append(i)
    return f'{sum(visited)}\n{" ".join(map(str, answer))}'



if __name__ == '__main__':
    f = open('../input.txt', 'r')
    print(Solution(f.read()))