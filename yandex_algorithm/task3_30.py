def dfs(graph, visited, now):
    visited[now] = True
    tmp = 0
    stack = [1]
    comp = []
    while stack:
        tmp = stack.pop()
        if not visited[tmp]:
            visited[tmp] = True
            stack.extend(graph[tmp])
            comp.append(tmp)
    print(comp)
    return 0


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

    visited = [False] * (matrix[0][0] + 1)

    dfs(graph, visited, 1)




if __name__ == '__main__':

    f = open('../test.txt', 'r')
    print(Solution(f.read().rstrip('\n')))