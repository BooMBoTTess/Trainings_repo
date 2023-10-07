def dfs(graph, visited, now, comp):
    tmp = 0
    stack = [now]
    comp_elements = []
    while stack:
        tmp = stack.pop()
        if not visited[tmp]:
            visited[tmp] = comp
            stack.extend(graph[tmp])
            comp_elements.append(tmp)
    return comp, comp_elements

def output(comp, visited):
    arr = {i : [] for i in range(1, comp)}
    for i in range(1, len(visited)):
        arr[visited[i]].append(i)
    return arr

def Solution(matrix):
    matrix = matrix.split('\n')
    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(' ')
        matrix[i] = [int(num) for num in matrix[i]]
    # print(matrix)

    graph = {i: [] for i in range(1, matrix[0][0] + 1)}

    for i in range(1, len(matrix)):
        graph[matrix[i][0]].append(matrix[i][1])
        graph[matrix[i][1]].append(matrix[i][0])

    visited = [0] * (matrix[0][0] + 1)
    comp = 1
    ans = []
    for key in graph.keys():
        if visited[key] == 0:
            ans.append(dfs(graph, visited, key, comp))
            comp += 1
    comp_list = output(comp, visited)
    fstring = ''
    print(comp-1)
    for key, value in comp_list.items():

        fstring += str(key) + '\n' + ' '.join(map(str, value)) + '\n'
    return fstring

if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))
