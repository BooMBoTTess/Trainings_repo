def make_bucker(arr, phase: int):
    print('**********')
    print('Phase', phase)
    bucket = [[] for i in range(10)]
    for elem in arr:
        bucket[int(elem[0 - phase])].append(elem)
    #print(bucket)
    return bucket


def Solution(arr):
    print('Initial array:')
    print(' '.join(arr))
    for phase in range(1, len(arr[0])+1):
        bucket = make_bucker(arr, phase)
        arr = []
        counter = 0
        for elem in bucket:
            if elem != []:
                print(f"Bucket {counter}: {' '.join(elem)}")
                for i in elem:
                    arr.append(i)
            else:
                print(f"Bucket {counter}: Empty")
            counter += 1
    print('**********')
    print('Sorted array:')
    print(', '.join(arr))



if __name__ == '__main__':
    f = open('input.txt', 'r')
    n = f.readline()
    arr = f.read().split('\n')
    Solution(arr)
    #print(' '.join(list(map(str, Solution(arr)))))