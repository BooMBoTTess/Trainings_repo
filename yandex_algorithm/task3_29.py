def Solution(matrix):
    matrix = list(map(int, matrix.split('\n')))
    days = matrix[0]
    matrix = matrix
    coupons = len([i for i in matrix if i > 100])

    dp = [[10000 for i in range(coupons + 2)]]
    for i in range(days):
        dp.append([10000 for i in range(coupons + 3)])
    if matrix[1] <= 100:
        dp[1][1] = matrix[1]
    else:
        dp[1][2] = matrix[1]

    for day in range(2, days + 1):
        for coupon in range(1, coupons + 2):
            if (matrix[day] <= 100):
                dp[day][coupon] = min(dp[day - 1][coupon] + matrix[day],
                                      dp[day - 1][coupon + 1])
            else:
                dp[day][coupon] = min(dp[day - 1][coupon - 1] + matrix[day],
                                      dp[day - 1][coupon + 1])
    min_val, day, coup = 10000, days, coupons
    for i in range(1, coupons + 1):
        if dp[day][i] < min_val:
            coup = i
            min_val = dp[day][i]

    days_when_use_coupons = []
    while day != 0:
        if matrix[day] <= 100:
            if dp[day][coup] == (dp[day-1][coup] + matrix[day]):
                day = day-1
                coup = coup
            else:
                days_when_use_coupons.append(day)
                day = day - 1
                coup = coup + 1
        else:
            if dp[day][coup] == (dp[day-1][coup-1] + matrix[day]):
                day = day-1
                coup = coup-1
            else:
                day = day-1
                coupon = coupon+1



    return dp


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))
