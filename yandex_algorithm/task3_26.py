def Solution(matrix):
    matrix = matrix.split('\n')
    matrix = [elem.split(' ') for elem in matrix]
    matrix = [list(map(int, elem)) for elem in matrix]
    index = matrix[0]
    matrix = matrix[1:]

    dp = [[matrix[0][0]]]
    for row in range(1, index[1]):
        dp.append([matrix[row][0]+dp[row-1][0]])
    for col in range(1, index[0]):
        dp[0].append(matrix[0][col] + dp[0][col-1])


    for row in range(1, index[0]):
        for col in range(1, index[1]):
            tmp = min(dp[row-1][col], dp[row][col-1]) + matrix[row][col]
            dp[row].append(tmp)


    return dp[index[0]-1][index[1]-1]
if __name__ == '__main__':
    f = open('../input.txt', 'r')
    print(Solution(f.read()))
