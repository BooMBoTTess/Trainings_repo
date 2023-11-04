def merge(arrL, arrR):
    L = 0
    R = 0
    result = []
    while L != len(arrL) and R != len(arrR):
        if arrL[L] > arrR[R]:
            result.append(arrR[R])
            R += 1
        else:
            result.append(arrL[L])
            L += 1

    if L == len(arrL):
        result.extend(arrR[R:])
    else:
        result.extend(arrL[L:])
    return result


def Solution(arr):
    k = 2
    while k < len(arr):

        for i in range(0, len(arr), k):
            L = i
            R = i + k
            arr[L : R] = merge(arr[L : R - k// 2], arr[R - k// 2 : R])
        k = k * 2
    for i in range(0, len(arr), k):
        L = i
        R = i + k
        arr[L: R] = merge(arr[L: R - k // 2], arr[R - k // 2: R])

    return arr


if __name__ == '__main__':
    f = open('input.txt', 'r')
    n = f.readline()
    if int(n) == 0:
        arr1 = []
        f.readline()
    else:
        arr1 = list(map(int, f.readline().split(' ')))
    m = f.readline()
    if int(m) == 0:
        arr2 = []
        f.readline()
    else:
        arr2 = list(map(int, f.readline().split(' ')))
    print(' '.join(list(map(str, merge(arr1, arr2)))))