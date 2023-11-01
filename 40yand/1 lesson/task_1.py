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
    inp = list(map(int, f.read().rstrip('\n').split(' ')))
    print(Solution(inp))