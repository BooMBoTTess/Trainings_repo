def pros(arr):
    multiply = 1
    for i in range(len(arr)):
        multiply *= arr[i]
    return multiply

def solution(arr):
    arr2 = []
    for pos in range(len(arr)):
        tmp = arr.pop(pos)
        arr2.append(pros(arr))
        arr.insert(pos, tmp)
    return arr2


if __name__ == '__main__':
    print(solution([1, 2, 3]))