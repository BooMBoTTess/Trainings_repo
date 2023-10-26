def Solution(s):
    index = s.split('\n')
    srting1 = list(map(int, index[0].split(' ')))
    n = srting1[0]
    b = srting1[1]
    arr = list(map(int, index[1].split(' ')))
    dp = [0]

    for now in range(1, n):
        tmp = [0]
        for prev in range(now):
            if (arr[prev] <= arr[now]) and ((arr[prev] + b) >= arr[now]):
                tmp.append(dp[prev]+1)
            if max(tmp) == len(dp):
                break
        dp.append(max(tmp))

    return max(dp)+1


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))