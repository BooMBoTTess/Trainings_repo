def Solution(rows, cols, arr):
    for row in range(rows):
        arr[row].insert(0, 0)
    arr.insert(0, [0 for i in range(cols + 1)])
    dp = [[0], []]
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            if arr[row-1][col] * arr[row][col-1] * arr[row-1][col-1] == 1:
                x = dp[row-1][col-1] + 1
            else:
                x = 0
            dp[row].append(x)
        dp.append([])

    max_size = 0
    for row in range(1,len(dp)-1):
        for col in range(1, len(dp[row])):
            if dp[row][col] > max_size:
                max_size = dp[row][col]


    return max_size


if __name__ == '__main__':
    f = open('input.txt', 'r')
    rows, cols = f.readline().split(' ')
    rows = int(rows)
    cols = int(cols)
    inp = list(f.read().rstrip('\n').split('\n'))
    arr = []
    for row in inp:
        arr.append(list(map(int, row.split(' '))))

    out = Solution(rows, cols, arr)
    print(out)