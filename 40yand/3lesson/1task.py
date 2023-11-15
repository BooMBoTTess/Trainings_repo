def smegn(n, matrix):
    result = []
    for row in range(n):
        result.append([])
        for col in range(n):
            if (row != col) and matrix[row][col] != -1:
                result[row].append([col, matrix[row][col]])
    return result


def add_to_stack(stack, elem, dist, visited):
    if len(stack) != 0:
        for i in range(len(stack)):
            if dist[stack[i]] >= dist[elem] and not visited[elem]:
                stack.insert(i, elem)
                return 1
    if not visited[elem]:
        stack.append(elem)

def deich(matrix, elem, dist, stack, visited):
    targ_m = matrix[elem]
    for neigh, d in targ_m:
        dist[neigh] = min(d + dist[elem], dist[neigh])
        add_to_stack(stack, neigh, dist, visited)



def Solution(n, S1, S2, matrix):
    visited = [0 for i in range(n)]
    dist = [100000 for i in range(n)]
    dist[S1] = 0
    stack = [S1]
    while visited[S2] == 0 and stack != []:
        elem = stack.pop(0)
        visited[elem] = 1
        deich(matrix, elem, dist, stack, visited)
    return dist





if __name__ == '__main__':
    with open('input.txt','r') as f:
        n, S1, S2 = list(map(int, f.readline().rstrip('\n').split(' ')))
        if S1 == S2:
            print(0)
        else:
            matrix = f.read().rstrip('\n').split('\n')
            matrix2 = []
            S1 -= 1
            S2 -= 1
            for row in matrix:
                matrix2.append(list(map(int, row.split(' '))))
            matrix = matrix2
            m_sm = smegn(n,matrix)
            dist_sol = Solution(n, S1, S2, m_sm)[S2]
            if dist_sol == 100000:
                print(-1)
            else:
                print(dist_sol)
