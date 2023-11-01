def partition(n, arr, x):
    L = []
    R = []
    for i in range(len(arr)):
        if arr[i] >= x:
            R.append(arr[i])
        else:
            L.append(arr[i])
    return len(L), len(R)

def quicksort(arr):
    pass


if __name__ == '__main__':
    f = open('input.txt', 'r')
    inp = f.read().rstrip('\n').split('\n')
    n = int(inp[0])
    x = int(inp[2])
    arr = list(map(int, inp[1].split(' ')))
    out = partition(n, arr, x)
    print('\n'.join(list(map(str, out))))