def MatrixToList(matrix: list) -> list:
    m, n = matrix[0][0], matrix[0][1]
    arr = [[0]] * max(m, n)
    kj = 1
    for i in range(m):
        kj += 1
        for j in range(kj, n):
            print(matrix[i], [j], i, j)
    return arr


def Solution(matrix):
    matrix = matrix.split('\n')
    matrix2 = []
    for i in matrix:
        matrix2.append(i.split(' '))
    matrix2 = [[int(i) for i in j] for j in matrix2]
    edge_list = MatrixToList(matrix2)


if __name__ == '__main__':
    f = open('../test.txt', 'r')
    print(Solution(f.read()))
