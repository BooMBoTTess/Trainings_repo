def dfs(graph, visited, now):
    tmp = 0
    stack = [now]
    group_student = 1
    while stack:
        past = tmp
        tmp = stack.pop()
        if visited[tmp] == 0:
            visited[tmp] = group_student
            stack.extend(graph[tmp])
            group_student = 3 - group_student
        else:
            if visited[tmp] == visited[past]:
                return False
    return True

def Solution(matrix):
    matrix = matrix.split('\n')
    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(' ')
        matrix[i] = [int(num) for num in matrix[i]]

    graph = {i: [] for i in range(1, matrix[0][0] + 1)}

    for i in range(1, len(matrix)):
        graph[matrix[i][0]].append(matrix[i][1])
        graph[matrix[i][1]].append(matrix[i][0])

    visited = [0] * (matrix[0][0] + 1)

    for key in graph.keys():
        if visited[key] == 0:
            is_accept = dfs(graph, visited, key)
            if not is_accept:
                return 'NO'
    return 'YES'



if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))
