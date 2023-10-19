from typing import List


def matrix_to_graph(matrix: List):

    graph = {}
    matrix = matrix.split('\n')
    for row in range(1, len(matrix[1:])+1):
        matrix[row] = matrix[row].split(' ')
        matrix[row] = list(map(int, matrix[row]))
        tmp = []
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 1:
                tmp.append(col+1)
        graph[row] = tmp

    return graph

def dfs(graph, visited: List, now: int):
    stack = [now]
    path = []
    tmp = 0

    while len(stack) != 0:
        past = tmp
        tmp = stack.pop()
        if visited[tmp] == 0:
            path.append(tmp)
            for i in graph[tmp]:
                if i != past:
                    stack.append(i)
            visited[tmp] = 1
        else:
            return True, path
    return False, path




def solution(matrix: str):
    lenght = int(matrix.split('\n')[0])
    graph = matrix_to_graph(matrix)
    visited = [0 for i in range(lenght+1)]
    for now in range(1, lenght):
        if visited[now] != 1:
            flag, path = dfs(graph, visited, now)

    if flag:
        return f'YES\n{len(path)}\n{" ".join(map(str, path))}'
    else:
        return 'NO'


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(solution(f.read().rstrip('\n')))