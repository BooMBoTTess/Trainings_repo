def Solution(arr):



if __name__ == '__main__':
    f = open('input.txt', 'r')
    n = f.readline()
    if int(n) == 0:
        arr1 = []
    else:
        arr1 = list(map(int, f.readline().split(' ')))
    m = f.readline()
    if int(m) == 0:
        arr2 = []
    else:
        arr2 = list(map(int, f.readline().split(' ')))
    print(' '.join(list(map(str, merge(arr1, arr2)))))