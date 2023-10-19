from typing import List


def way(dp, index) -> List:
    path = []
    row, col = (index[0], index[1])
    while (row != 1) or (col != 1):
        if dp[row - 1][col] > dp[row][col - 1]:
            path.insert(0, 'D')
            row -= 1
        else:
            path.insert(0, 'R')
            col -= 1
    return path


def Solution(matrix):
    matrix = matrix.split('\n')
    matrix = [elem.split(' ') for elem in matrix]
    matrix = [list(map(int, elem)) for elem in matrix]
    index = matrix[0]
    matrix = matrix[1:]
    matrix.insert(0, [0 for i in range(index[1])])
    for row in range(index[0] + 1):
        matrix[row].insert(0, 0)

    dp = [[-1] for i in range(index[0] + 1)]
    for i in range(index[1]):
        dp[0].append(-1)

    for row in range(1, index[0] + 1):
        for col in range(1, index[1] + 1):
            if row == 1 and col == 1:
                dp[row].append(matrix[row][col])
            else:
                min_dp = max(dp[row - 1][col], dp[row][col - 1])
                tmp = min_dp + matrix[row][col]
                dp[row].append(tmp)

    return f"{dp[index[0]][index[1]]}\n{' '.join(way(dp, index))}"


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))
