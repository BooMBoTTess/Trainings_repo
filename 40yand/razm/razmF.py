def bad_solution(k, n, arr):
    result = 0
    while arr != []:
        i = len(arr) - 1
        path = i + 1 + i + 1
        f = 0
        while f != k and i != -1:
            if arr[i] > k - f:
                arr[i] -= k - f
                f = k

            elif arr[i] == k:
                f = k
                i -= 1
                arr.pop()
            else:
                f += arr[i]
                i -= 1
                arr.pop()
        result += path
    return result

def Solution(k, n, arr):
    x = [0 for i in range(len(arr))]
    ostatok = 0
    for i in range(len(arr)-1, 0, -1):
        if arr[i] - ostatok > 0:
            if (arr[i] - ostatok) % k == 0:
                x[i] = ((arr[i] - ostatok) // k)
            else:
                x[i] = (arr[i] - ostatok) // k + 1

            ostatok += k * x[i] - arr[i]
        else:
            ostatok -= arr[i]
    if (arr[0] - ostatok) % k == 0:
        x[0] = ((arr[0] - ostatok) // k)
    else:
        x[0] = (arr[0] - ostatok) // k + 1

    result = 0
    for i in range(len(x)):
        result += (x[i] * (i+1)) * 2

    return result





if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        inp = f.read().rstrip('\n').split('\n')
        k = int(inp[0])
        n = int(inp[1])
        arr = list(map(int, inp[2:]))
        print(Solution(k, n, arr))